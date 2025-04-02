const API_URL = "http://localhost:8080/vehicle/getAllVehicles"; 

// Function to fetch vehicles from API
async function fetchVehicles() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error("Failed to fetch vehicles");
        }
        const vehicles = await response.json();
        renderVehicles(vehicles);
    } catch (error) {
        console.error("Error fetching vehicles:", error);
        document.getElementById("vehicles-grid").innerHTML = `
            <div class="loading">Failed to load vehicles. Try again later.</div>
        `;
    }
}

// Function to render vehicles on the page
function renderVehicles(vehicles) {
    const vehiclesGrid = document.getElementById("vehicles-grid");

    if (vehicles.length === 0) {
        vehiclesGrid.innerHTML = `<div class="loading">No vehicles available.</div>`;
        return;
    }

    vehiclesGrid.innerHTML = vehicles.map(vehicle => `
        <div class="vehicle-card">
            <div class="vehicle-image">
                <i class="fas fa-${vehicle.type === "CAR" ? "car" : "motorcycle"}"></i>
            </div>
            <div class="vehicle-details">
                <span class="availability ${vehicle.availability === "AVAILABLE" ? "available" : "unavailable"}">
                    ${vehicle.availability}
                </span>
                <h3 class="vehicle-name">${vehicle.name}</h3>
                <span class="vehicle-type">${vehicle.type}</span>
                <div class="vehicle-info">Model: ${vehicle.model || "N/A"}</div>
                <div class="vehicle-info">Reg: ${vehicle.registration_number}</div>
                <div class="vehicle-price">Rs. ${vehicle.price_per_day}/day</div>
                
            </div>
        </div>
    `).join("");
}

document.addEventListener("DOMContentLoaded", fetchVehicles);