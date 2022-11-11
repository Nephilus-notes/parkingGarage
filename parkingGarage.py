# Start Your Code here

text = {
    "garage_full": "Sorry, our parking garage is full! Please come back soon.",
}

class CarGarage:
    def __init__(self, tickets=100, parking_spaces=100, space_cost=3.45):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = {'paid':"False in_garage"}
        

    def take_ticket(self):
        if self.tickets > 0:
            self.tickets -= 1
            self.parking_spaces -= 1
            self.current_ticket['paid'] = "False in_garage"
            print(f"spaces left = {self.parking_spaces}")
        else:
            print(text["garage_full"])
    
    def pay_for_parking(self):
        price = input("How much does your ticket cost today?")
        while True:
            try:
                if int(price): 
                    print("Your ticket has been paid. You have 15 minutes to leave!")
                    self.current_ticket['paid'] = 'True Leave Garage'
                    print("Thank you, have a nice day!")
                    break
            except ValueError:
                price = input("Sorry, that wasn't a number. Try again.")
        self.tickets += 1
        self.parking_spaces += 1


The_Parking_Garage = CarGarage()
The_Parking_Garage.take_ticket()
            
        
The_Parking_Garage.pay_for_parking()