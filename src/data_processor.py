def validate_record(item):

    required_fields = [
        "date",
        "employee",
        "product",
        "quantity",
        "price"
    ]

    for field in required_fields:

        if item.get(field) is None:
            print(f"Missing field: {field}")
            return False

    try:
        quantity = float(item["quantity"])
        price = float(item["price"])

    except (TypeError, ValueError):

        print("Invalid quantity or price")
        return False

    if quantity <= 0:
        print("Invalid quantity")
        return False

    if price <= 0:
        print("Invalid price")
        return False

    return True


def clean_data(data):

    clean_records = []

    for item in data:

        if validate_record(item):

            clean_records.append(item)

        else:

            print(
                f"Skipping invalid record: {item}"
            )

    return clean_records


def remove_duplicates(data):

    unique_records = []
    seen = set()

    for item in data:

        record_key = (
            item["date"],
            item["employee"],
            item["product"],
            item["quantity"],
            item["price"]
        )

        if record_key not in seen:

            seen.add(record_key)

            unique_records.append(item)

        else:

            print(
                f"Duplicate record skipped: {item}"
            )

    return unique_records


def calculate_sale_totals(data):

    for item in data:

        item["quantity"] = float(
            item["quantity"]
        )

        item["price"] = float(
            item["price"]
        )

        item["total"] = (
            item["quantity"] *
            item["price"]
        )

    return data


def calculate_summary(data):

    if not data:
        return {}

    total_revenue = sum(
        item["total"]
        for item in data
    )

    total_quantity = sum(
        item["quantity"]
        for item in data
    )

    sales_values = [
        item["total"]
        for item in data
    ]

    average_sale = (
        total_revenue / len(data)
    )

    highest_sale = max(
        sales_values
    )

    lowest_sale = min(
        sales_values
    )

    employees = set(
        item["employee"]
        for item in data
    )

    products = set(
        item["product"]
        for item in data
    )

    return {
        "total_revenue": total_revenue,
        "total_quantity": total_quantity,
        "average_sale": average_sale,
        "highest_sale": highest_sale,
        "lowest_sale": lowest_sale,
        "number_of_employees": len(employees),
        "number_of_products": len(products),
        "total_records": len(data)
    }


def employee_summary(data):

    summary = {}

    for item in data:

        employee = item["employee"]

        if employee not in summary:

            summary[employee] = {
                "total_sales": 0,
                "total_quantity": 0,
                "number_of_orders": 0
            }

        summary[employee]["total_sales"] += (
            item["total"]
        )

        summary[employee]["total_quantity"] += (
            item["quantity"]
        )

        summary[employee]["number_of_orders"] += 1

    return summary


def product_summary(data):

    summary = {}

    for item in data:

        product = item["product"]

        if product not in summary:

            summary[product] = {
                "total_sales": 0,
                "total_quantity": 0,
                "number_of_orders": 0
            }

        summary[product]["total_sales"] += (
            item["total"]
        )

        summary[product]["total_quantity"] += (
            item["quantity"]
        )

        summary[product]["number_of_orders"] += 1

    return summary