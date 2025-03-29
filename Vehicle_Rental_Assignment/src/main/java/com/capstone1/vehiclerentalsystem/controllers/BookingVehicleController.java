package com.capstone1.vehiclerentalsystem.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.capstone1.vehiclerentalsystem.entities.BookingVehicle;
import com.capstone1.vehiclerentalsystem.services.BookingVehicleService;

@RestController
@CrossOrigin("*")
@RequestMapping("/booking")
public class BookingVehicleController {

    @Autowired
    BookingVehicleService bookingVehicleService;

    // Adding the Booking
    @PostMapping("/add")
    public ResponseEntity<String> AddBooking(@RequestParam String email, @RequestParam String registration_no,
            @RequestParam String startDate, @RequestParam String endDate) {
        try {
            return bookingVehicleService.addBooking(email, registration_no, startDate, endDate);
        } catch (Exception e) {
            e.printStackTrace();
        }

        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Something went wrong!!");

    }

    @GetMapping("/getAllBookings")
    public ResponseEntity<List<BookingVehicle>> getAllBookedVehicles(@RequestParam String email) {
        return bookingVehicleService.getAllBookings(email);
    }

    @GetMapping("/getByEmail")
    public ResponseEntity<List<BookingVehicle>> getBookingHistoryByMail(@RequestParam String email) {
        return bookingVehicleService.getBookings(email);
    }
}
