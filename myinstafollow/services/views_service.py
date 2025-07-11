from .base_service import BaseService

class ViewsService(BaseService):
    """
    Provides free Instagram views by implementing the BaseService.
    """
    def __init__(self, service_config, api_client):
        """Initializes the ViewsService."""
        super().__init__(service_config, api_client)

    def _prepare_form_data(self):
        """
        Prepares the form data specific to the 'views' service.
        """
        print(f"[INFO] Preparing form data for '{self.service_type}' service.")
        return {
            'service': self.config['service_id'],
            'photoLink': self.config['reel_link'],
            'viewsQuantity': self.config['quantity'],
        }