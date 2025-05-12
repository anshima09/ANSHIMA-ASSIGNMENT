package com.capstone1.vehiclerentalsystem.servicesImplementation;

import com.capstone1.vehiclerentalsystem.entities.Booking.BookingStatus;
import com.capstone1.vehiclerentalsystem.entities.User.Role;
import com.capstone1.vehiclerentalsystem.entities.Booking;
import com.capstone1.vehiclerentalsystem.entities.User;
import com.capstone1.vehiclerentalsystem.entities.Vehicle;
import com.capstone1.vehiclerentalsystem.repositories.BookingRepository;
import com.capstone1.vehiclerentalsystem.repositories.VehicleRepository;
import com.capstone1.vehiclerentalsystem.services.BookingService;
import com.capstone1.vehiclerentalsystem.services.UserService;
import com.capstone1.vehiclerentalsystem.services.VehicleService;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class BookingServiceImplementation implements BookingService {

    @Autowired
    VehicleRepository vehicleRepository;
    @Autowired
    BookingRepository bookingRepository;
    @Autowired
    UserService userService;
    @Autowired
    VehicleService vehicleService;


    public ResponseEntity<String> addBooking(String email, String registration_no, String startDate, String endDate) {
        try {
            User u1 = userService.getUserByEmail(email);
            if (u1 == null) {
    return ResponseEntity.status(HttpStatus.NOT_FOUND).body("User not found with email: " + email);
}
            Vehicle v1 = vehicleService.getByRegistrationNumber(registration_no);
            
            if (v1 == null) {
    return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Vehicle not found with registration number: " + registration_no);
}
            LocalDate start = LocalDate.parse(startDate);
            LocalDate end = LocalDate.parse(endDate);

            System.out.println("Date is correct huraahhhhhhhhhhhhhh");

            if (end.isBefore(start)) {
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("End date cannot be earlier than start date.");
            }

            // calculating total price;
            long days = ChronoUnit.DAYS.between(start, end) + 1; // including the initial too
            System.out.println("Total Days are : " + days);
            double totalPrice = v1.getPrice_per_day() * days;

            
            Booking booking = new Booking();
            booking.setUser(u1);
            booking.setVehicle(v1);
            booking.setbTime(LocalDateTime.now());
            booking.setStartDate(start);
            booking.setEndDate(end);
            booking.setPrice(totalPrice);
            booking.setBookingStatus(BookingStatus.CONFIRMED);

            Booking bookSaved = bookingRepository.save(booking);
            u1.addBooking(bookSaved);
            v1.addBooking(bookSaved);
            System.out.println(bookSaved);

            return ResponseEntity.ok("Successfully Booked");
            

        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Something went wrong while booking");
        }

    }

    public ResponseEntity<List<Booking>> getBookings(String email) {

        try {

            User user = userService.getUserByEmail(email);
            List<Booking> bookingsList = bookingRepository.findByUser(user);
            return ResponseEntity.ok().body(bookingsList);

        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(new ArrayList<>());
        }

    }

    public ResponseEntity<List<Booking>> getAllBookings(String email) {
        try {
            User user = userService.getUserByEmail(email);
            if (user.getRole() == Role.ADMIN)
                return ResponseEntity.ok().body((List<Booking>) bookingRepository.findAll());
            else
                return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(new ArrayList<>());
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(new ArrayList<>());
        }
    }

    @Override
public ResponseEntity<String> deleteBooking(String email, Integer bookingId) {
    try {
        User user = userService.getUserByEmail(email);
        Booking booking = bookingRepository.findById(bookingId)
                .orElseThrow(() -> new RuntimeException("Booking not found"));

        // Check if the user is the owner of the booking or an admin
        if (user.getRole() == Role.ADMIN || booking.getUser().getEmail().equals(email)) {
            bookingRepository.delete(booking);
            return ResponseEntity.ok("Booking deleted successfully");
        } else {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("You are not authorized to delete this booking");
        }
    } catch (Exception e) {
        e.printStackTrace();
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Something went wrong while deleting the booking");
    }
}

@Override
public Booking getBookingById(Integer bookingId) {
    return bookingRepository.findById(bookingId).orElse(null);
}

}
