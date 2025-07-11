from .base_service import BaseService

class LikesService(BaseService):
    """
    Provides free Instagram likes by implementing the BaseService.
    """
    def __init__(self, service_config, api_client):
        super().__init__(service_config, api_client)
    
    def _prepare_form_data(self):
        """
        Prepares the form data specific to the 'likes' service.
        """
        print(f"[INFO] Preparing form data for '{self.service_type}' service.")
        return {
            'service': self.config['service_id'],
            'postlink': self.config['post_link'],
            'likesQuantity': self.config['quantity'],
        }