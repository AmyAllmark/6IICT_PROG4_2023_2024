# Bepaal de som van alle elementen (en sub-elementen) in een (geneste) lijst.
import test_module

def som_lijst(lijst):
    aantal = 0
    for element in lijst:
        if type(element) == int:
           aantal= element+ aantal
        elif type(element)== list:
           aantal= aantal+som_lijst(element)

        # ALS element een sublijst is...
        #   DAN tel som van sublijst op bij aantal.
 
    return aantal
print( som_lijst([1, [2, 3] , 4]) ) # 10



print( som_lijst([1,2,3,4]) )           # 10
print( som_lijst([1, [2,3], 4]) )       # 10
print( som_lijst([1,2,[3,[4]]]) )       # 10
print( som_lijst([1, [2, [3, [4]]]]) )  # 10
print(som_lijst([2,3]))