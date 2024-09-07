package com.example.demo.Services;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.annotation.Id;

@Setter
@Getter
@NoArgsConstructor
@AllArgsConstructor
//USE FACTORY
public class Services {
    @Id
    private ServiceType serviceType;
    private float cost;
    private String Description;
}
