document.getElementById("lab7-2").addEventListener("submit", (e) => {
    e.preventDefault();
    let num1 = Number(document.getElementById("firstnum").value);
    let num2 = Number(document.getElementById("secnum").value);
    let num3 = Number(document.getElementById("thirdnum").value);
    let opr = document.getElementById("operator").value;

    let result;

    switch(opr) {
        case "+":
            result = num1 + num2
            break;
        case "-":
            result = num1 - num2
            break;
        case "/":
            result = num1 / num2
            break;
        case "*":
            result = num1 * num2
            break;
    }

    if(num3 === result){
        document.getElementById("msg").innerHTML = "Correct!";
    } else{
        document.getElementById("msg").innerHTML = "Incorrect, please try again.";
    }

});