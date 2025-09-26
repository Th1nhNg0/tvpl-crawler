# Legal Document Scraper

This Python project scrapes legal documents from the Vietnamese Legal Library (thuvienphapluat.vn) using Scrapy.

## Features

- Downloads sitemap index and subsitemaps
- Filters URLs based on modification date (last 180 days)
- Scrapes document details via API

## Requirements

- Python 3.8+
- Dependencies: scrapy, pandas, tqdm

Install dependencies:

```bash
pip install scrapy pandas tqdm
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
   scrapy runspider spider.py -o output/result.jsonl
   ```
   This runs the spider to scrape document details from the filtered URLs and outputs JSON Lines data to `output/result.jsonl`.

## Files

- `main.py`: Downloads sitemaps
- `filter.py`: Filters URLs by date
- `spider.py`: Scrapy spider for scraping documents
- `data/`: Directory containing downloaded sitemap files
- `filtered_urls.csv`: Filtered list of URLs to scrape

## Output

- Scrapy outputs scraped document data to `output/result.jsonl` in JSON Lines format.

## Notes

- Ensure you have sufficient disk space for the sitemap downloads (hundreds of XML files).
- Respect the website's terms of service and robots.txt.
- The project uses a custom User-Agent to mimic a browser.

## Disclaimer

This project is provided for educational and research purposes only. It is not affiliated with or endorsed by thuvienphapluat.vn or any related entities.

- **Data Accuracy:** The scraped data may not be complete, accurate, or up-to-date. Always verify information from official sources.
- **Legal Compliance:** Ensure your use complies with Vietnamese laws, international copyright laws, and the website's terms of service. Web scraping may be restricted in some jurisdictions.
- **Usage Risk:** Use this tool responsibly. The authors are not liable for any misuse, damages, or legal consequences arising from its use.
- **No Warranty:** This software is provided "as is" without warranty of any kind.
