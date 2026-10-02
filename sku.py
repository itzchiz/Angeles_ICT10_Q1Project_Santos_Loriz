from pyscript import document


SKU_CODES= {
    "Keychains": "KC",
    "Beverages": "BE",
    "Snacks": "SN",
    "Baggies": "BG",
}

category_input = document.getElementById("category")
name_input = document.getElementById("product-name")
quantity_input = document.getElementById("quantity")
result_box = document.getElementById("output")

def click(event):
    category = category_input.value
    name = name_input.value.strip()
    quantity = quantity_input.value.strip()

    if not category or not name or not quantity:
        result_box.textContent = "Please fill in all fields."
        return

    if len(name) < 3:
        result_box.textContent = "Product name must have at least 3 characters."
        return

    if category not in SKU_CODES:
        result_box.textContent = "Invalid category selected."
        return

    try:
        quantity_int = int(quantity)
        if quantity_int < 1 or quantity_int > 999:
            raise ValueError
    except ValueError:
        result_box.textContent = "Quantity must be a whole number from 1 to 999."
        return

    sku = f"{SKU_CODES[category]}{name[:3].upper()}{quantity_int:03d}"
    result_box.textContent = f"Generated SKU: {sku}"
