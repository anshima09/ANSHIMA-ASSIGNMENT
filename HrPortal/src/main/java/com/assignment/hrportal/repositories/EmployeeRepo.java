package com.assignment.hrportal.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.assignment.hrportal.Entities.Employee;

@Repository
public interface EmployeeRepo extends JpaRepository<Employee,Long> {

    
} 
