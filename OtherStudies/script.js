"use strict";

/*let a = [1,2];

for (let i=2; i<=100; i++){
    for(let j=2; j<i; j++) {
        if (i%j==0){
            break;
        }else if (j==i-1){
            console.log(i);
            a.push(i);
        }
    }
    
}
console.log(a);
let min = a[1];
let max = 0; 

for (let i =0; i<a.length; i++){
    if(min>a[i]){
        min=a[i];
    }
    if(max<a[i]){
        max=a[i];
    }
}
console.log(min);
console.log(max);
console.log(Math.max(...a));
console.log(Math.min(...a));

for (let i =0; i<a.length; i++){
    console.log(a[i]);
}*/




let a = prompt("Дайте список чисел через кому").split(",");
let x = 0;
for (let i=0;i<a.length;i++){
    if(Number.parseFloat(a[i])%2==0)
    {
        x+=Number.parseFloat(a[i])**2;
    }
}
console.log('Cума всіх парних в квадраті ${x}');





// let a = 20;
// let b = 90;
// let x = 0;
// for (a; a <= b; a++) {
//     if (a % 7 == 1 || a % 7 == 2 || a % 7 == 5) {
        
//         x = x + a;
//     }
// }
// console.log(x);