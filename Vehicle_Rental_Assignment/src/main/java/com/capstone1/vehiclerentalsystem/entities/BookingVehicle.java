package com.capstone1.vehiclerentalsystem.entities;

import java.time.LocalDate;
import java.time.LocalDateTime;

import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import jakarta.persistence.Version;

@Entity
@Table(name = "booking_vehicle")
public class BookingVehicle {
    public enum BookingStatus {
        CONFIRMED, CANCELLED;
    }

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int bId;

    private LocalDateTime bTime;

    private LocalDate startDate;

    private LocalDate endDate;

    private double price;

    @Enumerated(EnumType.STRING)
    private BookingStatus bookingStatus;

    @ManyToOne
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    @ManyToOne
    @JoinColumn(name = "vehicle_id", nullable = false)
    private Vehicle vehicle;

    @Version
    private int version;

    public BookingVehicle() {
    }

    public BookingVehicle(LocalDate startDate, LocalDate endDate, double price,
            BookingStatus bookingStatus) {

        this.bTime = LocalDateTime.now();
        this.startDate = startDate;
        this.endDate = endDate;
        this.price = price;
        this.bookingStatus = bookingStatus;
    }

    public int getbId() {
        return bId;
    }

    public void setbId(int bId) {
        this.bId = bId;
    }

    public LocalDateTime getbTime() {
        return bTime;
    }

    public void setbTime(LocalDateTime bTime) {
        this.bTime = bTime;
    }

    public LocalDate getStartDate() {
        return startDate;
    }

    public void setStartDate(LocalDate startDate) {
        this.startDate = startDate;
    }

    public LocalDate getEndDate() {
        return endDate;
    }

    public void setEndDate(LocalDate endDate) {
        this.endDate = endDate;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public BookingStatus getBookingStatus() {
        return bookingStatus;
    }

    public void setBookingStatus(BookingStatus bookingStatus) {
        this.bookingStatus = bookingStatus;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public Vehicle getVehicle() {
        return vehicle;
    }

    public void setVehicle(Vehicle vehicle) {
        this.vehicle = vehicle;
    }

    @Override
    public String toString() {
        return "Booking [booking_id=" + bId + ", startDate=" + startDate + ", endDate=" + endDate
                + ", totalPrice=" + price + ", bookingStatus=" + bookingStatus + "]";
    }

}
