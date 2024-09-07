package com.example.demo.Cars;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/cars")
public class CarController {
    @Autowired
    CarRepo carrepo;
    @GetMapping("/")
    public ResponseEntity<List<Car>> allCars(){
        try{
            List<Car> cars = new ArrayList<>();
            carrepo.findAll().forEach(cars::add);
            if(cars.isEmpty()){
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }
            return new ResponseEntity<>(cars,HttpStatus.OK);
        }
        catch (Exception ex){
            System.out.println(ex.getMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    @PostMapping("/addcar")
    public ResponseEntity<Car> addCar(@RequestBody Car newcar){
        try{
            Car carObj = carrepo.save(newcar);
            return new ResponseEntity<>(carObj, HttpStatus.CREATED);
        }catch(Exception e){
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    @DeleteMapping("/removecar/{carid}")
    public ResponseEntity<HttpStatus> removeCar(@PathVariable Long carid){
        try {
            carrepo.deleteById(carid);
            return new ResponseEntity<>(HttpStatus.OK);
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    @PostMapping("/updatecar/{carid}")
    public ResponseEntity<Car> updateCar(@PathVariable Long carid, @RequestBody Car changedcar){
        try {
            Optional<Car> cardata = carrepo.findById(carid);
            if (cardata.isPresent()) {
                Car updatedcarData = cardata.get();
                updatedcarData.setCarId(changedcar.getCarId());
                updatedcarData.setCarModel(changedcar.getCarModel());
                updatedcarData.setCarManufacturer(changedcar.getCarManufacturer());
                updatedcarData.setQuotedPrice(changedcar.getQuotedPrice());
                updatedcarData.setInsuranceProvider(changedcar.getInsuranceProvider());
                updatedcarData.setManufactureYear(changedcar.getManufactureYear());

                Car carObj = carrepo.save(updatedcarData);
                return new ResponseEntity<>(carObj, HttpStatus.CREATED);
            }
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
            } catch (Exception e) {
                return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
    }
    // search car by id
    @GetMapping("/searchcar/{carid}")
    public ResponseEntity<Car> searchCar(@PathVariable Long carid){
        Optional<Car> carObj = carrepo.findById(carid);
        if (carObj.isPresent()) {
            return new ResponseEntity<>(carObj.get(), HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
}
