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
