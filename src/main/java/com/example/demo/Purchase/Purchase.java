package com.example.demo.Purchase;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;

//@Entity
//@Table(name="purchases")
@Document("purchases")
@Setter
@Getter
@NoArgsConstructor
@AllArgsConstructor
public class Purchase {
        @Id
        private Long purchaseID;
        private Long carId;
        private Long customerId;
        private Long paymentId;
        private LocalDateTime purchaseDate;
}
