package com.example.demo.Cars;

import lombok.*;
import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.Year;
import java.util.Date;

//@Entity
//@Table(name="cars")
@Document("cars")
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
@ToString
public class Car {
    @Id
    private Long carId;
    private String carManufacturer;
    private String carModel;
    private Date manufactureYear;
    private double quotedPrice;
    private String insuranceProvider;
}
