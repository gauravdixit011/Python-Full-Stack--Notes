Here are 50 practical, real-world scenario-based questions using Python conditional statements:

## Banking & Finance Scenarios (Questions 1-10)

**1. ATM Withdrawal**
- Input Hint: Create variables `balance = 5000` and `withdraw = 4500`. Check if withdrawal amount is less than or equal to balance
- Output Hint: 
```
Withdrawal successful. Remaining balance: 500
```

**2. Minimum Balance Penalty**
- Input Hint: Create `account_balance = 800`. Minimum balance required is 1000. Check if account falls below minimum balance
- Output Hint: 
```
Warning: Maintain minimum balance of 1000. Current balance: 800
```

**3. Loan Eligibility**
- Input Hint: Create variables `salary = 35000`, `credit_score = 720`. Loan eligible if salary >= 30000 and credit_score >= 700
- Output Hint: 
```
Congratulations! You are eligible for loan
```

**4. Credit Card Approval**
- Input Hint: `age = 22`, `annual_income = 450000`. Approval criteria: age >= 21 and income >= 300000
- Output Hint: 
```
Credit card approved
```

**5. FD Maturity Calculator**
- Input Hint: `principal = 50000`, `years = 3`, `rate = 6.5`. Calculate and check if maturity amount > 60000
- Output Hint: 
```
Maturity amount: 59750. Target not achieved
```

**6. Tax Calculation**
- Input Hint: `income = 850000`. Tax slab: >10 lakh = 30%, 5-10 lakh = 20%, <5 lakh = 0%
- Output Hint: 
```
Tax payable: 70000
```

**7. UPI Transaction Limit**
- Input Hint: `transaction_amount = 95000`. Daily UPI limit is 100000. Check if transaction within limit
- Output Hint: 
```
Transaction processed successfully
```

**8. Fixed Deposit Renewal**
- Input Hint: `fd_amount = 25000`, `fd_status = "matured"`. Auto-renew if amount > 20000 and status is "matured"
- Output Hint: 
```
FD auto-renewed for 1 year
```

**9. Exchange Rate Check**
- Input Hint: `dollar_rate = 83.50`. If rate > 83, suggest to wait for USD selling
- Output Hint: 
```
Wait for better rate to sell USD
```

**10. EMI Calculation**
- Input Hint: `monthly_emi = 15000`, `monthly_salary = 45000`. EMI should not exceed 40% of salary
- Output Hint: 
```
EMI is within limit (33.33% of salary)
```

## E-commerce & Shopping Scenarios (Questions 11-20)

**11. Free Shipping Eligibility**
- Input Hint: `cart_total = 750`. Free shipping on orders above 500
- Output Hint: 
```
Congratulations! You get free shipping
```

**12. Coupon Code Validation**
- Input Hint: `coupon = "SAVE20"`, `cart_value = 1200`. Valid if coupon is "SAVE20" and cart >= 1000
- Output Hint: 
```
Coupon applied successfully. Discount: 240
```

**13. Product Stock Check**
- Input Hint: `product_stock = 3`, `requested_quantity = 5`. Check if enough stock available
- Output Hint: 
```
Sorry! Only 3 items available
```

**14. Member Discount**
- Input Hint: `is_member = True`, `purchase_amount = 2500`. Members get 10% off on purchases above 2000
- Output Hint: 
```
Member discount applied. Final amount: 2250
```

**15. Gift Card Balance**
- Input Hint: `gift_card_balance = 800`, `item_price = 1200`. Check if balance sufficient
- Output Hint: 
```
Insufficient balance. Need 400 more
```

**16. Return Policy Check**
- Input Hint: `days_since_purchase = 25`. Return accepted within 30 days
- Output Hint: 
```
Eligible for return
```

**17. Bulk Order Discount**
- Input Hint: `quantity = 15`. Discount: 5% on 10+ items, 10% on 20+ items
- Output Hint: 
```
5% discount applied
```

**18. Festival Sale Eligibility**
- Input Hint: `is_premium_member = False`, `sale_type = "early_access"`. Early access only for premium members
- Output Hint: 
```
Wait for public sale on Friday
```

**19. Cashback Offer**
- Input Hint: `payment_method = "credit_card"`, `amount = 3000`. 5% cashback on credit card payments above 2000
- Output Hint: 
```
Cashback earned: 150
```

**20. Exchange Offer**
- Input Hint: `old_product_value = 4000`, `new_product_price = 15000`. Exchange discount 20% of old product value
- Output Hint: 
```
Final price after exchange: 14200
```

## Healthcare & Fitness Scenarios (Questions 21-30)

**21. BMI Calculator**
- Input Hint: `weight = 75`, `height = 1.75`. Calculate BMI and categorize: <18.5 underweight, 18.5-25 normal, >25 overweight
- Output Hint: 
```
Your BMI is 24.5 (Normal weight)
```

**22. Blood Donation Eligibility**
- Input Hint: `age = 32`, `weight = 55`, `last_donated_months = 8`. Eligible if age 18-60, weight>50, last donated >6 months
- Output Hint: 
```
You can donate blood
```

**23. Fever Diagnosis**
- Input Hint: `temperature = 101.5`. Normal <98.6, Mild 98.6-100.4, High >100.4
- Output Hint: 
```
High fever. Consult doctor immediately
```

**24. Medicine Dosage**
- Input Hint: `patient_age = 8`, `medicine_strength = "250mg"`. Children under 12 get half dose
- Output Hint: 
```
Recommended dose: 125mg
```

**25. Gym Membership Renewal**
- Input Hint: `membership_expired = True`, `pending_dues = 0`. Renew if expired and no pending dues
- Output Hint: 
```
Membership renewed successfully
```

**26. Calorie Intake Check**
- Input Hint: `daily_calories = 2200`, `goal_calories = 2000`. Warn if exceeded
- Output Hint: 
```
Warning: You've exceeded daily calorie limit by 200
```

**27. Vaccination Eligibility**
- Input Hint: `child_age_months = 14`, `vaccine_due = "MMR"`. MMR vaccine due at 12-15 months
- Output Hint: 
```
MMR vaccine is due
```

**28. Heart Rate Monitor**
- Input Hint: `resting_heart_rate = 82`. Normal range 60-100 bpm
- Output Hint: 
```
Heart rate is normal
```

**29. Sleep Tracker**
- Input Hint: `sleep_hours = 5`. Recommended: adults 7-9 hours
- Output Hint: 
```
Insufficient sleep. Aim for 7-9 hours
```

**30. Health Insurance Premium**
- Input Hint: `age = 45`, `smoker = False`. Premium: <30 = 5000, 30-50 = 8000, >50 = 12000, smokers +2000
- Output Hint: 
```
Your premium: 8000
```

## Transportation & Travel Scenarios (Questions 31-40)

**31. Metro Fare Calculator**
- Input Hint: `distance_km = 12`. Fare: 0-5km = 10, 5-10km = 20, 10-15km = 30, >15km = 40
- Output Hint: 
```
Metro fare: 30
```

**32. Flight Check-in**
- Input Hint: `hours_before_departure = 2`. Online check-in available 48 hours to 60 minutes before departure
- Output Hint: 
```
Check-in successful
```

**33. Driving License Eligibility**
- Input Hint: `applicant_age = 17`. Minimum age for license: 18
- Output Hint: 
```
Not eligible. Need to wait 1 more year
```

**34. Cab Surge Pricing**
- Input Hint: `demand_level = "high"`, `base_fare = 150`. Surge price 1.5x if demand is high
- Output Hint: 
```
Current fare with surge: 225
```

**35. Parking Fee Calculator**
- Input Hint: `parking_hours = 4`. Rate: First 2 hours = 20/hour, after that = 30/hour
- Output Hint: 
```
Total parking fee: 100
```

**36. Train Ticket Confirmation**
- Input Hint: `available_seats = 5`, `passengers = 3`. Check if seats available
- Output Hint: 
```
Tickets confirmed for 3 passengers
```

**37. Fuel Efficiency Check**
- Input Hint: `mileage = 14`, `fuel_type = "petrol"`. Warning if mileage <15 for petrol cars
- Output Hint: 
```
Low fuel efficiency. Service recommended
```

**38. Luggage Weight Check**
- Input Hint: `luggage_weight = 23`, `flight_class = "economy"`. Economy limit 20kg, Business 30kg
- Output Hint: 
```
Excess baggage fee applicable: 3000
```

**39. Toll Tax Calculation**
- Input Hint: `vehicle_type = "car"`, `round_trip = True`. Car toll 100, round trip 150
- Output Hint: 
```
Toll amount: 150
```

**40. Speed Fine Calculator**
- Input Hint: `speed = 85`, `speed_limit = 70`. Fine: 1000 for 1-20km over limit, 2000 for >20km over
- Output Hint: 
```
Fine: 1000 for overspeeding
```

## Education & Employment Scenarios (Questions 41-50)

**41. Scholarship Eligibility**
- Input Hint: `marks_percentage = 92`, `family_income = 400000`. Scholarship if marks>90 or income<300000
- Output Hint: 
```
Eligible for merit scholarship
```

**42. Exam Result Declaration**
- Input Hint: `physics = 75`, `chemistry = 68`, `math = 82`. Pass if all subjects >=40
- Output Hint: 
```
Result: PASS with 75% aggregate
```

**43. Job Application Filter**
- Input Hint: `experience_years = 3`, `skills = ["python", "sql", "java"]`. Job requires 2+ years and Python
- Output Hint: 
```
Profile shortlisted for interview
```

**44. Attendance Shortage Warning**
- Input Hint: `attendance_percentage = 72`. Minimum required attendance: 75%
- Output Hint: 
```
Warning: Attendance shortage (3% required)
```

**45. Salary Hike Calculation**
- Input Hint: `current_salary = 50000`, `performance_rating = 4.5`. Hike: 5% for rating 3-4, 10% for 4-5, 15% for 5
- Output Hint: 
```
New salary after 10% hike: 55000
```

**46. Course Prerequisite Check**
- Input Hint: `completed_courses = ["python", "sql"]`, `prerequisites = ["python", "database"]`. Check if eligible for advanced course
- Output Hint: 
```
Missing prerequisite: database. Cannot enroll
```

**47. Leave Approval System**
- Input Hint: `leave_days_requested = 5`, `leave_balance = 8`, `project_deadline = False`. Approved if balance sufficient and no deadline
- Output Hint: 
```
Leave approved. Remaining balance: 3
```

**48. Overtime Pay Calculation**
- Input Hint: `hours_worked = 50`, `hourly_rate = 500`. Regular 40 hours, overtime 1.5x rate
- Output Hint: 
```
Total pay: 27500 (Regular: 20000, Overtime: 7500)
```

**49. Internship Stipend**
- Input Hint: `internship_duration_months = 3`, `performance = "excellent"`. Stipend: 10000/month, excellent performance gets 20% bonus
- Output Hint: 
```
Total stipend with bonus: 36000
```

**50. Retirement Planning**
- Input Hint: `current_age = 45`, `retirement_age = 60`, `current_savings = 2500000`. Target retirement corpus 1 crore. Check if on track
- Output Hint: 
```
Need to save more. Current projection: 7500000
```