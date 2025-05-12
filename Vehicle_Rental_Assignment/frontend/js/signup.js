// Email validation function
function validateEmail() {
    const emailInput = document.getElementById("email");
    const emailError = document.getElementById("emailError");

    // Check if the email ends with @gmail.com
    if (!emailInput.value.endsWith("@gmail.com")) {
        emailError.style.display = "block"; // Show error message
        return false;
    } else {
        emailError.style.display = "none"; // Hide error message
        return true;
    }
}

// Add event listener to the form
document.getElementById("registerForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    // Validate email before proceeding
    if (!validateEmail()) {
        alert("Please enter a valid @gmail.com email address.");
        return;
    }

    const userData = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        password: document.getElementById("password").value,
        contact_number: document.getElementById("contact").value,
        role: "USER"  
    };

    try {
        const response = await fetch("http://localhost:8080/authentication/signup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(userData)
        });

        if (response.ok) {
            document.getElementById("message").innerHTML = "✅ Registration Successful!";
            document.getElementById("message").className = "message success";
            document.getElementById("registerForm").reset();
            window.location.href = "home.html";
        } else {
            document.getElementById("message").innerHTML = "❌ Registration Failed!";
            document.getElementById("message").className = "message error";
        }
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("message").innerHTML = "❌ Something went wrong!";
        document.getElementById("message").className = "message error";
    }
});