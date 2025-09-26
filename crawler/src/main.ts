// For more information, see https://crawlee.dev/
import { launchOptions } from "camoufox-js";
import { PlaywrightCrawler } from "crawlee";
import { firefox } from "playwright";

import { router } from "./routes.js";
import { loadUrls } from "./utils.js";

async function main() {
  const crawler = new PlaywrightCrawler({
    requestHandler: router,
    postNavigationHooks: [
      async ({ handleCloudflareChallenge }) => {
        await handleCloudflareChallenge();
      },
    ],
    browserPoolOptions: {
      useFingerprints: false,
    },
    launchContext: {
      launcher: firefox,
      launchOptions: await launchOptions({
        headless: true,
      }),
    },
  });

  // Load URLs from the CSV file and add them to the crawler's request queue
  const urls = await loadUrls();
  console.log(`Loaded ${urls.length} URLs from CSV`);

  await crawler.addRequests(urls);
  // Run the crawler
  await crawler.run();
}

// Run the main function
main().catch(console.error);
