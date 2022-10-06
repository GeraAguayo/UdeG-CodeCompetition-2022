print('Escribe la primer secuencia de ADN: ')
secuencia1 = input()
secuencia1 = secuencia1.swapcase()
arraySec1 = []

for i in secuencia1:
    arraySec1.append(i)


print('Escribe la segunda secuencia: ')
secuencia2 = input()
secuencia2 = secuencia2.swapcase()
arraySec2 = []

for i in secuencia2:
    arraySec2.append(i)

j = 0
coincidencia1 = ""
coincidencia2 = ""
coincidencia3 = ""
coincidencia4 = ""
coincidencia5 = ""
print('La coincidencia es: ')
while j < 13:
    if(arraySec1[j] == arraySec2[j]):
        print(arraySec1[j])
       
        if coincidencia1 == "":
             coincidencia1 = coincidencia1 + arraySec1[j]
        elif coincidencia1 != "":
             coincidencia2 = coincidencia2 + arraySec1[j]
        elif coincidencia2 != "":
             coincidencia3 = coincidencia3 + arraySec1[j]
        elif coincidencia3 != "":
             coincidencia4 = coincidencia4 + arraySec1[j]
        elif coincidencia4 != "":
             coincidencia5 = coincidencia5 + arraySec1[j]
             
        else:
         pass
    j +=1
if len(coincidencia1) > len(coincidencia2) and len(coincidencia1) > len(coincidencia3) and len(coincidencia1) > len(coincidencia4) and len(coincidencia1) > len(coincidencia5):
    print('La coincidencia mas grannde fue '+ coincidencia1)
elif len(coincidencia2) > len(coincidencia1) and len(coincidencia2) > len(coincidencia3) and len(coincidencia2) > len(coincidencia4) and len(coincidencia2) > len(coincidencia5):
     print('La coincidencia mas grannde fue '+ coincidencia2)
elif len(coincidencia3) > len(coincidencia1) and len(coincidencia3) > len(coincidencia2) and len(coincidencia3) > len(coincidencia4) and len(coincidencia3) > len(coincidencia5):
     print('La coincidencia mas grannde fue '+ coincidencia2)
elif len(coincidencia4) > len(coincidencia1) and len(coincidencia4) > len(coincidencia3) and len(coincidencia4) > len(coincidencia1) and len(coincidencia4) > len(coincidencia5):
     print('La coincidencia mas grannde fue '+ coincidencia1)
elif len(coincidencia5) > len(coincidencia1) and len(coincidencia5) > len(coincidencia3) and len(coincidencia5) > len(coincidencia4) and len(coincidencia5) > len(coincidencia2):
     print('La coincidencia mas grannde fue '+ coincidencia1)
        


