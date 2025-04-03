package com.capstone1.vehiclerentalsystem.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.capstone1.vehiclerentalsystem.entities.Vehicle;

@Repository
public interface VehicleRepository extends JpaRepository<Vehicle, Integer> {


    Vehicle findVehicleByRegistrationNumber(String registrantionNumber);

}
