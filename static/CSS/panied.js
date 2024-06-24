
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
// hdhdj2.addEventListener('click',()=>{
//     hdhdj2.classList.remove('active');
//     bww.classList.remove('active');
//     aee.classList.remove('active');
   
// });

// let dd = document.querySelector('#ecran');


// const cleud = document.querySelector('#hdhdj')
// const monfixder = document.querySelector('.menuddg')

// cleud.addEventListener('click',()=>{

//     monfixder.classList.add('active');
// })
let mnum = document.querySelector('#mnum')
function moinsp(ecranid) {
    couterw =document.querySelector("#couterw").value
    et = "#" + ecranid + ""
    let ecraid  = document.querySelector(et)
    if (ecraid.value >= 1){
        ecraid.value = parseInt(ecraid.value) - 1; 
        somiu = document.querySelector("#somiu")
    
        somiu.innerHTML = parseInt(somiu.innerHTML)  - 1// Mettre à jour le contenu de l'élément
        quantiteplos = document.querySelector("#quantiteplos")
        quantiteplos.value = somiu.innerHTML
        lepris = document.querySelector("#lepris")
        lepris.innerHTML = lepris.innerHTML - parseInt(couterw)
    }
    
    console.log(et);
    
    return 0
}

function plusp(ecranid) {
    couterw =document.querySelector("#couterw").value
    et = "#" + ecranid + ""
    let ecraid  = document.querySelector(et)
    ecraid.value = parseInt(ecraid.value) + 1; // Mettre à jour le contenu de l'élément
    console.log(et);
    somiu = document.querySelector("#somiu")
    
    
    somiu.innerHTML = parseInt(somiu.innerHTML)  + 1
    quantiteplos = document.querySelector("#quantiteplos")
    quantiteplos.value = somiu.innerHTML
    lepris = document.querySelector("#lepris")
    lepris.innerHTML = somiu.innerHTML * parseInt(couterw)
    return 0
}


function verif(ide,quantep) {
    et = "#" + quantep + ""
    let ecraid  = document.querySelector(et)
    let a = ecraid.innerHTML
    if ( parseInt(a) > 0){
        let lien ="'" + `https://hington-shop.onrender.com/ssm/${ide}` + "'"
        console.log(lien);
        console.log(window.location);
        // window.location.remove = lien
        return window.location = '/ssm/1'
    }
    if (parseInt(a) < 1){
        console.log("000");
        console.log(window.location);
        return 0
    }
        
}
