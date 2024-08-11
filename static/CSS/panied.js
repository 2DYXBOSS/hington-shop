




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
function moinsp(ecranid,prix) {
    couterw =document.querySelector("#couterw").value
    et = "#" + ecranid + ""
    let ecraid  = document.querySelector(et)
    if (ecraid.value >= 2){
        ecraid.value = parseInt(ecraid.value) - 1; 
        somiu = document.querySelector("#somiu")
    
        somiu.innerHTML = parseInt(somiu.innerHTML)  - prix// Mettre à jour le contenu de l'élément
        quantiteplos = document.querySelector("#quantiteplos")
        quantiteplos.value = somiu.innerHTML
        lepris = document.querySelector("#lepris")
        lepris.innerHTML = lepris.innerHTML - parseInt(couterw)
    }
    
    console.log(et);
    
    return 0
}

function plusp(ecranid,prix) {
    
  

    couterw =document.querySelector("#couterw").value
    et = "#" + ecranid + ""
    let ecraid  = document.querySelector(et)
    ecraid.value = parseInt(ecraid.value) + 1; // Mettre à jour le contenu de l'élément
    console.log(et);
    somiu = document.querySelector("#somiu")
    somiu.innerHTML = parseInt(somiu.innerHTML) + parseInt(prix)
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



let tabUsere = JSON.parse(localStorage.getItem("inscpce"))


let reczz = document.querySelector(".imahdjd2");
let rec = document.querySelector(".meselele");
let darsghd = document.querySelector(".darsghd");
let darsghdzs = document.querySelector("#darsghdzs");
let caeekr = 0
let taer = 0
tabUsere.forEach((i) => {
    let user = i["data"]
    taer+=1
    console.log(user);
    console.log(user.image);
    console.log(user.porceprix);

    rettr =  `<div class="lesvrai">
                <div class="geujdjd">
                    <div class="imahdjd1">
                        <a href="/montres/${user.produite}">
                        <img src="static/uploads/${user.image}"  width="100%" height="90%" alt="" >
                        </a>
                    </div>
                    <div class="imahdjd2">
                        
                    </div>
                    <div class="imahdjd3">
                        
                        <p style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;padding-top: 5px;color: black;" id="sadtdyayuda" >${user.porceprix} FCFA</p>
                        <p style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;font-size: 0.7rem;padding-top: 5px;color: rgb(53, 53, 53);"><s>${user.prixtottal} FCFA</s></p>
                        <div class="uufw" style="background-color: rgba(170, 170, 170, 0.289);width: 50px;border-radius: 5px;margin-top: 10px;">
                            <p style="color: rgba(255, 102, 0, 0.865);font-size: 0.7rem;padding-left: 5px;padding-right: 5px;padding-top: 5px;padding-bottom: 5px;">- ${user.porce} %</p>
                        </div>
                        
                    </div>
                </div>
                <div class="duudcddc">
                    <div class="jujdcuudwucd">
                        <img src="static/IMAGE/pouebd.png"  width="15px" style="filter: invert(38%) sepia(73%) saturate(4864%) hue-rotate(1deg) brightness(102%) contrast(105%);" height="15px" alt="" >
                        <form >
                            
                            <button classe="sereghfjf" onclick="zqszds(${user.produite})" type="submit" style="background-color: transparent;border:none ;font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;font-size: 0.7rem;padding-top: 5px;color: rgba(255, 102, 0, 0.865);">SUPPRIMER</button>
                        </form>
                    </div>
                    <div class="jujdcuudwucd1">
                        
                        <div class="ududdw2" onclick="moinsp('mnumq')">
                            <p style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;font-size: 1.2rem;color: white;">-</p>
                        </div>
                        <div class="ududdw1">
                            <input type="text" name="" id="mnumq"   style="width: 100%;height: 100%;padding-left: 10px;border: none;outline: none;" value="${user.quantiteto
                            }">
                        </div>
                        <div class="ududdw" onclick="plusp('mnumq')">
                            <p style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;font-size: 1.2rem;color: white;">+</p>
                        </div>
                    </div>
                </div>
            </div> `

    rec.innerHTML += rettr


    console.log(rec);


    caeekr += parseInt(user.porceprix)*parseInt(user.quantiteto)                      
    darsghd.innerHTML = taer
    darsghdzs.innerHTML = caeekr


    

});



let sereghfjf = document.querySelectorAll(".sereghfjf")

sereghfjf.forEach(user => {
    user.addEventListener('click',()=>{
        let sereghfjfzd = document.querySelector(".sereghfjfzd").value
        console.log("cdbvvdhgshsdgh",sereghfjfzd)

    }

    )
});



function zqszds(sereghfjfzd) {
    let eyyr = []
    let tabUsere = JSON.parse(localStorage.getItem("inscpce"))
    
    console.log();

    tabUsere.forEach(element => {
        let user = element["data"]
        console.log(user["produite"]);
        if (parseInt(user["produite"]) !== parseInt(sereghfjfzd)){
                let usere = {
                    data : user ,
                }
                eyyr.push(usere)
            }
        // user.forEach(er => {
        //     if (parseInt(er["produite"]) == parseInt(sereghfjfzd)){
        //         console.log("trouver",er);
        //     }
        // });
        
        // console.log(element);
        // let data = {"image":image,"tailed" : "","produite":noumeme,"categorie":categorie,"porce":porce,"porceprix":porceprix,"prixtottal":prix,"quantiteto":quantite,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}  
        // let usere = {
        //     data : data ,
        // }
    
        // tabUsere.push(usere)
        // localStorage.setItem('inscpce',JSON.stringify(tabUsere))
        
    });
    
    console.log("restant",eyyr);
    localStorage.removeItem("inscpce");
    tabUsere = JSON.parse(localStorage.getItem("inscpce")) || []
    tabUsere = eyyr
    localStorage.setItem('inscpce',JSON.stringify(tabUsere))


    // let usere = {
    //     data : data ,
    // }
    
    // tabUsere.push(usere)
    // localStorage.setItem('inscpce',JSON.stringify(tabUsere))
}



// [
//     "[{'id': 1, 'element': '3', 'prix': '4850', 'image': 'mon1.jpeg', 'quantite': '3', 'taille': '', 'nom': 'montre homme', 'description': \"Sur notre site web, vous trouverez une variété d'articles informatifs, captivants et pertinents qui couvrent un large éventail de sujets passionnants. Que vous soyez intéressé par la technologie, la santé, le bien-être, les voyages, la cuisine ou tout autre domaine, nous avons quelque chose pour vous. Nos articles sont rédigés par des experts dans leur domaine, garantissant ainsi des contenus de haute qualité et fiables. Que vous cherchiez des conseils pratiques, des analyses approfondies ou des informations de pointe, vous trouverez tout cela dans nos articles. Explorez notre site web dès maintenant pour découvrir des articles qui vous informeront, vous divertiront et vous inspireront.\", 'pource': '3443', 'porce': '29', 'tailed': '', 'categorie': 'Montre'",
//     ", {'id': 2, 'element': '4', 'prix': '8500', 'image': 'H9e45d4f41c6e4625becc80fa829d18bd1.jpg', 'quantite': '3', 'taille': '', 'nom': 'montre homme', 'description': \"Sur notre site web, vous trouverez une variété d'articles informatifs, captivants et pertinents qui couvrent un large éventail de sujets passionnants. Que vous soyez intéressé par la technologie, la santé, le bien-être, les voyages, la cuisine ou tout autre domaine, nous avons quelque chose pour vous. Nos articles sont rédigés par des experts dans leur domaine, garantissant ainsi des contenus de haute qualité et fiables. Que vous cherchiez des conseils pratiques, des analyses approfondies ou des informations de pointe, vous trouverez tout cela dans nos articles. Explorez notre site web dès maintenant pour découvrir des articles qui vous informeront, vous divertiront et vous inspireront.\", 'pource': '7820', 'porce': '8', 'tailed': '', 'categorie': 'Montre'",
//     ", {'id': 3, 'element': '5', 'prix': '7300', 'image': 'Hbbd6a9e74c1944eca2097a91fbdd3c8f8.jpg', 'quantite': '2', 'taille': '', 'nom': 'montre homme cuir', 'description': \"Sur notre site web, vous trouverez une variété d'articles informatifs, captivants et pertinents qui couvrent un large éventail de sujets passionnants. Que vous soyez intéressé par la technologie, la santé, le bien-être, les voyages, la cuisine ou tout autre domaine, nous avons quelque chose pour vous. Nos articles sont rédigés par des experts dans leur domaine, garantissant ainsi des contenus de haute qualité et fiables. Que vous cherchiez des conseils pratiques, des analyses approfondies ou des informations de pointe, vous trouverez tout cela dans nos articles. Explorez notre site web dès maintenant pour découvrir des articles qui vous informeront, vous divertiront et vous inspireront.\", 'pource': '5548', 'porce': '24', 'tailed': '', 'categorie': 'Montre'",
//     ", {'id': 4, 'element': '4', 'prix': '8500', 'image': 'H9e45d4f41c6e4625becc80fa829d18bd1.jpg', 'quantite': '3', 'taille': '', 'nom': 'montre homme', 'description': \"Sur notre site web, vous trouverez une variété d'articles informatifs, captivants et pertinents qui couvrent un large éventail de sujets passionnants. Que vous soyez intéressé par la technologie, la santé, le bien-être, les voyages, la cuisine ou tout autre domaine, nous avons quelque chose pour vous. Nos articles sont rédigés par des experts dans leur domaine, garantissant ainsi des contenus de haute qualité et fiables. Que vous cherchiez des conseils pratiques, des analyses approfondies ou des informations de pointe, vous trouverez tout cela dans nos articles. Explorez notre site web dès maintenant pour découvrir des articles qui vous informeront, vous divertiront et vous inspireront.\", 'pource': '7820', 'porce': '8', 'tailed': '', 'categorie': 'Montre'",
//     "]"
// ]