text = {
    "garage_full": "Sorry, our parking garage is full! Please come back soon.",
    "tic_num_assign":"Your ticket number is {ticket}",
    "tic_num_prompt": "What is your ticket number? ",
    "tic_wrong_prompt":"Check that number again. Needs to be between {tics_left} & {max_tics}: ",
    "Thanks":"""
                Thank you, have a nice day!""",
    "payment_needed": "You have not payed yet.",
    "time_parked_prompt": "And how many hours were you parked today? ",
    "border":'~='*8,
    'total': 'Your total for the day is: ${total:.2f}',
    'leave':"""Lucky you! Our currency acceptance machine is broken and you don't have to pay.\n 
                    You have 15 minutes to leave!
                        [Press Enter]""",
    "time_wrong_prompt": "Sorry, that wasn't a number. Try again.",
}

class CarGarage:
    def __init__(self, tickets=[i for i in range(1,101)], parking_spaces=[i for i in range(100)], price=1.20):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.price = price
        self.current_ticket = {}
        self.max_ticket = len(tickets)
        
    def take_ticket(self):
        if self.tickets:
            ticket=self.tickets.pop()
            self.parking_spaces.pop()
            print(text["tic_num_assign"].format(ticket=ticket))
            self.current_ticket[ticket] = {"paid": "False in garage", 'price': self.price}
        else:
            print(text["garage_full"])
    
    def pay_for_parking(self):
        tic_num = input(text["tic_num_prompt"])
        while True:
            try:
                if int(tic_num) <= len(self.tickets) or int(tic_num) > self.max_ticket:
                    raise ValueError
                else:
                    tic_num = int(tic_num)
                    break
            except (ValueError):
                tic_num = int(input(text["tic_wrong_prompt"].format(tics_left=len(self.tickets), max_tics=self.max_ticket)))
        if self.current_ticket[tic_num]['paid'] == "True Leave Garage":
            print(text["Thanks"])
        else:
            print(text["payment_needed"])
            
        hours = input(text["time_parked_prompt"])
        while True:
            try:
                if float(hours): 
                    total = float(hours)*self.current_ticket[tic_num]["price"]
                    print(text["border"])
                    print(text['total'].format(total=total))
                    print(text["border"])

                    input(text["leave"])
                    self.current_ticket[tic_num]['paid'] = 'True Leave Garage'
                    print(text["Thanks"])
                    self.tickets.append(tic_num)
                    self.parking_spaces.append(tic_num)
                    del self.current_ticket[tic_num]
                    break
            except ValueError:
                hours = input(text["time_wrong_prompt"])
        
    def change_price(self, new_price):
        self.price = new_price
        print(f"Price successfully changed! \nNew price: ${self.price} per hour")

    def check_tickets(self):
        print("\nYour outstanding tickets are:")
        for tic_num in self.current_ticket.keys():
            if tic_num not in self.tickets:
                print(f'{tic_num}')

    def owner_interface(self):
        while True:
            owner_task = input('What would you like to do? (Change [Price]/ Check [Tickets]/Quit) ').lower().strip()
            if owner_task == 'price':
                new_price = input("And what would you like the new price to be? ")
                self.change_price(new_price)
            elif owner_task == 'tickets':
                self.check_tickets()
            elif owner_task == 'quit':
                print("Thanks for using our software!\nGoodbye.")
                break
            else:
                print("Whoops, we didn't recognize that. Try again. [Enter]")


The_Parking_Garage = CarGarage()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
            
        
# The_Parking_Garage.pay_for_parking()

The_Parking_Garage.owner_interface()