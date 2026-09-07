let consolebutton = document.getElementById("consolebutton");
consolebutton.addEventListener("click", conPrint)

let alertbutton = document.getElementById("alertbutton");
alertbutton.addEventListener("click", pageAlert);

/*let lionbutton = document.getElementById("lionbutton");
lionbutton.addEventListener("click", function() {
    clicked(lionbutton)});*/

/*let frogbutton = document.getElementById("frogbutton");
frogbutton.addEventListener("click", function (){
    clicked(frogbutton)});*/

let lionbutton = document.getElementById("lionbutton");
let lionimg = document.getElementById("lionimg");
let roar = document.getElementById("roar");
let lioncount = document.getElementById("lioncount");
let lionclick = 0;
lionbutton.addEventListener("click", function() {
    roar.style.display = "block"
    ribbit.style.display = "none"
    lionclick++;
    lioncount.textContent = `Clicked ${lionclick} times!`

});

let frogbutton = document.getElementById("frogbutton");
let frogimg = document.getElementById("frogimg");
let ribbit = document.getElementById("ribbit");
let frogcount = document.getElementById("frogcount");
let frogclick = 0;
frogbutton.addEventListener("click", function() {
    ribbit.style.display = "block"
    roar.style.display = "none"
    frogclick++;
    frogcount.textContent = `Clicked ${frogclick} times!`
});

function conPrint(){
    console.log("Hi there! JavaScript is cool!")
};

function pageAlert(){
    alert("Hi there! JavaScript is cool!")
};

function clicked(button){
    button.textContent = `The ${button.id} is clicked`
};