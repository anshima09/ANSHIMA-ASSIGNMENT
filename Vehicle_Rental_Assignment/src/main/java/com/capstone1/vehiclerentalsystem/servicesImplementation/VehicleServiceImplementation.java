package com.capstone1.vehiclerentalsystem.servicesImplementation;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import com.capstone1.vehiclerentalsystem.entities.Vehicle;
import com.capstone1.vehiclerentalsystem.repositories.VehicleRepository;
import com.capstone1.vehiclerentalsystem.services.UserService;
import com.capstone1.vehiclerentalsystem.services.VehicleService;

@Service
public class VehicleServiceImplementation implements VehicleService {

    @Autowired
    VehicleRepository vehicleRepository;
    @Autowired
    UserService loginService;

    @Override
    public ResponseEntity<String> addVehicle(String email, Vehicle vehicle) {
        try {
            if (loginService.isAdmin(email)) {
                System.out.println(vehicle);
                vehicleRepository.save(vehicle);
                return ResponseEntity.ok("Vehicle Added Successfully");
            } else {
                return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                        .body("Only admins are allowed to add the vehicle");
            }
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.internalServerError()
                    .body("Vehicle might already be registered or an error occurred");
        }
    }

    public ResponseEntity<List<Vehicle>> getAllVehicles() {

        List<Vehicle> all = vehicleRepository.findAll();

        return ResponseEntity.status(HttpStatus.ACCEPTED).body(all);
    }

    

    @Override
    public Vehicle getByRegistrationNumber(String registration_no) {
        return vehicleRepository.findVehicleByRegistrationNumber(registration_no);
    }

}
