from text_parking_garage import text as txt, input_options as i_o

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
        try:
            if self.current_ticket[tic_num]['paid'] == "True Leave Garage":
                print(txt["already_paid"])
                return
            else:
                print(txt["payment_needed"])
        except (KeyError, ValueError):
            lo_key = self.max_ticket
            for key in self.current_ticket.keys():
                if key < lo_key:
                    lo_key = key
            tic_num = int(input(txt["tic_wrong_prompt"].format(tics_left=lo_key, max_tics=self.max_ticket)))
            
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
        lo_key = self.max_ticket
        for key in self.current_ticket.keys():
            if key < lo_key:
                lo_key = key
        while True:
            try:
                if int(tic_num) < lo_key or int(tic_num) > self.max_ticket:
                    raise ValueError
                else:
                    tic_num = int(tic_num)
                    break
            except (ValueError):
                tic_num = int(input(txt["tic_wrong_prompt"].format(tics_left=lo_key, max_tics=self.max_ticket)))
        if self.current_ticket[tic_num]['paid'] == "True Leave Garage":
            print(txt["Thanks"])
            self.parking_spaces.append(tic_num)
            del self.current_ticket[tic_num]
        else:
            print(txt["payment_needed2"])
        
    def change_price(self, new_price):
        self.price = new_price
        print(txt['price_change_success'].format(price=self.price))

    def check_tickets(self):
        print(txt['outstanding_tickets'])
        for tic_num in self.current_ticket.keys():
            if tic_num not in self.tickets:
                print(f'{tic_num}')

    def check_spots(self):
        cnt= len(self.current_ticket)
        print(txt['spots_left'].format(cnt=self.max_ticket-cnt))

    def owner_interface(self):
        while True:
            owner_task = input(txt['user_prompt']).lower().strip()
            if owner_task == 'price':
                new_price = input(txt['new_price'])
                self.change_price(new_price)
            elif owner_task in i_o['tickets']:
                self.check_tickets()
            elif owner_task in i_o['spots']:
                self.check_spots()
            elif owner_task in i_o['take ticket']:
                self.take_ticket()
            elif owner_task in i_o['pay for parking']:
                self.pay_for_parking()
            elif owner_task in i_o['leave garage']:
                self.leave_garage()
            elif owner_task in i_o['quit']:
                print(txt['user_thanks'])
                break
            else:
                print(txt['user_error'])


The_Parking_Garage = CarGarage(tickets=[i for i in range(1,360)])
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
The_Parking_Garage.take_ticket()
            
        
# The_Parking_Garage.pay_for_parking()

The_Parking_Garage.owner_interface()