import json
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def scrape_site():
    url = "https://www.nytimes.com/puzzles/spelling-bee"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    script_tag = soup.find('script', string=lambda t: 'window.gameData' in t)
    json_str = script_tag.string.split(' = ', 1)[1].rstrip(';')
    game_data = json.loads(json_str)
    today_data = game_data['today']
    return today_data['answers']

def main():
    answers = scrape_site()
    answers = sorted(answers,key=len) 
    print(answers[::-1])
main()
