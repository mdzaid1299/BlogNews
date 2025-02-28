import json
import requests
from bs4 import BeautifulSoup

def scrape_techcrunch():
    url = 'https://techcrunch.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for article in soup.find_all('div', class_='loop-card'):
        title_tag = article.find('h3', class_='loop-card__title')
        img_tag = article.find('img')
        link_tag = article.find('a', class_='loop-card__title-link')

        if title_tag and link_tag and img_tag:
            articles.append({
                "title": title_tag.text.strip(),
                "link": link_tag['href'],
                "image": img_tag['src']
            })

    with open('scraped_data.json', 'w') as f:
        json.dump(articles, f, indent=4)

    print(f'Scraped {len(articles)} articles and saved to scraped_data.json')

if __name__ == "__main__":
    scrape_techcrunch()
