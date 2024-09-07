package com.example.demo.Payment;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface PaymentRepo extends MongoRepository<Payment,Long> {
}
