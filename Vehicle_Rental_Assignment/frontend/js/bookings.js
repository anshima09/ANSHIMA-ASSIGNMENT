// Fetch user profile details
function fetchUserProfile() {
    const user = JSON.parse(localStorage.getItem("user"));

    if (!user) {
        alert("User not logged in!");
        window.location.href = "index.html";
        return;
    }

    // Display user details
    document.getElementById("userName").textContent = user.name || "N/A";
    document.getElementById("userEmail").textContent = user.email || "N/A";
    document.getElementById("userContact").textContent = user.contact_number || "N/A";
}

// Fetch bookings for the logged-in user
async function fetchBookings() {
    const user = JSON.parse(localStorage.getItem("user"));

    if (!user || !user.email) {
        document.getElementById("bookings-table-body").innerHTML = `<tr><td colspan="9" class="loading">Please log in to view your bookings.</td></tr>`;
        return;
    }

   

    const API_URL = `http://localhost:8080/booking/getByEmail?email=${encodeURIComponent(user.email)}`;
    console.log("Fetching data from:", API_URL);

    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
        }

        const bookings = await response.json();
        console.log("API Response:", bookings);

        if (!bookings || bookings.length === 0) {
            document.getElementById("bookings-table-body").innerHTML = `<tr><td colspan="9" class="loading">No Bookings Found.</td></tr>`;
            return;
        }

        renderBookings(bookings);
    } catch (error) {
        console.error("Error fetching bookings:", error);
        document.getElementById("bookings-table-body").innerHTML = `<tr><td colspan="9" class="loading">Failed to load bookings. Try again later.</td></tr>`;
    }
}

// Function to render bookings in the table
// Function to render bookings in the table
// Function to render bookings in the table
function renderBookings(bookings) {
    const bookingsTableBody = document.getElementById("bookings-table-body");

    bookingsTableBody.innerHTML = bookings.map(booking => {
        const startDate = new Date(booking.startDate);
        const endDate = new Date(booking.endDate);
        const today = new Date();

        // Check if the booking is expired
        const isExpired = endDate < today;
        const bookingStatus = isExpired ? "EXPIRED" : booking.bookingStatus;

        // Check if the delete button should be shown (only if within 7 days of the start date)
        const daysSinceStart = Math.floor((today - startDate) / (1000 * 60 * 60 * 24)); // Days difference
        const deleteButton = daysSinceStart <= 7 && !isExpired
            ? `<button class="delete-btn" onclick="deleteBooking(${booking.bId})">Remove</button>`
            : `<span class="disabled-btn">Not Allowed</span>`;

        return `
            <tr>
                <td>${booking.bId}</td>
                <td>${new Date(booking.bTime).toLocaleString()}</td>
                <td class="${bookingStatus === "CONFIRMED" ? "status-confirmed" : bookingStatus === "EXPIRED" ? "status-expired" : "status-cancelled"}">
                    ${bookingStatus}
                </td>
                <td>${booking.startDate}</td>
                <td>${booking.endDate}</td>
                <td>Rs.${booking.price.toFixed(2)}</td>
                <td>${booking.vehicle.name}</td>
                <td>${booking.vehicle.model}</td>
                <td>${booking.vehicle.registration_number}</td>
                <td>${deleteButton}</td>
            </tr>
        `;
    }).join("");
}

// Delete a booking
async function deleteBooking(bookingId) {
    const user = JSON.parse(localStorage.getItem("user"));

    if (!user || !user.email) {
        alert("Please log in to delete a booking.");
        return;
    }

    const API_URL = `http://localhost:8080/booking/delete?email=${encodeURIComponent(user.email)}&bookingId=${bookingId}`;

    if (confirm("Are you sure you want to delete this booking?")) {
        try {
            const response = await fetch(API_URL, { method: "DELETE" });

            if (response.ok) {
                alert("Booking deleted successfully!");
                fetchBookings(); // Reload bookings after deletion
            } else {
                const errorMessage = await response.text();
                alert(`Failed to delete booking: ${errorMessage}`);
            }
        } catch (error) {
            console.error("Error deleting booking:", error);
            alert("An error occurred while deleting the booking.");
        }
    }
}

// Load user profile and bookings when the page loads
document.addEventListener("DOMContentLoaded", () => {
    fetchUserProfile();
    fetchBookings();
});