history = []

# My functions:
def convctof(temp): #from C to F
    answer = round((temp * 9/5) + 32, 2) #<- 2 decimal places
    print(f'\n{answer} is your value in Fahrenheit!\n')
    history.append(f"{temp}°C → {answer}°F")
    print("Do another conversion?\n")

def convftoc(temp):  #from F to C
    answer = round((temp - 32) * 5/9, 2) #<- 2 decimal places
    print(f'\n{answer} is your value in Celsius!\n')
    history.append(f"{temp}°F → {answer}°C")
    print("Do another conversion?\n")

def convctok(temp):
    answer = round(temp + 273.15, 2)  # <- 2 decimal places
    print(f'\n{answer} is your value in Kelvin!\n')
    history.append(f"{temp}°C → {answer}K")
    print("Do another conversion?\n")

def convktoc(temp):
    answer = round(temp - 273.15, 2)  # <- 2 decimal places
    print(f'\n{answer} is your value in Celsius!\n')
    history.append(f"{temp}K → {answer}°C")
    print("Do another conversion?\n")

def convftok(temp):
    answer = round(((temp - 32) * 5/9) + 273.15, 2)  # <- 2 decimal places
    print(f'\n{answer} is your value in Kelvin!\n')
    history.append(f"{temp}°F → {answer}K")
    print("Do another conversion?\n")

def convktof(temp):
    answer = round(((temp - 273.15) * 9/5) + 32, 2)  # <- 2 decimal places
    print(f'\n{answer} is your value in Fahrenheit!\n')
    history.append(f"{temp}K → {answer}°F")
    print("Do another conversion?\n")

import re

def is_valid_filename(name):
    reserved = {
        "CON", "PRN", "AUX", "NUL",
        *(f"COM{i}" for i in range(1, 10)),
        *(f"LPT{i}" for i in range(1, 10))
    }
    if not name or name.strip() == "":
        return False
    if re.search(r'[<>:"/\\|?*]', name):
        return False
    if name.rstrip('. ').upper() in reserved:
        return False
    if name[-1] in {' ', '.'}:
        return False
    return True

def exiting_in_style():

    try:
        import os
        while True:

            # asking for the name and assigning it a location in the Downloads folder:
                file_name = input("\nWhat would you like to name your file (exclude '.txt')?\n").strip()
                if not is_valid_filename(file_name):
                    print("\nInvalid file name. Use only letters, numbers, spaces, '-', '_' and '.' (no special characters like ? : / \\ * < > | ) and don't leave it empty. Avoid reserved names (CON, PRN, etc.), and don't end with space or period.")
                    continue
                file_name = file_name.strip() + ".txt"

                downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
                file_path = os.path.join(downloads_folder, file_name)

               # What if file already exists with that same name?:
                if os.path.exists(file_path):
                    print(f"\nWARNING: '{file_name}' already exists in Downloads folder.")
                    choice = input("Type 'd' to enter a different name, or 'q' to quit without saving:\n").strip().lower()
                    if choice == "d":
                        continue
                    elif choice == "q":
                        print("\nQuitting without saving...\n")
                        return
                    else:
                        print("Invalid choice, please try again.")
                        continue
                else:
                    break
    except KeyboardInterrupt:
        print("\nProgram exited by user (Ctrl+C). Goodbye!")

    # getting date info:
    import datetime
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d @ %H:%M")  # <-- Format as: YYYY-MM-DD HH:MM
    # Writing to the file:
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"Temperature Conversion History, {formatted_date} :\n\n")
            for item in history:
             file.write(item + "\n")

        print(f"\nHistory successfully saved to '{file_path}'.\n")

    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
# END OF EXITING WITH STYLE FUNCTION


# Decision making
print("Hi! Choose a conversion.")
while True:  #True is always true
    import math
    try:
        decision = input(" 1. Celsius → Fahrenheit\n 2. Fahrenheit → Celsius\n 3. Celsius → Kelvin\n 4. Kelvin → Celsius\n 5. Fahrenheit → Kelvin\n 6. Kelvin → Fahrenheit\n 0. Quit without saving\n Q. Quit and save history to txt file\n")
        if decision.casefold() == "q":
            if not history:
                print("\nNo conversions have been done yet, so nothing to save!")
                print("You quit.")
                input("\nPress Enter to exit...")
                quit()
            else:
                exiting_in_style()
                print("You quit.")
                input("\nPress Enter to exit...")
                quit()
        decision = int(decision)
        if decision == 0:
            if not history:
                print("\nYou quit.")
                input("\nPress Enter to exit...")
                quit()
            else:
                print(f"Before you quit, here are all the conversions you've done:\n")
                print("\n".join(history))
                input("\nPress Enter to exit...")
                quit()
        if decision == 1:
            temp = float(input("\nGreat! Now input the value of the temperature you want to convert to Fahrenheit.\n"))
            if not math.isfinite(temp):
                print("\nPlease enter a real, finite number.")
                continue
            convctof(temp)
        elif decision == 2:
            temp = float(input("\nGreat! Now input the value of the temperature you want to convert to Celsius.\n"))
            if not math.isfinite(temp):
                print("\nPlease enter a real, finite number.")
                continue
            convftoc(temp)
        elif decision == 3:
            temp = float(input("\nGreat! Now input the value of the temperature you want to convert to Kelvin.\n"))
            if not math.isfinite(temp):
                print("\nPlease enter a real, finite number.")
                continue
            convctok(temp)
        elif decision == 4:
            temp = float(input("\nGreat! Now input the value of the temperature you want to convert to Celsius.\n"))
            if not math.isfinite(temp):
                print("\nPlease enter a real, finite number.")
                continue
            convktoc(temp)
        elif decision == 5:
            temp = float(input("\nGreat! Now input the value of the temperature you want to convert to Kelvin.\n"))
            if not math.isfinite(temp):
                print("\nPlease enter a real, finite number.")
                continue
            convftok(temp)
        elif decision == 6:
            temp = float(input("\nGreat! Now input the value of the temperature you want to convert to Fahrenheit.\n"))
            if not math.isfinite(temp):
                print("\nPlease enter a real, finite number.")
                continue
            convktof(temp)
        else: print("Your input is wrong, maybe try something else?\n")
    except ValueError:
        print("Your input is wrong, maybe try something else?\n")
    except KeyboardInterrupt:
        print("\nProgram exited by user. Goodbye!")
        input("\nPress Enter to exit...")
        quit()




# Stuff to add:
# - GUI
