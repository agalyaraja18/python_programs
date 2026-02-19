import re

def mask_credit_card(card_number):
    masked = re.sub(r'\d(?=\d{4})', '*', card_number)
    print("Masked Card Number:", masked)

card_no=input("Enter Card Number: ")
mask_credit_card(card_no)