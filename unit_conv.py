
# Unit Conversion System


# function for Length Conversion
def length_conversion(value, option):

    if option== "1":
        return value*0.621371

    else:
        return value/0.621371

# function for Weight Conversion
def weight_conversion(value, option):

    if option== "1":
        return value* 1000

    else:
        return value/1000

# function for Temperature Conversion
def temperature_conversion(value, option):

    if option =="1":
        return(value * 9/5) + 32

    else:
        return(value - 32) * 5/9

# function for Time Conversion
def time_conversion(value, option):

    if option =="1":
        return value * 60

    else:
        return value / 60

# Main Program

print("===== UNIT CONVERSION SYSTEM =====")

print("1. Length")
print("2. Weight")
print("3. Temperature")
print("4.Time")

choice = input("Enter your choice (1-4): ")


# checking menu choice
if choice not in ["1", "2", "3", "4"]:
    print("Invalid choice. Select 1 to 4.")

else:
    # Displaying conversion options

    if choice == "1":
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")

    elif choice == "2":
        print("1. Kilograms to Grams")
        print("2. Grams to Kilograms")

    elif choice == "3":
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")

    elif choice == "4":
        print("1. Hours to Minutes")
        print("2. Minutes to Hours")

    option = input("Choose conversion (1-2): ")

    if option not in ["1", "2"]:
        print("Invalid conversion choice.")

    else:

        try:
            value = float(input("Enter the value: "))

            if choice == "1":
                result = length_conversion(value, option)

                if option == "1":
                    print(value, "km =", round(result, 2), "miles")
                else:
                    print(value, "miles =", round(result, 2), "km")

            elif choice == "2":
                result = weight_conversion(value, option)

                if option == "1":
                    print(value, "kg =", round(result, 2), "g")
                else:
                    print(value, "g =", round(result, 2), "kg")

            elif choice == "3":
                result = temperature_conversion(value, option)

                if option == "1":
                    print(value, "C =", round(result, 2), "F")
                else:
                    print(value, "F =", round(result, 2), "C")

            elif choice == "4":
                result = time_conversion(value, option)

                if option == "1":
                    print(value,"hours =", round(result, 2), "minutes")
                else:
                    print(value,"minutes =", round(result, 2), "hours")

        except ValueError:
            print("Invalid value. Enter a number.")


print("===== THANK YOU =====")
