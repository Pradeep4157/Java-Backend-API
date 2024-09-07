package com.example.demo.Payment;


import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

//FACTORY CREATIONAL PATTERN
//@Entity
//@Table(name="payments")
@Document("payments")
@AllArgsConstructor
@NoArgsConstructor
@Setter
@Getter
public class Payment {
    @Id
    private Long paymentId;
    private Long purchaseId;
    private float amount;
    private  PaymentStatus paymentStatus;
    private String paymentMode;
}

