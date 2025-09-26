import urllib.request
import xml.etree.ElementTree as ET
import os
from tqdm import tqdm
import concurrent.futures


def download_file(loc):
    filename = os.path.join("data", os.path.basename(loc))
    urllib.request.urlretrieve(loc, filename)


# Create data folder
os.makedirs("data", exist_ok=True)

# Download sitemap index
url = "https://thuvienphapluat.vn/sitemap.xml"
filename = "sitemap.xml"
urllib.request.urlretrieve(url, filename)
print(f"Sitemap index downloaded to {filename}")

# Parse sitemap.xml
tree = ET.parse(filename)
root = tree.getroot()

# Namespace
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}

# Find all sitemap loc
sitemaps = []
for sitemap in root.findall("s:sitemap", ns):
    loc_element = sitemap.find("s:loc", ns)
    if loc_element is not None:
        loc = loc_element.text
        if loc:
            sitemaps.append(loc)

total = len(sitemaps)
print(f"Found {total} subsitemaps to download.")

# Download in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(download_file, loc) for loc in sitemaps]
    for future in tqdm(
        concurrent.futures.as_completed(futures),
        total=total,
        desc="Downloading subsitemaps",
    ):
        future.result()
