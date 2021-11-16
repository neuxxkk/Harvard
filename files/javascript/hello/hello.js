var i=0
let aga1 = document.querySelector('h1')
let btn = document.querySelector('button')
function bye(){
    if (i==0){
        btn.innerText="Enter"
        aga1.innerHTML="Bye, world!"
        i=1
    }else{
        btn.innerText="Exit"
        aga1.innerHTML="Hello, world!"
        i=0
    }
}