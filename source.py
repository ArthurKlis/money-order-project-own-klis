# version 1.x
# 2024-02-10
i=1
listaJednosci=[]
listaCzesciDziesietnych=[]
sumaJednosci=0
sumaCzesciDziesietnych=0
while i:
 liczba=input(': ')
 if liczba != "" and liczba != "exit": 
  listaJednosci.append(int(liczba.split(",")[0]))
  listaCzesciDziesietnych.append(int(liczba.split(",")[1]))
 elif liczba == "exit":
  break
 else:
  break
nominalyJednosci = {'100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0}
nominalyCzesciDziesietnej={'50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0}
for liczba in listaJednosci:
 for key in nominalyJednosci.keys():
  if liczba >= int(key):
   nominalyJednosci[key] += int(liczba//int(key))
   liczba %= int(key)
for liczba in listaCzesciDziesietnych:
 for key in nominalyCzesciDziesietnej.keys():
  if liczba >= int(key):
   nominalyCzesciDziesietnej[key] += int(liczba//int(key))
   liczba %= int(key)
print('') #dodanie by się ładnie wyświetlało w aplikacji iPhone-a
for k, v in nominalyJednosci.items(): print(k, v)
for k, v in nominalyCzesciDziesietnej.items():
 if len(k)==1:
  k='0.0'+k
 else:
  k='0.'+k
 print(k,v)
for jednosc in listaJednosci:
 sumaJednosci+=jednosc
for czescDziesietna in listaCzesciDziesietnych:
 sumaCzesciDziesietnych+=czescDziesietna
calosciZdziesietnych=sumaCzesciDziesietnych//100
sumaCzesciDziesietnych=sumaCzesciDziesietnych-calosciZdziesietnych*100
sumaJednosci=sumaJednosci+calosciZdziesietnych
print('suma kwot:', str(sumaJednosci)+','+str(sumaCzesciDziesietnych))
