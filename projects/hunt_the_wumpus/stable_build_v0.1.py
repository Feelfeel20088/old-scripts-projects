import random
import logging









class Text:
    def __init__(self) -> None:
            self.room_Text_Var = [
        "You enter a dimly lit cavern. The air is stale, and the ground is uneven. The only sound is the echo of your footsteps against the rocky walls.\n",
        "As you step into the room, a flurry of wings startles you. A colony of bats screeches and swoops overhead, disturbing your senses. they pick you up with there hard boned claws and lift you off the ground you try to fight it but they have a to good grip on you. they carry you elseware. later, you are dropped into another room\n",
        "A sudden chill runs down your spine as you peer into the darkness below. The floor drops away abruptly, revealing a bottomless pit. You take a step forward, but before you can react, you plummet into the abyss. The fall seems to last forever, but the impact is sudden and final. Darkness envelops you as you realize that there is no escape from the depths below. Game over."
        "You catch a whiff of a foul stench, like rotting flesh, as you enter the chamber. In the shadows, you catch a glimpse of glowing red eyes, and you know you're not alone.\n",
    ]
    
    def player_attack_text(self,obj):
        player_attacks_text = [f"\nThe Wumpus roars in pain as the {obj} strikes its hide.",
        f"\nThe {obj} finds its mark, causing The Wumpus to recoil in agony.",
        f"\nThe Wumpus staggers as the {obj} pierces its flesh.",
        f"\nWith a mighty throw, the {obj} hits The Wumpus, eliciting a howl of pain.",
        f"\nThe Wumpus grunts in pain as the {obj} makes contact.",
        f"\nThe {obj} strikes true, causing The Wumpus to bellow in anguish.",
        f"\nA direct hit with the {obj} sends The Wumpus reeling.",
        f"\nThe Wumpus flinches as the {obj} strikes its vulnerable spot.",
        f"\nThe {obj} inflicts a wound on The Wumpus, causing it to falter.",
        f"\nThe Wumpus winces as the {obj} embeds itself in its flesh.",
        f"\nThe impact of the {obj} leaves The Wumpus visibly injured.",
        f"\nThe Wumpus lets out a pained growl as the {obj} hits home.",
        f"\nThe {obj} finds its target, causing The Wumpus to writhe in pain.",
        f"\nThe Wumpus snarls in pain as the {obj} strikes with precision.",
        f"\nThe {obj} strikes a blow against The Wumpus, causing it to stagger.",
        f"\nThe Wumpus grimaces as the {obj} bites into its tough hide.",
        f"\nWith a solid hit, the {obj} causes The Wumpus to howl in agony.",
        f"\nThe Wumpus recoils as the {obj} leaves a painful mark.",
        f"\nThe {obj} delivers a powerful blow to The Wumpus, eliciting a roar of pain.",
        f"\nThe Wumpus flails in pain as the {obj} makes contact.",
        f"\nThe {obj} strikes The Wumpus with force, causing it to wince in pain.",
        f"\nThe Wumpus groans as the {obj} strikes a vulnerable spot.",
        f"\nWith a mighty swing, the {obj} lands a solid hit on The Wumpus.",
        f"\nThe Wumpus stumbles as the {obj} finds its mark.",
        f"\nThe {obj} finds purchase, causing The Wumpus to cry out in pain.",
        f"\nThe Wumpus yelps in pain as the {obj} pierces its tough hide.",
        f"\nThe {obj} connects with The Wumpus, causing it to grunt in pain.",
        f"\nThe Wumpus winces as the {obj} draws blood.",
        f"\nThe {obj} strikes true, causing The Wumpus to reel in pain.",
        f"\nThe Wumpus snarls as the {obj} strikes a critical blow.",
        f"\nWith a well-aimed throw, the {obj} lands a hit on The Wumpus.",
        f"\nThe Wumpus roars in frustration as the {obj} inflicts a wound.",
        f"\nThe {obj} strikes The Wumpus with surprising force, causing it to falter.",
        f"\nThe Wumpus grunts as the {obj} hits home.",
        f"\nThe {obj} finds its mark, causing The Wumpus to stagger backward.",
        f"\nThe Wumpus winces as the {obj} finds a weak spot.",
        f"\nWith a precise throw, the {obj} lands a hit on The Wumpus.",
        f"\nThe Wumpus recoils in pain as the {obj} bites deep.",
        f"\nThe {obj} strikes a critical blow, causing The Wumpus to howl in pain.",
        f"\nThe Wumpus growls as the {obj} inflicts a wound.",
        f"\nThe {obj} connects solidly, causing The Wumpus to wince in pain.",
        f"\nThe Wumpus stumbles as the {obj} strikes with unexpected force.",
        f"\nThe {obj} embeds itself in The Wumpus's flesh, eliciting a cry of pain.",
        f"\nThe Wumpus lets out a pained roar as the {obj} finds its target.",
        f"\nThe {obj} lands a powerful blow, causing The Wumpus to reel backward.",
        f"\nThe Wumpus snarls as the {obj} inflicts a painful wound."]
        return random.choice(player_attacks_text)
    
    def combat_attacks_text(self):
        attacks = ["slashes viciously at", "lunges aggressively towards", "strikes with formidable strength at", "charges ferociously at", "pounces menacingly on", "ambushes cunningly at", "swipes dangerously at", "bites savagely into", "grabs fiercely at", "rams violently into"]
        wumpus_attacks_text = [f"With a bloodcurdling roar, the creature {random.choice(attacks)} the unsuspecting victim.",
        f"The earth trembles as the monster {random.choice(attacks)} with the force of a raging storm.",
        f"In a swift motion, the fiend {random.choice(attacks)} with unparalleled ferocity.",
        f"Unleashing its wrath, the entity {random.choice(attacks)} as if possessed by a demon.",
        f"The air crackles with tension as the terror {random.choice(attacks)} with deadly precision.",
        f"A shiver runs down the spine as the horror {random.choice(attacks)} in a calculated strike.",
        f"With a thunderous growl, the nightmare {random.choice(attacks)} with malicious intent.",
        f"The ground quakes beneath as the menace {random.choice(attacks)} in an onslaught of terror.",
        f"Whispers of dread fill the air as the creature {random.choice(attacks)} in a relentless assault.",
        f"Under the cover of darkness, the horror {random.choice(attacks)} with silent menace.",
        f"The shadows writhe as the monstrosity {random.choice(attacks)} with primal rage.",
        f"A chill grips the heart as the apparition {random.choice(attacks)} with supernatural force.",
        f"The very earth recoils as the nightmare {random.choice(attacks)} in a surge of malevolence.",
        f"In the dim light, the abomination {random.choice(attacks)} with nightmarish strength.",
        f"With a roar that echoes through eternity, the demon {random.choice(attacks)} with unholy fury.",
        f"Eyes gleaming with malice, the horror {random.choice(attacks)} with relentless aggression.",
        f"Every step closer sends a wave of terror as the entity {random.choice(attacks)} with chilling precision.",
        f"With every strike, the terror grows as the monstrosity {random.choice(attacks)} with monstrous power.",
        f"The very air seems to thicken as the creature {random.choice(attacks)} with supernatural speed.",
        f"Every blow strikes fear into the hearts as the horror {random.choice(attacks)} with otherworldly force.",
        f"In the silence, the dread mounts as the abomination {random.choice(attacks)} with silent malice.",
        f"Amidst the darkness, the terror strikes as the demon {random.choice(attacks)} with spectral grace.",
        f"The darkness envelopes all as the nightmare {random.choice(attacks)} with shadowy tendrils.",
        f"With each attack, the horror grows as the entity {random.choice(attacks)} with ferocious might.",
        f"The very fabric of reality quakes as the monstrosity {random.choice(attacks)} with primal strength.",
        f"In the heart of the abyss, the terror strikes as the creature {random.choice(attacks)} with unfathomable power.",
        f"Through the veil of nightmares, the horror strikes as the demon {random.choice(attacks)} with infernal wrath.",
        f"Amidst the chaos, the terror looms as the nightmare {random.choice(attacks)} with boundless fury.",
        f"In the depths of despair, the horror strikes as the entity {random.choice(attacks)} with relentless savagery.",
        f"With each strike, the terror grows as the abomination {random.choice(attacks)} with insatiable hunger.",
        f"In the grip of fear, the horror strikes as the monstrosity {random.choice(attacks)} with unyielding ferocity.",
        f"In the heart of darkness, the terror strikes as the creature {random.choice(attacks)} with predatory grace.",
        f"Through the mists of terror, the horror strikes as the demon {random.choice(attacks)} with indomitable rage.",
        f"In the silence of the night, the terror strikes as the nightmare {random.choice(attacks)} with silent malice.",
        f"In the depths of despair, the horror strikes as the entity {random.choice(attacks)} with primal strength.",
        f"Through the shadows, the terror strikes as the abomination {random.choice(attacks)} with spectral fury.",
        f"Within the heart of madness, the horror strikes as the monstrosity {random.choice(attacks)} with infernal power.",
        f"In the grip of fear, the terror strikes as the creature {random.choice(attacks)} with unyielding force.",
        f"With each strike, the horror grows as the demon {random.choice(attacks)} with relentless savagery.",
        f"Within the abyss, the terror strikes as the nightmare {random.choice(attacks)} with boundless fury.",
        f"Through the veil of nightmares, the horror strikes as the entity {random.choice(attacks)} with primal might.",
        f"In the silence of the void, the terror strikes as the abomination {random.choice(attacks)} with silent malice.",
        f"In the depths of despair, the horror strikes as the monstrosity {random.choice(attacks)} with primal power.",
        f"Through the shadows, the terror strikes as the creature {random.choice(attacks)} with spectral fury.",
        f"Within the heart of madness, the horror strikes as the demon {random.choice(attacks)} with infernal strength.",
        f"In the grip of fear, the terror strikes as the nightmare {random.choice(attacks)} with unyielding savagery.",
        f"With each strike, the horror grows as the entity {random.choice(attacks)} with relentless force.",
        f"Within the abyss, the terror strikes as the abomination {random.choice(attacks)} with boundless malice.",
        f"Through the veil of nightmares, the horror strikes as the monstrosity {random.choice(attacks)} with primal fury."]
        return random.choice(wumpus_attacks_text)
    
    def room_text(self, number):
        # bug 01: when a room calls to retrive text indexing goes wrong and index erroh acorse 
        room_Text_Var = [
        "You enter a dimly lit cavern. The air is stale, and the ground is uneven. The only sound is the echo of your footsteps against the rocky walls, you decide to move on to the next room.\n",
        "As you step into the room, a flurry of wings startles you. A colony of bats screeches and swoops overhead, disturbing your senses. they pick you up with there hard boned claws and lift you off the ground you try to fight it but they have a to good grip on you. they carry you elseware. later, you are dropped into another room\n",
        "A sudden chill runs down your spine as you peer into the darkness below. The floor drops away abruptly, revealing a bottomless pit. You take a step forward, but before you can react, you plummet into the abyss. The fall seems to last forever, but the impact is sudden and final. Darkness envelops you as you realize that there is no escape from the depths below. Game over.",
        "You catch a whiff of a foul stench, like rotting flesh, as you enter the chamber. In the shadows, you catch a glimpse of glowing red eyes, and you know you're not alone.\n",
        "You enter a dimly lit chamber. The air is thick with tension as you sense a presence lurking in the shadows. Suddenly, with a guttural growl, a menacing figure emerges from the darkness. It's a formidable opponent, ready to engage in combat. You must prepare yourself for a fierce battle to survive.\n"
    ]   
        return room_Text_Var[number]
        
        
        
class var:
    def __init__(self) -> None:
        
        
        self.roomlist = []
        
        # moster stuff
        self.monster_list = ["Bear", "Sneak", "giant spider", "troll"]
        self.monster_dict = {"Bear" : 75, "Sneak" : 50, "giant spider" : 100, "troll" : 200, "Wumpus" : 300}
    
        self.player_health_G = 100
        # wepon stuff
        self.wepondamnge = {"hands" : 5, "bat": 25, "pan": 15, "sword": 50, "axe": 20, "debug" : 10000}
        self.weapon_duribility = {"hands" : 50, "bat": 3, "pan": 3, "sword": 3, "axe": 3, "debug" : 3}
        self.weapons_player = ["hands", "debug"]
        self.weapons = ["Hands", "Bat", "Pan", "Sword", "axe"]
        self.monster_weapons = []
        # room stuff        
        self.room_Name = ["wumpus_room", "bat_room", "hole_room", "combat_room", "empty_room"]
        self.room_mapping = ["up", "down"]
        self.room_dead = {}
        
        
        
        
        
        
        
        



        
        
        
        
        
        
        
        
        
        
        
        
class connections:
    
    def random_c():
        pass
        


def decorator(func):
    def wrapper(*args, **kargs):
        print("befor starting")
        func()
        print("after starting")
    return wrapper
    





class room_Gen:
    
    def __init__(self) -> None:
        self.ID = 0
        self.call_room_dict = {"bat_room" : self.bat_room, "hole_room" : self.hole_room, "wumpus_room" : self.wumpus_room, "empty_room" : self.empty_room, "combat_room": self.combat_room}
        self.call_room_list = [self.bat_room, self.hole_room, self.wumpus_room, self.empty_room, self.combat_room]
        self.v = var()
        self.t = Text()
        self.c = combat()
        
    
    
        
    
    def generate_room(self, rooms = 20):
        for _ in range(rooms):
            x = random.choice(self.call_room_list)
            self.v.roomlist.append(x)
        
        self.generate_value_key(rooms)
        self.choose_room(rooms)
        
        
   
   
    def generate_value_key(self, rooms):
        
        for key in range(rooms):
            self.v.room_dead[key] = True
        print(self.v.room_dead)
                
        
        
        
    

    def choose_room(self, rooms):
        while self.v.monster_dict["Wumpus"] != 0:
            x = input("You find a hole in the cave. Will you venture up or down the tunnle (type 'up' or 'down'): ")
            if x in self.v.room_mapping:
                self.move(x, rooms)
            else:
                print("Invalid input. Please choose 'up' or 'down'.\n")
           
                
    def move(self, command, rooms_counter):

        print(f"befor room change: {self.ID}")
        if command == "up":
            self.ID = (self.ID + 1) % rooms_counter 
            print(f"after room change: {self.ID}")
            self.v.roomlist[self.ID]()
            return self.ID
        elif command == "down":
            if self.ID == 0:
                self.ID == rooms_counter 
                print(f"after room change: {self.ID}")
                self.v.roomlist[self.ID]()
                return self.ID
            
            self.ID = self.ID - 1
            print(f"after room change: {self.ID}")
            self.v.roomlist[self.ID]()
            return self.ID
        
                
            
        
        
        
        
        
        
    
    
        
        
        
    
        
            
       
                
    def fight_momster(self):
        monster = random.choice(self.v.monster_list)
        print(f"you encounter a {monster}\n") 
        self.c.Combat(monster)
        return monster
            
        
    def empty_room(self):
        print(self.t.room_text(0))
        print("current room: empty room\n")
        return None
        
        
        
    def bat_room(self):
        print(self.t.room_text(1))
        print("current room: bat room\n")
        return None
        
    def hole_room(self, p = .2):
        print("current room: hole room\n")
        p = .2
        if random.random() < p:
            print(self.t.room_text(2))
            exit()
        else:
            print("you carfully walk around the hole making carefull steps not to slip you make it to the end of the room\n")
        
        
    def combat_room(self):
        if self.v.room_dead[self.ID]:
            print(self.t.room_text(4))
            self.fight_momster()
            self.v.room_dead[self.ID] = False
        else:
            print("You grimace at the sight of the dead monster on the floor, but you steel yourself and carefully step over its repulsive form to continue your journey through the dungeon.\n")
        
    def wumpus_room(self):
        p = .2
        if random.random() < p:
            print(self.t.room_text(3))
            print("you encounter the Wumpus.\n")
            print("current room: wumpus room\n")
            self.c.Combat("Wumpus")
            self.v.room_dead[self.ID] = False
        else: 
            print("you walk into a room that smells horrble, bones and rotting meat fill your lungs, you know something evil was here, if you come back here something horrble may be here.\n")
        
            
        
    
        
    
    
            
            
        
    

    
        
 # finds the number in the list of what room text to print out.
        
        
class combat():
    
    
    def __init__(self) -> None:
        self.v = var()
        self.t = Text()
    
    
    
    
    
    
    
    def weapon_generator(self):
            new_weapon = random.choice(self.v.weapons)
            self.v.weapons_player.append(new_weapon)
            print(self.v.weapons_player)
            print(f"you got a new {new_weapon} you can use it to fight more monsters and possibly the wumpus.\n")
            
    
    

    
    def Combat(self, monster):
            while self.v.monster_dict[monster] > 0: # and this
                weapon_choice = input(f"Choose a weapon to attack the {monster} with!, or press i to display your inventory").lower()
                
                if weapon_choice in self.v.weapons_player:  
                    dam = self.v.wepondamnge[weapon_choice]
                    self.attacker(dam, weapon_choice, monster)
                    
            
                    
                else:
                    print("Please choose a weapon in your inventory.\n")
            print(f"you killed the {monster} concragulaishons!\n")
            self.weapon_generator()
            
        
        
        
                

    def attacker(self,dam,wepon, monster):
        print(f"{self.t.player_attack_text(wepon)}\n")
        durability_text = self.durability(wepon, monster)
        new_helth = self.player_attack(dam, monster)
        self.informer(durability_text, monster, dam, new_helth)
        
        
       
    
        
        
        
    def durability(self, wepon, monster):
        self.v.weapon_duribility[wepon] -= 1
        if self.v.weapon_duribility[wepon] > 0:
            return f"Your {wepon} took dmamnge it now only has {self.v.weapon_duribility[wepon]} hits left\n"
        else:
            self.v.weapons_player.remove(wepon)
            return f"your {wepon} broke and was destoyed while attking the {monster}\n"
        
        
        
    def player_attack(self, dam, monster):
        self.v.monster_dict[monster] = self.v.monster_dict[monster] - dam
        return self.v.monster_dict[monster]
        
        
    
    
        
    def monster_attack(self, dam):
        self.v.player_health_G -= dam
        return self.v.player_health_G 
        
    
    
    def informer(self, durability_text, monster, dam, new_helth):
        # inform user
        print(f"The {monster} lost {dam} health! {monster} has {new_helth} left!\n\n{durability_text}")

            
            



    








         
            

        



    
    


x = int(input("how many rooms do you want: "))
RG = room_Gen()
RG.generate_room(x)



