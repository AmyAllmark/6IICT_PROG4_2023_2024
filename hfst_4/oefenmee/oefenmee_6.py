fruit_lijst = ["Appel", "Banaan", "Meloen", "Mango", "Druif"]

try:
    getal = int( input("Hoeveel fruit uit de lijst wil je printen: ") )
    for i in range(getal):
        fruit = fruit_lijst[i]
        print(fruit)

except IndexError:
    print("je ingegeven getal was te groot voor aantal dat je hebt")


except ValueError:
    print("geen int getal ingegeven snul")

