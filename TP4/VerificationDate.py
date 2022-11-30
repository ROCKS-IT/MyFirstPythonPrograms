date = str(input("entrer le date dans l'ordre JJMMAAAA: "))

if len(date) == 8:
    J = int(date[0] + date[1])
    M = int(date[2] + date[3])
    A = int(date[4] + date[5] + date[6] + date[7])

    if 0 < A < 9999:
        if M == 1 or M == 3 or M == 5 or M == 7 or M == 10 or M == 12:
            if J >= 1 and J <= 31:
                print("Date correct ")
            else:
                print("Date incorrecte")
        elif M == 2:
            if (A % 4 == 0 and A % 100 != 0) or (A % 400 == 0):
                if J >= 1 and J <= 29:
                    print("Date correcte ")
                else:
                    print("date incorrect")
            else:
                if J >= 1 and J <= 28:
                    print("Date correcte ")
                else:
                    print("date incorrecte")
        elif M == 4 or M == 6 or M == 8 or M == 9 or M == 11:
            if J >= 1 and J <= 30:
                print("Date correcte ")
            else:
                print("date incorecte")
        else:
            print("date incorrecte ")

    else:
        print("date incorrecte ")
    
else:
    print("date incorect")


