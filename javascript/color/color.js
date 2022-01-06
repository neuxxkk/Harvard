h1=document.querySelector('h1')

document.querySelectorAll('button').forEach( //Para cada botão da NodeList crie uma função com o param do path deste botão, ao clicar execute 
    btn=>{ //Grande sadaca: o paramentro da primeira função ser o 'document.querySelectorAll('button')[i]'(a var muda de btn para btn)
        btn.onclick= ()=>{ //function(n){} == n=>{}
            console.log(btn.id)
            h1.style.color=btn.dataset.color //Está referindo a 'data-color="rgb"' but Could be 'btn.id'
        }
}
)


document.querySelector('select').onchange=function(){//         ^^
    console.log(this.value) //'this'== selected option == 'btn' ||
    h1.style.color=this.value
}




// btn=document.querySelectorAll('button').forEach
// btn[0].onclick=function(){h1.style.color='red'}
// btn[1].onclick=function(){h1.style.color='green'}
// btn[2].onclick=function(){h1.style.color='blue'}


// function b(n){
//     document.querySelector(`#${n}`).onclick=function(){
//         console.log(n)
//         h1.style.color=n
//     }
// }
// b('red')
// b('green')
// b('blue')
