document.getElementById("lab7").addEventListener("submit", (e) => {
    e.preventDefault();

    let val1 = document.getElementById("sub1").value;
    let val2 = document.getElementById("sub2").value;
    let val3 = document.getElementById("sub3").value;
    let val4 = document.getElementById("sub4").value;

    document.getElementById("output").innerHTML= `You have selected ${val1}, ${val2}, ${val3}, ${val4}`
});



