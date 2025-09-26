import * as fs from "fs";
import * as path from "path";

export async function loadUrls(): Promise<string[]> {
  const urls: string[] = [];
  const csvPath = path.resolve("../filtered_urls.csv");

  try {
    const csvContent = fs.readFileSync(csvPath, "utf-8");
    const lines = csvContent.split("\n").slice(1); // Skip header

    for (const line of lines) {
      const url = line.trim();
      if (url) {
        // Extract the ID from the URL (number before .aspx)
        const match = url.match(/(\d+)\.aspx$/);
        if (match) {
          const lawId = match[1];
          const apiUrl = `https://apimobile.thuvienphapluat.vn/Document/GetDocumentDetail?LawID=${lawId}`;
          urls.push(apiUrl);
        }
      }
    }

    return urls;
  } catch (error) {
    console.error("Error reading CSV file:", error);
    throw error;
  }
}
