const API_URL = "http://localhost:8080/booking/getAllBookings?email=admin@example.com"; 

        // Function to fetch and display bookings
        async function fetchBookings() {
            try {
                console.log("Fetching data from API:", API_URL);
                const response = await fetch(API_URL);

                console.log("data fetched");

                if (!response.ok) {
                    throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
                }

                const bookings = await response.json();
                console.log("API Response:", bookings); // ✅ Log response

                if (!bookings || bookings.length === 0) {
                    document.getElementById("bookings-table-body").innerHTML = `
                        <tr><td colspan="8" class="loading">No Bookings Found.</td></tr>
                    `;
                    return;
                }

                renderBookings(bookings);
            } catch (error) {
                console.error("Error fetching bookings:", error);
                document.getElementById("bookings-table-body").innerHTML = `
                    <tr><td colspan="8" class="loading">Failed to load bookings. Try again later.</td></tr>
                `;
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
                    <td>Rs.${booking.price.toFixed(2)}</td>
                    <td>${booking.user.name}</td>
                    <td>${booking.vehicle.name}</td>
                </tr>
            `).join("");
        }

        // Load bookings when the page loads
        document.addEventListener("DOMContentLoaded", fetchBookings);