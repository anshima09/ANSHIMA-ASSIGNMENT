package com.capstone1.vehiclerentalsystem.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.capstone1.vehiclerentalsystem.entities.Vehicle;
import com.capstone1.vehiclerentalsystem.services.VehicleService;

@CrossOrigin("*")
@RestController
@RequestMapping("/vehicle")
public class VehicleController {
    @Autowired
    VehicleService vehicleService;

    // @Autowired

    @GetMapping("/getAllVehicles")
    public ResponseEntity<List<Vehicle>> getVehicles() {
        return vehicleService.getAllVehicles();
    }

    // Admin Specific Functionalities
    @PostMapping("/add/{email}")
    public ResponseEntity<String> addingVehicleByAdminOnly(@PathVariable("email") String email,
            @RequestBody Vehicle vehicle) {
        try {
            return vehicleService.addVehicle(email, vehicle);
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Can't store the vehicle.");
        }

    }

}
