



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




const boutonshd = document.querySelector("#boutonshd")
boutonshd.addEventListener('click',()=>{
    
    // let tabUsere = JSON.parse(localStorage.getItem("inscpce")) || []
    // let image = document.querySelector(".image").value
    // let noumeme = document.querySelector(".noumeme").value
    // let prix = document.querySelector(".prix").value
    // let quantite = document.querySelector("#quantiteplos").value
    // let categorie = document.querySelector("#categorie").value
    // let data = {"image":image,"tailed" : "","produite":noumeme,"prixtottal":prix,"quantiteto":quantite,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
    let tabUsere = JSON.parse(localStorage.getItem("inscpce")) || []
    let image = document.querySelector(".image").value
    let noumeme = document.querySelector(".noumeme").value
    let prix = document.querySelector(".prix").value
    let quantite = document.querySelector("#quantiteplos").value
    let porce = document.querySelector(".porce").value
    let porceprix = document.querySelector(".porceprix").value
    let categorie = document.querySelector(".categorie").value

    let data = {"image":image,"tailed" : "","produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":quantite,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
    let usere = {
        data : data ,
    }
    
    tabUsere.push(usere)
    localStorage.setItem('inscpce',JSON.stringify(tabUsere))
    console.log('Data successfully sent to Python:', data);
    window.location.href = "http://127.0.0.1:5005/monpanierls"
})
// boutonshd.addEventListener('click',()=>{
//     let tabUsere = JSON.parse(localStorage.getItem("inscpce")) || []
//     // let nameid = document.querySelector("#nome").value;
    
    
    

//     // let dataz = JSON.parse(localStorage.getItem("inscpce"))
//     fetch('/ssme', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         // body: JSON.stringify({ data: dataz })
        
//     })
//     .then(response => response.json())
//     .then(data => {
//         let usere = {
//             data:data,
//         }
    
//         tabUsere.push(usere)
//         localStorage.setItem('inscpce',JSON.stringify(tabUsere))
//         console.log('Data successfully sent to Python:', data);
//         window.location.href = "/monpanierls"
        
//     })
//     .catch(error => {
//         console.error('Error sending data to Python:', error);
//     });

// })


// const bouto = document.querySelector('.bouto');
// const formuhfh = document.querySelector('.formuhfh');
// const formuhfhe = document.querySelector('.ccrrooii');

// bouto.addEventListener('click',()=>{
//     formuhfh.classList.add("active");
// });
// formuhfhe.addEventListener('click',()=>{
//     formuhfh.classList.remove("active");
// })

// ;




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





















let a = document.querySelectorAll('.coloope')
// let b = document.querySelector('.b')

a.forEach(a => {
    a.addEventListener('click',()=>{
        // wee.style.border = '10px solid red'
        // a.style.border = '10px solid pink';
        a.style.background = 'white';
        // wee.style.background = 'url(/menu.png) 50% no-repeat'
        // wee.backgroundSize= "cover";
        
    }

)
});



// const xl = document.querySelector('#xlp');

// const xlnum = document.querySelector('#xlnum');

// xl.addEventListener('click',()=>{
   
//     xl.style.background = 'yellow';
// })
// ;

// console.log("dedy")


let xl = document.querySelector('#xlp')
let xs = document.querySelector('#xsp')
let xxl = document.querySelector('#xxlp')
let l = document.querySelector('#lp')
let m = document.querySelector('#mp')
let s = document.querySelector('#sp')

let xsnum = document.querySelector('#xsnum')
let xlnum = document.querySelector('#xlnum')
let lnum = document.querySelector('#lnum')
let snum = document.querySelector('#snum')
let mnum = document.querySelector('#mnum')
let xxlnum = document.querySelector('#xxlnum')

// let b = document.querySelector('.b')


xl.addEventListener('click',()=>{
   
    // wee.style.border = '10px solid red'
    // a.style.border = '10px solid pink';
    xl.style.background = 'green';
    // wee.style.background = 'url(/menu.png) 50% no-repeat'
    // wee.backgroundSize= "cover";
    
    xlnum.classList.add("active")
    xlnum.value = 0
})


l.addEventListener('click',()=>{
    // wee.style.border = '10px solid red'
    // a.style.border = '10px solid pink';
    l.style.background = 'green';
    // wee.style.background = 'url(/menu.png) 50% no-repeat'
    // wee.backgroundSize= "cover";
    
    lnum.classList.add("active")
    lnum.value = 0
}

)
s.addEventListener('click',()=>{
    // wee.style.border = '10px solid red'
    // a.style.border = '10px solid pink';
    s.style.background = 'green';
    // wee.style.background = 'url(/menu.png) 50% no-repeat'
    // wee.backgroundSize= "cover";
    
    snum.classList.add("active")
    snum.value = 0
}

)
m.addEventListener('click',()=>{
    // wee.style.border = '10px solid red'
    // a.style.border = '10px solid pink';
    m.style.background = 'green';
    // wee.style.background = 'url(/menu.png) 50% no-repeat'
    // wee.backgroundSize= "cover";
    
    mnum.classList.add("active")
    mnum.value = 0
}

)
xxl.addEventListener('click',()=>{
    // wee.style.border = '10px solid red'
    // a.style.border = '10px solid pink';
    xxl.style.background = 'green';
    // wee.style.background = 'url(/menu.png) 50% no-repeat'
    // wee.backgroundSize= "cover";
    
    xxlnum.classList.add("active")
    xxlnum.value = 0
}

)
xs.addEventListener('click',()=>{
    
    // wee.style.border = '10px solid red'
    // a.style.border = '10px solid pink';
    xs.style.background = 'green';
    // wee.style.background = 'url(/menu.png) 50% no-repeat'
    // wee.backgroundSize= "cover";
    
    xsnum.classList.add("active")
    xsnum.value = 0
}

)




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



// const moins = document.querySelectorAll('#moins');
// const numeric = document.querySelector('#numeric'); // Sélectionnez l'élément lui-même
// const eeecran = document.querySelector('#eeecran'); // Sélectionnez l'élément lui-même
// const plus = document.querySelectorAll('#plus');

// moins.forEach(moins => {
    
// moins.addEventListener('click', () => {
//     numeric.value = parseInt(numeric.value) - 1; // Mettre à jour le contenu de l'élément
//     eeecran.value = parseInt(eeecran.value) - 1; // Mettre à jour le contenu de l'élément
//     console.log(numeric.value);
// });
// });
// plus.forEach(plus => {
// plus.addEventListener('click', () => {
//     numeric.value = parseInt(numeric.value) + 1; // Mettre à jour le contenu de l'élément
//     eeecran.value = parseInt(eeecran.value) + 1; // Mettre à jour le contenu de l'élément
//     console.log(numeric.value);
// });
// });

// function dedy() {
//     let tabUsere = JSON.parse(localStorage.getItem("inscpce")) || []
//     // let nameid = document.querySelector("#nome").value;
    
    
    

//     // let dataz = JSON.parse(localStorage.getItem("inscpce"))
//     fetch('/ssme', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         // body: JSON.stringify({ data: dataz })
        
//     })
//     .then(response => response.json())
//     .then(data => {
//         let usere = {
//             data:data,
//         }
    
//         tabUsere.push(usere)
//         localStorage.setItem('inscpce',JSON.stringify(tabUsere))
//         console.log('Data successfully sent to Python:', data);
//         window.location.href = "/monpanierls"
        
//     })
//     .catch(error => {
//         console.error('Error sending data to Python:', error);
//     });

// }
// function dedy() {
    

//     function updateTime() {
//         let now = new Date();
//         let hours = now.getHours();
//         let minutes = now.getMinutes();
//         let seconds = now.getSeconds();
//         console.log(seconds,"nom");
//     }

   
//     window.onload = function() {
//         updateTime();
//         let intervalId = setInterval(updateTime, 1000);

       
//         setTimeout(function() {
//             clearInterval(intervalId);
//             let now = new Date();
            
//             let seconds = now.getSeconds();
//             console.log(seconds,"pres")
//             let tabUsere = JSON.parse(localStorage.getItem("inscpce")) || []
//             // let nameid = document.querySelector("#nome").value;
            
            
            

//             // let dataz = JSON.parse(localStorage.getItem("inscpce"))
//             fetch('/ssme', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json'
//                 },
//                 // body: JSON.stringify({ data: dataz })
                
//             })
//             .then(response => response.json())
//             .then(data => {
//                 let usere = {
//                     data:data,
//                 }
            
//                 tabUsere.push(usere)
//                 localStorage.setItem('inscpce',JSON.stringify(tabUsere))
//                 console.log('Data successfully sent to Python:', data);
//                 window.location.href = "/monpanierls"
                
//             })
//             .catch(error => {
//                 console.error('Error sending data to Python:', error);
//             });
//         }, 0); // 5000 millisecondes = 10 secondes

        
//     };
        
            
        
    
    
// }
// let boutonid = document.querySelector("#bouste");
// boutonid.addEventListener("click",(event)=>{
//     event.preventDefault()
    
   
//     fetch('http://127.0.0.1:5005/song', {
//         method: 'GET',
//         headers: {
//             'Content-Type': 'application/json'
//         },
        
//     })
//     .then(response => response.json())
//     .then(data => {
//         let tabUsere = JSON.parse(localStorage.getItem("inscpce")) || []
//         let nom =data["prenom"];
//         let prenom =data["prenom"];
    
//         let usere = {
//             nom,
//             prenom,
//         }
//         tabUsere.push(usere)

//         localStorage.setItem('inscpce',JSON.stringify(tabUsere))
//         console.log('Data successfully sent to Python:', data);
//     })
//     .catch(error => {
//         console.error('Error sending data to Python:', error);
//     });
// }) 




function zoommer() {
    
}