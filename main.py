user_one = {
    "full_name": "Sheldon Cooper",
    "user_name": "Bazinga",
    "password": "Stringtheory",
    "account_balance": 5000,
    "connected_banks": [
        ("Chase",10000),
        ("Discover",7500)
    ]
}

user_two = {
    "full_name": "Howard Wolowitz",
    "user_name": "Engineer",
    "password": "Nasamission",
    "account_balance": 950,
    "connected_banks": [
        ("Regions",4500),
        ("Citigroup",15450)
    ]
}


def bank_transaction ():
    username = input("What is your username?")
    password_right = input("What is your password?")
    if username != (user_one.get("user_name")) and password_right != (user_one.get("password")) :
        print("Please check the username and password.")
        username = input("What is your username?")
        password_right = input("What is your password?")
    if username == (user_one.get("user_name")) and password_right == (user_one.get("password")):
        print("You are now logged into your account.")
    print("This is your current information on your account........")
    print("Your available balance is ",(user_one.get("account_balance")))
    print("The funds available in the connect accounts are:")
    for bank in user_one["connected_banks"]:
      bank_name ,balance = bank
      print(f"{bank_name}: $ {balance} ")
    name = user_two["full_name"]
    transfer = input(f"Would you like to transfer money to {name}?")
    if transfer != "yes":
        transfer = input(f"Would you like to transfer money to {name}?")
    if transfer == "yes":
        transfer_amount = input("How much would you like to transfer?")
        money = int(transfer_amount)
    if money > user_one["account_balance"] :
        print("You do not have enough funds.")
        transfer_amount = input("How much would you like to transfer?")
    if money < user_one["account_balance"] :
        money_after_transfer = user_one["account_balance"] - money
        user_two["account_balance"]= user_two["account_balance"] + money
        transfer = input(f"Would you like to transfer money to {name}?")
        print(user_one["full_name"],"has an account balance of", money_after_transfer, "Have a great day!")
        
       

    

bank_transaction()
