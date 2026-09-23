print("\t\t\tWelcome")
#back end codenn  
pin=8888
balance=10000
def withdraw_amount():
    print("\t\t\tINSERT YOUR ATM CARD...........")
    check_pin=int(input("\t\t\tENTER YOUR PIN NUMBER:"))
    if check_pin==pin:
        w_amount=int(input("\t\t\tENTER THE AMOUNT TO BE WITHDRAW:") )   
        if w_amount<=balance:
            print("\t\t\tYOUR TRANSACTION IS GOING ON........... ")
            print("\t\t\tCASH WITHDRAW SUCCESSFULL........")
            balance_check=input("\t\t\tDO YOU WANT TO KNOW YOUR BALANCE(Y/N)..........")
            balance_check.upper()
            if balance_check=="y":
                print("\t\t\tYOUR BALANCE............")
                print(balance-w_amount)           
def deposit_amount():
    print("\t\t\tINSERT YOUR ATM CARD.............")
    check_pin=int(input("\t\t\tENTER YOUR PIN NUMBER:"))
    if check_pin==pin:
        d_amount=int(input("\t\t\tENTER THE AMOUNT TO BE DEPOSITED:"))
        balance+=d_amount
        balance_check=input("\t\t\tDO YOU WANT TO KNOW YOUR BALANCE(Y/N)........")
        balance_check.upper()
        if balance_check=="Y":
            print("\t\t\tYOUR BALENCE.........")
            print(balance)
def balance_amount():
    print("\t\t\tINSERT YOUR ATM CARD..........")
    check_pin=int(input("\t\t\tENTER YOUR PIN:"))
    if check_pin==pin:
        print("\t\t\tYOUR BALANCE............")            
        print(balance)
# front end code
op="Y"
while op=="Y":
    print("1.Withdraw Amount")
    print("2.Deposit Amount")
    print("3.Balance Check")
    a=int(input("\t\t\tENTER YOUR OPTION:"))
    if a==1:
        print(withdraw_amount())
    elif a==2:
        print(deposit_amount())
    elif a==3:
        print(balance_amount())
    else:
        print("\t\t\tINVALIED OPTION.....") 
    print("WRONG PIN.........")       
    op=input("\t\t\tDO YOU WANT TO DO AGAIN(Y/N):")






