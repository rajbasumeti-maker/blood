
blood_stock = {
    "A+": 0,
    "A-": 0,
    "B+": 0,
    "B-": 0,
    "AB+": 0,
    "AB-": 0,
    "O+": 0,
    "O-": 0
}


def add_blood(group, units):
    group = group.upper()

    if group not in blood_stock or units <= 0:
        return False

    blood_stock[group] += units
    return True


def search_blood(group):
    group = group.upper()

    if group not in blood_stock:
        return None

    return blood_stock[group]


def issue_blood(group, units):
    group = group.upper()

    if group not in blood_stock or units <= 0:
        return False

    if blood_stock[group] >= units:
        blood_stock[group] -= units
        return True

    return False


def display_stock():
    for group, units in blood_stock.items():
        print(group, ":", units, "units")


def main():
    while True:
        print("\n===== BLOOD BANK MANAGEMENT =====")
        print("1. Add Blood")
        print("2. Display Blood Stock")
        print("3. Search Blood Group")
        print("4. Issue Blood")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            group = input("Enter blood group: ")
            try:
                units = int(input("Enter units: "))
                if add_blood(group, units):
                    print("Blood added successfully!")
                else:
                    print("Invalid blood group or units!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "2":
            print("\nAvailable Blood Stock:")
            display_stock()

        elif choice == "3":
            group = input("Enter blood group: ")
            result = search_blood(group)

            if result is not None:
                print(group.upper(), "Available:", result, "units")
            else:
                print("Invalid blood group!")

        elif choice == "4":
            group = input("Enter blood group: ")
            try:
                units = int(input("Enter units required: "))
                if issue_blood(group, units):
                    print("Blood issued successfully!")
                else:
                    print("Invalid group, units, or insufficient stock!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
