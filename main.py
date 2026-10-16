import asyncio
import logging
import sys
from parser import AsyncJobScraper
from exporter import LeadExporter

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("LeadScraper.Main")

async def run_pipeline():
    logger.info("==================================================")
    logger.info("Initializing Lead Generation Pipeline Execution Layer...")
    logger.info("==================================================")
    
    # 1. Run the async parser engine
    scraper = AsyncJobScraper()
    leads = await scraper.scrape_leads()
    
    if not leads:
        logger.error("Pipeline aborted: No data entries compiled.")
        return

    # 2. Export collected leads to a structured Excel file
    output_file = "business_leads.xlsx"
    success = LeadExporter.export_to_excel(leads, filename=output_file)
    
    if success:
        logger.info("==================================================")
        logger.info(f"SUCCESS: Pipeline finished. Artifact created: {output_file}")
        logger.info("==================================================")
    else:
        logger.error("Pipeline execution failed during export phase.")

if __name__ == "__main__":
    # Start the async event loop
    asyncio.run(run_pipeline())
