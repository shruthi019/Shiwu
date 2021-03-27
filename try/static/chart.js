let chart = document.querySelector(".chart");
let circle = document.querySelectorAll(".circle");
let extra = document.querySelector(".extra");
let part1 = document.querySelector(".part1");
let part2 = document.querySelector(".part2");
// let popup = document.querySelector(".popup");
// let popSignIn = document.querySelector(".pop-signin");
// let popSignUp = document.querySelector(".pop-signup");
// let inputSignIn = document.querySelector(".input-signin");
// let inputSignUp = document.querySelector(".input-signup");
// let login = document.querySelector(".login");
// let signup = document.querySelector(".signup");
// let cross = document.querySelector(".cross");

let arrPart1 = ["Step:","Step:","Step:","Step:"];
let arrPart2 = [`Our first layer is sequential as there's only a single input. Since it is a picture we need to flatten the RGB content.`,
 `We have then used batch normalisation layer to normalise the mean output and standard deviation.`,
`Then we have densely connected 4 layers. Again, to normalise the output we have used batch normalisation and we have used the activation function 'softmax'.`,
`We have compiled the whole model using optimiser 'Adam' , handled losses using 'categoricalCrossentropy' and using metrics 'accuracy'. We have set up 50 epochs for better accuracy.`];

for(let i=0;i<4;i++){
    circle[i].addEventListener("click",function(){
        change(i);
    });
}

function change(i){
    part1.innerHTML = arrPart1[i];
    part2.innerHTML = arrPart2[i];
    for(let j=0;j<4;j++){
        if(i!=j){
            circle[j].style.borderWidth = "3px";
        }
    }
    circle[i].style.borderWidth = "thick";
}

// login.addEventListener("click",openPopupLogin);
// signup.addEventListener("click",openPopupSignup);
// popSignIn.addEventListener("click",signinDiv);
// popSignUp.addEventListener("click",signupDiv);

// function openPopupLogin(){
//     signinDiv();
//     popup.style.display = "flex";
// }

// function openPopupSignup(){
//     signupDiv();
//     popup.style.display ="flex";
// }

// function signinDiv(){
//     inputSignIn.style.display = "flex";
//     inputSignUp.style.display = "none";
//     popSignIn.style.color = "gray";
//     popSignIn.style.backgroundColor = "#d2d8d8";
//     popSignUp.style.backgroundColor = "white";
// }
// function signupDiv(){
//     inputSignUp.style.display = "flex";
//     inputSignIn.style.display = "none";
//     popSignUp.style.color = "gray";
//     popSignUp.style.backgroundColor = "#d2d8d8";
//     popSignIn.style.backgroundColor = "white";
// }

// cross.addEventListener("click",crossController);

// function crossController(){
//     popup.style.display = "none";
// }