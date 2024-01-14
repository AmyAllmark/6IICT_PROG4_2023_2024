fruit_lijst = ["Appel", "Banaan", "Kers"]
try:
    getal = input( "Geef een getal: " )
    if "." in getal:
        getal = float( getal )
    else:
        getal = int( getal )
    print( fruit_lijst[getal] )

except ValueError:
    print("geen nummer ingegeven")

except IndexError:
    print("te hoog nummer ingegeven voor de lijst")

except TypeError:
    print("gebruik een int en geen float")

except Exception:
    print( "Er ging iets fout" ) 

print("Programma klaar") 