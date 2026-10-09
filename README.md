# Mini Calculator

A beginner-friendly calculator project with a FastAPI backend and a responsive HTML, CSS, and JavaScript frontend.

## Features

- Basic calculations: addition, subtraction, multiplication, and division
- More math operations: powers, modulus, percentage, square, square root, cube, cube root, and absolute value
- Scientific functions: factorial, natural logarithm, trigonometric functions, inverse trigonometric functions, and logarithms
- ANS button to reuse the previous answer
- Repeat Last button to run the previous calculation again
- Calculation history with search, individual delete, and Clear All options
- Responsive layout for smaller screens

## Technologies

- Python
- FastAPI
- HTML
- CSS
- JavaScript
- Font Awesome

## Project Structure

```text
Calculator/
├── backend/
│   ├── calculator.py
│   └── main.py
└── frontend/
    ├── index.html
    ├── script.js
    └── style.css

1.Start the backend
Open a terminal in the project folder and run:
cd backend
python -m pip install fastapi uvicorn
uvicorn main:app --reload

Keep this terminal running. The FastAPI backend will be available at:
http://127.0.0.1:8000

You can also open FastAPI's interactive API documentation at:
http://127.0.0.1:8000/docs

2. Start the frontend
Open frontend/index.html with the VS Code Live Server extension.
Keep both the backend and Live Server running while using the calculator.
How to Use
1. Enter numbers in the input fields.
2. Choose a calculator operation.
3. Use ANS to reuse the previous answer.
4. Open History to search past calculations, repeat one, delete one, or clear the history.

Learning Project
This project was built as a learning project to practise connecting a frontend to a Python API and adding interactive calculator features.
