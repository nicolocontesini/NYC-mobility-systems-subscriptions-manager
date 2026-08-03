
active_subscriptions = {}


purchasable = """
Available subscriptions are the following
=========================================
SERVICE      MONTHLY PRICE

MTA          $70
TAXI         $175
LYFT         $100
CITI BIKE    $90
=========================================
"""



services = {
    "MTA": 70, 
    "TAXI": 175,  
    "LYFT": 100, 
    "CITI BIKE": 90
}
print(purchasable)
budget = float(input("Please enter budget:")) 



while True:
    required = input("Choose a service:")
    if required in active_subscriptions:
        print(required, "service is already on") 
    elif required == "exit":
        logout = input("Logging out: are you sure?")
        if logout == "yes":
            print("The following subscriptions are now active for the following months:", active_subscriptions)
            break
        elif logout == "no":
            print("Your choice:", required)
    elif required in services:
        print("Your choice:", required)
        if required == "LYFT":
            age = int(input("We have to be sure you are 21 or older: enter your age"))
            if 0 < age < 21:
                print("We are sorry, but the service is not available for you")
                print(required)
            elif age >= 21:
                months = int(input(f"For how many months would you like to use {required} service?"))
                amount = services[required] * months
                print("Months:", months)
                print("Amount to pay:", amount)
                if amount > budget:
                    print("Insufficient funds")
                    recharge = input("Do you want to recharge?") 
                    if recharge == "yes":
                        recharging = float(input("how much do you want to recharge?"))
                        budget += recharging
                        print("To be paid:", amount)
                        print("Residual budget:", budget)
                        print("Your choice:", required)
                        confirm = input(f"Do you want to purchase {required} for {months} months?")
                        if confirm == "yes":
                            active_subscriptions[required] = months
                            print("The following subscriptions are now active for the following months:", active_subscriptions)
                            budget -= amount
                            print("Residual budget:", budget)
                        elif confirm == "no":
                            print("Redirecting you to the home page")        
                    elif recharge == "no":
                        print("Residual budget:", budget)
                        print("Your choice:", required)
                        print("Redirecting you to the home page") 
                elif amount <= budget:
                    confirm = input(f"Do you want to purchase {required} for {months} months?")
                    if confirm == "yes":
                        budget -= amount
                        active_subscriptions[required] = months
                        print("The following subscriptions are now active for the following months:", active_subscriptions)
                        print("Residual budget:", budget)
                    elif confirm == "no":
                        print("Redirecting you to the home page") 
                    
        elif required == "MTA" or required == "TAXI" or required == "CITI BIKE":
            months = int(input(f"For how many months would you like to use {required} service?"))
            amount = services[required] * months      
            print("Months", months)
            print("Amount to pay:", amount)
            if amount > budget:
                print("Insufficient funds")
                recharge = input("Do you want to recharge?") 
                if recharge == "yes":
                    recharging = float(input("how much do you want to recharge?"))
                    budget += recharging
                    print("To be paid:", amount)
                    print("Residual budget:", budget)
                    print("Your choice:", required)
                    confirm = input(f"Do you want to purchase {required} for {months} months?")
                    if confirm == "yes":
                        active_subscriptions[required] = months
                        print("The following subscriptions are now active for the following months:", active_subscriptions)
                        budget -= amount
                        print("Residual budget:", budget)
                    elif confirm == "no":
                        print("Redirecting you to the home page")        
                elif recharge == "no":
                    print("Residual budget:", budget)
                    print("Your choice:", required)
                    print("Redirecting you to the home page") 
            elif amount <= budget:
                confirm = input(f"Do you want to purchase {required} for {months} months?")
                if confirm == "yes":
                    active_subscriptions[required] = months
                    print("The following subscriptions are now active for the following months:", active_subscriptions)
                    budget -= amount
                    print("Residual budget:", budget)
                elif confirm == "no":
                    print("Redirecting you to the home page") 

    else:
        print("Not available")
        print("The following subscriptions are now active for the following months:", active_subscriptions)