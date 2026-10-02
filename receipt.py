from pyscript import document
from datetime import datetime

customer_name = document.getElementById("customer")
cash_paid = document.getElementById("cash")
result_box = document.getElementById("output")
error_box = document.getElementById("order-error")

PRICES = {
	"Ulam": 250,
	"Beverages": 150,
	"Snacks": 150,
	"Candy": 500,
}


def click(event):
	error_box.textContent = ""
	customer = customer_name.value.strip()
	if not customer:
		error_box.textContent = "Enter the customer name."
		return

	items = []
	total = 0
	for row in document.querySelectorAll(".menu-item"):
		checkbox = row.querySelector("input[type='checkbox']")
		if not checkbox.checked:
			continue

		try:
			quantity = int(row.querySelector(".menu-quantity").value)
		except ValueError:
			error_box.textContent = "Enter a quantity of 1 or more for each selected item."
			return
		if quantity < 1:
			error_box.textContent = "Enter a quantity of 1 or more for each selected item."
			return

		item_name = checkbox.value
		subtotal = PRICES[item_name] * quantity
		total += subtotal
		items.append(f"{item_name} x {quantity}: ₱{subtotal}")

	if not items:
		error_box.textContent = "Select at least one menu item."
		return

	try:
		cash = int(cash_paid.value)
	except ValueError:
		error_box.textContent = "Enter the cash received."
		return
	if cash < total:
		error_box.textContent = "Cash received is less than the total."
		return

	lines = [
		"-------------------RECEIPT----------------",
		datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
		"------------------------------------------",
		f"Customer: {customer}",
		*items,
		f"Total: ₱{total}",
		f"Cash: ₱{cash}",
		f"Change: ₱{cash - total}",
	]
	result_box.textContent = "\n".join(lines)