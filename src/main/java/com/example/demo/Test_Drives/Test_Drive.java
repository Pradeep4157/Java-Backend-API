package com.example.demo.Test_Drives;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;
//@Entity
@Document("testdrives")
//@Table(name="testdrives")
@Setter
@Getter
@AllArgsConstructor
@NoArgsConstructor
public class Test_Drive {
    @Id
    private Long appointmentId;
    private Long customerId;
    private Long carId;
    private LocalDateTime dateTime;
}
