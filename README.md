# Web Page Link Finder

The **Web Page Link Finder** is a Python script that recursively searches a target domain for links to other pages within the domain. It utilizes the `requests`, `urllib.parse`, and `BeautifulSoup` libraries to retrieve and parse HTML content, and then identifies and prints links to more pages within the specified domain.

## Requirements

- Python 3.x
- `requests` library (`pip install requests`)
- `BeautifulSoup` library (`pip install beautifulsoup4`)

## Usage

1. Clone this repository or download the `web_page_link_finder.py` script.

2. Install the required libraries if you haven't already:
   ```bash
   pip install requirements.txt

3. Provide the start_url within the script to specify the URL from which the search should begin.

4. The script will recursively traverse the specified domain, identifying links to more pages within the domain and printing them.

5. The output will also display a list of all visited URLs within the target domain.

## Functionality

- The script uses the find_urls function to search for links to more pages.
- It avoids duplicate URLs by maintaining a set of visited URLs.
- Links are identified through anchor (<a>) tags in the HTML content.
- Absolute URLs are constructed using the urljoin function.
- The script catches and displays any request-related errors.