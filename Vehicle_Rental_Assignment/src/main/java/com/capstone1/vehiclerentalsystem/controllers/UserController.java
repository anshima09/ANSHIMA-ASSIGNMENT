package com.capstone1.vehiclerentalsystem.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.capstone1.vehiclerentalsystem.entities.User;
import com.capstone1.vehiclerentalsystem.services.UserService;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/authentication")
public class UserController {
    @Autowired
    UserService userService;
   


    @GetMapping("/login")
    public ResponseEntity<User> getUserByEmailAndPassword(@RequestParam String email, @RequestParam String password) {
        try {
            User u1 = userService.getUserByEmailAndPassword(email, password);
            if (u1 != null)
                return ResponseEntity.ok().body(u1);
            else
                return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.internalServerError().build();
        }
    }

    @PostMapping("/signup")
    public ResponseEntity<User> signUp(@RequestBody User user) {
        User u1;
        System.out.println("Hello World");
        System.out.println(user);
        try {
            u1 = userService.storeUserData(user);
            if (u1 != null) {
                return ResponseEntity.ok().body(u1);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).build();

    }

    // Admin Specific fucntionalities

    @GetMapping("/getAllUsers")
    public ResponseEntity<List<User>> getAllUsers(@RequestHeader("Admin-Email") String email) {
        try {
            return userService.getAllUsers(email);

        } catch (Exception e) {
            e.printStackTrace();
        }

        return ResponseEntity.internalServerError().build();

    }

}
