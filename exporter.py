import logging
import pandas as pd

logger = logging.getLogger("LeadScraper.Exporter")

class LeadExporter:
    @staticmethod
    def export_to_excel(leads: list[dict], filename: str = "business_leads.xlsx") -> bool:
        """Convert a list of dicts into a structured Excel spreadsheet"""
        if not leads:
            logger.warning("No data structural layers found to export.")
            return False

        try:
            # Build a DataFrame from the collected async results
            df = pd.DataFrame(leads)

            # Write with the openpyxl engine for advanced formatting
            with pd.ExcelWriter(filename, engine="openpyxl") as writer:
                df.to_excel(writer, index=False, sheet_name="Leads Analysis")

                # Auto-fit column widths to their content for a polished look
                worksheet = writer.sheets["Leads Analysis"]
                for col in worksheet.columns:
                    max_len = max(len(str(cell.value or "")) for cell in col)
                    col_letter = col[0].column_letter
                    worksheet.column_dimensions[col_letter].width = max(max_len + 3, 12)

            logger.info(f"Operational data layer successfully exported to production file: {filename}")
            return True
        except Exception as e:
            logger.error(f"Critical error compiling excel spreadsheet artifact: {e}")
            return False
