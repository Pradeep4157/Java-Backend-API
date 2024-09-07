package com.example.demo.Employee.Enggineer;

import com.example.demo.Payment.Payment;
import com.example.demo.Services.ServiceRepo;
import com.example.demo.Services.ServiceRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.time.LocalDateTime;


@RestController
@RequestMapping("/engineer")
public class EnggineerController {
    @Autowired
    private ServiceRepo serverepo;
    @PostMapping("/appointments/{appointmentId}/estimateCost")
    public ResponseEntity<ServiceRequest> giveCostEstimate(@PathVariable Long appointmentId, @RequestBody float estimate){
        ServiceRequest serviceRequest = serverepo.findById(appointmentId)
                .orElseThrow(() -> new RuntimeException("Service appointment not found with id: " + appointmentId));
        serviceRequest.setTotalCost(estimate);
        // Save the updated service appointment
        serverepo.save(serviceRequest);
        return new ResponseEntity<>(serviceRequest,HttpStatus.OK);
    }
    @PutMapping("/appointments/{appointmentId}/updateProgress")
    public ResponseEntity<ServiceRequest> updateServiceProgress(@PathVariable Long appointmentId, @RequestBody String update){
        ServiceRequest serviceRequest = serverepo.findById(appointmentId)
                .orElseThrow(() -> new RuntimeException("Service appointment not found with id: " + appointmentId));
        LocalDateTime currentDateTime = LocalDateTime.now();
        serviceRequest.getUpdates().put(currentDateTime, update);
        serverepo.save(serviceRequest);
        return new ResponseEntity<>(serviceRequest,HttpStatus.OK);
    }
}
