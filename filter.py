import os
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
import csv
from tqdm import tqdm

# Define the cutoff date: 365 days ago from now
now_utc = datetime.now(timezone.utc)
cutoff = now_utc - timedelta(days=365)

# List to hold filtered URLs
filtered_urls = []

# Namespace for XML parsing
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}

# Counters
total_urls = 0

# Get all resitemap files in data directory
data_dir = "data"
resitemap_files = [
    f for f in os.listdir(data_dir) if f.startswith("resitemap") and f.endswith(".xml")
]
for filename in tqdm(resitemap_files, desc="Processing sitemaps"):
    filepath = os.path.join(data_dir, filename)
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        for url_element in root.findall("s:url", ns):
            loc_element = url_element.find("s:loc", ns)
            lastmod_element = url_element.find("s:lastmod", ns)
            if loc_element is not None and lastmod_element is not None:
                url = loc_element.text
                lastmod_str = lastmod_element.text
                if url and lastmod_str:
                    total_urls += 1
                    try:
                        # Parse the lastmod date
                        lastmod_dt = datetime.fromisoformat(lastmod_str)
                        # Convert to UTC
                        lastmod_utc = lastmod_dt.astimezone(timezone.utc)
                        # Check if within last 365 days
                        if lastmod_utc >= cutoff:
                            filtered_urls.append(url)
                    except ValueError:
                        # Skip if date parsing fails
                        continue
    except ET.ParseError:
        # Skip if XML parsing fails
        continue

# Write to CSV
with open("filtered_urls.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["url"])
    for url in filtered_urls:
        writer.writerow([url])

print(
    f"Processed {total_urls} URLs, filtered {len(filtered_urls)} URLs and saved to filtered_urls.csv"
)
