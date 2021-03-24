let chart = document.querySelector(".chart");
let circle = document.querySelectorAll(".circle");
let extra = document.querySelector(".extra");
let part1 = document.querySelector(".part1");
let part2 = document.querySelector(".part2");

let arrPart1 = ["Lorem ipsum dolor sit.","Lorem ipsum","agyvgfueguehgoiehg","guegfueguegfguqgfu"];
let arrPart2 = [`Lorem, ipsum dolor sit amet consectetur adipisicing elit. Impedit
neque eius sed, dolor quo accusamus, ea illo iure quis iste ipsum
accusantium id consequatur nam voluptas architecto. Fuga, aliquam.
At.`, `Lorem, ipsum dolor sit amet consectetur adipisicing elit. Impedit
neque eius sed, dolor quo accusamus, ea illo iure quis iste ipsum
accusantium id consequatur nam voluptas architecto. Fuga, aliquam.
At Nishtha`,`Lorem, ipsum dolor sit amet consectetur adipisicing elit. Impedit
neque eius sed, dolor quo accusamus, ea illo iure quis iste ipsum
accusantium id consequatur nam voluptas architecto. Fuga, aliquam.
At. Archit`,`Lorem, ipsum dolor sit amet consectetur adipisicing elit. Impedit
neque eius sed, dolor quo accusamus, ea illo iure quis iste ipsum
accusantium id consequatur nam voluptas architecto. Fuga, aliquam.
At.Harshit`];

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

