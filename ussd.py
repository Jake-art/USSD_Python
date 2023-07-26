def process_input(text):
    if text == "234":

        response = "CON What do you want to check?\n"
        response += "1. My Account No.\n"
        response += "2. My Phone Number.\n"
    elif text in "1":

        response = "CON Choose account information.\n"
        response += "1. Account Number.\n"
        response += "2. Account Balance.\n"
    elif text == "1*1":
        # Second level
        accountNumber = "ACC001"
        response = "END Your account Number is: " + accountNumber
    elif text == "1*2":
        balance = "KES 100,000"
        response = "END Your balance is: " + balance
    elif text == "2":
        phone = "0722352740"
        response = "END Your phone is: " + phone
    else:
        # Default response if no matching condition is found
        response = "END Invalid input."

    return response


if __name__ == '__main__':
    while True:
        user_input = input("Enter input: ")
        response = process_input(user_input)
        print(response)
