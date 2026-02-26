# python compound interest calculator

principal_balance = 0
rate = 0
time = 0

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
total = (principal_balance * (1 + (rate/100)) ** (time))
print(f"Balance after {time} year/s: ${total:.2f}")
