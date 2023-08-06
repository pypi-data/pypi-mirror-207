from setuptools import setup, find_packages

import os

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="openai-pricing-scraper",
    version="0.1.1",
    packages=find_packages(),
    url="https://github.com/8ByteSword/openai_pricing_scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="8ByteSword",
    description="Simple way to fetch and parse the pricing data from the OpenAI pricing page.",
    install_requires=[
        "beautifulsoup4",
        "requests",
    ],
)
