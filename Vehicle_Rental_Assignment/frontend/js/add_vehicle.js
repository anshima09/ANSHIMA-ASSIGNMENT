document.getElementById("vehicleForm").addEventListener("submit", function(event) {
    event.preventDefault(); 
    
    const vehicleData = {
        name: document.getElementById("name").value,
        type: document.getElementById("type").value,
        model: document.getElementById("model").value,
        registration_number: document.getElementById("registrationNumber").value,
        availability: document.getElementById("availability").value,
        price_per_day: parseFloat(document.getElementById("price").value)
    };

    fetch("http://localhost:8080/vehicle/add/admin@example.com", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(vehicleData)
    })
    .then(response => response.text()) 
    .then(data => {
        document.getElementById("message").innerHTML = "✅ Vehicle Added Successfully!";
        document.getElementById("message").style.color = "green";
        document.getElementById("vehicleForm").reset();
    })
    .catch(error => {
        document.getElementById("message").innerHTML = "❌ Error adding vehicle!";
        document.getElementById("message").style.color = "red";
    });
});