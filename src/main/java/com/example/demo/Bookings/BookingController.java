package com.example.demo.Bookings;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/bookings")
public class BookingController {
    @Autowired
    private BookingRepo bookingRepo;
    //returns all booking objects
    @GetMapping("/")
    public ResponseEntity<List<Booking>> allBookings(){
        try{
            List<Booking> bookings = new ArrayList<>();
            bookingRepo.findAll().forEach(bookings::add);
            if(bookings.isEmpty()){
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }
            return new ResponseEntity<>(bookings,HttpStatus.OK);
        }
        catch (Exception ex){
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    // deletes booking by id
    @DeleteMapping("/deleteBooking/{bookingId}")
    public ResponseEntity<Object> deleteBooking(@RequestParam Long bookingId){
        try {
            bookingRepo.deleteById(bookingId);
            return new ResponseEntity<>(HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    // checks if already booking present under customer if yes then replaces that with new booking else adds new booking.
    @PostMapping("/createBooking")
    public ResponseEntity<String> createBooking(@RequestParam Booking newBooking) {
        Optional<Booking> existingBookingOptional = bookingRepo.findById(newBooking.getBookingId());
        existingBookingOptional.ifPresent(booking -> bookingRepo.deleteById(booking.getBookingId()));

        Booking savedBooking = bookingRepo.save(newBooking);
        if (savedBooking != null) {
            return ResponseEntity.status(HttpStatus.CREATED).body("Booking created successfully");
        } else {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Failed to create booking");
        }
    }


}
