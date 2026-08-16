from pathlib import Path

from excel_reader import read_excel_files

from data_processor import (
    clean_data,
    remove_duplicates,
    calculate_sale_totals,
    calculate_summary,
    employee_summary,
    product_summary
)

from excel_writer import (
    create_workbook,
    create_sales_sheet,
    create_summary_sheet,
    create_employee_sheet,
    create_product_sheet,
    save_workbook
)
from pdf_generator import generate_pdf

from email_sender import (
    create_email,
    attach_file,
    send_email
)

from logger import setup_logger


def main():

    logger = setup_logger()

    logger.info("====================================")
    logger.info("Automation started")
    logger.info("====================================")

    try:

        # ==========================================
        # PATHS
        # ==========================================

        base_dir = Path(__file__).resolve().parent.parent

        input_folder = base_dir / "input"

        output_folder = base_dir / "output"

        output_folder.mkdir(
            exist_ok=True
        )


        # ==========================================
        # PART 2 - READ EXCEL
        # ==========================================

        logger.info(
            "Searching for Excel files..."
        )

        raw_data = read_excel_files(
            input_folder
        )

        logger.info(
            f"Raw records: {len(raw_data)}"
        )


               # ==========================================
        # PART 3 - PROCESS DATA
        # ==========================================

        logger.info(
            "Starting data processing..."
        )

        clean_records = clean_data(
            raw_data
        )

        logger.info(
            f"After validation: {len(clean_records)}"
        )

        unique_records = remove_duplicates(
            clean_records
        )

        logger.info(
            f"After duplicate removal: {len(unique_records)}"
        )

        data = calculate_sale_totals(
            unique_records
        )

        summary = calculate_summary(
            data
        )

        employees = employee_summary(
            data
        )

        products = product_summary(
            data
        )

        logger.info(
            f"After processing: {len(data)} records"
        )

        logger.info(
            "Data processing completed"
        )


        # ==========================================
        # PART 4 - EXCEL REPORT
        # ==========================================

        logger.info(
            "Generating Excel report..."
        )

        workbook = create_workbook()

        create_sales_sheet(
            workbook,
            data
        )

        create_summary_sheet(
            workbook,
            summary
        )

        create_employee_sheet(
            workbook,
            employees
        )

        create_product_sheet(
            workbook,
            products
        )

        output_file = (
            output_folder /
            "sales_report.xlsx"
        )

        save_workbook(
            workbook,
            output_file
        )

        logger.info(
            f"Excel report created: {output_file}"
        )


        # ==========================================
        # PART 5 - PDF REPORT
        # ==========================================

        logger.info(
            "Generating PDF report..."
        )

        pdf_file = (
            output_folder /
            "sales_report.pdf"
        )

        generate_pdf(
            pdf_file,
            data,
            summary,
            employees,
            products
        )

        logger.info(
            f"PDF report created: {pdf_file}"
        )


        # ==========================================
        # PART 6 - EMAIL
        # ==========================================

        logger.info(
            "Preparing email..."
        )

        message = create_email()

        attach_file(
            message,
            output_file
        )

        attach_file(
            message,
            pdf_file
        )

        logger.info(
            "Sending email..."
        )

        send_email(
            message
        )

        logger.info(
            "Email sent successfully"
        )


        # ==========================================
        # SUCCESS
        # ==========================================

        logger.info(
            "===================================="
        )

        logger.info(
            "Automation completed successfully"
        )

        logger.info(
            "===================================="
        )

        print(
            "Automation completed successfully!"
        )

        return {
            "success": True,
            "data": data,
            "summary": summary,
            "employees": employees,
            "products": products,
            "excel_file": output_file,
            "pdf_file": pdf_file
        }



    except Exception as e:

        logger.error(
            f"Automation failed: {e}"
        )

        logger.exception(
            "Full error details:"
        )

        print(
            "Automation failed!"
        )

        print(
            "Check logs/automation.log"
        )


if __name__ == "__main__":
    main()