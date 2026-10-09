import math

menu_options={
    "1":"Addition",
    "2":"Subtraction",
    "3":"Multiplication",
    "4":"Division",
    "5":"power",
    "6":"Modulus",
    "7":"Percentage",
    "8":"Square",
    "9":"Squareroot",
    "10":"Cube",
    "11":"Cuberoot",
    "12":"Absolutevalue",
    "13":"Factorial",
    "14":"logarithm",
    "15":"naturallog",
    "16":"sine",
    "17":"cosine",
    "18":"tan",
    "19":"logwithbase",
    "20":"arcsine",
    "21":"arccosine",
    "22":"arctan",
    "history":"View history",
    "clear":"history clear",
    "exit":"Exit Calculator",
    "delete":"delete history item",
    "search":"search history",
    "repeat":"repeat last calculation"
    }
def show_menu():
    for key,value in menu_options.items():
        print(f"{key}. {value}")



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a**b

def modulus(a, b):
    return a%b

def percentage(a, b):
    return (a * b) / 100

def square(a):
    return a**2

def squareroot(a):
    return math.sqrt(a)

def cube(a):
    return a**3

def cuberoot(a):
    if a < 0:
        return -(abs(a) ** (1/3))
    else:
        return a ** (1/3)

def absolutevalue(a):
    return abs(a)

def factorial(a):
    return math.factorial(a)

def logarithm(a):
    return math.log10(a)

def naturallog(a):
    return math.log(a)

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tan(a):
    radians=math.radians(a)
    if math.isclose(math.cos(radians), 0, abs_tol=1e-10):
        raise ValueError("tan is undefined for this angle")
    return math.tan(radians)

def logarithm1(a, base):
    return math.log(a,base)

def arcsine(a):
    return math.degrees(math.asin(a))

def arccosine(a):
    return math.degrees(math.acos(a))

def arctan(a):
    return math.degrees(math.atan(a))

ans= None
last_calculation=None
last_operation = None
last_num1 = None
last_num2 = None
last_operation_name = None

#get number
def get_number(message):
    
    while True:
    
        try:
            value = input(message)
            if value.upper()=="ANS":
                if ans is None:
                    print("no answer available")
                    continue
                num= ans
            else:
                num=float(value)
            return num
        except ValueError:
            print("enter a valid number")

#get gistory number
def get_history_number():
    while True:
        value = input("Enter history number: ")
        try:
            number=int(value)
            return number
        except ValueError:
            print("enter a valid number")


#all valid devisor function
def valid_divisor(num2):
    if num2!=0:
        return True
    else:
        return False

def valid_squareroot(num):
    if num >=0:
        return True
    else:
        return False

def valid_factorial(num):
    if num>=0 and num==int(num):
        return True
    else:
        return False
def valid_logarithm(num):
    if num>0:
        return True
    else:
        return False

def valid_inverse_trig(num):
    if -1<=num<=1:
        return True
    else:
        return False

def valid_log_with_base(num3, num4):
    if ((num3>0 )and (num4>0 and num4!=1)):
        return True
    else:
        return False


#process result
def process_result(result,calculation,operation,first_number,second_number=None):
    global ans,last_calculation
    print(f"RESULT:{result:.2f}")
    ans = result
    if second_number is not None:
        calculation_data = {
            "first_number": first_number,
            "operation": operation,
            "second_number": second_number,
            "result": result
        }
        history.append(calculation_data)
    else:
        one_calculation_data={
            "operation": operation,
            "first_number": first_number,
            "result": result
        }
        history.append(one_calculation_data)
        
    
    last_calculation=calculation

#save last calculation
def save_last_calculation(operation,operation_name, num1=None, num2=None):
    global last_operation, last_num1, last_num2,last_operation_name
    last_operation = operation
    last_operation_name=operation_name
    last_num1 = num1
    last_num2 = num2




history=[]
def show_history():
    print("\n----------History----------")
    if (len(history)==0):
        print("No Calculations Yet")
        return
    else:
        for number, item in enumerate(history,start=1):
            if "second_number" in item:
                print(
                    f"{number}. {item['first_number']}",
                    f"{item['operation']}",
                    f"{item['second_number']}","=",
                    f"{item['result']}"
                )
            else:
                print(
                    f"{number}.{item['first_number']}",
                    f"{item['operation']}","=",
                    f"{item['result']}"
                )
    print("-----------------------------")

def search_history():
    if len(history)==0:
        print("No Calculations Yet")
        return
    keyword = input("Enter Choice:").lower().strip()
    found= False
    for number,item in enumerate(history,start=1):
        for value in item.values():
            if keyword in str(value).lower():
                if "second_number" in item:
                    print(
                        f"{number}.{item['first_number']}",
                        f"{item['operation']}",
                        f"{item['second_number']}","=",
                        f"{item['result']}"
                    )
                else:
                    print(
                        f"{number}.{item['operation']}",
                        f"({item['first_number']})","=",
                        f"{item['result']}"
                    )
                found=True
                break
    if not found:
        print("no matched item found")

def show_clear():
    while True:
        if len(history)==0:
            print("no calculations yet")
            return
        confirm=input("are you sure you want to clear history? (yes/no):").lower().strip()
        if confirm=="yes":
            history.clear()
            print("history cleared")
            break
        elif confirm=="no":
            print("history not cleared")
            break
        else:
            print("choose yes or no")

def show_delete():
    if len(history)==0:
        print("NO calculations yet")
        return
    delete_number= get_history_number()
    if delete_number >= 1 and delete_number <= len(history):
        delete_item=history.pop(delete_number-1)
        if "second_number" in delete_item:
            print(
                "Deleted: "
                f"{delete_item['first_number']}",
                f"{delete_item['operation']}",
                f"{delete_item['second_number']}","=",
                f"{delete_item['result']}"
            )
        else:
            print(
                "deleted:"
                f"{delete_item['operation']}",
                f"({delete_item['first_number']})","=",
                f"{delete_item['result']}",
            )
    else:
        print("invalid history number")

def show_repeat():
    if last_calculation is None or last_operation is None or last_num1 is None:
        print("No Previous Calculation")
    else:
        print(f"repeating:{last_calculation}")
        if last_num2 is not None:
            result= last_operation(last_num1,last_num2)
            process_result(result,last_calculation,last_operation_name,last_num1,last_num2)

        else:
            result=last_operation(last_num1)
            process_result(result,last_calculation,last_operation_name,last_num1)


            
     
#dictionaries
two_numbers_operations={
    "1":add,
    "2":subtract,
    "3":multiply,
    "4":divide,
    "5":power,
    "6":modulus,
    "7":percentage,
    "19":logarithm1
}

one_numbers_operations={
    "8":square,
    "9":squareroot,
    "10":cube,
    "11":cuberoot,
    "12":absolutevalue,
    "13":factorial,
    "14":logarithm,
    "15":naturallog,
    "16":sine,
    "17":cosine,
    "18":tan,
    "20":arcsine,
    "21":arccosine,
    "22":arctan
}

symbols = {
    "1": "+",
    "2": "-",
    "3": "x",
    "4": "/",
    "5": "**",
    "6": "%",
    "7": " % of ",
    "19": " log base "
}
one_number_names = {
    "8": "square",
    "9": "sqrt",
    "10": "cube",
    "11": "cuberoot",
    "12": "abs",
    "13": "factorial",
    "14": "log",
    "15": "ln",
    "16": "sin",
    "17": "cos",
    "18": "tan",
    "20": "arcsin",
    "21": "arccos",
    "22": "arctan"
}

two_number_names = {
    "1": "add",
    "2": "subtract",
    "3": "multiply",
    "4": "divide",
    "5": "power",
    "6": "modulus",
    "7": "percentage",
    "19": "logwithbase"
}

def handle_two_numbers(choice):
    num1= get_number("enter first number:")
    num2= get_number("enter second number:")
    if choice in ["4","6"]:
        if not valid_divisor(num2):
            print("numbers cannot divide by zero")    
            return
    if choice=="19":
        if not valid_log_with_base(num1,num2):
            print("Invalid number or base")
            return
    try:
        result=two_numbers_operations[choice](num1,num2)
        process_result(result,
                       f"{num1:.2f}{symbols[choice]}{num2:.2f}",
                       two_number_names[choice],
                       num1,
                       num2
                    )
        save_last_calculation(two_numbers_operations[choice],   two_number_names[choice],num1,num2)
    except ValueError:
        print("invalid value")
    except Exception as e:
        print("something went wrong",e)
        print("\n")

def handle_one_number(choice):
    num= get_number("enter number:")
    if choice=="9":
        if not valid_squareroot(num):
            print("number cannot be negative")
            return
    if choice=="13":
        if not valid_factorial(num):
            print("number must be integer and greater than or equal to zero")
            return
        num=int(num)
    if choice in ["14","15"]:
        if not valid_logarithm(num):
            print("number must be greater than zero")
            return
    if choice in ["20","21"]:
        if not valid_inverse_trig(num):
            print("Number must be between -1 and 1")
            return
    try:
        result=one_numbers_operations[choice](num)
        process_result(result,
                       f"{one_number_names[choice]}({num:.2f})",
                       one_number_names[choice],
                       num,
                    )
        save_last_calculation(one_numbers_operations[choice],one_number_names[choice],num)
    except ValueError as e:
        print(e)
    except Exception as e:
        print("something went wrong",e)
        print("\n")
if __name__ == "__main__":
    print("----mini calc-----")
    while True:
        show_menu()
        
        choice = (input("Enter your choice: ")).lower().strip()
            
        if choice=="exit":
            print("calculator closed")
            break

        elif choice=="repeat":
            show_repeat()
            

        elif choice=="search":
            search_history()


        elif choice=="history":
            show_history()

        elif choice=="clear":
            show_clear()

        elif choice=="delete":
            show_delete()
            
        elif choice in two_numbers_operations:
            handle_two_numbers(choice)

        elif choice in one_numbers_operations:
            handle_one_number(choice)
            
        else:
            print("invalid choice")



