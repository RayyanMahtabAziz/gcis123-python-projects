def breakfast():
    print("1-omellete\n2-sausages\n3-special breakfast burger")
    inp = int(input("Enter order here"))
    if inp == 1:
        print("omelette  AED 7")
    elif inp == 2:
        print("sausages  AED 12")
    elif inp == 3:
        print("special breakfast burger AED 20")
    else:
        print("Invalid input!")

def appetizers():
    print("french fries\nhummus\nchicken pastry")
    inp = int(input("Enter order here"))
    if inp == 1:
        print("french fries  AED 9")
    elif inp == 2:
        print("hummus  AED 15")
    elif inp == 3:
        print("chicken pastry  AED 5")
    else:
        print("Invalid input!")

def main_course():
    print("chicken(with lemon)\nkobe beef\nwaffle burger\nfriend chicken")
    inp = int(input("Enter order here"))
    if inp == 1:
        print("chicken(with lemon)  AED 21")
    elif inp == 2:
        print("kobe beef  AED 130")
    elif inp == 3:
        print("waffle burger AED 45")
    elif inp == 4:
        print("friend chicken  AED 25")
    else:
        print("Invalid input!")


def side_dishes():
    print("calzone\nmac n cheese\ntomato soup")
    inp = int(input("Enter order here"))
    if inp == 1:
        print("calzone  AED 17")
    elif inp == 2:
        print("mac n cheese  AED 15")
    elif inp == 3:
        print("tomato soup  AED 11")
    else:
        print("Invalid input!")

def drinks():
    print("water\nsoft beverages\niced tea\ncoffee")
    inp = int(input("Enter order here"))
    if inp == 1:
        print("water  AED 3")
    elif inp == 2:
        print("soft beverages  AED 7")
    elif inp == 3:
        print("iced tea  AED 7")
    elif inp == 4:
        print("coffee  AED 16")
    else:
        print("Invalid input!")

def desserts():
    print("tiramisu\nlava cake\nice cream sundae")
    inp = int(input("Enter order here"))
    if inp == 1:
        print("tiramisu  AED 20")
    elif inp == 2:
        print("lava cake  AED 15")
    elif inp == 3:
        print("ice cream sundae  AED 23")
    else:
        print("Invalid input!")



def menuoptions():

    print("1: breakfast")
    print("2: appetizers")
    print("3: main course")
    print("4: side dishes")
    print("5: drinks")
    print("6: desserts")
    inp = int(input("Enter a number: "))

    if inp == 1:
        print("breakfast")
        breakfast()
    elif inp == 2:
        print("appetizers")
        appetizers()
    elif inp == 3:
        print("main course")
        main_course()
    elif inp == 4:
        print("side dishes")
        side_dishes()
    elif inp == 5:
        print("drinks")
        drinks()
    elif inp == 6:
        print("desserts")
        desserts()
    else:
        print("Invalid input!")


menuoptions()






def restaurant_bill_order():
    print("\nRestaurant bill order.\n\nEnter the quantity of ordered items= ")
    print("\n\nplease pay aed=")
restaurant_bill_order()












