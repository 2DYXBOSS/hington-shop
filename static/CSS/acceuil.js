
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






// function moinsp(ecranid) {
//     couterw =document.querySelector("#couterw").value
//     et = "#" + ecranid + ""
//     let ecraid  = document.querySelector(et)
//     if (ecraid.value >= 1){
//         ecraid.value = parseInt(ecraid.value) - 1; 
//         somiu = document.querySelector("#somiu")
    
//         somiu.innerHTML = parseInt(somiu.innerHTML)  - 1// Mettre à jour le contenu de l'élément
//         quantiteplos = document.querySelector("#quantiteplos")
//         quantiteplos.value = somiu.innerHTML
//         lepris = document.querySelector("#lepris")
//         lepris.innerHTML = lepris.innerHTML - parseInt(couterw)
//     }
    
//     console.log(et);
    
//     return 0
// }

// function plusp(ecranid) {
//     couterw =document.querySelector("#couterw").value
//     et = "#" + ecranid + ""
//     let ecraid  = document.querySelector(et)
//     ecraid.value = parseInt(ecraid.value) + 1; // Mettre à jour le contenu de l'élément
//     console.log(et);
//     somiu = document.querySelector("#somiu")
    
    
//     somiu.innerHTML = parseInt(somiu.innerHTML)  + 1
//     quantiteplos = document.querySelector("#quantiteplos")
//     quantiteplos.value = somiu.innerHTML
//     lepris = document.querySelector("#lepris")
//     lepris.innerHTML = somiu.innerHTML * parseInt(couterw)
//     return 0
// }






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





let sections = document.querySelectorAll('section');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop -500;
        let height = sec.offsetHeight;

        // Condition modifiée ici
        if (top >= offset && top < offset + height) {
            sec.classList.add('show-animate');
        } 
        else {
            sec.classList.remove('show-animate');
        }
    });
};




const aee = document.querySelector('#hdhdj')
const hdhdj2 = document.querySelector('#hdhdj2')
const menu = document.querySelector('.menu')
const recherche = document.querySelector('.recherche')
const imsdghde1 = document.querySelector('.imsdghde1')
const imsdghde12 = document.querySelector('.imsdghde12')

const bww = document.querySelector('.menuddg')
let dd = document.querySelector('#ecran')


aee.addEventListener('click',()=>{
    bww.classList.add('active');
    aee.classList.add('active');
    hdhdj2.classList.add('active');
   
});
hdhdj2.addEventListener('click',()=>{
    hdhdj2.classList.remove('active');
    bww.classList.remove('active');
    aee.classList.remove('active');
   
});
imsdghde1.addEventListener('click',()=>{
    recherche.classList.add('active');
    imsdghde1.classList.add('active');
    imsdghde12.classList.add('active');
    
   
});
imsdghde12.addEventListener('click',()=>{
    recherche.classList.remove('active');
    imsdghde1.classList.remove('active');
    imsdghde12.classList.remove('active');
    
   
});