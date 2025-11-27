from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="real_headers",
    version="0.1.2",
    author="Muhammad Nadeem",
    author_email="nadeemdsb5@gmail.com",
    description="Real Headers is a Python library that generates random HTTP headers and browser fingerprints that mimic real browsers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iNadeemDev/real_headers",
    packages=find_packages(),
    install_requires=[],
    project_urls={
        "Source": "https://github.com/iNadeemDev/real_headers",
    },
    entry_points={
        'console_scripts': [
            'real_headers=real_headers.cli:show_headers',
            'real-headers=real_headers.cli:show_headers',
            'real_user_agent=real_headers.cli:show_user_agent',
            'real-user-agent=real_headers.cli:show_user_agent',
        ],
    },
    keywords=["headers", "user-agent", "browser", "fingerprint", "fake headers", "real headers", "request headers",
              "http headers", "random headers", "realheaders"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
