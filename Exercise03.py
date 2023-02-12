
COMMERCIAL = 0.5
RESIDENTIAL = 0.25


while True:
    building_type = input("residential or commercial or 'x' to exit: ").lower()

    if building_type[0] != "r" and building_type[0] != "c" \
            and building_type[0] != "x":
        print("please enter a 'r' or 'c' or 'x'")
    if building_type == "x":
        exit("Bruh")



