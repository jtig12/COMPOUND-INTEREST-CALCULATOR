# COMPOUND INTEREST CALCULATOR

### DESCRIPTION

    This app is used to calculate compound interest.

### Steps taken to develop the project

---

1. we first set all the parameters to zero.
2. Then we write a loop function where users can put in certain numbers for each parameters in which will be calculated.

   ```py
       while principal_balance <= 0:
           principal_balance = float(input("Enter initial principal balance: "))
           if principal_balance <= 0:
               print("Principle can't be less than or equal to zero")

       while rate <= 0:
           rate = float(input("Interest rate%: "))
           if rate <= 0:
               print("rate can't be less than or equal to zero")

       while time <= 0:
           time = int(input("Enter number of time periods elapsed: "))
           if time <= 0:
               print("time can't be less than or equal to zero")
   ```

3. Then we write codes used in calculating compound interest and then display it.
   ```py
     total = (principal_balance * (1 + (rate/100)) ** (time))
     print(f"Balance after {time} year/s: ${total:.2f}")
   ```

## OUTCOME EXECUTION

![alt text](<compoud interest .png>)
