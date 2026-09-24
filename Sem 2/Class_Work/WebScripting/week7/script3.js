let count = 0;
let intervalId = null;

document.getElementById("start").addEventListener("click", ()=>{
    if (intervalId !== null){
        return;
    }
    
    intervalId = setInterval(()=> {
        count += 1;
        document.getElementById("msg").innerHTML = count;
    }, 1000)
});

document.getElementById("stop").addEventListener("click", () => {
    clearInterval(intervalId);
    intervalId = null;
    count = 0
    document.getElementById("msg").innerHTML = count;
});