const num1 = document.getElementById("num1");
const num2 = document.getElementById("num2");
const addBtn = document.getElementById("addBtn");
const result = document.getElementById("result");
const subtractBtn = document.getElementById("subtractBtn");
const multiplyBtn = document.getElementById("multiplyBtn");
const divideBtn = document.getElementById("divideBtn");
const powerBtn = document.getElementById("powerBtn");
const modulusBtn = document.getElementById("modulusBtn");
const squareBtn = document.getElementById("squareBtn");
const squarerootBtn = document.getElementById("squarerootBtn");
const cubeBtn = document.getElementById("cubeBtn");
const cuberootBtn = document.getElementById("cuberootBtn");
const absolutevalueBtn = document.getElementById("absolutevalueBtn");
const percentageBtn = document.getElementById("percentageBtn");
const factorialBtn = document.getElementById("factorialBtn");
const naturallogBtn = document.getElementById("naturallogBtn");
const sineBtn = document.getElementById("sineBtn");
const cosineBtn = document.getElementById("cosineBtn");
const tanBtn = document.getElementById("tanBtn");
const logarithm1Btn = document.getElementById("logarithm1Btn");
const arcsineBtn = document.getElementById("arcsineBtn");
const arccosineBtn = document.getElementById("arccosineBtn");
const arctanBtn = document.getElementById("arctanBtn");
const logarithmBtn = document.getElementById("logarithmBtn");
const historyList = document.getElementById("historyList");
const historyToggle = document.getElementById("historyToggle");
const historySection = document.querySelector(".history-section");
const ansBtn = document.getElementById("ansBtn");
const clearHistoryBtn = document.getElementById("clearHistoryBtn");
const repeatBtn = document.getElementById("repeatBtn");
const historySearch = document.getElementById("historySearch");




num1.addEventListener("input", function () {
    if (num1.value==="" && num2.value==="") {
        result.textContent="";
    }
});

num2.addEventListener("input", function () {
    if (num1.value==="" && num2.value==="") {
        result.textContent="";
    }
})




addBtn.addEventListener("click", function () {
    if (num1.value === "" || num2.value === "") {
    result.textContent = "Please enter both numbers";
    return;
    }
    const a = Number(num1.value);
    const b = Number(num2.value);

    fetch(`http://127.0.0.1:8000/add?a=${a}&b=${b}`)
    .then(response => response.json())
    .then(data => {
        result.textContent = data.result;
        loadHistory();
    });
});

subtractBtn.addEventListener("click", function () {
    if (num1.value === "" || num2.value === "") {
    result.textContent = "Please enter both numbers";
    return;
    }
    const a = Number(num1.value);
    const b = Number(num2.value);

    fetch(`http://127.0.0.1:8000/subtract?a=${a}&b=${b}`)
        .then(response => response.json())
        .then(data => {
            result.textContent = data.result;
            loadHistory();
        });
});

multiplyBtn.addEventListener("click",function () {
    if (num1.value === "" || num2.value === "") {
    result.textContent = "Please enter both numbers";
    return;
    }
    const a = Number(num1.value);
    const b = Number(num2.value);

    fetch(`http://127.0.0.1:8000/multiply?a=${a}&b=${b}`)
    .then(response => response.json())
    .then(data => {
        result.textContent = data.result;
        loadHistory();
    });
});

divideBtn.addEventListener("click", function () {
    console.log("DIVIDE BUTTON CLICKED");
    if (num1.value === "" || num2.value === "") {
    result.textContent = "Please enter both numbers";
    return;
    }
    const a = Number(num1.value);
    const b = Number(num2.value);

    fetch(`http://127.0.0.1:8000/divide?a=${a}&b=${b}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                result.textContent = data.error;
            } else {
                result.textContent = data.result;
                loadHistory();
            }
        });
});

powerBtn.addEventListener("click", function () {
    if (num1.value === "" || num2.value === "") {
    result.textContent = "Please enter both numbers";
    return;
    }
    const a = Number(num1.value);
    const b = Number(num2.value);

    fetch(`http://127.0.0.1:8000/power?a=${a}&b=${b}`)
        .then(response => response.json())
        .then(data => {
            result.textContent = data.result;
            loadHistory();
        });
});

modulusBtn.addEventListener("click", function () {
    if (num1.value === "" || num2.value === "") {
    result.textContent = "Please enter both numbers";
    return;
    }
    const a = Number(num1.value);
    const b = Number(num2.value);

    fetch(`http://127.0.0.1:8000/modulus?a=${a}&b=${b}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                result.textContent = data.error;
            } else {
                result.textContent = data.result;
                loadHistory();
            }
        });
});

squareBtn.addEventListener("click", function () {
    if (num1.value === "") {
    result.textContent = "Please enter a number";
    return;
    }
    const a = Number(num1.value);

    fetch(`http://127.0.0.1:8000/square?a=${a}`)
        .then(response => response.json())
        .then(data => {
            result.textContent = data.result;
            loadHistory();
        });
});

squarerootBtn.addEventListener("click", function () {
    if (num1.value === "") {
    result.textContent = "Please enter a number";
    return;
    }
    const a = Number(num1.value);

    fetch(`http://127.0.0.1:8000/squareroot?a=${a}`)
        .then(response => response.json())
        .then(data => {
            result.textContent = data.result;
            loadHistory();
        });
});

cubeBtn.addEventListener("click", function () {
    if (num1.value === "") {
    result.textContent = "Please enter a number";
    return;
    }
    const a = Number(num1.value);

    fetch(`http://127.0.0.1:8000/cube?a=${a}`)
        .then(response => response.json())
        .then(data => {
            result.textContent = data.result;
            loadHistory();
        });
});

cuberootBtn.addEventListener("click", function () {
    if (num1.value === "") {
    result.textContent = "Please enter a number";
    return;
    }
    const a = Number(num1.value);

    fetch(`http://127.0.0.1:8000/cuberoot?a=${a}`)
        .then(response => response.json())
        .then(data => {
            result.textContent = data.result;
            loadHistory();
        });
});

absolutevalueBtn.addEventListener("click", function () {
    if (num1.value === "") {
    result.textContent = "Please enter a number";
    return;
    }
    const a = Number(num1.value);

    fetch(`http://127.0.0.1:8000/absolutevalue?a=${a}`)
        .then(response => response.json())
        .then(data => {
            result.textContent = data.result;
            loadHistory();
        });
});

percentageBtn.addEventListener("click", function () {
    if (num1.value === "" || num2.value === "") {
    result.textContent = "Please enter both numbers";
    return;
    }
    const a = Number(num1.value);
    const b = Number(num2.value);

    fetch(`http://127.0.0.1:8000/percentage?a=${a}&b=${b}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                result.textContent = data.error;
            } else {
                result.textContent = data.result;
                loadHistory();
            }
        });
});




factorialBtn.addEventListener("click", function () {
    if (num1.value === "") {
    result.textContent = "Please enter a number";
    return;
    }
    const a = Number(num1.value);

    fetch(`http://127.0.0.1:8000/factorial?a=${a}`)
        .then(response => response.json())
        .then(data => {
            if (data.detail) {
                result.textContent = data.detail;
            } else {
                result.textContent = data.result;
                loadHistory();
            }
        });
});

naturallogBtn.addEventListener("click", function () {
    if (num1.value === "") {
    result.textContent = "Please enter a number";
    return;
    }
    const a = Number(num1.value);

    fetch(`http://127.0.0.1:8000/naturallog?a=${a}`)
        .then(response => response.json())
        .then(data => {
            if (data.detail) {
                result.textContent = data.detail;
            } else {
                result.textContent = data.result;
                loadHistory();
            }
        });
});


sineBtn.addEventListener("click", function () {
    if (num1.value === "") {
    result.textContent = "Please enter a number";
    return;
    }
    const a = Number(num1.value);

    fetch(`http://127.0.0.1:8000/sine?a=${a}`)
        .then(response => response.json())
        .then(data => {
            if (data.detail) {
                result.textContent = data.detail;
            } else {
                result.textContent = data.result;
                loadHistory();
            }
        });
});


cosineBtn.addEventListener("click", function () {
    if (num1.value === "") {
    result.textContent = "Please enter a number";
    return;
    }
    const a = Number(num1.value);

    fetch(`http://127.0.0.1:8000/cosine?a=${a}`)
        .then(response => response.json())
        .then(data => {
            if (data.detail) {
                result.textContent = data.detail;
            } else {
                result.textContent = data.result;
                loadHistory();
            }
        });
});


tanBtn.addEventListener("click", function () {
    if (num1.value === "") {
    result.textContent = "Please enter a number";
    return;
    }
    const a = Number(num1.value);

    fetch(`http://127.0.0.1:8000/tan?a=${a}`)
        .then(response => response.json())
        .then(data => {
            if (data.detail) {
                result.textContent = data.detail;
            } else {
                result.textContent = data.result;
                loadHistory();
            }
        });
});


logarithm1Btn.addEventListener("click", function () {
    if (num1.value === "" || num2.value === "") {
    result.textContent = "Please enter both numbers";
    return;
    }
    const a = Number(num1.value);
    const base = Number(num2.value);

    fetch(`http://127.0.0.1:8000/logarithm1?a=${a}&base=${base}`)
        .then(response => response.json())
        .then(data => {
            if (data.detail) {
                result.textContent = data.detail;
            } else {
                result.textContent = data.result;
                loadHistory();
            }
        });
});


arcsineBtn.addEventListener("click", function () {
    if (num1.value === "") {
    result.textContent = "Please enter a number";
    return;
    }
    const a = Number(num1.value);

    fetch(`http://127.0.0.1:8000/arcsine?a=${a}`)
        .then(response => response.json())
        .then(data => {
            if (data.detail) {
                result.textContent = data.detail;
            } else {
                result.textContent = data.result;
                loadHistory();
            }
        });
});


arccosineBtn.addEventListener("click", function () {
    if (num1.value === "") {
    result.textContent = "Please enter a number";
    return;
    }
    const a = Number(num1.value);

    fetch(`http://127.0.0.1:8000/arccosine?a=${a}`)
        .then(response => response.json())
        .then(data => {
            if (data.detail) {
                result.textContent = data.detail;
            } else {
                result.textContent = data.result;
                loadHistory();
            }
        });
});


arctanBtn.addEventListener("click", function () {
    if (num1.value === "") {
    result.textContent = "Please enter a number";
    return;
    }
    const a = Number(num1.value);

    fetch(`http://127.0.0.1:8000/arctan?a=${a}`)
        .then(response => response.json())
        .then(data => {
            if (data.detail) {
                result.textContent = data.detail;
            } else {
                result.textContent = data.result;
                loadHistory();
            }
        });
});


logarithmBtn.addEventListener("click", function () {
    if (num1.value === "") {
    result.textContent = "Please enter a number";
    return;
    }
    const a = Number(num1.value);

    fetch(`http://127.0.0.1:8000/logarithm?a=${a}`)
        .then(response => response.json())
        .then(data => {
            if (data.detail) {
                result.textContent = data.detail;
            } else {
                result.textContent = data.result;
                loadHistory();
            }
        });
});


function loadHistory() {
    fetch("http://127.0.0.1:8000/history")
        .then(response => response.json())
        .then(data => {
            historyList.innerHTML = "";
            if (data.history.length === 0) {
                const emptyMessage = document.createElement("li");
                emptyMessage.textContent = "No history yet. Your calculations will appear here.";
                emptyMessage.className = "empty-history";
                historyList.appendChild(emptyMessage);
                return;
}
            data.history.forEach((item, index) => {
                const listItem = document.createElement("li");
                const calculationText = document.createElement("span");
                if ("second_number" in item) {
                    calculationText.textContent =
                        `${item.first_number} ${item.operation} ${item.second_number} = ${item.result}`;
                } else {
                    calculationText.textContent =
                        `${item.operation}(${item.first_number}) = ${item.result}`;
                }

                const repeatHistoryButton = document.createElement("button");
                repeatHistoryButton.textContent="↻";
                repeatHistoryButton.type="button";
                repeatHistoryButton.className="repeat-history-btn";
                repeatHistoryButton.title="Use this Calculation";
                repeatHistoryButton.setAttribute("aria-label","Use this Calculation");

                repeatHistoryButton.addEventListener("click", function () {
                    num1.value=item.first_number;
                    if ("second_number" in item){
                        num2.value=item.second_number;
                    } else {
                        num2.value="";
                    }
                });

                const deleteButton = document.createElement("button");
                deleteButton.textContent="x";
                deleteButton.type = "button";
                deleteButton.className = "delete-history-btn";

                deleteButton.addEventListener("click", function () {
                    fetch(`http://127.0.0.1:8000/history/${index + 1}`, {
                        method: "DELETE"
                    })
                        .then(response => response.json())
                        .then(()=> loadHistory());
                });

                listItem.appendChild(calculationText);
                listItem.appendChild(repeatHistoryButton)
                listItem.appendChild(deleteButton);
                historyList.appendChild(listItem);
                
            });
        });
}


historySearch.addEventListener("input", function () {
    const searchText = historySearch.value.trim().toLowerCase();
    const historyItems = historyList.querySelectorAll("li");
    historyItems.forEach( function (historyItem){
        const itemText = historyItem.textContent.toLowerCase();
        if(itemText.includes(searchText)){
            historyItem.style.display="";
        } else {
            historyItem.style.display = "none";
        }
    });  
});



document.addEventListener("click", function (event) {
    const clickedInsideHistory = historySection.contains(event.target);
    const clickedHistoryButton = historyToggle.contains(event.target);

    if (!clickedInsideHistory && !clickedHistoryButton) {
        historySection.style.display = "none";
    }
});



historySection.style.display = "none";

historyToggle.addEventListener("click", function () {
    const isHidden = historySection.style.display === "none";

    if (isHidden) {
        historySection.style.display = "block";
        loadHistory();
    } else {
        historySection.style.display = "none";
    }
});


ansBtn.addEventListener("click", function () {
    fetch("http://127.0.0.1:8000/ans")
        .then(response => response.json())
        .then(data => {
            if (data.ans === null) {
                result.textContent = "No previous answer";
            } else {
                num1.value = data.ans;
            }
        });
});

clearHistoryBtn.addEventListener("click", function () {
    const shouldClear = confirm("Are you sure you want to delete all history?");

    if (!shouldClear) {
        return;
    }

    fetch("http://127.0.0.1:8000/history", {
        method: "DELETE"
    })
        .then(response => response.json())
        .then(data => {
            
            loadHistory();
        });
});

repeatBtn.addEventListener("click", function () {
    fetch("http://127.0.0.1:8000/repeat", {
        method: "Post"
    })
    .then(response=> response.json())
    .then(data=> {
        if (data.detail){
            result.textContent = data.detail;
        } else{
            num1.value = data.first_number;
            if (num2.value !==null) {
                num2.value= data.second_number;
            } else {
                num2.value = "";
            }
            result.textContent = `${data.result}`
            loadHistory();
        }
    })
})



document.addEventListener("keydown", function (event) {
    if (event.key==="ArrowRight" && document.activeElement=== num1){
        num2.focus()
    }
});

document.addEventListener("keydown", function (event) {
    if (event.key==="ArrowLeft" && document.activeElement=== num2){
        num1.focus()
    }
});



