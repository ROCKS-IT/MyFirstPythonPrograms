jour = int(input("donne jour:"))
heure = int(input("donne heure:"))
minute = int(input("donne minute:"))

if jour > 31 or jour < 0:
             print("recommence:")
             jour = int(input("donne jour:"))

if heure > 24 or heure < 0:
             print("recommence:")
             heure = int(input("donne heure:"))

if minute > 60 or heure < 0:
             print("recommence:")
             minute = int(input("donne minute:"))
             
            
print(minute+(heure*60)+(jour*1440))
