def seconden_per_dag(aantal):
    """ return het aantal seconden in aantal dagen 
            Tip! een dag is 24u, 
                 een uur is 60min, 
                 een minuut is 60s
    """
    uitkomst= ((60*60)*24)*aantal
    return uitkomst

print( seconden_per_dag(1) )    # 86400
print( seconden_per_dag(3) )    # 259200
print( seconden_per_dag(7) )    # 604800
