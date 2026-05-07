#!/usr/bin/env python3
"""
Jekyll Link Checker - A tool to validate internal and external links in Jekyll sites.

This tool crawls a Jekyll site and checks all links for validity, reporting
broken links, redirects, and other issues.
"""

import argparse
import asyncio
import aiohttp
import aiofiles
import sys
import os
import re
from urllib.parse import urljoin, urlparse
from pathlib import Path
from typing import Set, List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class JekyllLinkChecker:
    def __init__(self, site_dir: str, base_url: str = "", timeout: int = 30):
        self.site_dir = Path(site_dir).resolve()
        self.base_url = base_url.rstrip('/') if base_url else ""
        self.timeout = timeout
        self.session: Optional[aiohttp.ClientSession] = None
        
        # Results tracking
        self.broken_links: List[Tuple[str, str, int]] = []  # (source_file, link, status_code)
        self.redirected_links: List[Tuple[str, str, str, int]] = []  # (source_file, link, final_url, status_code)
        self.valid_links: Set[str] = set()
        self.checked_links: Set[str] = set()
        
        # Jekyll-specific patterns
        self.markdown_extensions = {'.md', '.markdown', '.html', '.htm'}
        self.ignore_patterns = [
            r'^#',  # Anchor links
            r'^mailto:',  # Email links
            r'^tel:',  # Phone links
            r'^javascript:',  # Javascript links
        ]
        
    async def __aenter__(self):
        connector = aiohttp.TCPConnector(limit=100)
        self.session = aiohttp.ClientSession(
            connector=connector,
            timeout=aiohttp.ClientTimeout(total=self.timeout),
            headers={'User-Agent': 'JekyllLinkChecker/1.0'}
        )
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
            
    def _should_ignore_link(self, link: str) -> bool:
        """Check if a link should be ignored."""
        for pattern in self.ignore_patterns:
            if re.match(pattern, link, re.IGNORECASE):
                return True
        return False
        
    def _normalize_url(self, link: str, source_path: Path) -> Optional[str]:
        """Normalize a link to an absolute URL for checking."""
        if self._should_ignore_link(link):
            return None
            
        # Handle relative URLs
        if not link.startswith(('http://', 'https://')):
            if self.base_url:
                # Make absolute URL based on site base URL
                normalized = urljoin(self.base_url + '/', link.lstrip('/'))
            else:
                # For local file checking, we'll handle differently
                return None
        else:
            normalized = link
            
        return normalized
        
    def _extract_links_from_content(self, content: str, file_path: Path) -> List[Tuple[str, str]]:
        """Extract all links from file content."""
        links = []
        
        # HTML <a href=""> links
        html_pattern = r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>'
        for match in re.finditer(html_pattern, content, re.IGNORECASE):
            links.append((match.group(1), f"HTML tag in {file_path}"))
            
        # Markdown [text](url) links
        md_pattern = r'\[[^\]]*\]\s*\(([^)]+)\)'
        for match in re.finditer(md_pattern, content):
            links.append((match.group(1), f"Markdown link in {file_path}"))
            
        # Direct URLs in text (simplified)
        url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
        for match in re.finditer(url_pattern, content):
            links.append((match.group(0), f"Plain URL in {file_path}"))
            
        return links
        
    async def _fetch_file_content(self, file_path: Path) -> Optional[str]:
        """Fetch content from a local file."""
        try:
            async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return await f.read()
        except Exception as e:
            logger.warning(f"Could not read file {file_path}: {e}")
            return None
            
    async def _check_link(self, url: str) -> Tuple[bool, Optional[str], int]:
        """Check a single URL and return (is_valid, final_url, status_code)."""
        if url in self.checked_links:
            # Return cached result if available
            if url in self.valid_links:
                return True, url, 200
            # For broken links, we'd need to cache more info - simplified for now
            
        self.checked_links.add(url)
        
        try:
            async with self.session.head(url, allow_redirects=True) as response:
                status = response.status
                final_url = str(response.url)
                
                if 200 <= status < 400:
                    self.valid_links.add(url)
                    if str(response.url) != url:
                        return False, final_url, status  # Redirected but still valid
                    return True, url, status
                else:
                    return False, final_url, status
                    
        except asyncio.TimeoutError:
            return False, url, 408
        except Exception as e:
            logger.debug(f"Error checking {url}: {e}")
            return False, url, 0
            
    async def _process_file(self, file_path: Path):
        """Process a single file for link checking."""
        content = await self._fetch_file_content(file_path)
        if content is None:
            return
            
        links = self._extract_links_from_content(content, file_path)
        
        for link, context in links:
            normalized_url = self._normalize_url(link, file_path)
            if normalized_url is None:
                continue
                
            is_valid, final_url, status_code = await self._check_link(normalized_url)
            
            if not is_valid:
                if 300 <= status_code < 400:
                    self.redirected_links.append((str(file_path), link, final_url, status_code))
                else:
                    self.broken_links.append((str(file_path), link, status_code))
            # Valid links are tracked in self.valid_links set
            
    async def _find_site_files(self) -> List[Path]:
        """Find all relevant files in the Jekyll site."""
        files = []
        
        # Common Jekyll directories to check
        dirs_to_check = ['', '_posts', '_drafts', '_pages']
        
        for dir_name in dirs_to_check:
            search_dir = self.site_dir / dir_name if dir_name else self.site_dir
            if search_dir.exists():
                for ext in self.markdown_extensions:
                    pattern = f"**/*{ext}"
                    files.extend(search_dir.glob(pattern))
                    
        # Also check the root for common files
        root_files = ['index.html', 'index.md', 'README.md']
        for filename in root_files:
            file_path = self.site_dir / filename
            if file_path.exists():
                files.append(file_path)
                
        return list(set(files))  # Remove duplicates
        
    async def check_site(self) -> dict:
        """Main method to check the entire Jekyll site."""
        logger.info(f"Starting link check for site: {self.site_dir}")
        if self.base_url:
            logger.info(f"Base URL: {self.base_url}")
            
        files = await self._find_site_files()
        logger.info(f"Found {len(files)} files to check")
        
        # Process files concurrently (but limit concurrency to be nice)
        semaphore = asyncio.Semaphore(20)
        
        async def process_with_semaphore(file_path):
            async with semaphore:
                await self._process_file(file_path)
                
        tasks = [process_with_semaphore(f) for f in files]
        await asyncio.gather(*tasks, return_exceptions=True)
        
        # Compile results
        results = {
            'total_files_checked': len(files),
            'total_links_checked': len(self.checked_links),
            'broken_links': len(self.broken_links),
            'redirected_links': len(self.redirected_links),
            'valid_links': len(self.valid_links),
            'broken_link_details': self.broken_links,
            'redirected_link_details': self.redirected_links
        }
        
        return results
        
    def print_report(self, results: dict):
        """Print a formatted report of the link checking results."""
        print("\n" + "="*60)
        print("JEKYLL LINK CHECKER REPORT")
        print("="*60)
        print(f"Files checked: {results['total_files_checked']}")
        print(f"Links checked: {results['total_links_checked']}")
        print(f"Valid links: {results['valid_links']}")
        print(f"Redirected links: {results['redirected_links']}")
        print(f"Broken links: {results['broken_links']}")
        
        if results['broken_links'] > 0:
            print("\nBROKEN LINKS:")
            print("-" * 40)
            for source_file, link, status_code in results['broken_link_details'][:10]:  # Limit output
                print(f"  {source_file}")
                print(f"    Link: {link}")
                print(f"    Status: {status_code}")
                print()
                
            if len(results['broken_link_details']) > 10:
                print(f"  ... and {len(results['broken_link_details']) - 10} more broken links")
                
        if results['redirected_links'] > 0:
            print("\nREDIRECTED LINKS:")
            print("-" * 40)
            for source_file, link, final_url, status_code in results['redirected_link_details'][:10]:
                print(f"  {source_file}")
                print(f"    Link: {link} -> {final_url}")
                print(f"    Status: {status_code}")
                print()
                
            if len(results['redirected_link_details']) > 10:
                print(f"  ... and {len(results['redirected_link_details']) - 10} more redirected links")
                
        print("="*60)


async def main():
    parser = argparse.ArgumentParser(description='Check links in a Jekyll site')
    parser.add_argument('site_dir', help='Path to the Jekyll site directory')
    parser.add_argument('--base-url', '', help='Base URL of the site (for resolving relative links)')
    parser.add_argument('--timeout', type=int, default=30, help='Request timeout in seconds')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        
    if not os.path.exists(args.site_dir):
        print(f"Error: Site directory '{args.site_dir}' does not exist")
        sys.exit(1)
        
    async with JekyllLinkChecker(args.site_dir, args.base_url, args.timeout) as checker:
        results = await checker.check_site()
        checker.print_report(results)
        
        # Exit with error code if broken links found
        if results['broken_links'] > 0:
            sys.exit(1)
        else:
            sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())