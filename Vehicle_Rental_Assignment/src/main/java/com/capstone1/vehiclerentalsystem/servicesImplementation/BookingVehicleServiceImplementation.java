package com.capstone1.vehiclerentalsystem.servicesImplementation;

import com.capstone1.vehiclerentalsystem.entities.BookingVehicle.BookingStatus;
import com.capstone1.vehiclerentalsystem.entities.User.Role;
import com.capstone1.vehiclerentalsystem.entities.BookingVehicle;
import com.capstone1.vehiclerentalsystem.entities.User;
import com.capstone1.vehiclerentalsystem.entities.Vehicle;
import com.capstone1.vehiclerentalsystem.repositories.BookingVehicleRepository;
import com.capstone1.vehiclerentalsystem.repositories.VehicleRepository;
import com.capstone1.vehiclerentalsystem.services.BookingVehicleService;
import com.capstone1.vehiclerentalsystem.services.LoginService;
import com.capstone1.vehiclerentalsystem.services.VehicleService;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class BookingVehicleServiceImplementation implements BookingVehicleService {

    @Autowired
    VehicleRepository vehicleRepository;
    @Autowired
    BookingVehicleRepository bookingRepository;
    @Autowired
    LoginService loginService;
    @Autowired
    VehicleService vehicleService;

    public ResponseEntity<String> searchForExistingBookings(String registration_no, LocalDate startDate,
            LocalDate endDate) {
        Vehicle vehicle = vehicleService.getByRegistrationNumber(registration_no);

        if (startDate.isAfter(endDate))
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Start Date must be before end date");

        List<BookingVehicle> existingBookings = bookingRepository
                .findByVehicleAndStartDateLessThanEqualAndEndDateGreaterThanEqualAndBookingStatus(vehicle, endDate,
                        startDate, BookingStatus.CONFIRMED);
        if (existingBookings.size() > 0) {
            System.out.println(existingBookings.toString());
            String[] bookedArr = new String[existingBookings.size()];
            Arrays.setAll(bookedArr, (i) -> existingBookings.get(i).getStartDate().toString() + " and "
                    + existingBookings.get(i).getEndDate().toString());

            return ResponseEntity.status(HttpStatus.CONFLICT).body(
                    """
                                The Vehicle "%s" is already booked between %s

                            """.formatted(registration_no, String.join(" , ", bookedArr)));
        }

        return ResponseEntity.ok("It is Available now");
    }

    public ResponseEntity<String> addBooking(String email, String registration_no, String startDate, String endDate) {
        try {
            User u1 = loginService.getUserByEmail(email);
            Vehicle v1 = vehicleService.getByRegistrationNumber(registration_no);
            LocalDate start = LocalDate.parse(startDate);
            LocalDate end = LocalDate.parse(endDate);

            // Checking for already booked case
            ResponseEntity<String> isAvailable = this.searchForExistingBookings(registration_no, start, end);

            if (isAvailable.getStatusCode() != HttpStatusCode.valueOf(200))
                return isAvailable;

            // calculating total price;
            long days = ChronoUnit.DAYS.between(start, end) + 1; // including the initial too
            System.out.println("Total Days are : " + days);
            double totalPrice = v1.getPrice_per_day() * days;

            BookingVehicle booking = new BookingVehicle();
            booking.setUser(u1);
            booking.setVehicle(v1);
            booking.setbTime(LocalDateTime.now());
            booking.setStartDate(start);
            booking.setEndDate(end);
            booking.setPrice(totalPrice);
            booking.setBookingStatus(BookingStatus.CONFIRMED);

            BookingVehicle bookSaved = bookingRepository.save(booking);
            u1.addBooking(bookSaved);
            v1.addBooking(bookSaved);
            System.out.println(bookSaved);

            return ResponseEntity.ok("Successfully Booked");

        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Something went wrong while booking");
        }

    }

    public ResponseEntity<List<BookingVehicle>> getBookings(String email) {

        try {
            User user = loginService.getUserByEmail(email);
            List<BookingVehicle> bookingsList = bookingRepository.findByUser(user);
            return ResponseEntity.ok().body(bookingsList);

        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(new ArrayList<>());
        }

    }

    public ResponseEntity<List<BookingVehicle>> getAllBookings(String email) {
        try {
            User user = loginService.getUserByEmail(email);
            if (user.getRole() == Role.ADMIN)
                return ResponseEntity.ok().body((List<BookingVehicle>) bookingRepository.findAll());
            else
                return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(new ArrayList<>());
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(new ArrayList<>());
        }
    }

}
