pi = 3.1415926535897931


def cube():
    while True:
        try:
            my1 = int(input("Enter the cube edge value: "))
            V = my1 * my1 * my1

        except:
            print("Error. Please enter numeric value only ->")
            continue
        else:
            print(f"The volume of your cube is {V}! Thank you!")
            break


def sphere():
    while True:
        try:
            my1 = int(input("Enter the sphere radius value: "))
            V = 4.0 / 3.0 * pi * my1**3

        except:
            print("Error. Please enter numeric value only ->")
            continue
        else:
            print(f"The volume of your sphere is {V}! Thank you!")
            break


def cuboid():
    while True:
        try:
            my1 = int(input("Enter the cuboid lenght value: "))
            my2 = int(input("Enter the cuboid width value: "))
            my3 = int(input("Enter the cuboid height value: "))
            V = my1 * my2 * my3

        except:
            print("Error. Please enter numeric value only ->")
            continue
        else:
            print(f"The volume of your cuboid is: {V}! Thank you!")
            break


def cone():
    while True:
        try:
            my1 = int(input("Enter the cone radius value: "))
            my2 = int(input("Enter the cone height value: "))
            V = pi * (my1 * my1) * my2 / 3

        except:
            print("Error. Please enter numeric value only.")
            continue
        else:
            print(f"The volume of your cone is {V}! Thank you!")
            break


def cylinder():
    while True:
        try:
            my1 = int(input("Enter the cylinder radius value: "))
            my2 = int(input("Enter the cylinder height value: "))
            V = pi * (my1 * my1) * my2
        except:
            print("Error. Please enter numeric value only")
            continue
        else:
            print(f"The volume of your cylinder is {V}! Thank you!")
            break


def prism():
    while True:
        try:
            my1 = int(input("Enter the prism base surface value: "))
            my2 = int(input("Enter the prism height value : "))
            V = my1 * my2

        except:
            print("Error. Please enter numeric value only")
            continue
        else:
            print(f"The volume of your prism is {V}! Thank you!")
            break


def pyramid():
    while True:
        try:
            my1 = int(input("Enter the pyramind base length value: "))
            my2 = int(input("Enter the pyramid base width value: "))
            my3 = int(input("Enter the pyramid height value: "))
            V = (my1 * my2 * my3) / 3

        except:
            print("Error. Please enter numeric value only.")
            continue
        else:
            print(f"The volume of your pyramid is {V}! Thank you!")
            break


def use_again():
    question = input("Would you like to choose another object (yes/no)?: ")
    if question.lower() == "yes":
        calculator()
    if question.lower() == "no":
        print("Thank you for using 3D object volume calculator!")
        quit()
    else:
        print("Error. Please answer with 'yes' or 'no' ->")
        use_again()


def calculator():
    print(
        "Welcome to the 3D object volume calculator. You can choose any of the given objects from the list: * Cube; * Sphere; * Cuboid; * Cone; * Cylinder; * Prism; * Pyramid."
    )
    choice = input("Choose your 3D object. Simply type the name of the object: ")
    if choice.lower() == "cube":
        cube()
        use_again()
    if choice.lower() == "sphere":
        sphere()
        use_again()
    if choice.lower() == "cuboid":
        cuboid()
        use_again()
    if choice.lower() == "cone":
        cone()
        use_again()
    if choice.lower() == "cylinder":
        cylinder()
        use_again()
    if choice.lower() == "prism":
        prism()
        use_again()
    if choice.lower() == "pyramid":
        pyramid()
        use_again()
    else:
        print(
            "Error. Please type the name of the object correctly and start from the start"
        )
        calculator()

calculator()
