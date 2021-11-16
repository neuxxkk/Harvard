var h=document.querySelector('h1')
var i=0

function alerta(){
    if (i%10==0 && i!=0){
        h.innerText=i
        window.alert(`${i} é divisível por 10`)
    }
}

function add(){
    i++
    h.innerText=i
    alerta()
}
function remove(){
    i--
    h.innerText=i
    alerta()
}

