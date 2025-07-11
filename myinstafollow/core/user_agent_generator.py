import random

class UserAgentGenerator:
    """
    Generates realistic and randomized User-Agent strings and extended data
    for Android devices. This is implemented as a static method as it does
    not depend on any instance state.
    """
    @staticmethod
    def generate():
        """
        Generate random Android user agent and extended user agent data.
        
        Returns:
            tuple: A tuple containing (user_agent_string, extended_user_agent_string).
        """
        chrome_major = random.randint(100, 138)
        chrome_minor = random.randint(0, 10)
        chrome_patch = random.randint(0, 9999)
        chrome_build = random.randint(100, 999)
        chrome_version = f"{chrome_major}.{chrome_minor}.{chrome_patch}.{chrome_build}"

        android_devices = [
            {"version": "13", "device": "SM-G991B", "model": "Galaxy S21", "build": "TP1A.220624.014"},
            {"version": "13", "device": "Infinix X6831", "model": "Infinix Note 12", "build": "TP1A.220624.014"},
            {"version": "12", "device": "SM-A525F", "model": "Galaxy A52s", "build": "SP1A.210812.016"},
            {"version": "13", "device": "RMX3461", "model": "Realme 9 Pro", "build": "TP1A.220624.014"},
            {"version": "12", "device": "CPH2389", "model": "OPPO A96", "build": "SP1A.210812.016"},
            {"version": "13", "device": "M2101K9G", "model": "Redmi Note 10 Pro", "build": "TKQ1.220829.002"},
            {"version": "13", "device": "2201117TG", "model": "Xiaomi 12", "build": "TKQ1.220829.002"},
            {"version": "12", "device": "V2111", "model": "Vivo Y21s", "build": "SP1A.210812.016"},
            {"version": "13", "device": "SM-M325FV", "model": "Galaxy M32", "build": "TP1A.220624.014"},
            {"version": "12", "device": "Lenovo TB-X606F", "model": "Lenovo Tab M10", "build": "SP1A.210812.016"}
        ]

        device_info = random.choice(android_devices)
        android_version = device_info["version"]
        device_model = device_info["device"]
        build_id = device_info["build"]

        mobile_resolutions = [
            "360x800", "360x780", "360x820", "393x851", "412x915", 
            "414x896", "375x812", "390x844", "428x926", "360x740"
        ]

        resolution = random.choice(mobile_resolutions)
        width, height = resolution.split('x')
        window_height = str(int(height) - random.randint(120, 180))
        
        memory_options = ["2 GB", "3 GB", "4 GB", "6 GB", "8 GB", "12 GB"]
        memory = random.choice(memory_options)

        concurrency_options = [4, 6, 8, 12]
        concurrency = random.choice(concurrency_options)

        color_depths = [24, 32]
        color_depth = random.choice(color_depths)

        timezones = [
            "Asia/Jakarta", "Asia/Bangkok", "Asia/Manila", "Asia/Kuala_Lumpur",
            "Asia/Singapore", "Asia/Tokyo", "Asia/Seoul", "Asia/Kolkata",
            "Asia/Ho_Chi_Minh", "Asia/Yangon", "Asia/Dhaka"
        ]
        timezone = random.choice(timezones)

        language_options = [
            {"primary": "id", "full": "id, id-ID, en-US"},
            {"primary": "en-US", "full": "en-US, en"},
            {"primary": "id", "full": "id, en-US, en"},
            {"primary": "en-US", "full": "en-US, id, en"},
        ]
        lang_choice = random.choice(language_options)
        primary_lang = lang_choice["primary"]
        full_languages = lang_choice["full"]

        user_agent = f"Mozilla/5.0 (Linux; Android {android_version}; {device_model} Build/{build_id}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36"
        
        extended_user_agent = (
            f"Browser CodeName: Mozilla | "
            f"Browser Name: Netscape | "
            f"Browser Version: 5.0 (Linux; Android {android_version}; {device_model} Build/{build_id}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36 | "
            f"Cookies Enabled: true | "
            f"Platform: Linux aarch64 | "
            f"User-agent header: {user_agent} | "
            f"Language: {primary_lang} | "
            f"Screen Resolution: {resolution} | "
            f"Color Depth: {color_depth} | "
            f"Browser Window Size: {width}x{window_height} | "
            f"Time Zone: {timezone} | "
            f"Languages: {full_languages} | "
            f"Hardware Concurrency: {concurrency} | "
            f"Device Memory: {memory} | "
            f"Touch Support: true | "
            f"JavaScript Enabled: true"
        )

        return user_agent, extended_user_agent