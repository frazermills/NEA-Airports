# CS Online class: Airports NEA with Mr Pizzey


# ------------------------------------------------
def main():
  data = read_airports_data()
  print(data)
  show_menu()

  # first choice
  choice = int(input("Choose a menu option: "))

  while choice != 9:
    # do the chosen item
    if choice == 1:
      enter_airport_details()
    elif choice == 2:
      enter_flight_details()
    elif choice == 3:
      enter_price_plan()
    elif choice == 4:
      clear_data()
    elif choice == 9:
      quit()
    else:
      print("illegal choice")
    
    show_menu()
    # get next choice
    choice = input("Choose a menu option: ")

# ------------------------------------------------

def print_horizontal_rule():
  print("-" * 25)

# ------------------------------------------------

def read_airports_data():
  return None

# ------------------------------------------------

def enter_airport_details():
  pass

# ------------------------------------------------

def enter_flight_details():
  pass

# ------------------------------------------------

def enter_price_plan():
  pass

# ------------------------------------------------

def clear_data():
  pass

# ------------------------------------------------

def show_menu():
  print_horizontal_rule()
  print("MENU: ")
  print("1- Enter airport details")
  print("2- Enter flight details")
  print("3- Enter price plan")
  print("4- Clear data")
  print("9- quit")

# ------------------------------------------------

main()