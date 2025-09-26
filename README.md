# Legal Document Scraper

This Python project scrapes legal documents from the Vietnamese Legal Library (thuvienphapluat.vn) using Crawlee.

## Features

- Downloads sitemap index and subsitemaps
- Filters URLs based on modification date (last 180 days)
- Scrapes document details via API

## Requirements

- Python 3.8+
- Dependencies: crawlee, camoufox, typing-extensions, pandas, tqdm

Install dependencies:

```bash
pip install crawlee camoufox typing-extensions pandas tqdm
```

## Usage

1. **Download sitemaps:**

   ```bash
   python main.py
   ```

   This downloads the main sitemap and all subsitemaps into the `data/` directory.

2. **Filter URLs:**

   ```bash
   python filter.py
   ```

   This processes the downloaded sitemaps, filters URLs modified in the last 180 days, and saves them to `filtered_urls.csv`.

3. **Scrape documents:**
   ```bash
   python crawler.py
   ```
   This runs the crawler to scrape document details from the filtered URLs and outputs JSON data to Crawlee's default dataset.

## Files

- `main.py`: Downloads sitemaps
- `filter.py`: Filters URLs by date
- `crawler.py`: Crawlee crawler for scraping documents
- `data/`: Directory containing downloaded sitemap files
- `filtered_urls.csv`: Filtered list of URLs to scrape

## Output

- Crawlee outputs scraped document data to its default dataset in JSON format.

## Notes

- Ensure you have sufficient disk space for the sitemap downloads (hundreds of XML files).
- Respect the website's terms of service and robots.txt.
- The project uses Camoufox browser to mimic a browser.

## Disclaimer

This project is provided for educational and research purposes only. It is not affiliated with or endorsed by thuvienphapluat.vn or any related entities.

- **Data Accuracy:** The scraped data may not be complete, accurate, or up-to-date. Always verify information from official sources.
- **Legal Compliance:** Ensure your use complies with Vietnamese laws, international copyright laws, and the website's terms of service. Web scraping may be restricted in some jurisdictions.
- **Usage Risk:** Use this tool responsibly. The authors are not liable for any misuse, damages, or legal consequences arising from its use.
- **No Warranty:** This software is provided "as is" without warranty of any kind, express or implied.
