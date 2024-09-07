API paths :
1. http://localhost:5000 - *base
2. http://localhost:5000/bookings/
3. http://localhost:5000/bookings/deleteBooking/{bookingId}
4. http://localhost:5000/bookings/createBooking
5. http://localhost:5000/cars/
6. http://localhost:5000/cars/addcar
7. http://localhost:5000/removecar/{carid}
8. http://localhost:5000/updatecar/{carid}
9. http://localhost:5000/searchcar/{carid}
10. http://localhost:5000/inventory/
11. http://localhost:5000/inventory/add/{carmodel}
12. http://localhost:5000/inventory/remove/{carmodel}
13. http://localhost:5000/inventory/checkavailable/{carmodel}
14. http://localhost:5000/payments/makepayment/{mode}
15. http://localhost:5000/payments/processpayment/{paymentid}
16. http://localhost:5000/purchases/
17. http://localhost:5000/purchases/makepurchase
18. http://localhost:5000/purchases/deletepurchase/{purchaseid}
19. http://localhost:5000/findpurchase/{purchaseid}
20. http://localhost:5000/servicerequest/{function}/service/{appointmentid}
21. http://localhost:5000/servicerequest/newappointment
22. http://localhost:5000/servicerequest/deleteappointment/{appointmentid}
23. http://localhost:5000/servicerequest/getappointment/{appointmentid}
24. http://localhost:5000/testdrives/
25. http://localhost:5000/testdrives/scheduleTestDrive
26. http://localhost:5000/testdrives/clearTestDrive
27. http://localhost:5000/testdrives/getTestDrives
28. http://localhost:5000/engineer/appointments/{appointmentId}/estimateCost
29. http://localhost:5000/engineer/appointments/{appointmentId}/updateProgress

UIs
1. Customer - Vamsheel
   1. [X]View Cars Catalog
   2. [X]Schedule Testdrive
   3. [X]Buy Cars - (adds to Purchase)
   4. [X]Schedule Service Appointment
   5. Make Payment
2. Salesperson
   1. [X]Manage Catalog - ME
   2. [X]Manage Inventory - SAH
   3. [X]Assist Customer - ME
      <!-- 1. View Cars - SAH -->
      1. [X]Check Availability - SAH
      2. [X]Make Booking - SAH
   4. [X]Process Payment - ME
3. Engg - Pradeep
   1. []Requests Dashboard
   2. []provide Cost Estimate
   3. []Update Progress
   4. []Alert Pickup
