#wap to login to phonepe by entering the correct otp
while True:
    otp=int(input("enter the otp"))
    if 1000<=otp<=9999:
        print("correct otp")
        break