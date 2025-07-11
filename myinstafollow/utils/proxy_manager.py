import random
import os

class ProxyManager:
    """
    Manages loading and providing formatted proxies from a file.
    """
    def __init__(self, proxy_file_path="config/proxy.txt"):
        """
        Initializes the ProxyManager.

        Args:
            proxy_file_path (str): The path to the proxy list file.
        """
        self.proxy_file_path = proxy_file_path
        self.proxies = []
        self._load_proxies()
    
    def _load_proxies(self):
        """
        Loads and parses proxies from the file.
        This is a private method, intended for internal use.
        """
        if not os.path.exists(self.proxy_file_path):
            print(f"[INFO] Proxy file not found at '{self.proxy_file_path}'. Running without proxies.")
            return

        try:
            with open(self.proxy_file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        self.proxies.append(line)
            
            if self.proxies:
                print(f"[INFO] Successfully loaded {len(self.proxies)} proxies from '{self.proxy_file_path}'.")
            else:
                print(f"[WARNING] Proxy file '{self.proxy_file_path}' is empty or contains no valid entries.")
        except Exception as e:
            print(f"[ERROR] Failed to read proxy file: {e}")
    
    def get_random_proxy(self):
        """
        Selects a random proxy and formats it for the 'requests' library.

        Returns:
            dict or None: A dictionary formatted for requests' proxies, or None if no proxies are available.
        """
        if not self.proxies:
            return None
        
        proxy = random.choice(self.proxies)

        if '@' in proxy:
            proxy_url = proxy if proxy.startswith(('http://', 'https://')) else f"http://{proxy}"
        else:
            parts = proxy.split(':')

            if len(parts) == 2:
                proxy_url = f"http://{parts[0]}:{parts[1]}"
            elif len(parts) == 4:
                proxy_url = f"http://{parts[2]}:{parts[3]}@{parts[0]}:{parts[1]}"
            else:
                print(f"[WARNING] Invalid proxy format detected: '{proxy}'. Skipping.")
                return None
        
        return {'http': proxy_url, 'https': proxy_url}