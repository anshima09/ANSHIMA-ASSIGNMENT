const API_URL = "http://localhost:8080/vehicle/getAllVehicles";
let selectedVehicleRegNo = "";

// Fetch Vehicles
async function fetchVehicles() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("Failed to fetch vehicles");
        const vehicles = await response.json();
        renderVehicles(vehicles);
    } catch (error) {
        console.error("Error fetching vehicles:", error);
        document.getElementById("vehicles-grid").innerHTML = `<div class="loading">Failed to load vehicles. Try again later.</div>`;
    }
}

// Render Vehicles
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
                <div class="vehicle-price">Rs.${vehicle.price_per_day}/day</div>
                <div class="vehicle-actions">
                    <button class="book-btn" onclick="openBookingForm('${vehicle.registration_number}')">
                        Book Now
                    </button>
                </div>
            </div>
        </div>
    `).join("");
}

// Open Booking Form
function openBookingForm(registrationNo) {
    selectedVehicleRegNo = registrationNo;
    document.getElementById("vehicleRegNo").innerText = registrationNo;
    document.getElementById("bookingModal").style.display = "flex";
}

// Close Booking Form
function closeBookingForm() {
    document.getElementById("bookingModal").style.display = "none";
}

// Submit Booking
async function submitBooking() {
    const user = JSON.parse(localStorage.getItem("user"));
    if (!user || !user.email) {
        alert("Please log in to book a vehicle!");
        return;
    }

    const startDate = document.getElementById("start-date").value;
    const endDate = document.getElementById("end-date").value;

    if (!startDate || !endDate) {
        alert("Please select both start and end dates!");
        return;
    }

    const API_URL = `http://localhost:8080/booking/add?email=${encodeURIComponent(user.email)}&registration_no=${encodeURIComponent(selectedVehicleRegNo)}&startDate=${encodeURIComponent(startDate)}&endDate=${encodeURIComponent(endDate)}`;
    
    try {
        const response = await fetch(API_URL, { method: "POST" });
        if (response.ok) {
            alert("✅ Successfully Booked!");
            closeBookingForm();
            fetchVehicles(); // Reload vehicles
        } else {
            alert("❌ Booking Failed! Try Again.");
        }
    } catch (error) {
        console.error("Error booking vehicle:", error);
        alert("❌ Something went wrong!");
    }
}

// Load Vehicles
document.addEventListener("DOMContentLoaded", fetchVehicles);