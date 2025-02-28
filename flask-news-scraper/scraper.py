import requests
from bs4 import BeautifulSoup
import json

def scrape_techcrunch():
    url = "https://techcrunch.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the "loop-card" divs - these are the articles
    articles = soup.find_all('div', class_="loop-card")

    data = []

    for article in articles:
        article_data = {}

        # Extract image URL
        img_tag = article.find('img')
        if img_tag and 'src' in img_tag.attrs:
            article_data['image'] = img_tag['src']

        # Extract title and link
        title_tag = article.find('a', class_='loop-card__title-link')
        if title_tag:
            article_data['title'] = title_tag.get_text(strip=True)
            article_data['link'] = title_tag['href']

        data.append(article_data)

    # Save to JSON file
    with open('output/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Scraped {len(data)} articles.")

    return data

# For testing - run directly
if __name__ == "__main__":
    scraped_data = scrape_techcrunch()
    print(json.dumps(scraped_data, indent=4, ensure_ascii=False))
