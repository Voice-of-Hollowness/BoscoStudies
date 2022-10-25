"use strict";

// const cars = ["bmw","Volkswagen","Daewoo","Mercedes","Lexus"]

// let i,
//   html = "",
//     count = cars.length;

// for (i=0;i<count;i++){

// html += cars[i]+"<br>";
// }




// let html = ""
// let button = document.querySelector("#calc");

// button.onclick = function(){
//     let num = document.querySelector("#a").value;

//     for(let i num.length; i>=0;i--){

//     }


//     document.querySelector("#test").innerHTML=html;
// }

let num = prompt("Bin num");
let k = 1;
sum=0
for (let i = 0; i<=num.length; i++ ){
sum += num[i]*k;
k= k*2;
}
console.log(sum);
