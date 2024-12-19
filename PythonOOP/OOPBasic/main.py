from car import Car
    
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(f"{car1.model} {car1.year} {car1.color} {car1.for_sale}")
print(f"{car2.model} {car2.year} {car2.color} {car2.for_sale}")
print(f"{car3.model} {car3.year} {car3.color} {car3.for_sale}")

car1.drive()
car2.stop()
car3.describe()
