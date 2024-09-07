package com.example.demo.Payment;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

//CREATIONAL PATTERN : FACTORY refer Customer
@RestController
@RequestMapping("/payments")
// no update method to make it immutable
public class PaymentController {
    @Autowired
    PaymentRepo paymentrepo;
//    @Autowired
//    private JavaMailSender emailSender;
    @Autowired
//    private EmailService emailService;
    @GetMapping("/")
    public ResponseEntity<List<Payment>> allPayments(){
        try{
            List<Payment> payments = new ArrayList<>();
            paymentrepo.findAll().forEach(payments::add);
            if(payments.isEmpty()){
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }
            return new ResponseEntity<>(payments,HttpStatus.OK);
        }
        catch (Exception ex){
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    @PostMapping("/makepayment/{mode}")
    public ResponseEntity<Payment> makepayment(@PathVariable String mode, @RequestBody Payment payment) {
        try {
            Payment newpayment = paymentrepo.save(payment);
            return new ResponseEntity<>(newpayment, HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    @PostMapping("/processpayment/{paymentid}")
    public ResponseEntity<Payment> processpayment(@PathVariable Long paymentid, @RequestParam String email){ // set status as accepted and email invoice
        try {
            Optional<Payment> payment = paymentrepo.findById(paymentid);
            if (payment.isPresent()) {
                Payment tovalidate = payment.get();
                if(tovalidate.getPaymentStatus() == PaymentStatus.PENDING) {
                    tovalidate.setPaymentStatus(PaymentStatus.ACCEPTED);
                }
                Payment paymentObj = paymentrepo.save(tovalidate);
//                emailService.sendEmail(email, "Payment Accepted", "Your payment has been accepted.");
                return new ResponseEntity<>(paymentObj, HttpStatus.OK);
            }
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
