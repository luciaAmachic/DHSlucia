#Si la clave no existe en el diccionario, se lanzará un error. 
# Para evitar este error, podemos utilizar el método get():
estudiantes = {'Juan': 16, 'Ana': 18, 'Luis': 17}
print(estudiantes.get('Maria', 'No existe')) # 'No existe'
