def run():
    
    age = input("Enter your age \n")
    assert age.isnumeric(), "Only numeric values greater than 0"
    
    incomes = input("Input your monthly income \n")
    assert incomes.isnumeric(), "Only numeric values greater than 0"

    if int(age)>17 and int(incomes) >=1000: print("Must Tribute")
    else: print("Must not tribute")



if __name__ == "__main__":
    run()