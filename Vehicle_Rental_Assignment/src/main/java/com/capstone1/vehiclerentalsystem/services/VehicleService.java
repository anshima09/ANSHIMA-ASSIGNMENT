package com.capstone1.vehiclerentalsystem.services;

import java.util.List;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import com.capstone1.vehiclerentalsystem.entities.Vehicle;

@Service
public interface VehicleService {

    public ResponseEntity<String> addVehicle(String email, Vehicle vehicle);

    public ResponseEntity<List<Vehicle>> getAllVehicles();

    public Vehicle getByRegistrationNumber(String registration_no);

}
