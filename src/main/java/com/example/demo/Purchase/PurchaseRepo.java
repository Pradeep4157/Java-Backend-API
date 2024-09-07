package com.example.demo.Purchase;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface PurchaseRepo extends MongoRepository<Purchase,Long> {

}
