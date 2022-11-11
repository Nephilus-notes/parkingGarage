﻿# Start Your Code here

text = {
    "garage_full": "Sorry, our parking garage is full! Please come back soon.",
}

class CarGarage:
    def __init__(self, tickets=100, parking_spaces=100, price=1.20):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = {'paid':"False in_garage"}
        self.price = price
        

    def take_ticket(self):
        if self.tickets > 0:
            self.tickets -= 1
            self.parking_spaces -= 1
            print(f"spaces left = {self.parking_spaces}")
        else:
            print(text["garage_full"])
    
    def pay_for_parking(self):
        self.current_ticket['paid'] = "False in_garage"
        hours = input("How many hours were you parked today? ")
        while True:
            try:
                if float(hours): 
                    print(f'{"~="*8}')
                    print(f'Your total for the day is: ${float(hours)*self.price}')
                    print(f'{"~="*8}')

                    input("""Lucky you! Our currency acceptance machine is broken and you don't have to pay.\n 
                    You have 15 minutes to leave!
                        [Press Enter]""")
                    self.current_ticket['paid'] = 'True Leave Garage'
                    print("""
                    Thank you, have a nice day!""")
                    break
            except ValueError:
                hours = input("Sorry, that wasn't a number. Try again.")
        self.tickets += 1
        self.parking_spaces += 1


The_Parking_Garage = CarGarage()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
            
        
The_Parking_Garage.pay_for_parking()