const API_URL = "http://localhost:8080/vehicle/getAllVehicles";
let selectedVehicleRegNo = "";
let allVehicles = []; // Store all vehicles for filtering
let currentBookingId = null;

// Fetch Vehicles
async function fetchVehicles() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("Failed to fetch vehicles");
        allVehicles = await response.json(); // Store all vehicles
        renderVehicles(allVehicles, "all"); // Initially show all vehicles
    } catch (error) {
        console.error("Error fetching vehicles:", error);
        document.getElementById("vehicles-grid").innerHTML = `<div class="loading">Failed to load vehicles. Try again later.</div>`;
    }
}

// Render Vehicles
function renderVehicles(vehicles, category) {
    const vehiclesGrid = document.getElementById("vehicles-grid");

    // Filter vehicles based on the selected category
    const filteredVehicles = category === "all"
        ? vehicles
        : vehicles.filter(vehicle => vehicle.type.toLowerCase() === category);

    if (filteredVehicles.length === 0) {
        vehiclesGrid.innerHTML = `<div class="loading">No vehicles available in this category.</div>`;
        return;
    }

    vehiclesGrid.innerHTML = filteredVehicles.map(vehicle => `
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

// Filter Vehicles by Category
function filterVehicles(category) {
    // Update active tab
    document.querySelectorAll(".tab-btn").forEach(btn => btn.classList.remove("active"));
    document.querySelector(`.tab-btn[onclick="filterVehicles('${category}')"]`).classList.add("active");

    // Render vehicles for the selected category
    renderVehicles(allVehicles, category);
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
// Global variable to store the booking ID for payment


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

    const today = new Date();
    today.setHours(0, 0, 0, 0); // Set time to midnight for comparison
    const selectedStartDate = new Date(startDate);

    if (selectedStartDate < today) {
        alert("Please select a valid date.");
        return;
    }

    const API_URL = `http://localhost:8080/booking/add?email=${encodeURIComponent(user.email)}&registration_no=${encodeURIComponent(selectedVehicleRegNo)}&startDate=${encodeURIComponent(startDate)}&endDate=${encodeURIComponent(endDate)}`;
    
    try {
        console.log("Calling Add Booking API:", API_URL);

        const response = await fetch(API_URL, { method: "POST" });

        if (response.ok) {
            const bookingResponse = await response.json();
            console.log("Booking successful:", bookingResponse);

            // Show booking success alert
            closeBookingForm();
            // Store the booking ID for payment
            currentBookingId = bookingResponse.bId;

            // Open the payment form modal
            openPaymentForm();
        } else {
            const errorText = await response.text();
            console.error("Booking API Error:", errorText);
            alert("❌ Booking Failed! Try Again.");
        }
    } catch (error) {
        console.error("Error booking vehicle:", error);
        alert(`❌ Something went wrong! Error: ${error.message}`);
    }
}

// Open Payment Form
function openPaymentForm() {
    document.getElementById("paymentModal").style.display = "block";
}

// Close Payment Form
function closePaymentForm() {
    document.getElementById("paymentModal").style.display = "none";
}

// Submit Payment
async function submitPayment() {
    const cardNumber = document.getElementById("card-number").value;
    const expiryDate = document.getElementById("expiry-date").value;
    const cvv = document.getElementById("cvv").value;

    if (!cardNumber || !expiryDate || !cvv) {
        alert("Please fill out all payment details!");
        return;
    }

    // Call the payment API
    await initiatePayment(currentBookingId);

    // Close the payment form modal
    closePaymentForm();
}

// Initiate Payment
async function initiatePayment(bookingId) {
    const API_URL = `http://localhost:8080/booking/payment/${bookingId}`;

    try {
        console.log("Calling Payment API:", API_URL);

        const response = await fetch(API_URL, { method: "POST" });

        if (response.ok) {
            const paymentResponse = await response.json();
            console.log("Payment successful:", paymentResponse);

            if (paymentResponse.status === "SUCCESS") {
                alert(paymentResponse.message);
            } else {
                alert(paymentResponse.message);
            }
            
        } else {
            const errorResponse = await response.json();
            console.error("Payment API Error:", errorResponse);
            alert(errorResponse.message || "❌ Payment Failed! Try Again.");
        }
    } catch (error) {
        console.error("Error initiating payment:", error);
        alert(`❌ Payment failed! Error: ${error.message}`);
    }
}
// Load Vehicles
document.addEventListener("DOMContentLoaded", fetchVehicles);