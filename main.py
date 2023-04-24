user_one = {
    "full_name": "Sheldon Cooper",
    "user_name": "Bazinga",
    "password": "Stringtheory",
    "account_balance": "5000",
    "connected_banks": [
        ("bank-one", {"bank_name": "Chase", "available_balance": 10000}),
        ("bank-two", {"bank_name": "Discover", "available_balance": 7500})
    ]
}

user_two = {
    "full_name": "Howard Wolowitz",
    "user_name": "Engineer",
    "password": "Nasamission",
    "account_balance": "950",
    "connected_banks": [
        ("bank-one", {"bank_name": "Regions", "available_balance": 4500}),
        ("bank-two", {"bank_name": "Citigroup", "available_balance": 15450})
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
    for bank,balance in user_one:
     bank = user_one["connected_banks"][0][1]["bank_name"]
     balance = user_one["connected_banks"][0][1]["available_balance"]
     print(bank,":","$",balance,"available" )
    
       

    

bank_transaction()
