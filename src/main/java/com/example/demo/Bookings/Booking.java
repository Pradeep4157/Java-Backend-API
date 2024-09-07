package com.example.demo.Bookings;

import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

//@Entity
//@Table(name="booking")
@Document(value = "bookings")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@ToString
@Builder
public class Booking {
    @Id
    private Long bookingId;
    private Long customerId;
    private String carModel;
}
