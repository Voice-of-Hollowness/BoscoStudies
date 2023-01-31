/*
let button = document.querySelector("#calc");
console.log(button);

button.onclick = function(){
    let a = document.querySelector("#a").value;
    let b = document.querySelector("#b").value;
    let c = document.querySelector("#c").value;

    if(b>0){
        if (c>0){document.querySelector("#expresion").innerHTML = a+"x^2+"+b+"x+"+c+"=0";}
        else if(c<0){document.querySelector("#expresion").innerHTML = a+"x^2+"+b+"x"+c+"=0";}
        else{document.querySelector("#expresion").innerHTML = a+"x^2"+b+"x+=0";}
    }
    else if(b<0){
        if (c>0){document.querySelector("#expresion").innerHTML = a+"x^2"+b+"x+"+c+"=0";}
        else if(c<0){document.querySelector("#expresion").innerHTML = a+"x^2"+b+"x"+c+"=0";}
        else{document.querySelector("#expresion").innerHTML = a+"x^2"+b+"x=0";}
    let d= (b**2 - 4*a*c);

    if(d>0){
        let x1 = (-b + Math.sqrt(d))/(2*a);
        let x2 = (-b - Math.sqrt(d))/(2*a);
        console.log("x1 ="+x1+", x2="+x2);
        document.querySelector("#result").innerHTML = "x1 = "+x1+", x2 = "+x2;
    } else if(d==0){
        let x1 = x2 = -b/(2*a);
        console.log("x1 = x2="+x1);
        document.querySelector("#result").innerHTML = "x1 = x2="+x2;
    } else {
        console.log("Коренів немає");
        document.querySelector("#result").innerHTML = "Коренів немає";
    } 

}
};*/

/*let html = ""
let button = document.querySelector("#calc");

button.onclick = function(){
    let a = document.querySelector("#a").value;
     for (let i=0; i<=a; i++){
        if (i == 0 || i%2==0){
            html += i +"<br>";
        }
    }
}*/

/*
let cnf = "This numb got into array",
    deny = "This numb didn`t got into array";
let button2 = document.querySelector("#show");

let html = ""
let button = document.querySelector("#calc");

button.onclick = function(){
    let a = document.querySelector("#a").value;

    if (a == 0 || a%2==0){
        html += a +"<br>";
        document.querySelector("#test").innerHTML=cnf;
    }
    else{
        document.querySelector("#test").innerHTML=deny;
    }
}


button2.onclick = function(){
    document.querySelector("#test").innerHTML=html;
}*/


/*let button = document.querySelector("#calc");
let a = document.querySelector("#a").value;
let b = document.querySelector("#b").value;
let c = document.querySelector("#c").value;
let x = document.querySelector("#x").value;
let y;
button.onclick = function(){
y=(a**2-b*x)/(a**2+c*x);
document.querySelector("#test").innerHTML= "y="+y ;
}
;*/

// const binnumb="11111111";
// let i = binnumb.length;
// let numb1 = 0;
// console.log(i);
// while (i!= 0){
//     numb1 += binnumb[i-1]*(2**i);
//     --i;
//     console.log(numb1);
// }
// if (binnumb[0]=="1"){numb1 +=1}
// console.log(numb1);

/*
let button = document.querySelector("#calc");
button.onclick = function(){
    let a1 = +document.querySelector("#a").value;
    let b = 1;
    if(isNaN(a1)){
        document.querySelector("#result").innerHTML = "Введіть число";
    }
    else if(a1<=0){
        document.querySelector("#result").innerHTML = "Введіть додатнє число";
    }
    else if(a1%2==0){
        for(let i = 1; i<=a1; i++){
            b*=i;
        }
        document.querySelector("#result").innerHTML = b;
    }
    else{
        b=a1**a1;
        document.querySelector("#result").innerHTML = b;
    }
}*/
