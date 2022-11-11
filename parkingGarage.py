# Start Your Code here

text = {
    "garage_full": "Sorry, our parking garage is full! Please come back soon.",
}

class CarGarage:
    def __init__(self, tickets=100, parking_spaces=100, space_cost=3.45):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = {}
        

    def take_ticket(self):
        if self.tickets > 0:
            self.tickets -= 1
            self.parking_spaces -= 1
            self.pay_for_parking()
        else:
            print(text["garage_full"])
    
    def pay_for_parking(self):
        input("")
