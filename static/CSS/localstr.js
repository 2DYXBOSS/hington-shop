

// # FIN CONNEXION {}

// AJOUTER AU PANIER LOCALSTORAGE 

// let boutonid = document.querySelector("#bouste");
// boutonid.addEventListener("click",(event)=>{
//     event.preventDefault()
//     let tabUserer = JSON.parse(localStorage.getItem("poster")) || []
//     let nome = document.querySelector("#nome").value;
    
//     let usere = {
//         nome : nome,
        
//     }
//     tabUserer.push(usere)
//     localStorage.setItem('poster',JSON.stringify(tabUserer))
    
//     window.location.href = "/monpanierls"
// })  




// fetch('http://localhost:8000/receive_data', {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({ data: dataFromLocalStorage })
// })
// .then(response => response.json())
// .then(data => {
//     console.log('Data successfully sent to Python:', data);
// })
// .catch(error => {
//     console.error('Error sending data to Python:', error);
// });


// Supposons que dataFromLocalStorage contient les données que vous avez récupérées depuis localStorage

// Définir l'URL du serveur Python où vous souhaitez envoyer les données
// const pythonServerUrl = 'http://localhost:8000/receive_data';

// // Préparer les données à envoyer sous forme d'objet JSON
// const jsonData = { data: dataFromLocalStorage };

// // Envoyer les données au serveur Python via une requête POST
// fetch(pythonServerUrl, {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/json'
//     },
//     body: JSON.stringify(jsonData)
// })
// .then(response => {
//     if (!response.ok) {
//         throw new Error('Network response was not ok');
//     }
//     return response.json();
// })
// .then(data => {
//     console.log('Response from Python server:', data);
// })
// .catch(error => {
//     console.error('Error sending data to Python server:', error);
// });
