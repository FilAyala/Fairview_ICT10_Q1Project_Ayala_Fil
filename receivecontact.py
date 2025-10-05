from js import document
from pyscript import display, display


def generate_messagesent(e):
    _name = document.getElementById("input_name").value
    _address = document.getElementById("input_address").value
    _contact = document.getElementById("input_contact").value
    _email = document.getElementById("emailselect").value
    _message = document.getElementById("enterusermessage").value


    message = f"""
    \n Name: {_name}
    \n Address: {_address}
    \n Contact Number: {_contact}
    \n Email sent to: {_email}
    \n Message received: {_message}
    \n \t Thank you for your message!
"""
    display(message, target="usermessage")