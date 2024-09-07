package com.example.demo.Purchase;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/purchases")
public class PurchaseController {
    @Autowired
    PurchaseRepo purchaserepo;
    @GetMapping("/")
    public ResponseEntity<List<Purchase>> allPurchases(){
        try{
            List<Purchase> purchases = new ArrayList<>();
            purchaserepo.findAll().forEach(purchases ::add);
            if(purchases .isEmpty()){
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }
            return new ResponseEntity<>(purchases ,HttpStatus.OK);
        }
        catch (Exception ex){
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    @PostMapping("/makepurchase")
    public ResponseEntity<Purchase> newPurchase(@RequestBody Purchase purchase){
        Optional<Purchase> findpurchase = purchaserepo.findById(purchase.getPurchaseID());
        if(findpurchase.isPresent()){
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }
        Purchase obj = purchaserepo.save(purchase);
        return new ResponseEntity<>(obj,HttpStatus.CREATED);
    }
    @DeleteMapping("/deletepurchase/{purchaseid}")
    public ResponseEntity<Purchase> deletePurchase(@PathVariable Long purchaseid){
        try {
            purchaserepo.deleteById(purchaseid);
            return new ResponseEntity<>(HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    @GetMapping("/findpurchase/{purchaseid}")
    public ResponseEntity<Purchase> findPurchase(@PathVariable Long purchaseid){
        Optional<Purchase> findpurchase = purchaserepo.findById(purchaseid);
        if (findpurchase.isPresent()) {
            return new ResponseEntity<>(findpurchase.get(), HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
}
