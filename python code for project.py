from datetime import datetime

# -------------------- Base Class --------------------
class Vehicle:
    def __init__(self, plate_number, owner_name, address, speed):
        self.plate_number = plate_number
        self.owner_name = owner_name
        self.address = address
        self.__speed = speed           # Encapsulation
        self.speed_limit = 80

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed >= 0:
            self.__speed = speed
        else:
            print("Invalid speed entered!")

    def calculate_challan(self):
        return 0


# -------------------- Child Class: Car --------------------
class Car(Vehicle):
    def calculate_challan(self):
        if self.get_speed() > self.speed_limit:
            extra = self.get_speed() - self.speed_limit
            return 1000 + (extra * 20)
        return 0


# -------------------- Child Class: Heavy Truck --------------------
class HeavyTruck(Vehicle):
    def calculate_challan(self):
        if self.get_speed() > self.speed_limit:
            extra = self.get_speed() - self.speed_limit
            return 2500 + (extra * 30)
        return 0


# -------------------- E-Challan System --------------------
class EChallanSystem:
    def __init__(self, location):
        self.location = location

    def check_speed(self, vehicle):
        fine = vehicle.calculate_challan()

        if fine > 0:
            current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

            print("\n" + "=" * 60)
            print("        HIGHWAY POLICE E-CHALLAN SYSTEM")
            print("=" * 60)

            print(f"Date & Time    : {current_time}")
            print(f"Camera Location: {self.location}")
            print(f"Vehicle Number : {vehicle.plate_number}")
            print(f"Owner Name     : {vehicle.owner_name}")
            print(f"Address        : {vehicle.address}")
            print(f"Recorded Speed : {vehicle.get_speed()} km/h")
            print(f"Speed Limit    : {vehicle.speed_limit} km/h")
            print(f"Fine Amount    : Rs. {fine}/-")

            print("-" * 60)
            print("STATUS : OVER-SPEEDING DETECTED")
            print("E-Challan has been generated successfully.")
            print("A printed copy will be sent to your home address.")
            print("=" * 60)

        else:
            print("\n" + "=" * 60)
            print("Vehicle Number :", vehicle.plate_number)
            print("Recorded Speed :", vehicle.get_speed(), "km/h")
            print("Status         : SAFE")
            print("No Challan Generated.")
            print("=" * 60)


# -------------------- Main Program --------------------
def main():

    print("=" * 60)
    print("      SMART SPEED CAMERA & E-CHALLAN SYSTEM")
    print("=" * 60)

    location = input("Enter Camera Location: ")

    camera = EChallanSystem(location)

    while True:

        print("\nSelect Vehicle Type")
        print("1. Car")
        print("2. Heavy Truck")

        choice = input("Enter your choice (1/2): ")

        plate = input("Enter Vehicle Number: ")
        owner = input("Enter Owner Name: ")
        address = input("Enter Owner Address: ")

        while True:
            try:
                speed = int(input("Enter Vehicle Speed (km/h): "))
                if speed < 0:
                    print("Speed cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        if choice == "1":
            vehicle = Car(plate, owner, address, speed)

        elif choice == "2":
            vehicle = HeavyTruck(plate, owner, address, speed)

        else:
            print("Invalid Vehicle Type.")
            continue

        print("\nChecking Vehicle Speed...")
        camera.check_speed(vehicle)

        print("\nDo you want to check another vehicle?")
        again = input("Enter Y for Yes or N for No: ").upper()

        if again != "Y":
            break

    print("\nThank you for using the Smart Speed Camera System.")
    print("Program Closed Successfully.")


# -------------------- Program Starts --------------------
if __name__ == "__main__":
    main()