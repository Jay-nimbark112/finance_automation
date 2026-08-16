from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)


def create_pdf(output_file):

    document = SimpleDocTemplate(
        str(output_file),
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm
    )

    return document


def get_styles():

    return getSampleStyleSheet()


def create_summary_table(summary):

    data = [
        ["Metric", "Value"],

        [
            "Total Revenue",
            f"Rs. {summary['total_revenue']:,.2f}"
        ],

        [
            "Total Quantity",
            summary["total_quantity"]
        ],

        [
            "Average Sale",
            f"Rs. {summary['average_sale']:,.2f}"
        ],

        [
            "Highest Sale",
            f"Rs. {summary['highest_sale']:,.2f}"
        ],

        [
            "Lowest Sale",
            f"Rs. {summary['lowest_sale']:,.2f}"
        ],

        [
            "Number of Employees",
            summary["number_of_employees"]
        ],

        [
            "Number of Products",
            summary["number_of_products"]
        ],

        [
            "Total Records",
            summary["total_records"]
        ]
    ]

    table = Table(
        data,
        colWidths=[80 * mm, 60 * mm]
    )

    table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.grey
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "ALIGN",
                (1, 1),
                (1, -1),
                "RIGHT"
            )
        ])
    )

    return table


def create_employee_table(employee_data):

    data = [
        [
            "Employee",
            "Total Sales",
            "Quantity",
            "Orders"
        ]
    ]

    for employee, values in employee_data.items():

        data.append([
            employee,
            f"Rs. {values['total_sales']:,.2f}",
            values["total_quantity"],
            values["number_of_orders"]
        ])

    table = Table(
        data,
        colWidths=[
            45 * mm,
            45 * mm,
            35 * mm,
            25 * mm
        ]
    )

    table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.grey
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "ALIGN",
                (1, 1),
                (-1, -1),
                "RIGHT"
            )
        ])
    )

    return table


def create_product_table(product_data):

    data = [
        [
            "Product",
            "Total Sales",
            "Quantity",
            "Orders"
        ]
    ]

    for product, values in product_data.items():

        data.append([
            product,
            f"Rs. {values['total_sales']:,.2f}",
            values["total_quantity"],
            values["number_of_orders"]
        ])

    table = Table(
        data,
        colWidths=[
            45 * mm,
            45 * mm,
            35 * mm,
            25 * mm
        ]
    )

    table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.grey
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "ALIGN",
                (1, 1),
                (-1, -1),
                "RIGHT"
            )
        ])
    )

    return table


def create_sales_table(data):

    table_data = [
        [
            "Date",
            "Employee",
            "Product",
            "Qty",
            "Price",
            "Total"
        ]
    ]

    for item in data:

        table_data.append([
            item["date"].strftime("%Y-%m-%d"),
            item["employee"],
            item["product"],
            item["quantity"],
            f"Rs. {item['price']:,.0f}",
            f"Rs. {item['total']:,.0f}"
        ])

    table = Table(
        table_data,
        repeatRows=1
    )

    table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.grey
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "FONTSIZE",
                (0, 0),
                (-1, -1),
                8
            ),
            (
                "ALIGN",
                (3, 1),
                (-1, -1),
                "RIGHT"
            )
        ])
    )

    return table


def generate_pdf(
    output_file,
    data,
    summary,
    employees,
    products
):

    document = create_pdf(output_file)

    styles = get_styles()

    elements = []

    # Title
    elements.append(
        Paragraph(
            "Sales Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    # Summary
    elements.append(
        Paragraph(
            "Report Summary",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 5)
    )

    elements.append(
        create_summary_table(summary)
    )

    elements.append(
        Spacer(1, 15)
    )

    # Employee Summary
    elements.append(
        Paragraph(
            "Employee Summary",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 5)
    )

    elements.append(
        create_employee_table(employees)
    )

    elements.append(
        Spacer(1, 15)
    )

    # Product Summary
    elements.append(
        Paragraph(
            "Product Summary",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 5)
    )

    elements.append(
        create_product_table(products)
    )

    elements.append(
        Spacer(1, 15)
    )

    # Sales Details
    elements.append(
        Paragraph(
            "Sales Details",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 5)
    )

    elements.append(
        create_sales_table(data)
    )

    document.build(elements)

    print(
        f"PDF report created: {output_file}"
    )