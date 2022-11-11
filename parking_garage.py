from text_parking_garage import text as txt

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
            print(txt["tic_num_assign"].format(ticket=ticket))
            self.current_ticket[ticket] = {"paid": "False in garage", 'price': self.price}
        else:
            print(txt["garage_full"])
    
    def pay_for_parking(self):
        tic_num = input(txt["tic_num_prompt"])
        while True:
            try:
                if int(tic_num) <= 1 or int(tic_num) > self.max_ticket:
                    raise ValueError
                else:
                    tic_num = int(tic_num)
                    break
            except (ValueError):
                tic_num = int(input(txt["tic_wrong_prompt"].format(tics_left = 1, max_tics=self.max_ticket)))
        if self.current_ticket[tic_num]['paid'] == "True Leave Garage":
            print(txt["already_paid"])
            return
        else:
            print(txt["payment_needed"])
            
        hours = input(txt["time_parked_prompt"])
        while True:
            try:
                if float(hours): 
                    total = float(hours)*self.current_ticket[tic_num]["price"]
                    print(txt["border"])
                    print(txt['total'].format(total=total))
                    print(txt["border"])
                    input(txt["leave"])
                    self.current_ticket[tic_num]['paid'] = 'True Leave Garage'
                    print(txt["Thanks"])
                    self.tickets.append(tic_num)
                    break
            except ValueError:
                hours = input(txt["time_wrong_prompt"])

    def leave_garage(self):
        tic_num = input(txt["tic_num_prompt"])
        while True:
            try:
                if int(tic_num) <= 1 or int(tic_num) > self.max_ticket:
                    raise ValueError
                else:
                    tic_num = int(tic_num)
                    break
            except (ValueError):
                tic_num = int(input(txt["tic_wrong_prompt"].format(tics_left=1, max_tics=self.max_ticket)))
        if self.current_ticket[tic_num]['paid'] == "True Leave Garage":
            print(txt["Thanks"])
            self.parking_spaces.append(tic_num)
            del self.current_ticket[tic_num]
        else:
            print(txt["payment_needed2"])
        
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
            elif owner_task == "tt":
                self.take_ticket()
            elif owner_task == "pp":
                self.pay_for_parking()
            elif owner_task == "lg":
                self.leave_garage()
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