# 📰 BlogNews Tech News API

This is a simple **Flask API** that provides the latest **Tech News** from TechCrunch. The news data is scraped daily and served as a **pre-scraped JSON feed** for faster performance.

## 🌐 API Endpoint

### 📥 Fetch Latest Tech News

**Endpoint:**
```
GET https://blognews-ju56.onrender.com/scrape
```

**Response Format:**
```json
[
    {
        "title": "Bluesky-based Instagram alternative Flashes launches publicly",
        "link": "https://techcrunch.com/2025/02/28/bluesky-based-instagram-alternative-flashes-launches-publicly/",
        "image": "https://techcrunch.com/wp-content/uploads/2025/02/flashes-logo.jpg?w=668"
    },
    {
        "title": "Researchers uncover unknown Android flaws used to hack into a student's phone",
        "link": "https://techcrunch.com/2025/02/28/researchers-uncover-unknown-android-flaws-used-to-hack-into-a-students-phone/",
        "image": "https://techcrunch.com/wp-content/uploads/2025/02/android-spyware-purple.jpg?w=668"
    }
]
```

---

## 🛠️ How It Works

- The backend **scraper fetches data from TechCrunch once every 24 hours**.
- The scraped articles (title, link, and image) are saved to a **JSON file**.
- The `/scrape` endpoint reads that **pre-scraped JSON** and returns it instantly.
- This approach ensures **faster responses** and reduces **unnecessary scraping**.

---

## 🔥 Features

- ✅ **TechCrunch News Aggregator**
- ✅ **Pre-scraped Data for Fast API Response**
- ✅ **Serves Title, URL & Image for Each Article**
- ✅ **Automatic Daily Scraping via GitHub Actions (optional)**

---

## 📂 Project Structure

```
.
├── app.py                  # Flask API that serves pre-scraped data
├── scraper.py               # Scraper that fetches TechCrunch news
├── scraped_data.json        # Saved news data (updated daily)
├── requirements.txt
└── README.md
```
