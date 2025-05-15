package com.capstone1.vehiclerentalsystem.controllers;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.capstone1.vehiclerentalsystem.entities.Booking;
import com.capstone1.vehiclerentalsystem.repositories.BookingRepository;
import com.capstone1.vehiclerentalsystem.services.BookingService;

@RestController
@CrossOrigin("*")
@RequestMapping("/booking")
public class BookingController {

    @Autowired
    BookingService bookingVehicleService;

    @Autowired
    BookingRepository bookingRepository;

    // Adding the Booking
    @PostMapping("/add")
    public ResponseEntity<Booking> AddBooking(@RequestParam String email, @RequestParam String registration_no,
            @RequestParam String startDate, @RequestParam String endDate) {
        try {
            return bookingVehicleService.addBooking(email, registration_no, startDate, endDate);
        } catch (Exception e) {
            e.printStackTrace();
        }

        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null);
    }

    @GetMapping("/getAllBookings")
    public ResponseEntity<List<Booking>> getAllBookedVehicles(@RequestParam String email) {
        return bookingVehicleService.getAllBookings(email);
    }

    @GetMapping("/getByEmail")
    public ResponseEntity<List<Booking>> getBookingHistoryByMail(@RequestParam String email) {
        return bookingVehicleService.getBookings(email);
    }

    @DeleteMapping("/delete")
    public ResponseEntity<String> deleteBooking(@RequestParam String email, @RequestParam Integer bookingId) {
        try {
            return bookingVehicleService.deleteBooking(email, bookingId);
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Something went wrong while deleting the booking");
        }
    }

    // Generic Payment Process API
   @PostMapping("/payment/{bookingId}")
public ResponseEntity<Map<String, Object>> processPayment(@PathVariable Integer bookingId) {
    try {
        // Fetch the booking details using bookingId
        Booking booking = bookingRepository.findById(bookingId)
                .orElseThrow(() -> new RuntimeException("Booking not found"));

        // Simulate payment processing
        double amount = booking.getPrice(); // Assuming price is in rupees
        String paymentStatus = simulatePayment(amount);

        // Prepare the response
        Map<String, Object> response = new HashMap<>();
        response.put("bookingId", bookingId);
        response.put("amount", amount);

        // Update booking status based on payment result
        if ("SUCCESS".equals(paymentStatus)) {
            booking.setPaymentStatus("PAID");
            bookingRepository.save(booking);

            response.put("status", "SUCCESS");
            response.put("message", "Booking and Payment successful for booking ID: " + bookingId);
            return ResponseEntity.ok(response);
        } else {
            response.put("status", "FAILURE");
            response.put("message", "Payment failed for booking ID: " + bookingId);
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(response);
        }
    } catch (RuntimeException e) {
        Map<String, Object> errorResponse = new HashMap<>();
        errorResponse.put("status", "ERROR");
        errorResponse.put("message", "Error: " + e.getMessage());
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(errorResponse);
    } catch (Exception e) {
        Map<String, Object> errorResponse = new HashMap<>();
        errorResponse.put("status", "ERROR");
        errorResponse.put("message", "Payment processing failed: " + e.getMessage());
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(errorResponse);
    }
}
    // Simulate Payment Processing
    private String simulatePayment(double amount) {
        // Simulate payment logic (e.g., random success/failure)
        if (amount > 0) {
            return "SUCCESS"; // Simulate successful payment
        } else {
            return "FAILURE"; // Simulate failed payment
        }
    }
}