package com.example.demo.Services;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Map;
//FLYWEIGHT
//extrinsic: othen than services
//intrinsic: services list
//@Entity
//@Table(name="service_request")
@Document("service_request")
@AllArgsConstructor
@NoArgsConstructor
@Setter
@Getter
public class ServiceRequest {
    @Id
    private Long appointmentId;
    private Long customerId;
    private Long carId;
    private List<Services> services;
    private LocalDateTime dateTime;
    private float totalCost;
    private Status status;
    private Map<LocalDateTime,String> Updates;
}
