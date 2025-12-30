print("\n Advanced Real Estate Price & Rent Estimator\n")

while True:

    flat = input("Is this a flat? (yes/no): ").strip().lower()
    if flat not in ["yes", "y"]:
        print("This tool only supports flats. Exiting ")
        break

    bhk = int(input("How many BHK?: "))
    mode = input("Is this for Rent or Buy? (rent/buy): ").strip().lower()
    area = int(input("Area in sq ft?: "))

    # ===== FLOOR EFFECT =====
    floor = int(input("Which floor is the flat on? (e.g., 1, 5, 10): "))
    
    # ===== AGE EFFECT =====
    age = int(input("Age of the building in years?: "))

    # ===== FURNISHING =====
    print("\nFurnishing Type:")
    print("1. Unfurnished")
    print("2. Semi-Furnished")
    print("3. Fully Furnished")

    furnish_choice = input("Choose 1–3: ")

    # ===== SOCIETY TYPE =====
    print("\nSociety Type:")
    print("1. Normal")
    print("2. Luxury")

    society_choice = input("Choose 1–2: ")

    # ===== CITY =====
    print("\nSelect City:")
    print("1. Delhi")
    print("2. Mumbai")
    print("3. Pune")
    print("4. Bangalore")
    print("5. Hyderabad")
    print("6. Chennai")
    print("7. Kolkata")
    print("8. Ahmedabad")
    print("9. Jaipur")
    print("10. Chandigarh")

    city_choice = input("Enter 1–10: ")

    # ===== CITY RATES =====
    city_rates_buy = {
        "1": 10000,
        "2": 22000,
        "3": 8000,
        "4": 9500,
        "5": 9000,
        "6": 8500,
        "7": 7500,
        "8": 6500,
        "9": 6000,
        "10": 11000
    }

    city_rates_rent = {
        "1": 25,
        "2": 55,
        "3": 22,
        "4": 28,
        "5": 26,
        "6": 24,
        "7": 20,
        "8": 18,
        "9": 17,
        "10": 27
    }

    city_names = {
        "1": "Delhi",
        "2": "Mumbai",
        "3": "Pune",
        "4": "Bangalore",
        "5": "Hyderabad",
        "6": "Chennai",
        "7": "Kolkata",
        "8": "Ahmedabad",
        "9": "Jaipur",
        "10": "Chandigarh"
    }

    if city_choice not in city_names:
        print("\n Invalid city option — try again!\n")
        continue

    city = city_names[city_choice]

    # ===== BASE PRICE =====
    if mode == "buy":
        price = area * city_rates_buy[city_choice]
    else:
        price = area * city_rates_rent[city_choice]

    # ===== FLOOR EFFECT =====
    # +1% per 5 floors (max +5%)
    floor_boost = min((floor // 5) * 0.01, 0.05)
    price *= (1 + floor_boost)

    # ===== AGE EFFECT =====
    # -0.7% per year (max –25%)
    age_drop = min(age * 0.007, 0.25)
    price *= (1 - age_drop)

    # ===== FURNISHING EFFECT =====
    furnish_factor = {
        "1": 1.00,  # Unfurnished
        "2": 1.07,  # Semi-furnished
        "3": 1.15   # Fully furnished
    }.get(furnish_choice, 1.00)

    price *= furnish_factor

    # ===== SOCIETY EFFECT =====
    society_factor = {
        "1": 1.00,  # Normal
        "2": 1.25   # Luxury
    }.get(society_choice, 1.00)

    price *= society_factor

    # ===== OUTPUT =====
    print("\n===============================")
    print(f" City: {city}")
    print(f" BHK: {bhk}")
    print(f" Area: {area} sq ft")
    print(f" Floor: {floor}")
    print(f" Age: {age} years")
    print("===============================\n")

    if mode == "buy":
        print(f" Estimated Property Price: ₹{price:,.0f}\n")
    else:
        print(f" Estimated Monthly Rent: ₹{price:,.0f}\n")

    again = input("Do you want to predict another property? (yes/no): ").strip().lower()
    if again not in ["yes", "y"]:
        print("\n Thanks for using the Real Estate Estimator!\n")
        break
