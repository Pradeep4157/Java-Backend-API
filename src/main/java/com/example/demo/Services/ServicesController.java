package com.example.demo.Services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/servicerequest")
public class ServicesController {
    @Autowired
    ServiceRepo servicerepo;
    @GetMapping("/")
    public ResponseEntity<List<ServiceRequest>> allAppointents(){
        try{
            List<ServiceRequest> bookings = new ArrayList<>();
            servicerepo.findAll().forEach(bookings::add);
            if(bookings.isEmpty()){
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }
            return new ResponseEntity<>(bookings,HttpStatus.OK);
        }
        catch (Exception ex){
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PostMapping("/{function}/service/{appointmentid}")
    public ResponseEntity<ServiceRequest> addServicetoAppointment(@PathVariable Long appointmentid , @RequestBody Services newservice, @PathVariable String function){
        try {
            Optional<ServiceRequest> findrequest = servicerepo.findById(appointmentid);
            if(findrequest.isPresent()){
                ServiceRequest updatedservreq = findrequest.get();
                List<Services> services = updatedservreq.getServices();
                if(function.equals("add")){
                    services.add(newservice);
                }
                else if (function.equals("remove")) {
                    // Remove the element from the list
//                  services.removeIf(element -> element.equals(newservice));
                    Iterator<Services> iterator = services.iterator();
                    while (iterator.hasNext()) {
                        Services element = iterator.next();
                        if (element.equals(newservice)) {
                            iterator.remove(); // Remove the element from the list
                        }
                    }
                }
                updatedservreq.setServices(services);
                ServiceRequest savedreq = servicerepo.save(updatedservreq);
                return new ResponseEntity<>(savedreq,HttpStatus.CREATED);
            }
        return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }

    @PostMapping("/newappointment")
    public ResponseEntity<ServiceRequest> newAppointment(@RequestBody ServiceRequest newservicerequest){
        try {
                Optional<ServiceRequest> checkpresent = servicerepo.findById(newservicerequest.getAppointmentId());
                if(checkpresent.isPresent()){
                    return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
                }
                ServiceRequest saved = servicerepo.save(newservicerequest);
                return new ResponseEntity<>(saved,HttpStatus.CREATED);
        } catch (Exception e ){
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @DeleteMapping("/deleteappointment/{appointmentid}")
    public ResponseEntity<ServiceRequest> removeAppointment(@PathVariable Long appointmentid){
            try {
                Optional<ServiceRequest> appointmentOptional = servicerepo.findById(appointmentid);
                if (appointmentOptional.isPresent()) {
                    servicerepo.deleteById(appointmentid);
                    return new ResponseEntity<>(HttpStatus.OK);
                } else {
                    return new ResponseEntity<>(HttpStatus.NOT_FOUND);
                }
            } catch (Exception e) {
                return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
    }
    @GetMapping("/getappointment/{appointmentid}")
    public ResponseEntity<ServiceRequest> getAppointment(@PathVariable Long appointmentid){
        try {
            Optional<ServiceRequest> appointmentOptional = servicerepo.findById(appointmentid);
            if (appointmentOptional.isPresent()) {
                ServiceRequest appointment = appointmentOptional.get();
                return new ResponseEntity<>(appointment, HttpStatus.OK);
            } else {
                return new ResponseEntity<>(HttpStatus.NOT_FOUND);
            }
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
