from datetime import date

def zoneA(place):
    """ Method to calculate the price of properties which are in zone A """
    year = date.today().year
    price = (place['metros']*1000 + place['habitaciones']*5000 + place['garaje']*15000) * (1 - (year-place['año'])/100)
    return place | {'precio': round(price, 2)}

def zoneB(place):
    """ Method to calculate the price of properties which are in zone B """
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
    
    #Se valida si el presupuesto ingresado es un número y también si es mayor que cero
    try:
        budget = float(budget)
        if budget<0: raise ValueError
    except ValueError:
        return print('Enter only numbers greater than 0')

    #Se realiza el calculo del precio de los inmuebles acorde a la zona que pertenezcan mediante un previo filtro, una vez hecho esto
    #se llama a los metodos zoneA y zoneB que se encargan de retornar el mismo diccionario junto a una nueva llave llamada precio
    #que tendrá el valor del mismo. Si bien es cierto que lo único que difieren los precios de la zonaB con la zonaA es un factor multiplicativo de 1.5
    #por temas de mantenimiento de código en caso de que estas fórmulas cambien y no dependan de la otra, es mejor tener la forma de sacar su precio en métodos separados
    prices_A = list(map(lambda place: zoneA(place), list(filter(lambda x: x['zona']=='A', DATA))))
    prices_B = list(map(lambda place: zoneB(place), list(filter(lambda x: x['zona']=='B', DATA))))

    estate_prices = list(filter(lambda x: x['precio']<=budget, prices_A+prices_B))
    
    #Finalmente si la lista es distinto de vacío imprime su contenido, caso contrario informa al usuario que no existen inmuebles con el presupuesto dado
    if estate_prices:
        return print(estate_prices)
    else:
        return print('No property available with the given budget')

if __name__ == "__main__":
    run()