with open("texto.txt") as file_object:
    texto = file_object.read()

cantidad_letras = len(texto.replace(' ',''))
cantidad_espacios = texto.count(' ')

print("La cantidad de letras que tiene el texto son",cantidad_letras)
print("La cantidad de espacios que tiene el texto son",cantidad_espacios)

with open("cantidad.txt","w") as file:
    file.write("La cantidad de letras que tiene el texto son: {}\n".format(cantidad_letras))
    file.write("La cantidad de espacios que tiene el texto son: {}".format(cantidad_espacios))
    