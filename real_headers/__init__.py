import random
import copy
from .headers import headers
from .user_agents import user_agents

def get_random_browser():
    """Select a random browser from available headers."""
    return random.choice(list(headers.keys()))

def real_headers():
    """Generate headers with a realistic browser fingerprint."""
    browser = get_random_browser()
    browser_headers = copy.deepcopy(headers[browser])

    # Assign a random User-Agent based on the selected browser
    browser_headers["User-Agent"] = random.choice(user_agents[browser])

    return browser_headers

def random_user_agent():
    """Return a random User-Agent string."""
    browser = get_random_browser()
    return random.choice(user_agents[browser])
