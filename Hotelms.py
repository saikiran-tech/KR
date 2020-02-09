print("   Hotel Management Project ")
class Hoteldetails():
    
    def __init__(self, room_rent=0, restaurent_bill=0, laundry_bill=0, game_bill=0, c_name, c_adress, c_mobile, total_bill, checkin_date, checkout_date ):
        self.room_rent = room_rent
        self.restaurent_bill = restaurent_bill
        self.laundry_bill = laundry_bill
        self.game_bill = game_bill
        self.c_name = c_name
        self.c_adress = c_adress
        self.c_mobile = c_mobile
        self.total_bill = total_bill
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
    
    def customer_data(self):
        self.c_name=input("Enter customer's name: ")
        self.c_adress=input(" Enter adress: ")
        self.c_mobile=input(" ENter the mobile number: ")
        self.checkin_date=input(" Enter the check in date: ")
        self.checkout_date=input(" Enter the check out date: ")
        
    def room_rent(self):
        
        room_type = {1: "AC room", 2: "Deluxe", 3: "Non AC room"}
        x = int(input(" Select the room: "))
        y = int(input(" Enter the no.of days of stay: "))
        if room_type==1:
            print(" Rent: 3000")
            self.room_rent = 3000*y
        elif room_type==2:
            print(" Rent: 2000")
            self.room_rent = y*2000
        elif room_type==3:
            print(" Rent: 1000")
            self.room_rent = y*1000
        else:
            print(" Select the room: ")
            
    
    def restaurent_bill(self):
        Menu = {A:"Breakkfast: Rs.100", B:"Lunch: Rs.200", C:"Dinner: Rs.200"}
        print(Menu)
        food_price = {A:100,B:200, C:200}
        food = input(" Select the menu: ")
        N = int(input(" Enter the no.of persons: "))
        if food==A:
            print(A*N)
        elif food==B:
            print(B*N)
        elif food==C:
            print(C*N) 
        else:
            print(" Select the Menu: ")
        self.restaurent_bill = (A*N + B*N + C*N)
    
    def game_bill(self):
        print("Tennis: Rs.100, Chess: Rs.150, Basket_ball: Rs.200")
        Games = {A: "Tennis", B: "Chess", C: "Basket_ball"}
        G = input(" Select the game: ")
        while True:
            if G== 'A':
                self.game_bill = 100
            elif G== 'B':
                self.game_bill = 150
            elif G== 'c':
                self.game_bill = 200
                break
            else:
                print("Select the game: ")
                
     def laundry_bill(self):
         print("1: Men's dress, 2: Women's dress, 3: children dress")
         Items = {1: "Men's dress", 2: "Women's dress", 3: "chidren dress" }
         L = input(" Select the item: ")
         while True:
             if L== 1:
                self.laundry_bill = 50
             elif L== 2:
                self.laundry_bill = 60
             elif L == 3:
                self.laundry_bill = 50
             break
         else:
             print(" Select an item ")
                    
            
      def total_bill(self):
          self.total_bil = self.room_rent+ self.game_bill+ self.laundry_bill+ self.restaurent_bill
          print(self.total_bill)
          

def main():
    HM = Hoteldetails()
    while true:
        print("1:Enter customer details: ")
        print("2:Enter the room number: ")
        print("3:Total bill: ")
        choose = input("Enter your choise ")
        if choose==1:
            HM.customer_data()
        elif choose==2:
            print(x)
        elif choose==3:
            HM.total_bill()
        