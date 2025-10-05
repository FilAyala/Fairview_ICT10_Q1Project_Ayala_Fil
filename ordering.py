from js import document
from pyscript import document, display

def generate_total_price(e):
    _name = document.getElementById("input_name").value
    _address = document.getElementById("input_address").value
    _contact = document.getElementById("input_contact").value

    TOTAL = 0

    if document.getElementById("product_1").checked:
        TOTAL += int(document.getElementById("product_1").value)

    if document.getElementById("product_2").checked:
        TOTAL += int(document.getElementById("product_2").value)

    if document.getElementById("product_3").checked:
        TOTAL += int(document.getElementById("product_3").value)

    if document.getElementById("product_4").checked:
        TOTAL += int(document.getElementById("product_4").value)

    if document.getElementById("product_5").checked:
        TOTAL += int(document.getElementById("product_5").value)

    message = f"""
    \n Name: {_name}
    \n Address: {_address}
    \n Contact Number: {_contact}
    \n Total Price: ₱{TOTAL}
"""
    display(message, target="DETAILS")