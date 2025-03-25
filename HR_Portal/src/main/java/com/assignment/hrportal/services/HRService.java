package com.assignment.hrportal.services;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.assignment.hrportal.Entities.HR;
import com.assignment.hrportal.repositories.HRRepo;

@Service
public class HRService{
     @Autowired
    private HRRepo hrRepo;

    // Authenticate HR
    public boolean authenticate(String username, String password) {
        Optional<HR> hr = hrRepo.findByUsername(username);
        return hr.isPresent() && hr.get().getPassword().equals(password);
    }

    // Add HR (only for first-time setup)
    public HR addHR(HR hr) {
        return hrRepo.save(hr);
    }
}
