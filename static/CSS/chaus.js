

const moins = document.querySelectorAll('#moins');
const numeric = document.querySelector('#numeric'); // Sélectionnez l'élément lui-même
const eeecran = document.querySelector('#eeecran'); // Sélectionnez l'élément lui-même
const plus = document.querySelectorAll('#plus');

moins.forEach(moins => {
    
moins.addEventListener('click', () => {
    numeric.value = parseInt(numeric.value) - 1; // Mettre à jour le contenu de l'élément
    eeecran.value = parseInt(eeecran.value) - 1; // Mettre à jour le contenu de l'élément
    console.log(numeric.value);
});
});
plus.forEach(plus => {
plus.addEventListener('click', () => {
    numeric.value = parseInt(numeric.value) + 1; // Mettre à jour le contenu de l'élément
    eeecran.value = parseInt(eeecran.value) + 1; // Mettre à jour le contenu de l'élément
    console.log(numeric.value);
});
});



const bouto = document.querySelector('.bouto');
const formuhfh = document.querySelector('.formuhfh');
const formuhfhe = document.querySelector('.ccrrooii');

bouto.addEventListener('click',()=>{
    formuhfh.classList.add("active");
});
formuhfhe.addEventListener('click',()=>{
    formuhfh.classList.remove("active");
})

;







const cliquer = document.querySelector('.te2')
// const cliquerw = document.querySelector('.menue')
const enleve = document.querySelector('.monfix')

// cliquerw.addEventListener('click',()=>{

//     enleve.classList.add('active');
// })
cliquer.addEventListener('click',()=>{

    enleve.classList.add('active');
    monfixder.classList.remove('active');
})


enleve.addEventListener('click',()=>{

    enleve.classList.remove('active');
})












const home = document.querySelector('#home')
const contact = document.querySelector('#contact')
const couleur = document.querySelector('.monfix')

home.addEventListener('click',()=>{

    contact.classList.remove('active');
    home.classList.add('active');
   
})
contact.addEventListener('click',()=>{

    home.classList.remove('active');
    contact.classList.add('active');
})


const cleud = document.querySelector('#cleud')
const monfixder = document.querySelector('.monfixder')

cleud.addEventListener('click',()=>{

    monfixder.classList.add('active');
})

monfixder.addEventListener('click',()=>{

    monfixder.classList.remove('active');
})




















let ecran = document.querySelector('#ecran')
let image0 = document.querySelector('#image0')
let image0Input = document.querySelector('#image0Input').value
let image1 = document.querySelector('#image1')
let image1Input = document.querySelector('#image1Input').value
let image2 = document.querySelector('#image2')
let image2Input = document.querySelector('#image2Input').value
let image3 = document.querySelector('#image3');
let image3Input = document.querySelector('#image3Input').value;


let im1 = document.querySelector('#im1')
let im2 = document.querySelector('#im2')
    

image0.addEventListener('click',()=>{
    ecran.src = `/static/uploads/${image0Input}`

    // ecran.style.background = `url(/static/uploads/${image0Input}) 50% no-repeat `
    // ecran.style.backgroundSize= "cover";
    image1.style.border = "none"
    image3.style.border = "none"
    image2.style.border = "none"
    image0.style.border = "2px solid black"

}

)
image1.addEventListener('click',()=>{
   
    ecran.src = `/static/uploads/${image1Input}`
    image2.style.border = "none"
    image3.style.border = "none"
    image0.style.border = "none"
    image1.style.border = "2px solid black"
}

)
image2.addEventListener('click',()=>{
   
    ecran.src = `/static/uploads/${image2Input}`
    image1.style.border = "none"
    image3.style.border = "none"
    image0.style.border = "none"
    image2.style.border = "2px solid black"

}

)
image3.addEventListener('click',()=>{
   
    ecran.src = `/static/uploads/${image3Input}`
    image1.style.border = "none"
    image2.style.border = "none"
    image0.style.border = "none"
    image3.style.border = "2px solid black"

}

)












let a = document.querySelectorAll('.coloope')
// let b = document.querySelector('.b')

a.forEach(a => {
    a.addEventListener('click',()=>{
        // wee.style.border = '10px solid red'
        // a.style.border = '10px solid pink';
        a.style.background = 'white'
        // wee.style.background = 'url(/menu.png) 50% no-repeat'
        // wee.backgroundSize= "cover";

    }

)
});



// let a = document.querySelectorAll('.coloope')
// // let b = document.querySelector('.b')

// a.forEach(a => {
//     a.addEventListener('click',()=>{
//         // wee.style.border = '10px solid red'
//         // a.style.border = '10px solid pink';
//         a.style.background = 'white'
//         // wee.style.background = 'url(/menu.png) 50% no-repeat'
//         // wee.backgroundSize= "cover";

//     }

// )
// });



