from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,HTTPException
try:
    from calculator import add,subtract,multiply,divide,power,modulus,square,squareroot,cube,cuberoot,absolutevalue,percentage,factorial,absolutevalue,logarithm,naturallog,sine,cosine,tan,logarithm1,arcsine,arccosine,arctan,valid_log_with_base,history,process_result
    import calculator as calculator_module
except ImportError:
    from backend.calculator import add,subtract,multiply,divide,power,modulus,square,squareroot,cube,cuberoot,absolutevalue,percentage,factorial,logarithm,naturallog,sine,cosine,tan,logarithm1,arcsine,arccosine,arctan,history,process_result
    import backend.calculator as calculator_module


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Calculator API is working"}

@app.get("/menu")
def get_menu():
    return {
        "operations": {
            "add": "/add?a=number&b=number",
            "subtract": "/subtract?a=number&b=number",
            "multiply": "/multiply?a=number&b=number",
            "divide": "/divide?a=number&b=number",
            "power": "/power?a=number&b=number",
            "modulus": "/modulus?a=number&b=number",
            "percentage": "/percentage?a=number&b=number",
            "square": "/square?a=number",
            "square_root": "/squareroot?a=number",
            "cube": "/cube?a=number",
            "cube_root": "/cuberoot?a=number",
            "absolute_value": "/absolutevalue?a=number",
            "factorial": "/factorial?a=number",
            "logarithm": "/logarithm?a=number",
            "natural_log": "/naturallog?a=number",
            "sine": "/sine?a=degrees",
            "cosine": "/cosine?a=degrees",
            "tangent": "/tan?a=degrees",
            "logarithm_with_base": "/logarithm1?a=number&base=number",
            "arcsine": "/arcsine?a=number",
            "arccosine": "/arccosine?a=number",
            "arctangent": "/arctan?a=number"
        }
    }

@app.get("/add")
def test_add(a:float,b:float):
    result = add(a, b)
    process_result(result,f"{a} + {b}","add",a , b)
    calculator_module.save_last_calculation(add, "add", a, b)
    return {"result": result}

@app.get("/subtract")
def test_subtract(a: float, b: float):
    result = subtract(a, b)
    process_result(result, f"{a} - {b}", "subtract", a, b)
    calculator_module.save_last_calculation(subtract, "subtract", a, b)
    return {"result": result}

@app.get("/multiply")
def test_multiply(a: float, b: float):
    result = multiply(a, b)
    process_result(result, f"{a} * {b}", "multiply", a, b)
    calculator_module.save_last_calculation(multiply, "multiply", a, b)
    return {"result": result}

@app.get("/divide")
def test_divide(a: float, b: float):
    if b==0:
        raise HTTPException(
            status_code=400,
            detail="Cannot divide by zero"
        )
    result = divide(a, b)
    process_result(result, f"{a} / {b}", "divide", a, b)
    calculator_module.save_last_calculation(divide, "divide", a, b)
    return {"result": result}

@app.get("/power")
def test_power(a: float, b: float):
    try:
        result = power(a, b)
    except ZeroDivisionError:
        raise HTTPException(
            status_code=400,
            detail="Cannot raise 0 to a negative power"
        )
    except OverflowError:
        raise HTTPException(
            status_code=400,
            detail="The result is too large to calculate"
        )
    process_result(result, f"{a} ** {b}", "power", a, b)
    calculator_module.save_last_calculation(power, "power", a, b)
    return {"result": result}


@app.get("/modulus")
def test_modulus(a: float, b: float):
    if b == 0:
        raise HTTPException(
            status_code=400,
            detail="Cannot calculate modulus with zero"
        )
    result = modulus(a, b)
    process_result(result, f"{a} % {b}", "modulus", a, b)
    calculator_module.save_last_calculation(modulus, "modulus", a, b)
    return {"result": result}

@app.get("/square")
def test_square(a: float):
    result = square(a)
    process_result(result, f"square({a})", "square", a)
    calculator_module.save_last_calculation(square, "square", a)
    return {"result": result}

@app.get("/squareroot")
def test_squareroot(a: float):
    if a<0:
        raise HTTPException(
            status_code=400,
            detail="Square root requires a number greater than or equal to 0"
        )
    result = squareroot(a)
    process_result(result, f"sqrt({a})", "sqrt", a)
    calculator_module.save_last_calculation(squareroot, "sqrt", a)
    return {"result": result}

@app.get("/cube")
def test_cube(a: float):
    result = cube(a)
    process_result(result, f"cube({a})", "cube", a)
    calculator_module.save_last_calculation(cube, "cube", a)
    return {"result": result}

@app.get("/cuberoot")
def test_cuberoot(a: float):
    result = cuberoot(a)
    process_result(result, f"cuberoot({a})", "cuberoot", a)
    calculator_module.save_last_calculation(cuberoot, "cuberoot", a)
    return {"result": result}

@app.get("/absolutevalue")
def test_absolutevalue(a: float):
    result = absolutevalue(a)
    process_result(result, f"abs({a})", "absolute value", a)
    calculator_module.save_last_calculation(absolutevalue, "absolute value", a)
    return {"result": result}

@app.get("/percentage")
def test_percentage(a: float, b: float):
    result = percentage(a, b)
    process_result(result, f"{b}% of {a}", "percentage", a, b)
    calculator_module.save_last_calculation(percentage, "percentage", a, b)
    return {"result": round(result, 2)}

@app.get("/factorial")
def test_factorial(a:float):
    if a<0 or not a.is_integer():
        raise HTTPException(
            status_code=400,
            detail="Factorial requires a non-negative integer"
        )

    result= factorial(int(a))
    process_result(result, f"{int(a)}!", "factorial", int(a))
    calculator_module.save_last_calculation(factorial, "factorial", int(a))
    return  {"result":result}

@app.get("/logarithm")
def test_logarithm(a:float):
    if a <= 0:
        raise HTTPException(
            status_code=400,
            detail="Logarithm requires a number greater than 0"
        )

    result=logarithm(a)
    process_result(result, f"log10({a})", "log10", a)
    calculator_module.save_last_calculation(logarithm, "log10", a)
    return {"result":result}

@app.get("/naturallog")
def test_naturallog(a:float):
    if a <= 0:
        raise HTTPException(
            status_code=400,
            detail="Natural logarithm requires a number greater than 0"
        )
    result=naturallog(a)
    process_result(result, f"ln({a})", "natural log", a)
    calculator_module.save_last_calculation(naturallog, "natural log", a)
    return {"result":result}

@app.get("/sine")
def test_sine(a:float):
    result= sine(a)
    process_result(result, f"sin({a} degrees)", "sine", a)
    calculator_module.save_last_calculation(sine, "sine", a)
    return{"result":result}

@app.get("/cosine")
def test_cosine(a:float):
    result=cosine(a)
    process_result(result, f"cos({a} degrees)", "cosine", a)
    calculator_module.save_last_calculation(cosine, "cosine", a)
    return {"result":result}

@app.get("/tan")
def test_tan(a:float):
    try:
        result=tan(a)
        process_result(result, f"tan({a} degrees)", "tangent", a)
        calculator_module.save_last_calculation(tan, "tangent", a)
        return{"result":result}
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="tan is undefined for this angle"
        )

@app.get("/logarithm1")
def test_loagrithm1(a:float,base:float):

    if not valid_log_with_base(a,base):
        raise HTTPException(
            status_code=400,
            detail="Invalid input:number must be greater than 0 and base must be greater than 0 and not equal to 1"
        )
    result=logarithm1(a,base)
    process_result(result, f"log({a}, base {base})", "log base", a, base)
    calculator_module.save_last_calculation(logarithm1, "log base", a, base)
    return {"result":result}

@app.get("/arcsine")
def test_arcsine(a:float):
    if a < -1 or a > 1:
        raise HTTPException(
            status_code=400,
            detail="Arcsine requires a number between -1 and 1"
        )
    result=arcsine(a)
    process_result(round(result, 2), f"arcsin({a})", "arcsine", a)
    calculator_module.save_last_calculation(arcsine, "arcsine", a)
    return{"result":round(result,2)}

@app.get("/arccosine")
def test_arccosine(a: float):
    if a < -1 or a > 1:
        raise HTTPException(
            status_code=400,
            detail="Arccosine requires a number between -1 and 1"
        )
    result = arccosine(a)
    process_result(round(result, 2), f"arccos({a})", "arccosine", a)
    calculator_module.save_last_calculation(arccosine, "arccosine", a)
    return {"result": round(result,2)}

@app.get("/arctan")
def test_arctan(a:float):
    result=arctan(a)
    process_result(round(result, 2), f"arctan({a})", "arctangent", a)
    calculator_module.save_last_calculation(arctan, "arctangent", a)
    return{"result":round(result,2)}

@app.get("/history")
def get_history():
    return {"history": history}

@app.get("/ans")
def get_ans():
    return{"ans": calculator_module.ans}


@app.delete("/history/{number}")
def delete_history_item(number: int):
    if number < 1 or number > len(history):
        raise HTTPException(status_code=404, detail="History item not found")

    deleted_item = history.pop(number - 1)
    return {"deleted": deleted_item}

@app.delete("/history")
def clear_history():
    history.clear()
    return {"message": "History cleared"}

@app.post("/repeat")
def repeat_last_calculation():
    if calculator_module.last_operation is None:
        raise HTTPException(status_code=400, detail="No previous Calculation")
    calculator_module.show_repeat()

    return{
        "result":calculator_module.ans,
        "calculation":calculator_module.last_calculation,
        "first_number": calculator_module.last_num1,
        "second_number": calculator_module.last_num2
    }
