// let labele = document.querySelector('.g')

// labele.addEventListener('mouseleave',()=>{
//     // wee.style.border = '10px solid red'
//     // a.style.border = '10px solid pink';
//     labele.style.background = 'white'
//     // wee.style.background = 'url(/menu.png) 50% no-repeat'
//     // wee.backgroundSize= "cover";

// }

// )

// let wee = document.querySelector('.ecran')
let a = document.querySelectorAll('.imagee1lo')
let ldppd = document.querySelectorAll('.imagee1lo img')
// let b = document.querySelector('.b')

a.forEach(a => {
    a.addEventListener('click',()=>{
        // wee.style.border = '10px solid red'
        // a.style.border = '10px solid pink';
        a.style.background = 'green'
        a.style.height = '50px'
        a.style.paddingLeft = '10px'
        a.style.paddingRight = '10px'
        a.style.paddingTop = '10px'
        ldppd.src = "static/IMAGE/telfg.png"
        // a.style.display = 'flex'
        // a.style.alignItem = 'center'
        // a.style.justifyContent = 'center'

        // wee.style.background = 'url(/menu.png) 50% no-repeat'
        // wee.backgroundSize= "cover";

    }

)
});