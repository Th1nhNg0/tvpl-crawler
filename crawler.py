import asyncio
from camoufox import AsyncNewBrowser
from typing_extensions import override
import pandas as pd
from crawlee.browsers import (
    BrowserPool,
    PlaywrightBrowserController,
    PlaywrightBrowserPlugin,
)
from crawlee.crawlers import PlaywrightCrawler, PlaywrightCrawlingContext
import re


def load_urls():
    urls = []
    df = pd.read_csv("filtered_urls.csv")
    for index, row in df.iterrows():
        url = row["url"]
        # Extract the ID from the URL (number before .aspx)
        match = re.search(r"(\d+)\.aspx$", url)
        if match:
            law_id = match.group(1)
            api_url = f"https://apimobile.thuvienphapluat.vn/Document/GetDocumentDetail?LawID={law_id}"
            urls.append(api_url)
    return urls


class CamoufoxPlugin(PlaywrightBrowserPlugin):
    """Example browser plugin that uses Camoufox browser,
    but otherwise keeps the functionality of PlaywrightBrowserPlugin.
    """

    @override
    async def new_browser(self) -> PlaywrightBrowserController:
        if not self._playwright:
            raise RuntimeError("Playwright browser plugin is not initialized.")

        return PlaywrightBrowserController(
            browser=await AsyncNewBrowser(
                self._playwright, **self._browser_launch_options
            ),
            # Increase, if camoufox can handle it in your use case.
            max_open_pages_per_browser=10,
            # This turns off the crawlee header_generation. Camoufox has its own.
            header_generator=None,
        )


async def main() -> None:
    crawler = PlaywrightCrawler(
        browser_pool=BrowserPool(plugins=[CamoufoxPlugin()]),
    )

    # Define the default request handler, which will be called for every request.
    @crawler.router.default_handler
    async def request_handler(context: PlaywrightCrawlingContext) -> None:
        #  response is a json from the API so just push whole response to
        data = await context.response.json()
        await context.push_data(data)

    # Load URLs from the CSV file and add them to the crawler's request queue.
    await crawler.add_requests(load_urls())
    # Run the crawler.
    await crawler.run()


if __name__ == "__main__":
    asyncio.run(main())
