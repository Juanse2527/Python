### Listas ###

my_lyst = list()
my_other_lyst =[]

print (len(my_lyst))

my_lyst = [35, 24, 62, 50, 30, 17, 30]

print ("---------------------------------")

print (my_lyst)
print (len(my_lyst))

print ("---------------------------------")

my_other_lyst = [23, 1.60, "Juan Sebastian", "Del Rio Layos"]

print(my_other_lyst)
print (type(my_other_lyst))

print ("---------------------------------")

print(my_other_lyst[2])
print(my_other_lyst[-1])
print(my_other_lyst[0])
# print(my_other_lyst [4])  error se sale del rango
print(my_lyst.count(30)) # Cuenta cuantos datos hay repetidos en una lista 

print(my_lyst + my_other_lyst)


print ("---------------------------------")


my_other_lyst.append("Sdelrio")
print(my_other_lyst)

my_other_lyst.insert(1,"Negro") # Inserta datos a la lista 
print(my_other_lyst)

my_other_lyst.remove("Negro")
print(my_other_lyst)
 

print ("---------------------------------")

print(my_other_lyst.pop())
print(my_other_lyst)
print(my_other_lyst.pop(2))

#pop quita un elemnto de la lista en especifico, y lo guarda no lo elimina 

my_pop= my_other_lyst.pop()
print(my_pop)

#.DEL sirve para eliminar por indice y remove sirve para eliminar por dato

del my_other_lyst[1]
#print(my_other_lyst)


print ("---------------------------------")
#Sirve para actualizar los valores de la lista 

#my_other_lyst[1]=24
#print(my_other_lyst)

print ("---------------------------------")
# copiar una lista
print("Lista copiada") 
my_new_list_copy = my_lyst.copy()
print(my_new_list_copy)

#darle la vuelta a la lista con reverse imprimiento los numero de adelante hacia atraz

my_lyst.reverse()
print(my_lyst)

# sort se usa para ordenar la lista 

my_lyst.sort()
print(my_lyst)



print ("---------------------------------")

### Tipos dinamicos 

my_lyst = "hola python"
print (my_lyst)
print (type(my_lyst))

### No se puede crear constantes ###

print ("---------------------------------")