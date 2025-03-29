package com.capstone1.vehiclerentalsystem.repositories;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.capstone1.vehiclerentalsystem.entities.User;

@Repository
public interface UserRepository extends JpaRepository<User, Integer> {

    Optional<User> findUserByEmailAndPassword(String email, String password);
    // find user by email and password

    Optional<User> findUserByEmail(String email);
}
