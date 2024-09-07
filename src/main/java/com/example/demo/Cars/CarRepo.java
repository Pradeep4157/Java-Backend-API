package com.example.demo.Cars;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface CarRepo extends MongoRepository<Car,Long> {
}
