import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

def find_urls(url, visited_urls):
    """
    Recursively finds and prints links to more pages within a target domain.
    
    Args:
        url (str): The URL to start the search from.
        visited_urls (set): A set of visited URLs to avoid duplicates.
    """
    
    # Check if the URL has already been visited
    if url in visited_urls:
        return

    # Add the URL to the set of visited URLs
    visited_urls.add(url)
    
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor (a) tags
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                # Construct absolute URL
                absolute_url = urljoin(url, href)

                # Check if the link contains the target domain
                if url in absolute_url:
                    print(f"Found link to more pages: {absolute_url}")
                    find_urls(absolute_url, visited_urls)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_url = "https://subdomain.example.com/subdirectory/"
    visited_urls = set()

    find_urls(start_url, visited_urls)

    print('-----------------------')
    print('Found URLs:')
    for link in visited_urls:
        print(link)