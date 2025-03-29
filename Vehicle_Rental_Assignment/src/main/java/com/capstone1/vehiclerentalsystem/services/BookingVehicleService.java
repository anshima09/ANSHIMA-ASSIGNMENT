package com.capstone1.vehiclerentalsystem.services;

import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import com.capstone1.vehiclerentalsystem.entities.BookingVehicle;

@Service
public interface BookingVehicleService {

    public ResponseEntity<String> addBooking(String email, String registration_no, String startDate, String endDate);

    public ResponseEntity<List<BookingVehicle>> getBookings(String email);

    public ResponseEntity<List<BookingVehicle>> getAllBookings(String email);

}
