const inpsub=document.querySelector('#subm')
const h1=document.querySelector('h1')
const inptxt=document.querySelector('#text')
const form=document.querySelector('form')

function format(){
    inptxt.style.display='none'
    inpsub.style.display='none'
    h1.style.textAlign='center'
    h1.style.fontFamily='candara'
    h1.style.lineHeight='540px'
}

function send(){
    h1.innerHTML=inptxt.value
    format()
}
