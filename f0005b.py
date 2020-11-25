jelszo = "jelszo1234"
b=0
i=0
while i<10:
  a = input("jelszó: ", read=password)
  if jelszo==a:
    i=10
    b=1
  i=i+1
  if b==0:
    print(f"márcsak {10-i} probálkozása van")

if b==1:
  print("jelszó elfogadva")
else:
  print("jelszó megtagadva")    