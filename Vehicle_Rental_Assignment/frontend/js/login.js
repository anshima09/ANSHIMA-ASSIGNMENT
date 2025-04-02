document.getElementById("loginForm").addEventListener("submit", login);

async function login(event) {
    console.log("btn clicked");
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch(`http://localhost:8080/authentication/login?email=${email}&password=${password}`, {
        method: "GET"
        
    });


    if (response.ok) {
        const data = await response.json();
        console.log(data);
        console.log(data.role);
        if(data.role == "ADMIN"){
            localStorage.setItem("admin",JSON.stringify(data));;
            window.location.href = "admin.html";
        }
        else{
            localStorage.setItem("user",JSON.stringify(data));;
           window.location.href = "home.html";
        }
        

    } else {
        alert("Invalid email or password.");
    }

}