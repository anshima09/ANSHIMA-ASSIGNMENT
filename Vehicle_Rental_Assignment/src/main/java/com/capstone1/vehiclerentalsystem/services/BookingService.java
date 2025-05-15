package com.capstone1.vehiclerentalsystem.services;

import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import com.capstone1.vehiclerentalsystem.entities.Booking;

@Service
public interface BookingService {

    public ResponseEntity<Booking> addBooking(String email, String registration_no, String startDate, String endDate);

    public ResponseEntity<List<Booking>> getBookings(String email);

    public ResponseEntity<List<Booking>> getAllBookings(String email);

    public ResponseEntity<String> deleteBooking(String email, Integer bookingId);

    Booking getBookingById(Integer bookingId);


}
