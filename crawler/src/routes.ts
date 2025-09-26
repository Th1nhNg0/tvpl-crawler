import { createPlaywrightRouter } from "crawlee";

export const router = createPlaywrightRouter();

// Define the default request handler, which will be called for every request
router.addDefaultHandler(async ({ request, response, log, pushData }) => {
  try {
    const data = await response?.json();
    if (data) {
      await pushData(data);
    } else {
      log.warning(`No data received for URL: ${request.loadedUrl}`);
    }
  } catch (error) {
    log.error(`Error processing URL ${request.loadedUrl}: ${error}`);
  }
});
