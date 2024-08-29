### Tuplas ###

my_tuple = tuple()
my_other_tupla = ()

my_tuple = (23, 1.60, "Juan Sebastian", "Del rio layos")
print(my_tuple)
print(type(my_tuple))

my_other_tupla = (23, 30, 65)

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) Este es error 
# print(my_tuple[-6]) Este es un  error 

# Operaciones con tuplas 

#Contador count

print(my_tuple.count("Del rio layos"))

# Nos dice donde esta el indice en especifico, deacuerdo con el dato que le pasemos 

print(my_tuple.index("Juan Sebastian"))

# Hay dos operaciones index y couut
# Los valores de las tuplas son inmutables a diferencia de las listas que si se dejan mutar 

my_sum_tuble = my_tuple + my_other_tupla
print(my_sum_tuble)

print(my_sum_tuble[3:6])


#CAmbiar la tubla a lista

my_tuple = list(my_tuple)
print(type(my_tuple))


