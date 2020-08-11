amount = int(input())
init_balance = int(input())

while amount % 5 == 0 :
    if amount + 0.5 < init_balance:
        print(init_balance-amount-0.5)
        break