import requests
from bs4 import BeautifulSoup

def get_links(url):
    """Fetches all links from a given URL."""

    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    soup = BeautifulSoup(response.content, 'html.parser')

    links = []
    for link in soup.find_all('a', href=True):
        links.append(link['href'])

    return links

if __name__ == "__main__":
    url = "https://www.nintendolife.com/games/browse?system=gba%2Cgbc%2Cn64%2Csnes%2Cgameboy&page="  # Replace with your desired URL
    links = get_links(url)
    for link in links:
        if "browse" in link:
            continue
        if "/games/" in link:
            print(link)
    for i in range(2,38):
        url2 = url + str(i)
        links = get_links(url2)

        for link in links:
            if "browse" in link: continue
            if "/games/" in link:
                print(link)
