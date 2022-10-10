def meter_fare():
    flagdown = float(input("What's the flag-down fare: $"))
    rate1 = float(input("What's the rate per 400 meters within 9.8km? :$"))
    rate2 = float(input("What's the rate per 350 meters beyond 9.8km? :$"))
    distance = int(input("What's the distance travelled (in metres)? :"))
    
    if distance > 9800: 
        total1 = round((distance -9800)/350) * rate2 + 22 * rate1 + flagdown
    elif distance > 1000: 
        total1 = round((distance - 1000)/400) * rate1 + flagdown
    else: 
        total1 = flagdown
    
    return total1 

def time_surcharge():
    peak = input("Is the ride during a peak period [yes|no]?")
    
    if peak == "yes": 
        total2 = total1 * 0.25
    else: 
        night = input("Is the ride between midnight and 6am [yes|no]?")
        if night == "yes": 
            total2 = total1 * 0.50 
        else: 
            total2 = 0 
    
    return total2

def location_surcharge():
    location = input("Is there any location surcharge [yes|no]?")
    if location == "yes":
        total3 = float(input("What's the location surcharge? :$"))
    else: 
        total3 = 0 
    
    return total3

total1 = meter_fare()
total2 = time_surcharge()
total3 = location_surcharge()
total4 = round (total1 + total2 + total3, 2)

print ("The total fare is $", str(total4))