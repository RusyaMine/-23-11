class Manufacturer:
    def __init__(self, name, country):
        self.name = name
        self.country = country
class Car:
    def __init__(self, model, manufacturer):
        self.model = model
        self.manufacturer = manufacturer
class Salon:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self, manufacturer_name):
        print(f"Cars in {self.name}:")
        found = False
        for c in self.cars:
            if c.manufacturer.name == manufacturer_name:
                print(f"- {c.model} by {c.manufacturer.name} "
                      f"(Country - {c.manufacturer.country})")
                found = True

        if not found:
            print("Мұндай өндірушінің көлігі табылмады!")
    def save_to_file(self, filename):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                for c in self.cars:
                    file.write(f"{c.model},{c.manufacturer.name},{c.manufacturer.country}\n")
            print(f"Мәлімет файлға сақталды: {filename}")
        except Exception as e:
            print("Файлды жазу кезінде қате шықты:", e)

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.cars = []
                for line in file:
                    model, name, country = line.strip().split(",")
                    manufacturer = Manufacturer(name, country)
                    car = Car(model, manufacturer)
                    self.cars.append(car)
            print(f"Мәлімет файлдан жүктелді: {filename}")
        except FileNotFoundError:
            print("Файл табылмады!")
        except Exception as e:
            print("Файлды оқу кезінде қате шықты:", e)

name = input("Өндірушінің атын енгіз: ")

manufacturer = Manufacturer("Camry", "Japan")
manufacturer1 = Manufacturer("Tesla","USA")
manufacturer2 = Manufacturer("TANK", "China")
manufacturer3 = Manufacturer("Bygati", "France")

car = Car("Camry", manufacturer)
car1 = Car("Tesla", manufacturer1)
car2 = Car("TANK", manufacturer2)
car3 = Car("Bygati", manufacturer3)

salon = Salon("Car Center")
salon.add_car(car)
salon.add_car(car1)
salon.add_car(car2)
salon.add_car(car3)

salon.show_cars(name)

salon.save_to_file("cars.txt")
print("\nФайлдан қайта оқылған мәлімет:\n")
salon.load_from_file("cars.txt")
salon.show_cars(name)