package com.example.demo.Customer;

import org.springframework.data.mongodb.core.mapping.Document;

@Document("customers")
public class Customer {
    private Long customerId;
    private String firstName;
    private String lastName;
    private int contactNumber;
//    private Email email;
}
