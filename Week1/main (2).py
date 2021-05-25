def Cm_to_Foot():
    CM = int(input("Cm:"))
    print("Transfer to", int(CM // 30.48), "foot", int((CM % 30.48) / 2.54), "inch\n")

def Foot_to_Cm():
    foot = int(input("Foot:"))
    inch = int(input("Inch:"))
    print("Transfer to", foot * 12 * 2.54 + inch * 2.54, "cm\n")

if __name__ == '__main__':
    while (1):
        print("Choice1:Centimeter To Foot (pleas enter 1)")
        print("Choice2:Foot To Centimeter (pleas enter 2)")
        print("Choice3:Exit this program (pleas enter 3)")
        choice = int(input("Please int put your choice"))
        if choice == 1:
            Cm_to_Foot()
        elif choice == 2:
            Foot_to_Cm()
        elif choice == 3:
            exit()
        else:
            print("Error Choice")


