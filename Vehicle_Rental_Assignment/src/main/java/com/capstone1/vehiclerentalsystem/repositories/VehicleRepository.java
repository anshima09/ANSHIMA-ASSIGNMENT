package com.capstone1.vehiclerentalsystem.repositories;

import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.capstone1.vehiclerentalsystem.entities.Vehicle;
import com.capstone1.vehiclerentalsystem.entities.Vehicle.VehicleType;

@Repository
public interface VehicleRepository extends JpaRepository<Vehicle, Integer> {

    List<Vehicle> findAllByType(VehicleType vType);

    Vehicle findVehicleByRegistrationNumber(String registrantionNumber);

}
