package com.example.demo.Services;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface ServiceRepo extends MongoRepository<ServiceRequest,Long> {

}
