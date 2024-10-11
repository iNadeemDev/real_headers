import json
from real_headers import real_headers, real_user_agent

def show_headers():
    """Display the full HTTP headers"""
    headers = real_headers()
    print(json.dumps(headers, indent=4))

def show_user_agent():
    """Display only the User-Agent"""
    print(real_user_agent())