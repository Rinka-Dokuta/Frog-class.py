class frog:
    def _init_(self, name, color, size):
        self.name = bob
        self.color = yellow
        self.size = small
        self.hunger_level = 0
        self.energy_level = 10
        self.fly_count = 0
        
    def ribbit(self):
        print(self.name + "says:Ribbit ribbit")
        self.hunger_level += 1
        self._check_levels()
        
    def jump(self):
        if self.size == "small":
            print(self.name+ "hops a little")
        elif self.size == "medium":
            print(self.name + "jumps pretty high")
        else:
            print(self.name + "jumps pretty high")
        self.energy_level -= 2
        self.hunger_level += 1
        self._check_levels()
        
        
    def eat(self):
        self.fly_count = fly_count
        self.energy_level += self.fly_count
        self.hunger_level -= self.fly_count/2
        print("Yum! Frog eats", self.fly_count, "flies")
        
    # Resets the energy_level to 10     
    def sleep(self):
        self.energy_level == 10
        print("zzzz....the frog is sleeping")
        
    
    # Prints the current status of the frog
    def status(self):
        
        
        
    
    
