package com.example.demo.Inventory;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
// SINGLETON CREATIONAL can be used
@RestController
@RequestMapping("/inventory")
public class InventoryController {
    @Autowired
    private InventoryRepo inventoryrepo;
    public List<Inventory> findCarsByModel(String carmodel) {
        return inventoryrepo.findBycarModel(carmodel);
    }
    @GetMapping("/")
    public ResponseEntity<List<Inventory>> allInventory(){
        try{
            List<Inventory> inventorys = new ArrayList<>();
            inventoryrepo.findAll().forEach(inventorys::add);
            if(inventorys.isEmpty()){
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }
            return new ResponseEntity<>(inventorys,HttpStatus.OK);
        }
        catch (Exception ex){
            System.out.println(ex.getMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    @PostMapping("/add/{carmodel}")
    public ResponseEntity<Inventory> addItem(@PathVariable String carmodel){
        try {
            List<Inventory> inventoryData = findCarsByModel(carmodel);
            if (!inventoryData.isEmpty()) {
                Inventory updatedinvData = inventoryData.get(0);
                updatedinvData.setUnits((updatedinvData.getUnits() + 1));
                Inventory invObj = inventoryrepo.save(updatedinvData);
                return new ResponseEntity<>(invObj, HttpStatus.CREATED);
            }
            else {
                Inventory inv = new Inventory();
                inv.setUnits(1);
                inv.setCarModel(carmodel);
                Inventory invObj = inventoryrepo.save(inv);
                return new ResponseEntity<>(invObj, HttpStatus.CREATED);
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    @PostMapping("/remove/{carmodel}")
    public ResponseEntity<Inventory> removeItem(@PathVariable String carmodel){
        try {
            List<Inventory> inventoryData = findCarsByModel(carmodel);
            if (!inventoryData.isEmpty()) {
                Inventory updatedinvData = inventoryData.get(0);
                updatedinvData.setUnits((updatedinvData.getUnits() - 1));
                Inventory invObj = inventoryrepo.save(updatedinvData);
                // if #units<0 remove from repo
                if(updatedinvData.getUnits()<0){
                    inventoryrepo.delete(updatedinvData);
                    return new ResponseEntity<>(HttpStatus.ACCEPTED);
                }
                return new ResponseEntity<>(invObj, HttpStatus.CREATED);
            }
            else {
                return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
            }
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    @GetMapping("/checkavailable/{carmodel}")
    public ResponseEntity<Inventory> checkAvailability(@PathVariable String carmodel){
        try{
            List<Inventory> inventoryData = findCarsByModel(carmodel);
            if (!inventoryData.isEmpty()) {
                Inventory invObj = inventoryData.get(0);
                return new ResponseEntity<>(invObj, HttpStatus.OK);
            }
            else return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
