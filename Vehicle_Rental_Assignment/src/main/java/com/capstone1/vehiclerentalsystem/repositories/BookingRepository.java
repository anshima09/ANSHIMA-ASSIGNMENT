package com.capstone1.vehiclerentalsystem.repositories;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.capstone1.vehiclerentalsystem.entities.Booking;
import com.capstone1.vehiclerentalsystem.entities.User;

@Repository
public interface BookingRepository extends JpaRepository<Booking, Integer> {

   

    List<Booking> findByUser(User user);
}
