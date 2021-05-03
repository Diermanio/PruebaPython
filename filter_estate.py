from datetime import date

def zoneA(place):
    year = date.today().year
    price = (place['metros']*1000 + place['habitaciones']*5000 + place['garaje']*15000) * (1 - (year-place['año'])/100)
    return place | {'precio': round(price, 2)}

def zoneB(place):
    year = date.today().year
    price = (place['metros']*1000 + place['habitaciones']*5000 + place['garaje']*15000) * (1 - (year-place['año'])/100) *1.5
    return place | {'precio': round(price, 2)}

def run():

    DATA = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
            {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
            {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
            {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
            {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
    
    budget = input("Enter the budget for the property purchase \n")
    
    try:
        budget = float(budget)
        if budget<0: raise ValueError
    except ValueError:
        return print('Enter only numbers greater than 0')

    prices_A = list(map(lambda place: zoneA(place), list(filter(lambda x: x['zona']=='A', DATA))))
    prices_B = list(map(lambda place: zoneB(place), list(filter(lambda x: x['zona']=='B', DATA))))

    estate_prices = list(filter(lambda x: x['precio']<=budget, prices_A+prices_B))
    
    if estate_prices:
        return print(estate_prices)
    else:
        return print('No property available with the given budget')

if __name__ == "__main__":
    run()