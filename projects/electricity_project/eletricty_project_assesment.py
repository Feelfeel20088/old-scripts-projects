import random

class Utility:
    
    def __init__(self) -> None:
        self.year = 100
        self.add_funds = 2000000
        self.pollution = 0
        self.bad_event_list = ["riots", "lower_yearly_funds", "crop_harvest_failed"]
        self.good_event_list = ["raise_yearly_funds", ]
        self.plants_list = ["nuclear", "coal", "natural_gas", "solar_field"]
        self.commands_list = ["help", "c", "cp", "np", "p", "pp", "add", "gb", "y"]
        
        self.good_event = {"raise_yearly_funds" : self.raise_yearly_funds}
        self.bad_event = {"riots" : self.riots, "lower_yearly_funds" :self.lower_yearly_funds, "crop_harvest_failed" : self.crop_harvest_failed}
        self.commands = {"help": self.help, "c": self.display_cash, "cp": self.display_current_power, "np": self.display_needed_power, "p": self.display_pollution, "pp": self.display_power_plant, "add": self.power_plant_add, "gb" : self.display_goodbad_event, "y" : self.end_year}
        
        self.data = {"funds": 100000000, "current_power": 0, "needed_power": 12500, "pollution_yearly": 0, "good_event_factor": 0, "bad_event_factor": 0}
       
        self.power_plants = {"nuclear": {"price": 650000000, "carbon_emission": 0.0005, "how_many": 0, "power": 350, "bad_event_factor": 0.005, "good_event_factor": 0}, 
                             "coal": {"price": 1300000, "carbon_emission": 0.005, "how_many": 0, "power": 40, "bad_event_factor": 0.010, "good_event_factor": 0},
                             "natural_gas": {"price": 1700000, "carbon_emission": 0.004, "how_many": 0, "power": 50, "bad_event_factor": 0.007, "good_event_factor": 0},
                             "solar_field": {"price": 1500000, "carbon_emission": 0, "how_many": 0, "power": 10, "bad_event_factor": 0, "good_event_factor": 0.05}}
        
    def help(self):
        print("# help = display all commands.\n# c = display your current funds.\n# cp = display your current power production.\n# np = display the world's needed power.\n# p = display current pollution.\n# pp = display power plant names and their stats.\n# gb = display your good and bad event factors\n# add = add apowerplant to produce eletricity!\n# y = end a year and retrive funds, make sure to meet your needed power before ending")
        
    def caller(self, command):
        self.commands[command]()
    
    def display_plants(self):
        print(self.plants_list)
        
    def display_cash(self):
        print(self.data["funds"])
        
    def display_current_power(self):
        print(f"{self.data['current_power']} (in megawatts)")
        
    def display_needed_power(self):
        print(f"{self.data['needed_power']} (in megawatts)")
        
    def display_pollution(self):
        print(f"pollution yearly: {self.data['pollution_yearly']}\npollution: {self.pollution}")
        
    def display_power_plant(self):
        print(self.plants_list)
        print(self.power_plants)
    
    def display_goodbad_event(self):
        print(f"good event factor: {self.data['good_event_factor']}\nbad event factor: {self.data['bad_event_factor']}")
        

class events(Utility):
    def bad_event_gen(self, how_many, power_plant_dict, power_plant_name):
       
        if random.random() < self.data["bad_event_factor"]:
            x = random.choice(self.bad_event_list)
            self.bad_event[x](how_many, power_plant_dict, power_plant_name)
            self.data["bad_event_factor"] = 0
            
    
    def riots(self, how_many, power_plant_dict, power_plant_name):
    
        print(f"riots break out all over the world becuse of your decitions, some exstreamits burn and destroy some of your plants you have lost a {power_plant_name} plant your energy output has been decreased")
        # did not have time to write a subtrack power plant func im just gonna subtracked the power
        print(f"old power: {self.data['current_power']}\n")
        self.data["current_power"] -= power_plant_dict["price"]
        print(f"new power {self.data['current_power']}")
        
            
    def lower_yearly_funds(self, how_many, power_plant_dict, power_plant_name):
        print("the UN is disatifide with your progress to there goal, they are moving funds to elsewhere, you will now get lower yeary funds")
        print(f"old yearly funds {self.add_funds}")
        self.add_funds -= 500000
        print(f"new yearly funds {self.add_funds}")
        
        
    def crop_harvest_failed(self, how_many, power_plant_dict, power_plant_name):
        print("farmers conplain of huge crop losses due to globle warming, you are to blame food shortges are everwhere your bad event factor increases")
        self.data["bad_event_factor"] += .5
        
        
    def good_event_factor(self, how_many, power_plant_dict, power_plant_name):
        if random.random() < self.data["good_event_factor"]:
            x = random.choice(self.good_event_list)
            self.good_event[x](how_many, power_plant_dict, power_plant_name)
            
    def raise_yearly_funds(self, how_many, power_plant_dict, power_plant_name):
        print("the UN is very satifide with the progress you have been making they have decided to raise your yearly funds")
        print(f"old yearly funds {self.add_funds}")
        self.add_funds += 500000
        print(f"new yearly funds {self.add_funds}")
        
        
   
        
        
class Main(events):
    def end_year(self):
        self.year -= 1
        print(f"year {self.year}")
    
        
    # REPL MAIN
    def main(self):
        
        while self.pollution< 37.94:
            if self.year == 0:
                print("you won! you have stayed under the goal congratilashons!!!")
            x = input("enter a command: ")
            if x in self.commands_list:
                self.caller(x)
            else:
                print("please enter a valid command, if you don't know the commands input 'help'")
        print("you lost you whent over your poloshen limit.")
    # REPL PLANT_ADD            
    def power_plant_add(self):
        while True:
            
            x = input("what type of power plant do you want to add? type 'break' to escape: ").lower().strip()
            if x in self.plants_list:
            
                how_many = int(input(f"how many {x} plants do you want to add?: "))
                power_plant_dict = self.power_plants[x]
                
                self.add_power_plant_work(power_plant_dict, how_many, x)
                self.bad_event_gen(how_many, power_plant_dict, x)
            elif x == "break":
                break
            else: 
                print("please enter a valid plant if you forgot what the plants are please break and then input 'pp'")
                
    def add_power_plant_work(self, power_plant_dict, y, x):
        if self.data["funds"] > (power_plant_dict["price"] * y):
                
            # price stuff
            self.data["funds"] -= (power_plant_dict["price"] * y)
            self.data["funds"] += self.add_funds
            # polushon stuff
            self.data["pollution_yearly"] += (power_plant_dict["carbon_emission"] * y)
            
            power_plant_dict["how_many"] += (power_plant_dict["how_many"] * y)
            
            self.pollution += self.data["pollution_yearly"]
            self.data["current_power"] += (power_plant_dict["power"] * y )
            self.data["needed_power"] += (random.randint(1,3) * self.data["needed_power"])
            self.data["good_event_factor"] += (power_plant_dict["good_event_factor"] * y)
            self.data["bad_event_factor"] += (power_plant_dict["bad_event_factor"] * y)
            self.data["funds"] += self.add_funds
            

            print(f"you added {y} {x} plants\nyear : {self.year}")
            
        else:
            print(f"you do not have enough funds to conplte this tranaction.\nfunds: {self.data['funds']}\ncost of purchase: {power_plant_dict['price'] * y}")
        

            
            
        
        
if __name__ == "__main__":
    x = Main()
    x.main()