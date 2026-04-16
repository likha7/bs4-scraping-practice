# 🕷️ Web Scraping Practice — BeautifulSoup & Requests

A hands-on learning project for web scraping with Python. Built while following along with real tutorials and practicing on both local HTML files and live websites.

---

## 📁 Project Structure

```
scrape/
├── home.html                  # Static HTML practice page (local)
├── main.py                    # Scraper for books.toscrape.com
├── real_web_sites.py          # Scraper for timesjobs.com (JS-rendered exploration)
├── posts/                     # Output folder — scraped book data saved as .txt files
│   ├── 0.txt
│   ├── 1.txt
│   └── ...
```

---

## 🧠 What I Learned

### 1. Static HTML vs JavaScript-Rendered Pages
- `requests` + BeautifulSoup only works on **static HTML**
- Modern sites built with **Next.js / React** render content via JavaScript — `requests` only gets the skeleton
- To detect: press `Cmd+U` in browser — if you see `<script>` tags instead of real content, the site is JS-rendered
- Solution for JS-rendered sites: **Playwright** or **Selenium**, or find the hidden API endpoint via the Network tab

### 2. Parsers
- `html.parser` — built into Python, no install needed, good for learning
- `lxml` — faster (written in C), better for production, handles broken HTML well
- BeautifulSoup is the **interface** — the parser is the **engine** underneath

### 3. BeautifulSoup Techniques Practiced
- `find()` and `find_all()` with tag names and CSS classes
- Navigating nested elements: `book.article.h3.a['href']`
- Extracting attributes: `element['href']`, `element['title']`
- Extracting text: `element.text`
- CSS selectors: `soup.select('.class-name')`

---

## ⚙️ Setup

```bash
# Clone the repo
git clone https://github.com/likha7/bs4-scraping-practice.git
cd bs4-scraping-practice

# Install dependencies
pip3 install requests beautifulsoup4 lxml

# Create the output folder (needed for main.py to save .txt files)
mkdir src/posts
```

---

## 🚀 Usage

**Scrape romance books from books.toscrape.com:**
```bash
python3 main.py
```
Saves each book's name, price, and detail page link into `posts/0.txt`, `posts/1.txt`, etc.

**Practice parsing local HTML:**
```bash
python3 scrape.py
```
Reads `home.html` and extracts product titles and prices.

---

## 🌐 Sites Used

| Site | Type | Purpose |
|------|------|---------|
| `books.toscrape.com` | Static HTML | Real scraping practice — books, prices, ratings |
| `home.html` (local) | Static HTML | Custom practice page for selectors |
| `timesjobs.com` | JS-rendered (Next.js) | Understanding why `requests` fails on dynamic sites |

---

## 📦 Dependencies

- [requests](https://pypi.org/project/requests/) — HTTP requests
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) — HTML parsing
- [lxml](https://pypi.org/project/lxml/) — Fast parser (optional, can use `html.parser`)

---

## 📌 Next Steps

- [ ] Handle pagination (scrape multiple pages)
- [ ] Use Playwright for JavaScript-rendered sites
- [ ] Store scraped data in a database (SQLite / PostgreSQL)
- [ ] Add proxy rotation and request delays
- [ ] Scrape a real job listing site

---

## 📚 Resources

- [Tutorial followed — Python Web Scraping](https://www.youtube.com/watch?v=XVv6mJpFOb0)
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [books.toscrape.com](https://books.toscrape.com) — practice scraping site
