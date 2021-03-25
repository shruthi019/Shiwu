let input = document.querySelector("#uploadImage");
let img = document.querySelector(".image img");

input.addEventListener("change",function(e){
    preview(e);
});

function preview(e){
    e.preventDefault();
    console.log(input.files[0]);
}