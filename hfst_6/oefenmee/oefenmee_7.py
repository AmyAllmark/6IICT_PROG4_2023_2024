# examen 


# Tel alle cijfers in een getal op.
# groote getallen elk getal daarvan bij elkaar optellen 

def optellen(getal):
    getal = f"{getal}" # string maken van het getalvbfgf
    if len(getal)== 1:
        return getal
    som= int(getal[0]) + int(optellen(getal[1:]))#  1 vanaf het tweede lettertje tot het einde omdat je : gebruikt  
    # int gebruiken want hij kan geen strings optellen 
    return som

print( optellen(12345) )            # 15
print( optellen(5) )                # 5
print( optellen(4687612962034330) ) # 64
print( optellen(6728003096702784) ) # 69