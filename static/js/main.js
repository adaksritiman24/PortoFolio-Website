console.log("main.js");
document.getElementById('body').onscroll = function myFunc(){
    let pos = -1* parseInt(document.documentElement.scrollTop)*1.5 + "px";
    document.getElementById('bg-banner').style.backgroundPositionY = pos;
    if(document.documentElement.scrollTop > 600){
        document.getElementById('navbar-id').style.backgroundColor = "rgba(20, 20, 20,0.9)"
    }else{
        document.getElementById('navbar-id').style.backgroundColor = "rgba(20, 20, 20,0.4)"
    }
}

const sendToPage = (page)=>{
    let a = document.createElement('a');
    a.href = "https://"+page;
    a.target = "_blank";
    a.click();
}

var selector = document.getElementById("selector");

const moveSelector=(type)=>{
    if(type === "about"){
        selector.style.transform = "translateX(6px)";
    }
    if(type === "home"){
        selector.style.transform = "translateX(-61px)";
    }
    if(type === "contact"){
        selector.style.transform = "translateX(68px)";
    }
}

//run logo

const turnLogo = ()=>{
    var yRot = 0;
    var speed = 90;
    cube = document.getElementById("cube");
    setInterval(()=>{
        yRot +=speed;
        cube.style.transform = `rotateY(${yRot}deg)`;
    }, 3000);
}

turnLogo();
