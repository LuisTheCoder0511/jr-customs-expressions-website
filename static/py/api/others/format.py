import re

def currency(str_input):
    cleaned = str_input.strip().replace('$', '')

    # Check if it's a valid number using regex (digits with optional single decimal point)
    if not currency_match(cleaned):
        return "Error: Invalid currency format."

    try:
        # Convert to float and ensure it's not negative
        value = max(0.00, float(cleaned))
        # Format to two decimal places
        return f"{value:.2f}"
    except ValueError:
        return "Error: Could not convert to number."


def currency_match(str_input):
    return re.match(r'^\d*\.?\d*$', str_input)