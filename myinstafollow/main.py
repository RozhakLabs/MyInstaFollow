import sys
import time
from .utils.config_loader import load_app_config
from .utils.proxy_manager import ProxyManager
from .utils.ui import (
    show_banner, show_info, show_warning, show_error, show_fatal,
    show_cycle_start, show_service_init, show_cycle_complete,
    show_sleep_info, show_countdown_progress, show_wake_message,
    show_service_status_table, show_no_services_message
)
from .core.api_client import ApiClient
from .services.likes_service import LikesService
from .services.views_service import ViewsService
from .services.followers_service import FollowersService

SERVICE_MAP = {
    'likes': LikesService,
    'views': ViewsService,
    'followers': FollowersService,
}

def main():
    show_banner()

    try:
        config = load_app_config()
    except (FileNotFoundError, ValueError) as e:
        show_fatal(str(e))
        sys.exit(1)

    proxy_manager = ProxyManager()
    api_client = ApiClient(
        base_url=config['settings']['base_url'],
        timeout=config['settings']['request_timeout'],
        proxy_manager=proxy_manager
    )

    while True:
        enabled_services = []
        for name, service_config in config['services'].items():
            if service_config.get('enabled', False):
                if name in SERVICE_MAP:
                    ServiceClass = SERVICE_MAP[name]
                    service_instance = ServiceClass(service_config, api_client)
                    enabled_services.append(service_instance)
                else:
                    show_warning(f"Service '{name}' is enabled but no matching class found. Skipping.")
        
        if not enabled_services:
            show_no_services_message()
            break

        show_service_status_table(enabled_services)
        show_cycle_start(time.strftime('%Y-%m-%d %H:%M:%S'))
        
        actual_wait_seconds = None
        
        for service in enabled_services:
            show_service_init(service.service_type)
            result = service.execute()
            
            if result and result.get("status") == "error" and "remainingTime" in result:
                service_wait = result["remainingTime"]
                if actual_wait_seconds is None or service_wait < actual_wait_seconds:
                    actual_wait_seconds = service_wait
        
        if actual_wait_seconds is None:
            min_interval_hours = min(s.config.get('interval_hours', 24) for s in enabled_services)
            actual_wait_seconds = min_interval_hours * 3600
        
        show_cycle_complete()
        show_sleep_info(actual_wait_seconds)
        
        show_countdown_progress(actual_wait_seconds)
        show_wake_message()

if __name__ == "__main__":
    main()