import requests
import json
from requests_toolbelt import MultipartEncoder
from .user_agent_generator import UserAgentGenerator
from ..utils.ui import show_error, show_info

class ApiClient:
    """
    A client to handle HTTP sessions, cookies, proxies, and requests
    to the myinstafollow.com service.
    """
    def __init__(self, base_url, timeout, proxy_manager):
        """
        Initializes the ApiClient.

        Args:
            base_url (str): The base URL of the service.
            timeout (int): The request timeout in seconds.
            proxy_manager (ProxyManager): An instance of the ProxyManager.
        """
        self.base_url = base_url
        self.timeout = timeout
        self.proxy_manager = proxy_manager
        self.session = requests.Session()

    def _get_cookies(self, page_path):
        """
        Establishes a session and retrieves initial cookies from a given page.
        
        Args:
            page_path (str): The path of the page to visit (e.g., /free-instagram-views/).

        Returns:
            str or None: A string of cookies, or None if the request fails.
        """
        user_agent, _ = UserAgentGenerator.generate()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Host": self.base_url.replace('https://', ''),
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": user_agent
        }
        try:
            response = self.session.get(self.base_url + page_path, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            cookies = self.session.cookies.get_dict()
            return "; ".join([f"{key}={value}" for key, value in cookies.items()])
        except requests.RequestException as e:
            show_error(f"Failed to retrieve cookies: {e}")
            return None
    
    def submit_form(self, service_type, form_data, endpoint, referer):
        """
        Submits a multipart form request to a specified endpoint.

        Args:
            service_type (str): The type of service (e.g., "views", "likes").
            form_data (dict): The form data payload.
            endpoint (str): The API endpoint path.
            referer (str): The referer URL.

        Returns:
            dict or None: The JSON response from the server, or None on failure.
        """
        self.session.proxies = self.proxy_manager.get_random_proxy()
        if self.session.proxies:
            proxy_display = self.session.proxies['http'].split('@')[-1].replace('http://', '')
            show_info(f"Using proxy for this request: {proxy_display}", "PROXY")
        else:
            show_info("No proxy configured, using direct connection", "PROXY")

        cookies_string = self._get_cookies(referer.replace(self.base_url, ''))
        if not cookies_string:
            show_error("Failed to retrieve cookies, cannot proceed with form submission")
            return None
        
        user_agent, extended_user_agent = UserAgentGenerator.generate()
        form_data['extended_user_agent'] = extended_user_agent

        data = MultipartEncoder(fields=form_data)

        headers = {
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "id,id-ID;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Cookie": cookies_string,
            "Content-Type": data.content_type,
            "Accept": "*/*",
            "Host": self.base_url.replace('https://', ''),
            "Origin": self.base_url,
            "Referer": referer,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": user_agent
        }
        
        try:
            show_info(f"Submitting request for '{service_type}' service...", "REQUEST")
            response = self.session.post(self.base_url + endpoint, data=data, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ProxyError as e:
            show_error(f"Proxy error: {e}. Check your proxy settings")
        except requests.exceptions.Timeout:
            show_error(f"Request timed out after {self.timeout} seconds")
        except requests.exceptions.ConnectionError as e:
            show_error(f"Connection error: {e}. Check internet or proxy")
        except json.JSONDecodeError:
            show_error("Failed to decode JSON response. Server may be down or response format changed")
        except requests.RequestException as e:
            show_error(f"An unexpected network error occurred: {e}")

        return None