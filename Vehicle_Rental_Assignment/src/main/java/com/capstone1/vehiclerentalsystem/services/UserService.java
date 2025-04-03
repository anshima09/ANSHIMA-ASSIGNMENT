package com.capstone1.vehiclerentalsystem.services;

import java.util.List;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import com.capstone1.vehiclerentalsystem.entities.User;

@Service
public interface UserService {

    User getUserByEmailAndPassword(String email, String password);

    User getUserByEmail(String email);

    User getById(int id);

    User storeUserData(User user);

    public boolean isAdmin(String alreadyAdminEmail);

    public ResponseEntity<List<User>> getAllUsers(String email);

}
