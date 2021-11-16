btns=document.querySelector('#btns')
color=document.querySelector("#color")
h1=document.querySelector('h1')
div_done=document.querySelector('#done')
div_h1=document.querySelector('#h1')
red=0
green=0
blue=0
i=0
rgb=`rgb(${red},${green},${blue})`
function change(){
    rgb=`rgb(${red},${green},${blue})`
    if(red+green+blue<=450 && green<=200){
        color.style.color='bisque'
    }else{color.style.color='black'}
    h1.style.color=`rgb(${blue},${red},${green})`
    color.style.backgroundColor=rgb   
    color.innerHTML=rgb
}
function control(){
    i++
    if(red>255){red=255}
    if(red<0){red=0}
    if(green>255){green=255}
    if(green<0){green=0}
    if(blue>255){blue=255}
    if(blue<0){blue=0}
    rgb=`rgb(${red},${green},${blue})`
    console.log(rgb)
}

document.querySelector('#btn_red_add').onclick=function(){red+=25.5,control(),change()}
document.querySelector('#btn_green_add').onclick=function(){green+=25.5,control(),change()}
document.querySelector('#btn_blue_add').onclick=function(){blue+=25.5,control(),change()}

document.querySelector('#btn_red_rm').onclick=function(){red-=25.5,control(),change()}
document.querySelector('#btn_green_rm').onclick=function(){green-=25.5,control(),change()}
document.querySelector('#btn_blue_rm').onclick=function(){blue-=25.5,control(),change()}

change()

function clear(n){
    console.log(n)
    if(red==0&&green==0&&blue==0){
        h1.style.color='bisque'
    }
    n.style.display='none'
    div_h1.style.lineHeight='650px'
    document.body.style.backgroundColor=rgb
}

document.querySelector('#done_btn').onclick=function(){
    clear(btns),clear(color),clear(div_done)
}
