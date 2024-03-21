

const cliquer = document.querySelector('.te2')
// const cliquerw = document.querySelector('.menue')
const enleve = document.querySelector('.monfix')

// cliquerw.addEventListener('click',()=>{

//     enleve.classList.add('active');
// })
cliquer.addEventListener('click',()=>{

    enleve.classList.add('active');
})


enleve.addEventListener('click',()=>{

    enleve.classList.remove('active');
})





// enleve.addEventListener('click',()=>{

//     enleve.classList.remove('active');
// })


// Mon animation en bleu


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



// let sctions = document.querySelectorAll('.lesimages');

// window.onscroll = () => {
//     sctions.forEach(sec => {

//         let top = window.scrollY;
//         let offset = sec.offsetTop;
//         let height = sec.offsetHeight;

//         if (top >= offset && offset + height){
//             sec.classList.add('show-animate');
//         }
//         else {
//             sec.classList.remove('show-animate');
//         }
//     })
// }

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



const moins = document.querySelector('#moins');
const numeric = document.querySelector('#numeric'); // Sélectionnez l'élément lui-même
const plus = document.querySelector('#plus');

moins.addEventListener('click', () => {
    numeric.value = parseInt(numeric.value) - 1; // Mettre à jour le contenu de l'élément
    console.log(numeric.value);
});

plus.addEventListener('click', () => {
    numeric.value = parseInt(numeric.value) + 1; // Mettre à jour le contenu de l'élément
    console.log(numeric.value);
});

