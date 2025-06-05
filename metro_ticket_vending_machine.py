import json
class MetroVendingMachine:
    
    def __init__(self):
        self.metro1 = ["VASTRAL_GAM", "NIRANT_CROSS_ROAD", "VASTRAL", "RABARI_COLONY", "AMARAI_VADI", 
                       "APERAL_PARK", "KAKARIYA_EAST", "KALUPUR", "GHEE_KANTA", "SHAHPUR", 
                       "OLD_HIGHCOURT", "S_P_STADIUM", "COMMERCE_SIX_ROAD", "GUJARAT_UNIVERCITY", 
                       "GURUKUL_ROAD", "DURDARSHAN_CENTER", "THALTEJ", "THALTEJ_GAM"]
        self.metro2 = ["APMC", "JIVRAJ", "RAJIVNAGAR", "SHREYAS", "PALADI", "GANDHIGRAM", 
                       "OLD_HIGHCOURT", "USMANPURA", "VIJAYNAGAR", "VADAJ", "RANIP", 
                       "SABARMATI_RAILWAY_STATION", "AEC", "SABARMATI", "MOTERA_STADIUM"]
        self.start_station = None
        self.end_station = None
        self.interchange = None
        self.distance = 0
        self.base_price = 0
        self.total_price = 0

    def set_data(self, s1, s2):
        self.start_station = s1
        self.end_station = s2

    def whole_route(self):
        print("""                ===============================================================================================================================================================================    
                                                                                  Ahmedabad Metro Route                                            
                ===============================================================================================================================================================================    
                                                                                                                                              (> section 3 <)")    
                                                                                                        |----gandhigram----paladi----shreyas----rajivnagar----jivrajpark----APMC---->   
                                (> section 2 <)                                                         |                                                                              
      <----thaltej gam===thaltej===durdarshan centar===gurukul road===commerce six road===SP stedium===(@)===shahpur===ghee kanta===kalupur===kakariya east===aperal park===ameraivadi   
                                                                                                 (old highcourt)                         (> section 4 <)                          |    
                                                                                                        |                                                                         |   
                                                                                                        |               <----vastral gam===nirant cross road===vastral===rabari colony   
                       AEC----sabarmati railway station----ranip----vadaj----vijaynagar----usmanpura----|                                             
                         |                 (> section 1 <)   
                         |    
                         |----sabarmati----motera stedium---->   
                =================================================================================================================================================================================""")

    def timetable(self):

        Mt=int(input("enter metro number to see timetable \n1.for metro 1 \n2.for metro 2 \nenter your choice"))
        print("============================================time table========================================================")
        if Mt==1:
            print("time table for metro 1 from thaltej gam to vastral gam")
            print("===================================train frequency=========================================================")
            print("train time on normal days  :  train avalible in every 9 minutes")
            print("train time on weekends and holidays :  train avalible in every 12 minutes")
            print("\n\n")
            print("===================================train Departure Time=========================================================")
            print("departure first train. \n 6:20 from vastral gam to thaltej gam\n 6:25 from thaltej gam to vastral gam ")
            print("departure last train. \n 22:00 from vastral gam to thaltej gam\n 22:05 from thaltej gam to vastral gam ")
            print("\n\n")
            print("===================================train run Time=========================================================")
            print("train run time for metro 1: 45 minutes ")
        elif Mt==2:
            print("time table for metro 2 from APMC to Motera stadium")
            print("===================================train frequency=========================================================")
            print("train time on normal days  :  train avalible in every 10 minutes")
            print("train time on weekends and holidays :  train avalible in every 12 minutes")
            print("\n\n")
            print("===================================train Departure Time=========================================================")
            print("departure first train. \n 6:20 from apmc to Motera stadium\n 6:25 from Motera stadium gam to APMC ")
            print("departure last train. \n 22:10 from Apmc to Motera Stadium\n 22:05 from Motera stadium to APMC ")
            print("\n\n")
            print("===================================train run Time=========================================================")
            print("train run time for metro 2: 33 minutes ")
        else:
            print("invalid input")




            
    def section(self, i):
        sections = {
            1: ["usmanpura", "vijaynagar", "vadaj", "ranip", "sabarmati railway station", "AEC", "sabarmati", "motera stadium"],
            2: ["S P stedium", "commerce six road", "gujarat univercity", "gurukul road", "durdarshan center", "thaltej", "thaltej gam"],
            3: ["gandhigram", "paladi", "shreyas", "rajivnagar", "jivraj", "APMC"],
            4: ["shahpur", "gee kanta", "kalupur", "kankariya east", "aperal park", "amarai vadi", "rabari colony", "vastral", "nirant cross road", "vastral gam"]
        }
        if i in sections:
            print(f"===============================")
            print(f"        : section {i} :")
            print(f"===============================")
            for j in sections[i]:
                print(j)

            print("===============================")
        else:
            print("Invalid section number.")

    def find_index(self, metro, station):
        try:
            return metro.index(station)
        except ValueError:
            return -1

    def get_distance(self, metro, s1, s2):
        starting_index = self.find_index(metro, s1)
        ending_index = self.find_index(metro, s2)
        if starting_index != -1 and ending_index != -1:
            return abs(ending_index - starting_index)
        else:
            return -1

    def is_interchange_needed(self):
        start_in_metro1 = self.start_station in self.metro1
        end_in_metro1 = self.end_station in self.metro1
        start_in_metro2 = self.start_station in self.metro2
        end_in_metro2 = self.end_station in self.metro2

        if start_in_metro1 and end_in_metro1:
            self.interchange = 1
        elif start_in_metro2 and end_in_metro2:
            self.interchange = 2
        elif start_in_metro1 and end_in_metro2:
            self.interchange = 3
        else:
            self.interchange = 4

    def final_distance(self, d1, d2):
        self.is_interchange_needed()
        if self.interchange == 1:
            self.distance = d1
        elif self.interchange == 2:
            self.distance = d2
        elif self.interchange == 3:
            distance_on_metro1 = self.get_distance(self.metro1, self.start_station, "OLD_HIGHCOURT")
            distance_on_metro2 = self.get_distance(self.metro2, "OLD_HIGHCOURT", self.end_station)
            self.distance = distance_on_metro1 + distance_on_metro2
        elif self.interchange == 4:
            distance_on_metro3 = self.get_distance(self.metro2, self.start_station, "OLD_HIGHCOURT")
            distance_on_metro4 = self.get_distance(self.metro1, "OLD_HIGHCOURT", self.end_station)
            self.distance = distance_on_metro3 + distance_on_metro4

    def find_price(self, use_card):
        distance1 = self.get_distance(self.metro1, self.start_station, self.end_station)
        distance2 = self.get_distance(self.metro2, self.start_station, self.end_station)
        self.final_distance(distance1, distance2)

        if self.distance <= 4:
            self.base_price = 5
        elif self.distance <= 8:
            self.base_price = 10
        elif self.distance <= 12:
            self.base_price = 15
        elif self.distance <= 16:
            self.base_price = 20
        else:
            self.base_price = 25

        if use_card:
            self.total_price = self.base_price - (self.base_price * 0.10)
        else:
            self.total_price = self.base_price

    def display(self):
        print(f"\nStarting station is {self.start_station}.")
        print(f"Ending station is {self.end_station}.")
        print(f"\nPrice of your ticket will be {self.total_price} from {self.start_station} to {self.end_station}")
    
    def get_token(self, payment_type):
        self.find_price(False)
        f=open('data.txt','a')
        data=self.start_station+" to "+self.end_station+" price will be "+str(self.total_price)
        
        self.display()
        if payment_type == 1:
            print("\nenter cash in machine.")
            money=int(input("insert "))
            if money==self.total_price:
                print("Your ticket is confirmed.")
                f.write(data+"\n")
                print("Take token from machine.")
                print("It will be valid for 120 minutes.\n")
            elif money>self.total_price:
                change=money-self.total_price
                print("plese collect your change",change,"rupee")
                print("Your ticket is confirmed.")
                f.write(data+"\n")
                print("Take token from machine.")
                print("It will be valid for 120 minutes.\n")
            else:
                print("add sufficient money to buy a ticket")
            
        elif payment_type==2:
            print('==========enter card details to get travel token=========')
            cardNumber=input("enter your card number")
            print("Your ticket is confirmed.")
            f.write(data+"\n")
            print("Take token from machine.")
            print("It will be valid for 120 minutes.\n")
            if len(cardNumber)==16 or cardNumber.isnumeric():
                print("your card details are match")
                print("Your ticket is confirmed.")
                f.write(data+"\n")
                print("Take token from machine.")
                print("It will be valid for 120 minutes.\n")
            else:
                print("Your card details are wrong")
        else:
            print('invalid input')

machine = MetroVendingMachine()
print("\n<-------Welcome to our system------->")
while True:
    print("\n1) To see whole route of Ahmedabad metro press 1.")
    print("2) To see timetable of Ahmedabad metro press 2.")
    print("3) To see all stations of particular section press 3.")
    print("4) To find price of ticket between two stations press 4.")
    print("5) To get traveling token press 5.")
    print("6) To exit the program press 6.")
    choice = input("Enter your choice: ")
    try:
        choice = int(choice)
        if choice == 1:
            machine.whole_route()
        elif choice==2:
            machine.timetable()
        elif choice == 3:
            section_number = int(input("Enter section number: "))
            machine.section(section_number)
        elif choice == 4:
            s1 = input("Enter starting station: ").strip().upper()
            s2 = input("Enter ending station: ").strip().upper()
            if (s1 in machine.metro1 or s1 in machine.metro2) and (s2 in machine.metro1 or s2 in machine.metro2):
                use_card = input("Will you use a metro card? 'yes' or 'no': ").strip().lower() == 'yes'
                machine.set_data(s1, s2)
                machine.find_price(use_card)
                machine.display()
            else:
                print("One or both stations not found.")
        elif choice == 5:
            st1 = input("Enter starting station: ").strip().upper()
            st2 = input("Enter ending station: ").strip().upper()
            if (st1 in machine.metro1 or st1 in machine.metro2) and (st2 in machine.metro1 or st2 in machine.metro2):
                payment_type = int(input("Would you like to pay with:\n1. Cash\n2. Payment card\nEnter your choice: "))
                machine.set_data(st1, st2)
                machine.get_token(payment_type)
            else:
                print("One or both stations not found.")
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
