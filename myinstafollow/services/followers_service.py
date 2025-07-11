from .base_service import BaseService

class FollowersService(BaseService):
    """
    Provides free Instagram followers by implementing the BaseService.
    """
    def __init__(self, service_config, api_client):
        """Initializes the FollowersService."""
        super().__init__(service_config, api_client)

    def _prepare_form_data(self):
        """
        Prepares the form data specific to the 'followers' service.
        """
        print(f"[INFO] Preparing form data for '{self.service_type}' service.")
        return {
            'service': self.config['service_id'],
            'username': self.config['username'],
            'followersQuantity': self.config['quantity'],
        }