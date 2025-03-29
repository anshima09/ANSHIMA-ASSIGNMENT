package com.capstone1.vehiclerentalsystem.repositories;

import java.time.LocalDate;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.capstone1.vehiclerentalsystem.entities.BookingVehicle;
import com.capstone1.vehiclerentalsystem.entities.BookingVehicle.BookingStatus;
import com.capstone1.vehiclerentalsystem.entities.User;
import com.capstone1.vehiclerentalsystem.entities.Vehicle;

@Repository
public interface BookingVehicleRepository extends JpaRepository<BookingVehicle, Integer> {

    List<BookingVehicle> findByVehicleAndStartDateLessThanEqualAndEndDateGreaterThanEqualAndBookingStatus(
            Vehicle vehicle, LocalDate endDate, LocalDate startDate, BookingStatus bookingStatus);

    List<BookingVehicle> findByUser(User user);
}
