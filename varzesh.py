import os
import requests
from bs4 import BeautifulSoup
import threading
import time
from urllib.parse import urlparse, urljoin

IMAGE_FOLDER = "downloaded_images"
os.makedirs(IMAGE_FOLDER, exist_ok=True)

olds = set()
def fetch_news_links():
    global olds
    while True:
        try:
            print("Fetching new links...")
            soup = BeautifulSoup(requests.get("https://varzesh3.com").content, "html.parser")
            divs = soup.find_all("div", {"class": "news-main-list"})
            links = []
            for dv in divs:
                links.extend(dv.find_all("a"))
            urls = map(lambda link: link["href"], links)
            links = filter(lambda url: not url.startswith("https://video.varzesh3.com"), urls)
            new_links = set(links) - olds
            olds.update(new_links)

            if new_links:
                print(f"Found {len(new_links)} new links.")
                threading.Thread(target=download_images_from_links, args=(new_links,)).start()

        except Exception as e:
            print(f"Error fetching links: {e}")
        time.sleep(30)

def download_images_from_links(links):
    for link in links:
        try:
            print(f"Processing link: {link}")
            soup = BeautifulSoup(requests.get(link).content, "html.parser")
            img_divs = soup.find_all("div", {"class": "news-main-image"})
            for img_div in img_divs:
                imgs = img_div.find_all("img")
                for img in imgs:
                    img_url = img["src"]
                    save_image(img_url)
        except Exception as e:
            print(f"Error processing link {link}: {e}")
def save_image(img_url):
    try:
        parsed_url = urlparse(img_url)
        base_name = os.path.basename(parsed_url.path)
        img_name = os.path.join(IMAGE_FOLDER, base_name)
        response = requests.get(img_url, stream=True)
        if response.status_code == 200:
            with open(img_name, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Image saved: {img_name}")
        else:
            print(f"Failed to download image: {img_url}")
    except Exception as e:
        print(f"Error saving image {img_url}: {e}")
if __name__ == "__main__":
    threading.Thread(target=fetch_news_links, daemon=True).start()
    while True:
        time.sleep(1)