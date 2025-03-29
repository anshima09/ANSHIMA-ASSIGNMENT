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
function renderBookings(bookings) {
    const bookingsTableBody = document.getElementById("bookings-table-body");

    bookingsTableBody.innerHTML = bookings.map(booking => `
        <tr>
            <td>${booking.bId}</td>
            <td>${new Date(booking.bTime).toLocaleString()}</td>
            <td class="${booking.bookingStatus === "CONFIRMED" ? "status-confirmed" : "status-cancelled"}">
                ${booking.bookingStatus}
            </td>
            <td>${booking.startDate}</td>
            <td>${booking.endDate}</td>
            <td>$${booking.price.toFixed(2)}</td>
            <td>${booking.vehicle.name}</td>
            <td>${booking.vehicle.model}</td>
            <td>${booking.vehicle.registration_number}</td>
        </tr>
    `).join("");
}

// Load bookings when the page loads
document.addEventListener("DOMContentLoaded", fetchBookings);