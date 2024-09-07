package com.example.demo.Inventory;

import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface InventoryRepo extends MongoRepository<Inventory,String> {
//    List<Inventory> findByCarmodel(String carmodel);

    List<Inventory> findBycarModel(String carmodel);
}
