import json
import requests
import os
from bs4 import BeautifulSoup

def scrape_techcrunch():
    url = 'https://techcrunch.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Load existing articles if the file exists
    existing_articles = []
    if os.path.exists('scraped_data.json'):
        with open('scraped_data.json', 'r') as f:
            existing_articles = json.load(f)

    existing_links = {article['link'] for article in existing_articles}

    new_articles = []
    for article in soup.find_all('div', class_='loop-card'):
        title_tag = article.find('h3', class_='loop-card__title')
        img_tag = article.find('img')
        link_tag = article.find('a', class_='loop-card__title-link')

        if title_tag and link_tag and img_tag:
            link = link_tag['href']
            if link not in existing_links:
                new_articles.append({
                    "title": title_tag.text.strip(),
                    "link": link,
                    "image": img_tag['src']
                })

    # Combine old and new, then save
    all_articles = existing_articles + new_articles
    with open('scraped_data.json', 'w') as f:
        json.dump(all_articles, f, indent=4)

    print(f'Added {len(new_articles)} new articles. Total: {len(all_articles)}')

if __name__ == "__main__":
    scrape_techcrunch()
