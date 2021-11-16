var nome=document.querySelector('#name')
var email=document.querySelector('#email')
var cpf=document.querySelector('#cpf')
var sub=document.querySelector('input.sub').value='Send'
var name_check
var email_check
var cpf_check
var check=0
var i=0

function done(){
    nome.style.borderColor='rgb(200, 200, 200)'
    nome.style.borderTopColor='rgb(83, 255, 112)'
    nome.style.borderRightColor='rgb(83, 255, 112)'

    cpf.style.borderColor='rgb(200, 200, 200)'
    cpf.style.borderTopColor='rgb(83, 255, 112)'
    cpf.style.borderRightColor='rgb(83, 255, 112)'

    email.style.borderColor='rgb(200, 200, 200)'
    email.style.borderTopColor='rgb(83, 255, 112)'
    email.style.borderRightColor='rgb(83, 255, 112)'

    document.querySelector('input.sub').value='Done!'
}

function cheq(){
    if(i>1){
        alert('Preencha os campos vazios!')
        i=0
    }
    check=0
    if (nome.value!=''){
        name_check=true
        check++
   }else{
    nome.style.borderColor='rgb(200, 200, 200)'
    nome.style.borderTopColor='rgb(255, 149, 149)'
    nome.style.borderRightColor='rgb(255, 149, 149)'
    }
    if (cpf.value!=''){
        cpf_check=true
        check++
    }else{
        cpf.style.borderColor='rgb(200, 200, 200)'
        cpf.style.borderTopColor='rgb(255, 149, 149)'
        cpf.style.borderRightColor='rgb(255, 149, 149)'
    }
    if (email.value!=''){
        email_check=true
        check++
    }else{
        email.style.borderColor='rgb(200, 200, 200)'
        email.style.borderTopColor='rgb(255, 149, 149)'
        email.style.borderRightColor='rgb(255, 149, 149)'
    }
}

function clean(){
    nome.value=''
    cpf.value=''
    email.value=''
}

function cliq(){
    cheq()
    if(check==3){
        i=0
        console.log(`Name: ${nome.value}`)
        console.log(`CPF: ${cpf.value}`)
        console.log(`email: ${email.value}`)
        clean()
        done()
    }else{
        i++
        console.log(check)
    }
}

document.addEventListener('DOMContentLoaded',function(){
    console.log('start')
})


var p=0
cpf.onkeydown= (m)=>{
    if(cpf.value[0]==undefined){p=5}
    if(cpf.value[2]!=undefined && cpf.value[4]==undefined &&cpf.value[3]==undefined&&p==5){
        console.log(p)
        document.body.style.background='purple'
        cpf.value=`${cpf.value}.`
        p+=5
    }
    console.log(p)

    if(cpf.value[6]!=undefined && cpf.value[8]==undefined&&cpf.value[7]==undefined&&p==10){
        console.log(p)
        document.body.style.background='yellow'
        cpf.value=`${cpf.value}.`
        p+=5
    }
    if(m==5){
        p=15
    }

    if(cpf.value[10]!=undefined && cpf.value[12]==undefined&&cpf.value[11]==undefined&&p==15){
        console.log(p)
        document.body.style.background='orange'
        cpf.value=`${cpf.value}-`
        p-=10
        m=5
    }
}