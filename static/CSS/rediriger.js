
function activesd(dedre) {
    let dataz = JSON.parse(localStorage.getItem("inscpce"));
    localStorage.removeItem("inscpce");
    fetch('/redsete', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data: dataz })
        
    })
    .then(data => {
        
        console.log('Data successfully sent to Python:', data);
        

        window.location.href = `/${dedre}`;
    })
    .catch(error => {
        console.error('Error sending data to Python:', error);
    });
}
