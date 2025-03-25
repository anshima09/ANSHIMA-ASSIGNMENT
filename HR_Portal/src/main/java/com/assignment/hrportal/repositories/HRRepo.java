package com.assignment.hrportal.repositories;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.assignment.hrportal.Entities.HR;

@Repository
public interface HRRepo extends JpaRepository<HR,Long> {

    Optional<HR> findByUsername(String username);
} 
