#!/usr/bin/env python3
"""
URL Checker CLI Tool

A simple command-line tool to check the status of one or more URLs.
It reports HTTP status code, response time, and SSL certificate validity (for HTTPS).
"""

import argparse
import sys
import time
import socket
import ssl
from urllib.parse import urlparse
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def create_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504)):
    """Create a requests session with retry strategy."""
    session = requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def check_url(url, timeout=10):
    """Check a single URL and return a dictionary of results."""
    parsed = urlparse(url)
    if not parsed.scheme:
        url = 'http://' + url
        parsed = urlparse(url)

    result = {
        'url': url,
        'status_code': None,
        'response_time': None,
        'ssl_valid': None,
        'error': None
    }

    session = create_session()
    start_time = time.time()
    try:
        response = session.get(url, timeout=timeout, allow_redirects=True, verify=True)
        result['status_code'] = response.status_code
        result['response_time'] = time.time() - start_time
        # If we got here without an SSL error, the certificate is valid (for HTTPS)
        if parsed.scheme == 'https':
            result['ssl_valid'] = True
    except requests.exceptions.SSLError as e:
        result['error'] = f'SSL Error: {str(e)}'
        if parsed.scheme == 'https':
            result['ssl_valid'] = False
    except requests.exceptions.RequestException as e:
        result['error'] = str(e)
    except Exception as e:
        result['error'] = f'Unexpected error: {str(e)}'

    return result


def main():
    parser = argparse.ArgumentParser(description='Check the status of one or more URLs.')
    parser.add_argument('urls', nargs='+', help='URLs to check')
    parser.add_argument('-t', '--timeout', type=int, default=10, help='Timeout in seconds (default: 10)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    args = parser.parse_args()

    for url in args.urls:
        result = check_url(url, timeout=args.timeout)
        if args.verbose:
            print(f"Checking {result['url']}...")
        if result['error']:
            print(f"❌ {result['url']} - Error: {result['error']}")
        else:
            status_emoji = "✅" if 200 <= result['status_code'] < 400 else "⚠️"
            ssl_info = ""
            if result['url'].startswith('https://'):
                ssl_info = " | SSL: " + ("Valid" if result['ssl_valid'] else "Invalid")
            print(f"{status_emoji} {result['url']} - Status: {result['status_code']} | "
                  f"Response Time: {result['response_time']:.2f}s{ssl_info}")


if __name__ == '__main__':
    main()