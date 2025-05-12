package com.capstone1.vehiclerentalsystem.servicesImplementation;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import com.capstone1.vehiclerentalsystem.entities.User;
//import com.capstone1.vehiclerentalsystem.entities.User.Role;
import com.capstone1.vehiclerentalsystem.repositories.UserRepository;
import com.capstone1.vehiclerentalsystem.services.UserService;
//import jakarta.annotation.PostConstruct;

@Service
public class UserServiceImplementation implements UserService {

    @Autowired
    PasswordEncoder passwordEncoder;

    @Autowired
    UserRepository userRepository;

    /*@PostConstruct
    public void init() {
        //Check if admin already exists
        if (userRepository.findById(20).isEmpty()) {
            User admin = new User();
            admin.setName("Admin");
            admin.setEmail("admin89669@example.com");
            admin.setPassword(passwordEncoder.encode("Admin@89669")); 
            admin.setRole(Role.ADMIN);
            userRepository.save(admin);

            System.out.println("Default admin created!");
        }
    } */
    
    @Override
    public User getUserByEmailAndPassword(String email, String password) {

        User user = userRepository.findUserByEmail(email).orElse(null);
        System.out.println(user);
        if (user != null && passwordEncoder.matches(password, user.getPassword())) {
            return user;
        }

        return null;
    }

    @Override
    public User getUserByEmail(String email) {
        return userRepository.findUserByEmail(email).get();
    }

    @Override
    public User getById(int id) {
        return userRepository.findById(id).get();
    }

    @Override
    public User storeUserData(User user) {
        user.setRole(User.Role.USER);
        user.setPassword(passwordEncoder.encode(user.getPassword()));
        return userRepository.save(user);
    }

    @Override
    public boolean isAdmin(String alreadyAdminEmail) {

        try {
            User alreadyAdmin = getUserByEmail(alreadyAdminEmail);

            if (alreadyAdmin != null && alreadyAdmin.getRole() == User.Role.ADMIN) {
                return true;
            }

        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }

        return false;

    }

    public ResponseEntity<List<User>> getAllUsers(String email) {

        try {
            if (isAdmin(email)) {
                List<User> users = userRepository.findAll();
                return ResponseEntity.ok().body(users);
            } else {
                return ResponseEntity.status(HttpStatus.UNAUTHORIZED).build();
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        return ResponseEntity.internalServerError().build();
    }

}
