class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def get_info(self):
        return f'{self.brand}, {self.year}'

class Car(Vehicle):
    def __init__(self, brand, year,num_doors,fuel_type):
        super().__init__(brand, year)
        self.num_doors=num_doors
        self.fuel_type=fuel_type
    def get_info(self):
        return f'{self.brand}, {self.year}, {self.num_doors} doors, {self.fuel_type}'
  
    

class Motorcycle(Vehicle):
    def __init__(self, brand, year,has_sidecar,engine_size):
        super().__init__(brand, year)
        self.has_sidecar=has_sidecar 
        self.engine_size=engine_size
    def get_info(self):
        return f'{self.brand}, {self.year},{"No" if self.has_sidecar==False else "Has sidecar" } sidecar,{self.engine_size}cc'

    
    


def main():
    Gari= Car("Toyota",2020,4,"Petrol")
    Hunda= Motorcycle("Honda",2021,False,500)
    print(Gari.get_info())
    print(Hunda.get_info())

main()