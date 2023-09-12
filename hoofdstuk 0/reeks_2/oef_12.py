""" Vraag een gebruiker naar de temperatuur in °F.
    Print de temp in °C (op 2 cijfers na de komma). 
    
    Celsius = (5/9)*(Fahrenheit-32)

    >>> Geef een temperatuur op in °F: 100
    100°F komt overeen met 37.78°C
"""
Fahrenheit= (int(input("geef de temperatuur in °F: ")))
Celsius = (5/9)*(Fahrenheit-32)
Celsius=round(Celsius,2)

print(f"{Fahrenheit}°F komt overeen met {Celsius}°C")