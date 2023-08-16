import requests
from bs4 import BeautifulSoup
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class WebPage:
    def __init__(self, url):
        self.url = url
        self.response = None
        self.html_content = None
        self.src_attributes = []

    def send_request(self):
        self.response = requests.get(self.url)

    def get_html_content(self):
        if self.response and self.response.status_code == 200:
            self.html_content = self.response.text

    def parse_src_attributes(self):
        if self.html_content:
            soup = BeautifulSoup(self.html_content, 'html.parser')
            self.src_attributes = [tag.get("src") for tag in soup.find_all(attrs={"src": True})]

    def validate_src_links(self):
        failing_links = []
        for src in self.src_attributes:
            full_url = src if src.startswith("http") else self.url + src
            try:
                response = requests.get(full_url)
                logger.info(response)
                if response.status_code == 200:
                    logger.info(f"Validado: {full_url}")
                else:
                    failing_links.append(full_url)
                    logger.info(f"Enlace no válido: {full_url}")
            except requests.exceptions.RequestException:
                failing_links.append(full_url)
        return failing_links