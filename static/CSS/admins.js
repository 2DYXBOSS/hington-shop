


function activatione(cliqueurid,activeid,imagew) {
    et = "#" + cliqueurid + ""
    const cliquere  = document.querySelector(et)
    eteq = "#" + activeid + ""
    let sortier  = document.querySelector(eteq)
    eteqq = "#" + imagew + ""
    let imahe  = document.querySelector(eteqq)

    cliquere.addEventListener('click',()=>{
        sortier.classList.add("active");
    
        imahe.src = `/static/IMAGE/cadeouver.png`
    })

}
function effacfe(cliqueurid,activeid,imagew) {
    et = "#" + cliqueurid + ""
    const cliquere  = document.querySelector(et)
    eteq = "#" + activeid + ""
    let sortier  = document.querySelector(eteq)
    eteqq = "#" + imagew + ""
    let imahe  = document.querySelector(eteqq)

    cliquere.addEventListener('click',()=>{
        sortier.classList.remove("active");
    
        imahe.src = `/static/IMAGE/cadefer.png`
    })

}

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