# Convertir grados decimales (DD) a grados minutos segundos (DMS)
import tkinter			# Esta es mi primera vez usando tkinter, seguramente sin darme cuenta hare cosas innecesarias en muchas ocasiones que puenden ser quitadas u optimizadas para un código limpio
from tkinter import *	# import * nos importa todos los atributos de tkinter de este modo no tendremos que importarlo uno por uno o tener que indicar "tkinter.atributoTal"
						# De tkinter salen elementos como Label, Button, Entry (TextBox). tkinter.Label seria la sintaxis para indicar que Label esta siendo llamado de la libreria tkinter que es la que nos permite optener atributos de una interfaz gráfica

#Funciones globales
"""
def validarEntrada(tecla):	# Aqui estamos creando una función que mediante la variable tecla revisa los datos ingresados al textbox
	if tecla.isdigit():		# isdigit verifica que el dato ingresado sea un digito (teclas 0, 1, 2, 3 etc.)
		return True			# cuando la condición se cumple retornara un True que en las propiedades del textbox sera leido para saber si debe dejar o no el ingreso de un valor; True = si, Falce = No
	elif tecla == ".":		# isdigit solo ingresa numeros, necesitamos el ingreso del punto para contar con datos decimales. Algunos países usan una coma pero creo que igual no es recomendable dado que las máquinas reconocen el punto
		return True			
	else:					# Cualquier otro caso es retornado como falso y esto inavilita el ingreso de letras entre otros no deseados
		return False
					### El código es medianamente funcional, pues no evita el ingreso de multiples puntos lo cual impide al dato ser tomado como un número, así que se desea resolver el como validar que el textbox contenga a lo mucho un único punto
"""
def validarSoloNumeros(tecla):	# Nuestro función solo permite el ingreso de números, ni siquiera deja pasar texto copiados a no ser que sean números enteros
	return tecla.isdecimal()



ventana = Tk()
ventana.title("Conversor de coordenadas por Darwin Méndez")
#ventana.geometry("360x360") # geometry nos permite especificar las dimensiones de una ventana aquí declarada como "ventana". Posdata: Como programador tu tabla sagrada debe ser la del 8 y tener en cuenta multiplos de 8

#Labels Cabecera
Label(ventana, text = "CONVERSOR DE COORDENADAS"
	).grid(row = 0, column = 0, columnspan = 9, padx = 8, pady = 8) # grid es un atributo de tkinter que nos permite aliner elementos mediante una grilla/matriz


Label(ventana, text = "Grados decimales"
	).grid(row = 1, column = 1, columnspan = 2, padx = 8, pady = 8) # Los elementos de la grilla inician en la posición 0 luego 1, 2...


Label(ventana, text = "Grados"
	).grid(row = 1, column = 3, columnspan = 2, padx = 8, pady = 8)	# columnspan indica cuantas columnas ocupa el elemento o cuantas columnas hay por encima y/o debajo

Label(ventana, text = "Minutos"
	).grid(row = 1, column = 5, columnspan = 2, padx = 8, pady = 8)	# En estos casos estamos haciendo que un rótulo/Label este por encima de 2 elementos, una caja de texto y otro rotulo para un signo (°, ', ")

Label(ventana, text = "Segundos"
	).grid(row = 1, column = 7, columnspan = 2, padx = 8, pady = 8) # padx & pady nos permiten crear un espacio en pixeles, creo, entre los elementos 


#Labels Laterales
Label(ventana, text = "Latitud:"
	).grid(row = 2, column = 0, padx = 8, pady = 8)

tkinter.Label(ventana, text = "Longitud:"
	).grid(row = 3, column = 0, padx = 8, pady = 8)


#Labels signos
Label(ventana, text = "°").grid(row = 2, column = 2, pady = 8)
Label(ventana, text = "°").grid(row = 3, column = 2, pady = 8)

Label(ventana, text = "°").grid(row = 2, column = 4, pady = 8)
Label(ventana, text = "°").grid(row = 3, column = 4, pady = 8)

Label(ventana, text = "'").grid(row = 2, column = 6, pady = 8)
Label(ventana, text = "'").grid(row = 3, column = 6, pady = 8)

Label(ventana, text = '"').grid(row = 2, column = 8, pady = 8)
Label(ventana, text = '"').grid(row = 3, column = 8, pady = 8)


#Entradas/Salidas
textLatitudDD = Entry(ventana, width = 14, justify = RIGHT, 
#validate = "key",	# DD = Decimal Degrees
	#validatecommand = (ventana.register(validarEntrada),"%S")
	)					# validatecommnad nos ayuda a optener nuestra función "validarEntrada", register es el registro del ingreso,... 
textLatitudDD.grid(row = 2, column = 1, pady = 8)								# ...luego llama a la función y si el valor de retorno es verdadero "%$" deja pasar el ingreso del teclado

textLongitudDD = Entry(ventana, width = 14, justify = RIGHT, 
#validate = "key",	# DD = Decimal Degrees
	#validatecommand = (ventana.register(validarEntrada),"%S")
	)
textLongitudDD.grid(row = 3, column = 1, pady = 8)



textLatitudGrados = Entry(ventana, width = 6, justify = RIGHT, validate = "key",
	validatecommand = (ventana.register(validarSoloNumeros),"%S"))
textLatitudGrados.grid(row = 2, column = 3, pady = 8)

textLongitudGrados = Entry(ventana, width = 6, justify = RIGHT, validate = "key",
	validatecommand = (ventana.register(validarSoloNumeros),"%S"))
textLongitudGrados.grid(row = 3, column = 3, pady = 8)


textLatitudMinutos = Entry(ventana, width = 6, justify = RIGHT, validate = "key",
	validatecommand = (ventana.register(validarSoloNumeros),"%S"))
textLatitudMinutos.grid(row = 2, column = 5, pady = 8)

textLongitudMinutos = Entry(ventana, width = 6, justify = RIGHT, validate = "key",
	validatecommand = (ventana.register(validarSoloNumeros),"%S"))
textLongitudMinutos.grid(row = 3, column = 5, pady = 8)


textLatitudSegundos = Entry(ventana, width = 6, justify = RIGHT, validate = "key",
	validatecommand = (ventana.register(validarSoloNumeros),"%S"))
textLatitudSegundos.grid(row = 2, column = 7, pady = 8)

textLongitudSegundos = Entry(ventana, width = 6, justify = RIGHT, validate = "key",
	validatecommand = (ventana.register(validarSoloNumeros),"%S"))
textLongitudSegundos.grid(row = 3, column = 7, pady = 8)


#Funciones locales
def convertirDDaDMS():
	latitudDD = float(textLatitudDD.get())					# Optenemos los datos del textbox y los convertimos en un valor flotante
	latitudGrados = int(latitudDD)							# Empleamos int para obtener la parte emtera de los grados
	latitudMinutosD = 60*(latitudDD - latitudGrados)		# Restando la parte entera de los grados nos quedamos con los decimales, por simplificación de la conversión de decimales a minutos multiplicamos por 60
	latitudMinutos = int(latitudMinutosD)					# Nuevamente con el int obtendremos la parte entera
	latitudSegundos = 60*(latitudMinutosD - latitudMinutos)	# El proceso es el mismo que con minutos
	textLatitudGrados.insert(0, latitudGrados)				# Inserta el valor entero de los grados en el textbox de grados
	textLatitudMinutos.insert(0, latitudMinutos)			# Inserta el valor entero de los minituos en el textbox de minutos
	textLatitudSegundos.insert(0, round(latitudSegundos))	# round nos redondea los segundos, como python usa variables dinamicas latitudSegundos contiene decimales
	# Lo siguiente es un copy paste cambiando latiud por longitud
	longitudDD = float(textLongitudDD.get())				# DD = Decimal Degrees
	longitudGrados = int(longitudDD)
	longitudMinutosD = 60*(longitudDD - longitudGrados)		# MinutosD = Minutos Decimales 
	longitudMinutos = int(longitudMinutosD)
	longitudSegundos = 60*(longitudMinutosD - longitudMinutos)	# Como estamos sacando solamente los decimales omitimos la parte de multiplicarlos por 100 porque luego encontrar un división entre 100, esta en la razón de multiplicar directamente por 60
	textLongitudGrados.insert(0, longitudGrados)
	textLongitudMinutos.insert(0, longitudMinutos)
	textLongitudSegundos.insert(0, round(longitudSegundos))	# Se tiene la opción de usar; round(longitudSegundos, n) que nos permitirá redonder en la posición decimal n que le indiquemos, esto si se desea contar con gran presición

def limpiar():							### Hay que ajustar la función dado que no limpia los textbox si contienen un punto en su contenido, posiblemente porque no estoy transformando el contenido del texbox en un tipo de dato especifico
	textLatitudDD.delete(0, END)
	textLatitudGrados.delete(0, END)
	textLatitudMinutos.delete(0, END)
	textLatitudSegundos.delete(0, END)
	textLongitudDD.delete(0, END)
	textLongitudGrados.delete(0, END)
	textLongitudMinutos.delete(0, END)
	textLongitudSegundos.delete(0, END)


def convertirDMSaDD():
	latitudGrados = int(textLatitudGrados.get())							# Es necesario convertir los valores de las textbox en un número, en estos casos todos son enteros pues los decimales de grados se estan expresando en minutos y segundos
	latitudMinutos = int(textLatitudMinutos.get())
	latitudSegundos = int(textLatitudSegundos.get())						# Podrían necesitarse segundo decimales por cuestiones de presición, en este caso recordar quitar la función validarSoloNúmeros en los textbox de segundos dado que no permitira el ingreso de dichos valores
	latitudDD = latitudGrados + latitudMinutos/60 + latitudSegundos/3600
	textLatitudDD.insert(0, latitudDD)										# La función global validarEntrada presenta problemas para reconocer el valor insertado por ende a sido desactivada en esta versión del proyecto
	# Lo siguiente es un copy paste cambiando latiud por longitud
	longitudGrados = int(textLongitudGrados.get())
	longitudMinutos = int(textLongitudMinutos.get())
	longitudSegundos = int(textLongitudSegundos.get())						# Si se usan segundos decimales recordar cambiar los int por float para latitudSegundos y longitudSegundos
	longitudDD = longitudGrados + longitudMinutos/60 + longitudSegundos/3600
	textLongitudDD.insert(0, longitudDD)


#Botones
Button(ventana, text = "Limpiar",
	command = lambda: limpiar()
	).grid(row = 4, column = 0, padx = 8, pady = 8)

Button(ventana, text = "Convertir DD a DMS",							# Realmente freferiria tener un solo boton, pero por cuestiones de tiempo me limitare a esto por ahora
	command = lambda: convertirDDaDMS()									# En el caso de ser un solo batón ambas funciones deben convinarse y ejecutarse con condiciones, es más trabajo, pero es mejor para el usuario final
	).grid(row = 4, column = 1, columnspan = 3, padx = 8, pady = 8)

Button(ventana, text = "Convertir DMS a DD",
	command = lambda: convertirDMSaDD()
	).grid(row = 4, column = 4, columnspan = 5, padx = 8, pady = 8)



ventana.mainloop()