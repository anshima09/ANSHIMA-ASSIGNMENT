async function fetchUsers() {
    try {
        const response = await fetch('http://localhost:8080/authentication/getAllUsers', {
            method: 'GET',
            headers: {
                'Admin-Email': 'admin89669@example.com' 
            }
        });

        if (response.status === 401) {
            alert("Unauthorized access!");
            return;
        }

        if (!response.ok) {
            throw new Error("Failed to fetch users");
        }

        const users = await response.json();
        const tableBody = document.getElementById("userTableBody");
       
        users.forEach(user => {
            if(user.role=="USER"){
            const row = document.createElement("tr");
              
            row.innerHTML = `
                <td>${user.user_id}</td>
                <td>${user.name}</td>
                <td>${user.email}</td>
                <td>${user.contact_number || "N/A"}</td>
                <td>${user.role}</td>
            `;

            tableBody.appendChild(row);
            }
        });

    } catch (error) {
        console.error("Error fetching users:", error);
    }
}

fetchUsers();