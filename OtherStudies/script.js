let button = document.querySelector("#calc");
console.log(button);

button.onclick = function(){
    let a = document.querySelector("#a").value;
    let b = document.querySelector("#b").value;
    let c = document.querySelector("#c").value;
}
    if(b>0){
        if (c>0){
            document.querySelector("#expresion").innerHTML = a+"x^2+"+b+"x+"+c+"=0";}
        else if(c<0){
            document.querySelector("#expresion").innerHTML = a+"x^2+"+b+"x"+c+"=0";}
        }
        else{document.querySelector("#expresion").innerHTML = a+"x^2"+b+"x+=0";}
    }
    else if(b<0){
        if (c>0){
            document.querySelector("#expresion").innerHTML = a+"x^2"+b+"x+"+c+"=0";}
        else if(c<0){
            document.querySelector("#expresion").innerHTML = a+"x^2"+b+"x"+c+"=0";}
        }
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

};