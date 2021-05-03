def run():
    
    #Se valida que la edad y los ingresos sean numeros y mayores a 0
    age = input("Enter your age \n")
    assert age.isnumeric(), "Only numeric values greater than 0"
    
    incomes = input("Input your monthly income \n")
    assert incomes.isnumeric(), "Only numeric values greater than 0"

    #Si cumple que es mayor de edad y sus ingresos son mayores o iguales a 1000 deberá tributar, caso contrario no
    if int(age)>17 and int(incomes) >=1000: print("Must Tribute")
    else: print("Must not tribute")



if __name__ == "__main__":
    run()