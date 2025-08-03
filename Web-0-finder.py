import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs

ascii_art = r"""
`              _            ___         __ _           _           
`__      _____| |__        / _ \       / _(_)_ __   __| | ___ _ __ 
`\ \ /\ / / _ \ '_ \ _____| | | |_____| |_| | '_ \ / _` |/ _ \ '__|
` \ V  V /  __/ |_) |_____| |_| |_____|  _| | | | | (_| |  __/ |   
`  \_/\_/ \___|_.__/       \___/      |_| |_|_| |_|\__,_|\___|_|   
`                                                                  
"""

print(ascii_art)
print("""
Made in Bangladesh
Owner: MD Haisam Hoque
webpage link: https://haisam10.github.io/freelancer/
version: 1.0
Happy Hacking (^-^)
""")

start_url = input("Give your URL (include http:// or https://): ").strip()

visited = set()
to_visit = [start_url]

page_links_count = {}
found_ids = set()

while to_visit:
    url = to_visit.pop(0)
    if url in visited:
        continue
    visited.add(url)

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch {url} with status code: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(url, href)
            if urlparse(full_url).netloc == urlparse(start_url).netloc:
                links.add(full_url)

                parsed_url = urlparse(full_url)
                query_params = parse_qs(parsed_url.query)
                if 'id' in query_params:
                    for val in query_params['id']:
                        if val.isdigit():
                            found_ids.add(val)

        page_links_count[url] = len(links)

        for link in links:
            if link not in visited and link not in to_visit:
                to_visit.append(link)

    except Exception as e:
        print(f"Failed to fetch {url}: {e}")

print(f"\nTotal pages found: {len(page_links_count)}")
for page_url, link_count in page_links_count.items():
    print(f"Page: {page_url} --> Number of links: {link_count}")

print("\nFound id values in URLs:")
if found_ids:
    for id_val in sorted(found_ids, key=int):
        print(f"id = {id_val}")
else:
    print("No id parameters with numeric values found.")
