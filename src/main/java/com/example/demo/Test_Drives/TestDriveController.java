package com.example.demo.Test_Drives;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/testdrives")
public class TestDriveController {
    @Autowired
    Test_DriveRepo scheduledtestdrives;
    @GetMapping("/")
    public ResponseEntity<List<Test_Drive>> allAppointents(){
        try{
            List<Test_Drive> bookings = new ArrayList<>();
            scheduledtestdrives.findAll().forEach(bookings::add);
            if(bookings.isEmpty()){
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }
            return new ResponseEntity<>(bookings,HttpStatus.OK);
        }
        catch (Exception ex){
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    @PostMapping("/scheduleTestDrive")
    public ResponseEntity<Test_Drive> scheduleTestDrive(@RequestBody Test_Drive testDrive) {
        try {
            scheduledtestdrives.save(testDrive);
            return new ResponseEntity<>(testDrive,HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PostMapping("/clearTestDrive")
    public ResponseEntity<?> clearTestDrive(@RequestParam Long appointmentId) {
        try {
            scheduledtestdrives.deleteById(appointmentId);
            return new ResponseEntity<>(HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping("/getTestDrives")
    public ResponseEntity<List<Test_Drive>> getTestDrives() {
        try {
            List<Test_Drive> testDrives = scheduledtestdrives.findAll();
            return new ResponseEntity<>(testDrives, HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
