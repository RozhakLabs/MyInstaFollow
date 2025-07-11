from abc import ABC, abstractmethod
from ..utils.ui import show_error, show_success, show_warning, show_info

class BaseService(ABC):
    """
    An abstract base class that defines the common interface for all services
    (Likes, Views, Followers).
    """
    def __init__(self, service_config, api_client):
        """
        Initializes the service.

        Args:
            service_config (dict): The specific configuration for this service.
            api_client (ApiClient): An instance of the ApiClient.
        """
        self.config = service_config
        self.api_client = api_client
        self.service_type = self.__class__.__name__.replace("Service", "").lower()

    @abstractmethod
    def _prepare_form_data(self):
        """
        Prepares the specific form data for the service request.
        This method MUST be implemented by subclasses.
        """
        pass
    
    @staticmethod
    def _format_time(seconds):
        """
        Converts seconds to a human-readable "hours, minutes, seconds" format.
        """
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60

        if hours > 0:
            return f"{hours} jam {minutes} menit {secs} detik"
        elif minutes > 0:
            return f"{minutes} menit {secs} detik"
        else:
            return f"{secs} detik"
    
    def execute(self):
        """
        Executes the service request and handles the response.
        """
        form_data = self._prepare_form_data()
        endpoint = f"/themes/vision/part/free-instagram-{self.service_type}/submitForm.php"
        referer = f"{self.api_client.base_url}/free-instagram-{self.service_type}/"

        result = self.api_client.submit_form(
            self.service_type, form_data, endpoint, referer
        )

        if not result:
            show_error(f"Service '{self.service_type}' failed to get a response from the server.")
            return None
        
        if result.get("status") == "success":
            message = result.get("message", "Order berhasil diproses.")
            show_success(f"{self.service_type.title()} - {message}")
            return result
        elif result.get("status") == "error" and "remainingTime" in result:
            remaining_time = result["remainingTime"]
            formatted_time = self._format_time(remaining_time)
            show_warning(f"Layanan '{self.service_type}' harus menunggu {formatted_time}")
            return result
        else:
            error_message = result.get("message", "Terjadi error yang tidak diketahui.")
            show_error(f"Gagal menjalankan layanan '{self.service_type}': {error_message}")
            return result