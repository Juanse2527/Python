### strings ###
my_string = "Mi estring"
my_other_string = "Mi otro string "

print("------------------------------------------------------------")

print(len(my_string))
print(len(my_other_string))

print("------------------------------------------------------------")

print (my_string + " " + my_other_string)

print("------------------------------------------------------------")

my_new_line_string = "Este es un string \nCon un salto de linea "
print(my_new_line_string)

print("------------------------------------------------------------")

my_new_tab_string = "\tEste es un string con tabulacion "
print(my_new_tab_string)

print("------------------------------------------------------------")

### Formateo ###

name, last_name, age = "Juan Sebastian", "Del Rio Layos", 23

print("Mi nombres es {} {} y tengo {} años".format(name, last_name, age))

print("Mi nombre es %s %s y tengo %d años" %(name, last_name, age))

print(f"Mi nombre es {name} {last_name} y tengo {age} años")

print("------------------------------------------------------------")

### Desempaquetado de caracteres ###

lenguage = "python"
a, b, c, d, e, f = lenguage
print(f, e, d, c, b, a )

print("------------------------------------------------------------")

### Funciones ###

print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.count("t"))
print(lenguage.isnumeric())
print("10".isnumeric())
print(lenguage.lower())
print(lenguage.isnumeric())

print("------------------------------------------------------------")