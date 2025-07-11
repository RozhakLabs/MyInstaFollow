import json
import os
from .ui import show_info

def load_app_config(config_path="config/services.json"):
    """
    Loads the main application configuration from a JSON file.

    Args:
        config_path (str): The path to the configuration file.

    Returns:
        dict: A dictionary containing the configuration.

    Raises:
        FileNotFoundError: If the configuration file is not found.
        ValueError: If the configuration file is empty or not valid JSON.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in {config_path}. Please check the file content.")
    
    if not config:
        raise ValueError(f"Configuration file {config_path} is empty.")
    
    if 'settings' not in config or 'services' not in config:
        raise ValueError("Config is missing required 'settings' or 'services' sections.")
    
    show_info(f"Successfully loaded configuration from {config_path}", "CONFIG")
    return config