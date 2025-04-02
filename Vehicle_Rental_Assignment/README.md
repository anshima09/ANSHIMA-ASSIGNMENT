# Vehicle Rental System

## Project Overview

The Vehicle Rental System (VRS) is an online platform that streamlines the vehicle rental process, offering users a hassle-free way to book vehicles while equipping administrators with robust tools for managing vehicles, reservations, users. With a secure and efficient booking mechanism, the system delivers an intuitive and responsive interface, ensuring a smooth and engaging user experience.

## Features

### User Features

- **User Registration & Login:** The login is provided to users, while the signup functionality is restricted to the admin, who can create new user accounts.
- **Booking System:** Select start and end dates for booking.
- **Booking History:** View past and current bookings.
- **Homepage Content:** The homepage contains recently added cars and bikes fetched dynamically from the backend.

### Admin Features

- **Admin Dashboard:** Manage vehicle inventory, bookings, and users.
- **Add Vehicles:** Add vehicles.
- **View Bookings:** Admin can view booking details.
- **User Management:** Admin can add registered users.
- **Profile:** Admin can see their own profile information.


## Technologies Used

### Frontend

- **HTML, CSS, JavaScript** - Core frontend technologies.

### Backend

- **Java Spring Boot** - Backend framework for handling business logic.
- **POSTGRESQL** - Database to store users, vehicles and booking information.



## Folder Structure

```
/VEHICLERENTALSYSTEM
├── /src
│   ├── /main
│   │   ├── /java/com/capstone1/vehicalrentalsystem
│   │   │   ├── /configurations
│   │   │   ├── /controllers
│   │   │   ├── /entities
│   │   │   ├── /repositories
│   │   │   ├── /services
|   |   |   ├── /servicesImplementation
│   │   │   └── VehicalrentalsytemApplication.java
│   │   ├── /resources
│   │   │   ├── /templates
│   │   │   ├── /static
│   │   │   │   
│   │   │   │   
│   │   │   │
├── /public
│   └── /uploads
└── /frontEnd_dev
    ├── about.html
    ├── add_vehicle.html
    ├── admin_bookings.html
    ├── admin_profile.html
    ├── admin_user.html
    ├── admin_vehicle.html
    ├── admin.html
    ├── bookings.html
    └── home.html
    ├── index.html
    ├── users.html
    └── vehicles.html
    ├── /css
    ├── /js
    └── /images


## How to Run

### Prerequisites

- **Java JDK 11+**
- **MySQL Database**
- **Spring Boot CLI**

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/anshima09/ANSHIMA-ASSIGNMENT
```

2. **Navigate to the project directory:**

```bash
cd vehicle-rental-system
```

3. **Configure Database:**

- Open `application.properties` and set your database credentials.

4. **Run the backend:**

```bash
mvn spring-boot:run
```

## Usage

- Navigate to the homepage.
- Select a vehicle in vehicles section
- Provide booking details and confirm.
- View top reviews, recently added cars, and recently added bikes.
- Add reviews after booking.
- View review and booking history.
- Admin can log in to manage the system, vehicles, bookings, users, and reviews.

## Contact

For inquiries, contact:

- **Email:** [anshima0906s@gmail.com](mailto:anshima0906s@gmail.com)
- **GitHub:** [GitHub Repository](https://github.com/anshima09/ANSHIMA-ASSIGNMENT/tree/main/Vehicle_Rental_Assignment)

---

Happy Coding! 

