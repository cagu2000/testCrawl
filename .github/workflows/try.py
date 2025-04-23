import requests
from bs4 import BeautifulSoup

# URL of the sitemap
sitemap_url = "https://libraryguides.fullerton.edu/sitemap.xml"

try:
    # Fetch the sitemap
    response = requests.get(sitemap_url)
    response.raise_for_status()  # Raise an error for HTTP issues

    # Parse the sitemap XML
    soup = BeautifulSoup(response.content, "xml")

    # Find all <loc> tags (these contain the URLs in the sitemap)
    urls = soup.find_all("loc")

    # Loop through each URL and print it
    for url in urls:
        print(url.text)

except requests.exceptions.RequestException as e:
    print(f"Error fetching the sitemap: {e}")