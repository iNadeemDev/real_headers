# Real Headers


**Real Headers** is a Python library that generates random HTTP headers and browser fingerprints that mimic real browsers. It is designed to be used in web scraping and automation tasks, where realistic headers are essential for avoiding detection and ensuring proper functionality.

## Installation

You can install the `real_headers` library using pip:

```bash
pip install real_headers
```

## Features

- Generates random HTTP headers based on popular web browsers like Chrome, Firefox, Opera, Edge, Chromium, and Safari.<br>
- Provides realistic random user agents.

## Usage

### Generating Real Headers

To generate a random set of HTTP headers that mimic real browsers:

```python
from real_headers import real_headers

headers = real_headers()
print(headers)
```

### Example Output:
```
{
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/58.0.3029.110 Chrome/58.0.3029.110 Safari/537.36'
}
```

### Generating a Random User Agent

To get a random user agent string:

```python
from real_headers import random_user_agent

user_agent = random_user_agent()
print(user_agent)
```

### Example Output:
```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/iNadeemDev/real_headers/blob/main/LICENSE) file for details.