#Hilda Beltrán A01251916
#Arturo Buttenklepper A01703892
#Rodrigo Nieto A01703520
#Importamos tkinter para usar la interfaz gráfica
from tkinter import *
from tkinter import ttk
#Importamos las librerías necesarias para poder enviar correos dentro de la aplicación
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#Creamos la ventana principal con las dimensiones y colores correspondientes
v = Tk()
v.title ("Fast Delivery")
v.configure(background='light blue')
v.geometry("950x450")
v.resizable(0,0)
#Creamos una etiqueta de dirección
label_direccion=Label(v, text="Dirección", font=("Helvetica", 18), bg='light blue')
#Utilizamos place para mostrar la etiqueta en la ventana
label_direccion.place(x=0, y=0)
#Creamos una entrada para poder obtener el dato del usuario
#Guardamos el dato obtenido como una cadena de texto
entry_direcciong=StringVar()
entry_direccion=Entry(v, textvariable=entry_direcciong, bg='light blue')
#Utilizamos place para mostrar nuestra entrada de texto en la ventana
entry_direccion.place(x=80, y=0)

#Creamos una etiqueta de usuario
label_usuario=Label(v, text="Usuario", font=("Helvetica", 18), bg='light blue')
label_usuario.place(x=685, y=0)
#Creamos una entrada para poder obtener el dato del usuario
#Guardamos el dato obtenido como cadena de texto
entry_usuariog=StringVar()
entry_usuario=Entry(v, textvariable=entry_usuariog, bg='light blue')
#Insertamos la terminación del correo electrónico para que los alumnos sepan que usuario utilizar
entry_usuario.insert(0, "@itesm.mx")
#Utilizamos place para mostrar la entrada de texto en la ventana
entry_usuario.place(x=758, y=0)

#Creamos una función para que al seleccionar el botón shop, nos mande a la siguiente ventana       
def shop (event):
    #Creamos la siguiente ventana con las especificaciones necesarias
    v4 = Toplevel()
    v4.title ("Fast Delivery")
    v4.configure(background='light blue')
    v4.geometry("950x750")
    v4.resizable(0,0)

    #Creamos una etiqueta de lugar    
    label_lugar=Label(v4, text="¿De dónde lo quieres?", bg='light blue', font=("Helvetica", 25))
    #Utilizamos place para mostrar nuestra etiqueta en la pantalla
    label_lugar.place(x=20, y=20)

    #Creamos nuestro primer combobox
    #Guardamos el dato obtenido como una cadena de texto
    combo=StringVar()
    combobox_lugar=ttk.Combobox(v4, font=("Helvetica", 20), state="readonly", values=["Under Armour", "Adidas", "Nike", "Calvin Klein", "American Eagle", "Vans"])
    #Hacemos que el texto por default en el combobox sea lugar
    combobox_lugar.set("Lugar")
    #Utilizamos place para mostrar nuestro combobox en la ventana
    combobox_lugar.place(x=20, y=70)

    #Creamos una etiqueta de producto
    label_producto=Label(v4, text="¿Qué deseas que te consigamos?", bg='light blue', font=("Helvetica", 25))
    #Utilizamos place para mostrar nuestra etiqueta en la ventana
    label_producto.place(x=550, y=20)
    #Creamos nuestro segundo combobox
    #Guardamos el dato obtenido como una cadena de texto
    combo1=StringVar()
    combobox_producto=ttk.Combobox(v4, font=("Helvetica", 20), state="readonly", values=["Camiseta", "Pantalón", "Tenis", "Zapatos", "Short", "Gorra", "Sudadera", "Camisa"])
    #Hacemos que el texto por default en el combobox sea producto
    combobox_producto.set("Producto")
    #Utilizamos place para mostrar nuestro combobox en la ventana
    combobox_producto.place(x=550, y=70)

    #Cremos una etiqueta de precio estimado
    label_precio=Label(v4, text="Precio estimado del producto", bg='light blue', font=("Helvetica", 25))
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_precio.place(x=275, y=200)
    #Creamos nuestro radiobutton
    #Guardamos el dato obtenido del radiobutton como cadena de texto
    tipo=StringVar()
    #Hacemos que por default el botón radial seleccionado sea el botón_1
    tipo.set("$0-$500")
    #Creamos el botón_1
    botón_1=Radiobutton(v4, text="$0-$500", variable=tipo, value="$0-$500", font=("Helvetica", 20), bg='light blue')
    #Utilizamos place para mostrar nuestro radiobutton en la ventana
    botón_1.place(x=370, y=250)
    #Creamos el botón_2
    botón_2=Radiobutton(v4, text="$500-$1000", variable=tipo, value="$500-$1000", font=("Helvetica", 20), bg='light blue')
    #Utilizamos place para mostrar nuestro radiobutton en la ventana
    botón_2.place(x=370, y=300)
    #Creamos el botón_3
    botón_3=Radiobutton(v4, text="$1000-$1500", variable=tipo, value="$1000-$1500", font=("Helvetica", 20), bg='light blue')
    #Utilizamos place para mostrar nuestro radiobutton en la ventana
    botón_3.place(x=370, y=350)
    #Creamos el botón_4
    botón_4=Radiobutton(v4, text="$1500-$2000", variable=tipo, value="$1500-$2000", font=("Helvetica", 20), bg='light blue')
    #Utilizamos place para mostrar nuestro radiobutton en la ventana
    botón_4.place(x=370, y=400)
    
    #Creamos una etiqueta de GRACIAS
    label_gracias=Label(v4, text="GRACIAS!! por confiar en nosotros", bg='light blue', font=("Helvetica", 40))
    #Utilizamos place para mostrar nuestra etiqueta en la ventana
    label_gracias.place(x=150, y=600)


    entry_v4g=StringVar()
    #Creamos una entrada de texto para guardar los datos obtenidos de ambos combobox y un radiobutton
    entry_v4=Entry(v4, bg='light blue', textvariable=entry_v4g)
    #Utilizamos place para mostrar nuestra entrada de texto en la ventana
    entry_v4.place(x=400, y=720)
    #Creamos una función para que al oprimir el botón listo, la información se imprima en la entrada de texto antes mencionada
    def precio1 (event):
       entry_v4.insert(0, tipo.get())
       entry_v4.insert(0, " de ")
       entry_v4.insert(0, combobox_lugar.get())
       entry_v4.insert(0, " , ")
       entry_v4.insert(0, combobox_producto.get())
    
    #Creamos el botón listo para añadir los datos seleccionados
    button_listo=Button(v4, text="Listo", font=("Helvetica", 25))
    #Enlazamos el botón con la acción precio1
    button_listo.bind("<Button-1>", precio1)
    #Utilizamos place para mostrar el botón en la pantalla
    button_listo.place(x=450, y=500)

    #Creamos una función para destruir la ventana al ir a otra, utilizando .destroy()
    def atrás1 (event):
        v4.destroy()

    #Creamos un botón 
    button_atrás6=Button(v4, text="Atrás")
    #Enlazamos el botón con la acción atrás1
    button_atrás6.bind("<Button>", atrás1)
    #Utilizamos place para mostrar el botón en la ventana
    button_atrás6.place(x=10, y=720)

    #Creamos una función para destruir una ventana e ir a otra al oprimir un botón
    def end1 (event):
        v4.destroy()
        v8 = Toplevel()
        v8.title ("Fast Delivery")
        v8.configure(background='light blue')
        v8.geometry("950x450")
        v8.resizable(0,0)
        #Comenzamos con el proceso para enviar un correo
        msg=MIMEMultipart()
        #Definimos en una variable el contenido de nuestro mensaje, en este caso la información almacenada en la entrada de texto
        message=entry_v4g.get()

        #Registramos los datos necesarios para mandar el correo
        #Contraseña
        password="*****"
        #Correo de salida
        msg['From']="A01251916@itesm.mx"
        #Correo de entrada
        msg['To']="A01251916@itesm.mx"
        #Asunto
        msg['Subject']="Nueva Orden"

        #Adjuntamos la variable del mensaje, antes definida
        msg.attach(MIMEText(message, 'plain'))

        #Definir el servidor junto al puerto
        server=smtplib.SMTP('SMTP.Office365.com:587')

        server.starttls()
        #Definir con qué datos se ingresará a la cuenta del correo electrónico
        server.login(msg['From'], password)
        #Definir la estructura del correo
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        #Cerrar la cuenta de correo al terminar
        server.quit()
        #Crear una etiqueta para indicar que la orden está siendo enviada
        etiqueta_total=Label(v8, text="Tu orden está siendo enviada!", bg='light blue', font=("Helvetica", 35))
        #Utilizar place para mostrar la etiqueta en la ventana
        etiqueta_total.place(x=215, y=150)

        #Crear una función para cerrar la ventana al oprimir un botón, utilizando .destroy()
        def kill1 (event):
            v8.destroy()

        #Crear un botón        
        button_kill=Button(v8, text="Salir")
        #Enlazar el botón a la acción kill1
        button_kill.bind("<Button-1>", kill1)
        #Utilizamos place para mostrar el botón en la ventana
        button_kill.place(x=910, y=420)

    #Creamos un botón
    button_ordenar=Button(v4, text="Ordenar")
    #Enlazamos el botón a la acción end1
    button_ordenar.bind("<Button-1>", end1)
    #Utilizamos place para mostrar el botón en la ventana
    button_ordenar.place(x=870, y=720)
#Para crear un botón con una imagen definimos el archivo que utilizaremos
imagen_bolsa=PhotoImage(file="bag.gif")
#Creamos el botón con todas las propiedades necesarias
button_shop=Button(v, image=imagen_bolsa, text="¿Qué deseas?", compound=RIGHT, font=("Helvetica", 35))
#Enlazamos el botón con la acción shop
button_shop.bind("<Button-1>", shop)
#Utilizamos place para mostrar el botón en la ventana
button_shop.place(x=90, y=150)

#Creamos una función para abrir otra ventana
def favor (event):
    v5 = Toplevel()
    v5.title ("Fast Delivery")
    v5.configure(background='light blue')
    v5.geometry("950x750")
    v5.resizable(0,0)

    #Creamos una etiqueta
    label_favor=Label(v5, text="Pídenos un favor", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_favor.place(x=0, y=0)

    #Creamos una etiqueta de dirección 1
    label_dirección2=Label(v5, text="Dirección 1", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_dirección2.place(x=50, y=50)

    #Creamos una entrada de texto
    #Guardamos el dato obtenido como una cadena de texto
    entry_dirección2g=StringVar()
    entry_dirección2=Entry(v5, bg='light blue', textvariable=entry_dirección2g)
    #Utilizamos place para mostrar la entrada de texto en la ventana
    entry_dirección2.place(x=150, y=50)
    #Utilizamos insert para agregar el dato de otra entrada de texto
    entry_dirección2.insert(0, entry_direccion.get())
    
    #Creamos una etiqueta de dirección 2
    label_dirección3=Label(v5, text="Dirección 2", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_dirección3.place(x=550, y=50)

    #Creamos una entrada de texto
    #Guardamos el dato obtenido como una cadena de texto
    entry_dirección3g=StringVar()
    entry_dirección3=Entry(v5, bg='light blue', textvariable=entry_dirección3g)
    #Utilizamos place para mostrar la entrada de texto en la ventana
    entry_dirección3.place(x=650, y=50)

    #Creamos una etiqueta de el producto a transportar
    label_productofavor=Label(v5, bg='light blue', text="¿Qué producto transportamos?", font=("Helvetica", 30))
    #Utilizamos place para mostrar la etiqueta en la pantalla
    label_productofavor.place(x=260, y=200)
    #Creamos nuestro radiobutton
    #Guardamos el dato obtenido como una cadena de texto
    tipo1=StringVar()
    #Creamos el botón_documentos
    botón_documentos=Radiobutton(v5, text="Documentos", variable=tipo1, value="Documentos", bg='light blue', font=("Helvetica", 20))
    #Utilizamos place para mostrar el botón en la ventana
    botón_documentos.place(x=93.75, y=350)
    #Creamos el botón_tecnología
    botón_tecnología=Radiobutton(v5, text="Tecnología", variable=tipo1, value="Tecnología", bg='light blue', font=("Helvetica", 20))
    #Utilizamos place para mostrar el botón en la ventana
    botón_tecnología.place(x=381.25, y=350)
    #Creamos el botón_mascotas
    botón_mascotas=Radiobutton(v5, text="Mascotas", variable=tipo1, value="Mascotas", bg='light blue', font=("Helvetica", 20))
    #Utilizamos place para mostrar el botón en la ventana
    botón_mascotas.place(x=638.75, y=350)

    #Creamos una entrada de texto
    #Guardamos el dato obtenido como cadena de texto
    entry_finalv5g=StringVar()
    entry_finalv5=Entry(v5, bg='light blue', textvariable=entry_finalv5g)
    #Utilizamos place para mostrar la entrada de texto
    entry_finalv5.place(x=400, y=720)
    #Creamos una función para ir insertando la información obtenida en los diferentes botones y entradas de texto
    def favorf (event):
        entry_finalv5.insert(0, entry_dirección3g.get())
        entry_finalv5.insert(0, " a ")
        entry_finalv5.insert(0, entry_dirección2g.get())
        entry_finalv5.insert(0, " de ")
        entry_finalv5.insert(0, tipo1.get())
    #Creamos un botón
    button_listo=Button(v5, text="Listo")
    #Enlazamos el botón a la acción favorf
    button_listo.bind("<Button-1>", favorf)
    #Utilizamos place para mostrar el botón en la pantalla
    button_listo.place(x=450, y=500)
    #Creamos una función para destruir una ventana por medio de .destroy()
    def atrás2 (event):
        v5.destroy()
    #Creamos un botón
    button_atrás5=Button(v5, text="Atrás")
    #Enlazamos el botón a la acción atrás 2
    button_atrás5.bind("<Button-1>", atrás2)
    #Utilizamos place para mostrar el botón en la ventana
    button_atrás5.place(x=10, y=720)
    #Crear una función para ir a otra ventana al oprimir un botón y eliminar la anterior
    def ordenar2 (event):
        v5.destroy()
        v8 = Toplevel()
        v8.title ("Fast Delivery")
        v8.configure(background='light blue')
        v8.geometry("950x450")
        v8.resizable(0,0)
        #Comenzamos con el proceso para enviar un correo
        msg=MIMEMultipart()
        #Definimos en una variable el contenido de nuestro mensaje, en este caso el valor de una entrada de texto
        message=entry_finalv5g.get()

        #Registramos los datos necesarios para mandar un correo
        #Contraseña
        password="*****!"
        #Correo de salida
        msg['From']="A01251916@itesm.mx"
        #Correo de entrada
        msg['To']="A01251916@itesm.mx"
        #Asunto
        msg['Subject']="Nuevo Favor"

        #Adjuntamos la variable del mensaje, antes definido
        msg.attach(MIMEText(message, 'plain'))
        
        #Definir el servidor junto al puerto
        server=smtplib.SMTP('SMTP.Office365.com:587')

        server.starttls()
        #Definir con qué datos se ingresará a la cuenta del correo electrónico
        server.login(msg['From'], password)
        #Definir la estructura del correo
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        #Cerrar la cuenta de correo al terminar
        server.quit()

        #Crear una etiqueta de que la orden está siendo enviada
        etiqueta_total=Label(v8, text="Tu orden está siendo enviada!", bg='light blue', font=("Helvetica", 35))
        #Utilizamos place para mostrar la etiqueta en la ventana
        etiqueta_total.place(x=215, y=150)

        #Creamos una función para destruir una ventana por medio de .destroy()
        def kill1 (event):
            v8.destroy()

        #Creamos un botón
        button_kill=Button(v8, text="Salir")
        #Enlazamos el botón a la acción kill1
        button_kill.bind("<Button-1>", kill1)
        #Utilizamos place para mostrar el botón en la ventana
        button_kill.place(x=910, y=420)

    #Creamos un botón
    button_ordenar=Button(v5, text="Ordenar")
    #Enlazamos el botón a la acción ordenar2
    button_ordenar.bind("<Button-1>", ordenar2)
    #Utilizamos place para mostrar el botón en la ventana 
    button_ordenar.place(x=870, y=720)
#Para crear un botón con una imagen, definimos el archivo que se va a utilizar
imagen_favor=PhotoImage(file="favor.gif")
#Creamos el botón con todas las propiedades necesarias
button_favor=Button(v, image=imagen_favor, compound=RIGHT, text="Pídenos un favor", font=("Helvetica", 35))
#Enlazamos el botón a la acción favor
button_favor.bind("<Button-1>", favor)
#Utilizamos place para mostrar el botón en la ventana
button_favor.place(x=520, y=150)

#Creamos una etiqueta de tendencias
etiqueta_tendencias=Label(v, text="Tendencias", font=("Helvetica", 40), bg='light blue')
#Utilizamos place para mostrar la etiqueta en la ventana
etiqueta_tendencias.place(x=90, y=250)    

#Creamos una función para abrir otra ventana
def vans (event):
    v9 = Toplevel()
    v9.title ("Fast Delivery")
    v9.configure(background='light blue')
    v9.geometry("950x750")
    v9.resizable(0,0)

    #Creamos una etiqueta del catálogo correspondiente
    label_marca1=Label(v9, text="Catálogo Vans", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la pantalla
    label_marca1.place(x=0, y=0)

    #Creamos una etiqueta de usuario en línea
    label_usuario1=Label(v9, text="Usuario en línea", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_usuario1.place(x=830, y=0)

    #Definimos el archivo que se utilizará
    imagen27=PhotoImage(file="tenis_vans.gif")
    #Creamos una etiqueta con la imagen
    tenisvans1=Label(v9, image=imagen27)
    #Definimos que image es igual a la imagen que mencionamos antes
    tenisvans1.image=imagen27
    #Utilizamos place para mostrar la etiqueta en la ventana
    tenisvans1.place(x=200, y=92)

    #Definimos el archivo que se utilizará
    imagen28=PhotoImage(file="camiseta_vans.gif")
    #Creamos una etiqueta con la imagen
    camisetavans=Label(v9, image=imagen28)
    #Definimos que image es igual a la imagen que mencionamos antes
    camisetavans.image=imagen28
    #Utilizamos place para mostrar la etiqueta en la ventana
    camisetavans.place(x=445, y=92)
    
    #Definimos el archivo que se utilizará
    imagen29=PhotoImage(file="mochila_vans.gif")
    #Creamos una etiqueta con la imagen
    mochilavans=Label(v9, image=imagen29)
    #Definimos que image es igual a la imagen que mencionamos antes
    mochilavans.image=imagen29
    #Utilizamos place para mostrar la etiqueta en la ventana
    mochilavans.place(x=670, y=92)
    
    #Definimos el archivo que se utilizará
    imagen30=PhotoImage(file="mochila_vans1.gif")
    #Creamos una etiqueta con la imagen
    mochilavans1=Label(v9, image=imagen30)
    #Definimos que image es igual a la imagen que mencionamos antes
    mochilavans1.image=imagen30
    #Utilizamos place para mostrar la etiqueta en la ventana
    mochilavans1.place(x=200, y=234)
    
    #Definimos el archivo que se utilizará
    imagen31=PhotoImage(file="sudadera_vans.gif")
    #Creamos una etiqueta con la imagen
    sudaderavans=Label(v9, image=imagen31)
    #Definimos que image es igual a la imagen que mencionamos antes
    sudaderavans.image=imagen31
    #Utilizamos place para mostrar la etiqueta en la ventana
    sudaderavans.place(x=445, y=234)

    #Definimos el archivo que se utilizará
    imagen32=PhotoImage(file="tenis_vans1.gif")
    #Creamos una etiqueta con la imagen
    tenisvans1=Label(v9, image=imagen32)
    #Definimos que image es igual a la imagen que mencionamos antes
    tenisvans1.image=imagen32
    #Utilizamos place para mostrar la etiqueta en la ventana
    tenisvans1.place(x=670, y=234)
    
    #Definimos el archivo que se utilizará
    imagen33=PhotoImage(file="tenis_vans2.gif")
    #Creamos una etiqueta con la imagen
    tenisvans2=Label(v9, image=imagen33)
    #Definimos que image es igual a la imagen que mencionamos antes
    tenisvans2.image=imagen33
    #Utilizamos place para mostrar la etiqueta en la ventana
    tenisvans2.place(x=200, y=376)
    
    #Definimos el archivo que se utilizará
    imagen34=PhotoImage(file="sudadera_vans1.gif")
    #Creamos una etiqueta con la imagen
    sudaderavans1=Label(v9, image=imagen34)
    #Definimos que image es igual a la imagen que mencionamos antes
    sudaderavans1.image=imagen34
    #Utilizamos place para mostrar la etiqueta en la ventana
    sudaderavans1.place(x=445, y=376)
    
    #Definimos el archivo que se utilizará
    imagen35=PhotoImage(file="tenis_vans3.gif")
    #Creamos una etiqueta con la imagen
    tenisvans3=Label(v9, image=imagen35)
    #Definimos que image es igual a la imagen que mencionamos antes
    tenisvans3.image=imagen35
    #Utilizamos place para mostrar la etiqueta en la ventana
    tenisvans3.place(x=670, y=376)

    #Definimos el archivo que se utilizará
    imagen36=PhotoImage(file="sudadera_vans2.gif")
    #Creamos una etiqueta con la imagen
    sudaderavans2=Label(v9, image=imagen36)
    #Definimos que image es igual a la imagen que mencionamos antes
    sudaderavans2.image=imagen36
    #Utilizamos place para mostrar la etiqueta en la ventana
    sudaderavans2.place(x=200, y=518)

    #Definimos el archivo que se utilizará
    imagen37=PhotoImage(file="camiseta_vans1.gif")
    #Creamos una etiqueta con la imagen
    camisetavans1=Label(v9, image=imagen37)
    #Definimos que image es igual a la imagen que mencionamos antes
    camisetavans1.image=imagen37
    #Utilizamos place para mostrar la etiqueta en la ventana
    camisetavans1.place(x=445, y=518)

    #Definimos el archivo que se utilizará
    imagen38=PhotoImage(file="tenis_vans4.gif")
    #Creamos una etiqueta con la imagen
    tenisvans4=Label(v9, image=imagen38)
    #Definimos que image es igual a la imagen que mencionamos antes
    tenisvans4.image=imagen38
    #Utilizamos place para mostrar la etiqueta en la ventana
    tenisvans4.place(x=670, y=518)

    #Creamos una etiqueta
    label_tenisv=Label(v9, text="Tenis", bg='light blue')
    #Utilizamos place para mostrarla en la ventana
    label_tenisv.place(x=215, y=170)
    
    #Creamos una etiqueta
    label_camisetav=Label(v9, text="Camiseta", bg='light blue')
    #Utilizamos place para mostrarla en la ventana
    label_camisetav.place(x=448, y=170)
    
    #Creamos una etiqueta
    label_mochilav=Label(v9, text="Mochila", bg='light blue')
    #Utilizamos place para mostrarla en la ventana
    label_mochilav.place(x=678, y=170)
    
    #Creamos una etiqueta
    label_mochilav1=Label(v9, text="Mochila", bg='light blue')
    #Utilizamos place para mostrarla en la ventana
    label_mochilav1.place(x=208, y=312)

    #Creamos una etiqueta
    label_sudaderav=Label(v9, text="Sudadera", bg='light blue')
    #Utilizamos place para mostrarla en la ventana
    label_sudaderav.place(x=449, y=312)

    #Creamos una etiqueta
    label_tenisv1=Label(v9, text="Tenis", bg='light blue')
    #Utilizamos place para mostrarla en la ventana
    label_tenisv1.place(x=682, y=312)

    #Creamos una etiqueta
    label_tenisv2=Label(v9, text="Tenis", bg='light blue')
    #Utilizamos place para mostrarla en la ventana
    label_tenisv2.place(x=217, y=454)

    #Creamos una etiqueta
    label_sudaderav1=Label(v9, text="Sudadera", bg='light blue')
    #Utilizamos place para mostrarla en la ventana
    label_sudaderav1.place(x=445, y=454)

    #Creamos una etiqueta
    label_tenisv3=Label(v9, text="Tenis", bg='light blue')
    #Utilizamos place para mostrarla en la ventana
    label_tenisv3.place(x=685, y=454)

    #Creamos una etiqueta
    label_sudaderav2=Label(v9, text="Sudadera", bg='light blue')
    #Utilizamos place para mostrarla en la ventana
    label_sudaderav2.place(x=201, y=596)

    #Creamos una etiqueta
    label_camisetav1=Label(v9, text="Camiseta", bg='light blue')
    #Utilizamos place para mostrarla en la ventana
    label_camisetav1.place(x=448, y=596)

    #Creamos una etiqueta
    label_tenisv4=Label(v9, text="Tenis", bg='light blue')
    #Utilizamos place para mostrarla en la ventana
    label_tenisv4.place(x=685, y=596)

    #Creamos una entrada de texto para guardar los datos
    #Guardamos los datos como cadena de texto
    entrypreg=StringVar()
    entrypre=Entry(v9, bg='light blue', textvariable=entrypreg)
    #Utilizamos place para mostrar la entrada de texto en la ventana
    entrypre.place(x=400, y=720)

    #Creamos una función para insertar una variable a una entrada de texo
    def click24 (event):
        entrypre.insert(0, text24)
    #Creamos el botón
    button_tenisv=Button(v9, text="$499")
    #Definimos la variable
    text24=("Tenis = 499; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_tenisv.place(x=216, y=195)
    #Enlazamos el botón a la acción click24
    button_tenisv.bind("<Button-1>", click24)

    #Creamos una función para insertar una variable a una entrada de texo
    def click25 (event):
        entrypre.insert(0, text25)
    #Creamos el botón
    button_camisetav=Button(v9, text="$599")
    #Definimos la variable
    text25=("Camiseta = 599; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_camisetav.place(x=460, y=195)
    #Enlazamos el botón a la acción click25
    button_camisetav.bind("<Button-1>", click25)

    #Creamos una función para insertar una variable a una entrada de texo
    def click26 (event):
        entrypre.insert(0, text26)
    #Creamos el botón
    button_mochilav=Button(v9, text="$449")
    #Definimos la variable
    text26=("Mochila = 449; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_mochilav.place(x=684, y=195)
    #Enlazamos el botón a la acción click26
    button_mochilav.bind("<Button-1>", click26)

    #Creamos una función para insertar una variable a una entrada de texo
    def click27 (event):
        entrypre.insert(0, text27)
    #Creamos el botón
    button_mochilav1=Button(v9, text="$599")
    #Definimos la variable
    text27=("Mochila = 599; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_mochilav1.place(x=216, y=337)
    #Enlazamos el botón a la acción click27
    button_mochilav1.bind("<Button-1>", click27)

    #Creamos una función para insertar una variable a una entrada de texo
    def click28 (event):
        entrypre.insert(0, text28)
    #Creamos el botón
    button_sudaderav=Button(v9, text="$949")
    #Definimos la variable
    text28=("Sudadera = 949; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_sudaderav.place(x=460, y=337)
    #Enlazamos el botón a la acción click28
    button_sudaderav.bind("<Button-1>", click28)

    #Creamos una función para insertar una variable a una entrada de texo
    def click29 (event):
        entrypre.insert(0, text29)
    #Creamos el botón
    button_tenisv1=Button(v9, text="$1,399")
    #Definimos la variable
    text29=("Tenis = 1399; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_tenisv1.place(x=681, y=337)
    #Enlazamos el botón a la acción click29
    button_tenisv1.bind("<Button-1>", click29)
    
    #Creamos una función para insertar una variable a una entrada de texo
    def click30 (event):
        entrypre.insert(0, text30)
    #Creamos el botón
    button_tenisv2=Button(v9, text="$499")
    #Definimos la variable
    text30=("Tenis = 499; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_tenisv2.place(x=215, y=479)
    #Enlazamos el botón a la acción click30
    button_tenisv2.bind("<Button-1>", click30)

    #Creamos una función para insertar una variable a una entrada de texo
    def click31 (event):
        entrypre.insert(0, text31)
    #Creamos el botón
    button_sudaderav1=Button(v9, text="$599")
    #Definimos la variable
    text31=("Sudadera = 599; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_sudaderav1.place(x=460, y=479)
    #Enlazamos el botón a la acción click31
    button_sudaderav1.bind("<Button-1>", click31)

    #Creamos una función para insertar una variable a una entrada de texo
    def click32 (event):
        entrypre.insert(0, text32)
    #Creamos el botón
    button_tenisv3=Button(v9, text="$1,499")
    #Definimos la variable
    text32=("Tenis = 1499; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_tenisv3.place(x=680, y=479)
    #Enlazamos el botón a la acción click32
    button_tenisv3.bind("<Button-1>", click32)

    #Creamos una función para insertar una variable a una entrada de texo
    def click33 (event):
        entrypre.insert(0, text33)
    #Creamos el botón
    button_sudaderav2=Button(v9, text="$599")
    #Definimos la variable
    text33=("Sudadera = 599; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_sudaderav2.place(x=215, y=621)
    #Enlazamos el botón a la acción click33
    button_sudaderav2.bind("<Button-1>", click33)

    #Creamos una función para insertar una variable a una entrada de texo
    def click34 (event):
        entrypre.insert(0, text34)
    #Creamos el botón
    button_camisetav1=Button(v9, text="$949")
    #Definimos la variable
    text34=("Camiseta = 949; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_camisetav1.place(x=460, y=621)
    #Enlazamos el botón a la acción click34
    button_camisetav1.bind("<Button-1>", click34)

    #Creamos una función para insertar una variable a una entrada de texo
    def click35 (event):
        entrypre.insert(0, text35)
    #Creamos el botón
    button_tenisv4=Button(v9, text="$1,399")
    #Definimos la variable
    text35=("Tenis = 1399; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_tenisv4.place(x=681, y=621)
    #Enlazamos el botón a la acción click35
    button_tenisv4.bind("<Button-1>", click35)

    #Crear una función para destruir una ventana con .destroy()
    def atrás3 (event):
        v9.destroy()
    #Creamos un botón
    button_atrás=Button(v9, text="Atrás")
    #Enlazamos el botón a la acción atrás3
    button_atrás.bind("<Button-1>", atrás3)
    #Utilizamos place para mostrar el botón en la ventana
    button_atrás.place(x=10, y=720)

    #Creamos una función para ir a otra ventana y destruir la anterior
    def end1 (event):
        v9.destroy()
        v8 = Toplevel()
        v8.title ("Fast Delivery")
        v8.configure(background='light blue')
        v8.geometry("950x450")
        v8.resizable(0,0)

        #Comenzamos con el proceso para mandar un correo
        msg=MIMEMultipart()
        #Definimos en una variable el contenido de nuestro mensaje, en este caso la entrada de texto
        message=entrypreg.get()

        #Registramos los datos necesarios para mandar el correo
        #Contraseña
        password="*****!"
        #Correo de salida
        msg['From']="A01251916@itesm.mx"
        #Correo de entrada
        msg['To']="A01251916@itesm.mx"
        #Asunto
        msg['Subject']="Nueva Orden Vans"

        #Ajuntamos la variable del mensaje, antes definiada
        msg.attach(MIMEText(message, 'plain'))

        #Definir el servidor junto al puerto
        server=smtplib.SMTP('SMTP.Office365.com:587')

        server.starttls()

        #Definir con qué datos se ingresará a la cuenta de correo electrónico
        server.login(msg['From'], password)
        #Definir la estructura del correo
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        #Cerrar la cuenta de correo al terminar
        server.quit()

        #Creamos una etiqueta de que la orden está siendo enviada
        etiqueta_total=Label(v8, text="Tu orden está siendo enviada!", bg='light blue', font=("Helvetica", 35))
        #Utilizamos place para mostrar la etiqueta en la pantalla
        etiqueta_total.place(x=215, y=150)

        #Creamos una función para destruir la ventana con .destroy()
        def kill1 (event):
            v8.destroy()

        #Creamos un botón 
        button_kill=Button(v8, text="Salir")
        #Enlazamos el botón a la acción kill1
        button_kill.bind("<Button-1>", kill1)
        #Utilizamos place para mostrar el botón en la ventana
        button_kill.place(x=910, y=420)

    #Creamos un botón
    button_ordenar3=Button(v9, text="Ordenar")
    #Enlazamos el botón a la acción end1
    button_ordenar3.bind("<Button-1>", end1)
    #Utilizamos place para mostrar el botón en la ventana
    button_ordenar3.place(x=870, y=720)
#Para crear un botón con una imagen definimos el archivo que se utilizará
imagen=PhotoImage(file="marca1.gif")
#Creamos el botón e indicamos que image es igual a la imagen antes definida
button_marca1=Button(image=imagen)
#Enlazamos el botón a la acción vans
button_marca1.bind("<Button-1>", vans)
#Utilizamos place para mostrar el botón en la ventana
button_marca1.place(x=105, y=325)

#Creamos una función para abrir otra ventana al oprimir un botón
def underarmour (event):
    v3 = Toplevel()
    v3.title ("Fast Delivery")
    v3.configure(background='light blue')
    v3.geometry("950x750")
    v3.resizable(1,1)

    #Crear una etiqueta para mostrar el catálogo a la marca a la que pertenece
    label_marca2=Label(v3, text="Catálogo Under Armour", bg='light blue')
    #utilizamos place para mostrar la etiqueta en la ventana
    label_marca2.place(x=0, y=0)

    #Creamos una etiqueta para mostrar que el usuario está en línea
    label_usuario2=Label(v3, text="Usuario en línea", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_usuario2.place(x=830, y=0)

    #Paara crear una etiqueta con una imagen definimos el archivo que se utilizará
    imagen15=PhotoImage(file="sudadera_underarmour1.gif")
    #Creamos una etiqueta y definimos la imagen a utilizar dentro de la etiqueta
    sudaderaunderarmour=Label(v3, image=imagen15)
    #Indicamos que image es igual a la imagen que utilizaremos
    sudaderaunderarmour.image=imagen15
    #Utilizamos place para mostrar la etiqueta en la ventana
    sudaderaunderarmour.place(x=200, y=92)
    
    #Para crear una etiqueta con una imagen definimos el archivo que se utilizará
    imagen16=PhotoImage(file="camiseta_underarmour1.gif")
    #Creamos una etiqueta y definimos la imagen a utilizar dentro de la etiqueta
    camisetaunderarmour=Label(v3, image=imagen16)
    #Indicamos que image es igual a la imagen que utilizaremos
    camisetaunderarmour.image=imagen16
    #Utilizamos place para mostrar la etiqueta en la ventana
    camisetaunderarmour.place(x=445, y=92)

    #Para crear una etiqueta con una imagen definimos el archivo que se utilizará
    imagen17=PhotoImage(file="gorra_underarmour1.gif")
    #Creamos una etiqueta y definimos la imagen a utilizar dentro de la etiqueta
    gorraunderarmour=Label(v3, image=imagen17)
    #Indicamos que image es igual a la imagen que utilizaremos
    gorraunderarmour.image=imagen17
    #Utilizamos place para mostrar la etiqueta en la ventana
    gorraunderarmour.place(x=670, y=92)

    #Para crear una etiqueta con una imagen definimos el archivo que se utilizará
    imagen18=PhotoImage(file="mochila_underarmour1.gif")
    #Creamos una etiqueta y definimos la imagen a utilizar dentro de la etiqueta
    mochilaunderarmour=Label(v3, image=imagen18)
    #Indicamos que image es igual a la imagen que utilizaremos
    mochilaunderarmour.image=imagen18
    #Utilizamos place para mostrar la etiqueta en la ventana
    mochilaunderarmour.place(x=200, y=234)
    
    #Para crear una etiqueta con una imagen definimos el archivo que se utilizará
    imagen19=PhotoImage(file="pants_underarmour1.gif")
    #Creamos una etiqueta y definimos la imagen a utilizar dentro de la etiqueta
    pantsunderarmour=Label(v3, image=imagen19)
    #Indicamos que image es igual a la imagen que utilizaremos
    pantsunderarmour.image=imagen19
    #Utilizamos place para mostrar la etiqueta en la ventana
    pantsunderarmour.place(x=445, y=234)
    
    #Para crear una etiqueta con una imagen definimos el archivo que se utilizará
    imagen20=PhotoImage(file="tenis_underarmour1.gif")
    #Creamos una etiqueta y definimos la imagen a utilizar dentro de la etiqueta
    tenisunderarmour=Label(v3, image=imagen20)
    #Indicamos que image es igual a la imagen que utilizaremos
    tenisunderarmour.image=imagen20
    #Utilizamos place para mostrar la etiqueta en la ventana
    tenisunderarmour.place(x=670, y=234)

    #Para crear una etiqueta con una imagen definimos el archivo que se utilizará
    imagen21=PhotoImage(file="camiseta_underarmour1.2.gif")
    #Creamos una etiqueta y definimos la imagen a utilizar dentro de la etiqueta
    camisetaunderarmour1=Label(v3, image=imagen21)
    #Indicamos que image es igual a la imagen que utilizaremos
    camisetaunderarmour1.image=imagen21
    #Utilizamos place para mostrar la etiqueta en la ventana
    camisetaunderarmour1.place(x=200, y=376)
    
    #Para crear una etiqueta con una imagen definimos el archivo que se utilizará
    imagen22=PhotoImage(file="mochila_underarmour1.1.gif")
    #Creamos una etiqueta y definimos la imagen a utilizar dentro de la etiqueta
    mochilaunderarmour1=Label(v3, image=imagen22)
    #Indicamos que image es igual a la imagen que utilizaremos
    mochilaunderarmour1.image=imagen22
    #Utilizamos place para mostrar la etiqueta en la ventana
    mochilaunderarmour1.place(x=445, y=376)
    
    #Para crear una etiqueta con una imagen definimos el archivo que se utilizará
    imagen23=PhotoImage(file="sandalias_underarmour1.gif")
    #Creamos una etiqueta y definimos la imagen a utilizar dentro de la etiqueta
    sandaliasunderarmour1=Label(v3, image=imagen23)
    #Indicamos que image es igual a la imagen que utilizaremos
    sandaliasunderarmour1.image=imagen23
    #Utilizamos place para mostrar la etiqueta en la ventana
    sandaliasunderarmour1.place(x=670, y=376)
    
    #Para crear una etiqueta con una imagen definimos el archivo que se utilizará
    imagen24=PhotoImage(file="pants_underarmour1.1.gif")
    #Creamos una etiqueta y definimos la imagen a utilizar dentro de la etiqueta
    pantsunderarmour1=Label(v3, image=imagen24)
    #Indicamos que image es igual a la imagen que utilizaremos
    pantsunderarmour1.image=imagen24
    #Utilizamos place para mostrar la etiqueta en la ventana
    pantsunderarmour1.place(x=200, y=518)
    
    #Para crear una etiqueta con una imagen definimos el archivo que se utilizará
    imagen25=PhotoImage(file="camiseta_underarmour1.1.gif")
    #Creamos una etiqueta y definimos la imagen a utilizar dentro de la etiqueta
    camisetaunderarmour1_1=Label(v3, image=imagen25)
    #Indicamos que image es igual a la imagen que utilizaremos
    camisetaunderarmour1_1.image=imagen25
    #Utilizamos place para mostrar la etiqueta en la ventana
    camisetaunderarmour1_1.place(x=445, y=518)
    
    #Para crear una etiqueta con una imagen definimos el archivo que se utilizará
    imagen26=PhotoImage(file="gorra_underarmour1.1.gif")
    #Creamos una etiqueta y definimos la imagen a utilizar dentro de la etiqueta
    gorraunderarmour1=Label(v3, image=imagen26)
    #Indicamos que image es igual a la imagen que utilizaremos
    gorraunderarmour1.image=imagen26
    #Utilizamos place para mostrar la etiqueta en la ventana
    gorraunderarmour1.place(x=670, y=518)

    #Creamos una etiqueta 
    label_sudadera2=Label(v3, text="Sudadera", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_sudadera2.place(x=203, y=170)

    #Creamos una etiqueta
    label_camiseta2=Label(v3, text="Camiseta", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_camiseta2.place(x=448, y=170)

    #Creamos una etiqueta
    label_gorra2=Label(v3, text="Gorra", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_gorra2.place(x=684, y=170)
    
    #Creamos una etiqueta
    label_mochila2=Label(v3, text="Mochila", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_mochila2.place(x=208, y=312)
    
    #Creamos una etiqueta
    label_pants2=Label(v3, text="Pants", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_pants2.place(x=460, y=312)
    
    #Creamos una etiqueta
    label_tenis2=Label(v3, text="Tenis", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_tenis2.place(x=685, y=312)
    
    #Creamos una etiqueta
    label_camiseta2_1=Label(v3, text="Camiseta", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_camiseta2_1.place(x=204, y=454)
    
    #Creamos una etiqueta
    label_mochila2_1=Label(v3, text="Mochila", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_mochila2_1.place(x=453, y=454)
    
    #Creamos una etiqueta
    label_sandalias1=Label(v3, text="Sandalias", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_sandalias1.place(x=673, y=454)
    
    #Creamos una etiqueta
    label_pants2_1=Label(v3, text="Pants", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_pants2_1.place(x=215, y=596)
    
    #Creamos una etiqueta
    label_camiseta2_2=Label(v3, text="Camiseta", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_camiseta2_2.place(x=448, y=596)
    
    #Creamos una etiqueta
    label_gorra2_1=Label(v3, text="Gorra", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_gorra2_1.place(x=685, y=596)
    
    #Creamos una entrada de texto
    #Guardamos el dato obtenido como una cadena de texto
    entrypg=StringVar()
    entryp=Entry(v3, bg='light blue', textvariable=entrypg)
    #Utilizamos place para mostrar la entrada de texto en la ventana
    entryp.place(x=400, y=720)

    #Creamos una función para insertar cadenas de texto a una entrada de texto
    def click (event):
        entryp.insert(0,text)
    #Creamos un botón
    button_sudadera2=Button(v3, text="$499")
    #Definimos la variable a insertar
    text=("Sudadera = 499; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_sudadera2.place(x=216, y=195)
    #Enlazamos el botón a la acción click
    button_sudadera2.bind("<Button-1>", click)

    #Creamos una función para insertar cadenas de texto a una entrada de texto
    def click1 (event):
        entryp.insert(0,text1)
    #Creamos un botón
    button_camiseta2=Button(v3, text="$599")
    #Definimos la variable a insertar
    text1=("Camiseta = 599; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_camiseta2.place(x=462, y=195)
    #Enlazamos el botón a la acción click
    button_camiseta2.bind("<Button-1>", click1)

    #Creamos una función para insertar cadenas de texto a una entrada de texto
    def click2 (event):
        entryp.insert(0,text2)
    #Creamos un botón
    button_gorra2=Button(v3, text="$449")
    #Definimos la variable a insertar
    text2=("Gorra = 449; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_gorra2.place(x=685, y=195)
    #Enlazamos el botón a la acción click2
    button_gorra2.bind("<Button-1>", click2)

    #Creamos una función para insertar cadenas de texto a una entrada de texto
    def click3 (event):
        entryp.insert(0,text3)
    #Creamos un botón
    button_mochila2=Button(v3, text="$599")
    #Definimos la variable a insertar
    text3=("Mochila = 599; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_mochila2.place(x=216, y=337)
    #Enlazamos el botón a la acción click3
    button_mochila2.bind("<Button-1>", click3)

    #Creamos una función para insertar cadenas de texto a una entrada de texto
    def click4 (event):
        entryp.insert(0,text4)
    #Creamos un botón
    button_pants2=Button(v3, text="$949")
    #Definimos la variable a insertar
    text4=("Pants = 949; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_pants2.place(x=461, y=337)
    #Enlazamos el botón a la acción click4
    button_pants2.bind("<Button-1>", click4)

    #Creamos una función para insertar cadenas de texto a una entrada de texto
    def click5 (event):
        entryp.insert(0,text5)
    #Creamos un botón
    button_tenis2=Button(v3, text="$1,399")
    #Definimos la variable a insertar
    text5=("Tenis = 1399; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_tenis2.place(x=681, y=337)
    #Enlazamos el botón a la acción click5
    button_tenis2.bind("<Button-1>", click5)

    #Creamos una función para insertar cadenas de texto a una entrada de texto
    def click6 (event):
        entryp.insert(0,text6)
    #Creamos un botón
    button_camiseta2_1=Button(v3, text="$1,399")
    #Definimos la variable a insertar
    text6=("Camiseta = 1399; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_camiseta2_1.place(x=210, y=479)
    #Enlazamos el botón a la acción click6
    button_camiseta2_1.bind("<Button-1>", click6)

    #Creamos una función para insertar cadenas de texto a una entrada de texto
    def click7 (event):
        entryp.insert(0,text7)
    #Creamos un botón
    button_mochila2_1=Button(v3, text="$1,399")
    #Definimos la variable a insertar
    text7=("Mochila = 1399; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_mochila2_1.place(x=455, y=479)
    #Enlazamos el botón a la acción click7
    button_mochila2_1.bind("<Button-1>", click7)

    #Creamos una función para insertar cadenas de texto a una entrada de texto
    def click8 (event):
        entryp.insert(0,text8)
    #Creamos un botón
    button_sandalias1=Button(v3, text="$1,399")
    #Definimos la variable a insertar
    text8=("Sandalias = 1399; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_sandalias1.place(x=680, y=479)
    #Enlazamos el botón a la acción click8
    button_sandalias1.bind("<Button-1>", click8)

    #Creamos una función para insertar cadenas de texto a una entrada de texto
    def click9 (event):
        entryp.insert(0,text9)
    #Creamos un botón
    button_pants2_1=Button(v3, text="$1,399")
    #Definimos la variable a insertar
    text9=("Pants = 1399; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_pants2_1.place(x=214, y=621)
    #Enlazamos el botón a la acción click9
    button_pants2_1.bind("<Button-1>", click9)

    #Creamos una función para insertar cadenas de texto a una entrada de texto
    def click10 (event):
        entryp.insert(0,text10)
    #Creamos un botón
    button_camiseta2_2=Button(v3, text="$1,399")
    #Definimos la variable a insertar
    text10=("Camiseta = 1399; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_camiseta2_2.place(x=459, y=621)
    #Enlazamos el botón a la acción click10
    button_camiseta2_2.bind("<Button-1>", click10)

    #Creamos una función para insertar cadenas de texto a una entrada de texto
    def click11 (event):
        entryp.insert(0,text11)
    #Creamos un botón
    button_gorra2_1=Button(v3, text="$1,399")
    #Definimos la variable a insertar
    text11=("Gorra = 1399; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_gorra2_1.place(x=681, y=621)
    #Enlazamos el botón a la acción click11
    button_gorra2_1.bind("<Button-1>", click11)

    #Creamos una función para destruir un ventana con .destroy()
    def atrás4 (event):
        v3.destroy()

    #Creamos un botón
    button_atrás2=Button(v3, text="Atrás")
    #Enlazamos el botón a la acción atrás4
    button_atrás2.bind("<Button-1>", atrás4)
    #Utilizamos place para mostrar el botón en la ventana
    button_atrás2.place(x=10, y=720)

    #Creamos una función para destruir una ventana
    def end1 (event):
        v3.destroy()
        v8 = Toplevel()
        v8.title ("Fast Delivery")
        v8.configure(background='light blue')
        v8.geometry("950x450")
        v8.resizable(0,0)

        #Comenzamos con el proceso para enviar correos
        msg=MIMEMultipart()
        #Definir en una variable
        message=entrypg.get()

        #Registrar los datos necesarios para mandar el correo
        #Contraseña
        password="*****!"
        #Correo de salida
        msg['From']="A01251916@itesm.mx"
        #Correo de entrada
        msg['To']="A01251916@itesm.mx"
        #Asunto
        msg['Subject']="Nueva Orden UnderArmour"

        #Adjuntar el mensaje
        msg.attach(MIMEText(message, 'plain'))
        #Definir el servidor y el puerto
        server=smtplib.SMTP('SMTP.Office365.com:587')

        server.starttls()
        #Definir los datos para inciar sesión en el correo electrónico
        server.login(msg['From'], password)
        #Definir la estructura del correo
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        #Cerrar la cuenta al terminar
        server.quit()

        #Crear una etiqueta de que la orden está siendo enviada
        etiqueta_total=Label(v8, text="Tu orden está siendo enviada!", bg='light blue', font=("Helvetica", 35))
        #Utilizamos place para mostrar la etiqueta en la ventana
        etiqueta_total.place(x=215, y=150)
        #Crear una función para destruir una ventana con .destroy()
        def kill1 (event):
            v8.destroy()
        #Creamos un botón
        button_kill=Button(v8, text="Salir")
        #Enlazamos el botón a la acción kill1
        button_kill.bind("<Button-1>", kill1)
        #Utilizamos place para mostrar el botón en la ventana
        button_kill.place(x=910, y=420)
    #Creamos un botón
    button_ordenar2=Button(v3, text="Ordenar")
    #Enlazamos el botón a la acción end1
    button_ordenar2.bind("<Button-1>", end1)
    #Utilizamos place para mostrar el botón en la ventana
    button_ordenar2.place(x=870, y=720)
#Para crear un botón con una imagen definimos al archivo a utilizar
image=PhotoImage(file="marca2.gif")
#Creamos el botón y definimos que image es igual a la imagen a utilizar
button_marca2=Button(image=image)
#Enlazamos el botón a la acción underarmour
button_marca2.bind("<Button-1>", underarmour)
#Utilizamos place para mostrar el botón en la pantalla
button_marca2.place(x=315, y=325)

#Creamos una función para ir a otra ventana
def adidas (event):
    v2 = Toplevel()
    v2.title ("Fast Delivery")
    v2.configure(background='light blue')
    v2.geometry("950x750")
    v2.resizable(0,0)

    #Creamos una etiqueta para mostrar a qué catálogo pertenece
    label_marca1=Label(v2, text="Catálogo Adidas", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_marca1.place(x=0, y=0)

    #Creamos una etiqueta para mostrar que el usuario está en línea
    label_usuario1=Label(v2, text="Usuario en línea", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_usuario1.place(x=830, y=0)

    #Definimos el archivo a utilizar 
    imagen3=PhotoImage(file="balón_adidas1.gif")
    #Creamos una etiqueta e indicamos la imagen que se encontrará dentro de la etiqueta
    balónadidas=Label(v2, image=imagen3)
    #Definimos que en la etiqueta se va a msotrar la imagen antes especificada
    balónadidas.image=imagen3
    #Utilizamos place para mostrar la etiqueta en la ventana
    balónadidas.place(x=200, y=92)

    #Definimos el archivo a utilizar
    imagen4=PhotoImage(file="camiseta_adidas1.gif")
    #Creamos una etiqueta e indicamos la imagen que se encontrará dentro de la etiqueta
    camisetaadidas=Label(v2, image=imagen4)
    #Definimos que en la etiqueta se va a msotrar la imagen antes especificada
    camisetaadidas.image=imagen4
    #Utilizamos place para mostrar la etiqueta en la ventana
    camisetaadidas.place(x=445, y=92)

    imagen5=PhotoImage(file="gorra_adidas1.gif")
    #Creamos una etiqueta e indicamos la imagen que se encontrará dentro de la etiqueta
    gorraadidas=Label(v2, image=imagen5)
    #Definimos que en la etiqueta se va a msotrar la imagen antes especificada
    gorraadidas.image=imagen5
    #Utilizamos place para mostrar la etiqueta en la ventana
    gorraadidas.place(x=670, y=92)

    imagen6=PhotoImage(file="mochila_adidas1.gif")
    #Creamos una etiqueta e indicamos la imagen que se encontrará dentro de la etiqueta
    mochilaadidas=Label(v2, image=imagen6)
    #Definimos que en la etiqueta se va a msotrar la imagen antes especificada
    mochilaadidas.image=imagen6
    #Utilizamos place para mostrar la etiqueta en la ventana
    mochilaadidas.place(x=200, y=234)

    imagen7=PhotoImage(file="pants_adidas1.gif")
    #Creamos una etiqueta e indicamos la imagen que se encontrará dentro de la etiqueta
    pantsadidas=Label(v2, image=imagen7)
    #Definimos que en la etiqueta se va a msotrar la imagen antes especificada
    pantsadidas.image=imagen7
    #Utilizamos place para mostrar la etiqueta en la ventana
    pantsadidas.place(x=445, y=234)

    imagen8=PhotoImage(file="sudadera_adidas1.gif")
    #Creamos una etiqueta e indicamos la imagen que se encontrará dentro de la etiqueta
    sudaderaadidas=Label(v2, image=imagen8)
    #Definimos que en la etiqueta se va a msotrar la imagen antes especificada
    sudaderaadidas.image=imagen8
    sudaderaadidas.place(x=670, y=234)

    imagen9=PhotoImage(file="balón1adidas.gif")
    #Creamos una etiqueta e indicamos la imagen que se encontrará dentro de la etiqueta
    balón1adidas=Label(v2, image=imagen9)
    #Definimos que en la etiqueta se va a msotrar la imagen antes especificada
    balón1adidas.image=imagen9
    #Utilizamos place para mostrar la etiqueta en la ventana
    balón1adidas.place(x=200, y=376)

    imagen10=PhotoImage(file="mochila1adidas.gif")
    #Creamos una etiqueta e indicamos la imagen que se encontrará dentro de la etiqueta
    mochila1adidas=Label(v2, image=imagen10)
    #Definimos que en la etiqueta se va a msotrar la imagen antes especificada
    mochila1adidas.image=imagen10
    #Utilizamos place para mostrar la etiqueta en la ventana
    mochila1adidas.place(x=445, y=376)

    imagen11=PhotoImage(file="tenis1adidas.gif")
    #Creamos una etiqueta e indicamos la imagen que se encontrará dentro de la etiqueta
    tenis1adidas=Label(v2, image=imagen11)
    #Definimos que en la etiqueta se va a msotrar la imagen antes especificada
    tenis1adidas.image=imagen11
    tenis1adidas.place(x=670, y=376)

    imagen12=PhotoImage(file="sudadera1adidas.gif")
    #Creamos una etiqueta e indicamos la imagen que se encontrará dentro de la etiqueta
    sudadera1adidas=Label(v2, image=imagen12)
    #Definimos que en la etiqueta se va a msotrar la imagen antes especificada
    sudadera1adidas.image=imagen12
    #Utilizamos place para mostrar la etiqueta en la ventana
    sudadera1adidas.place(x=200, y=518)

    imagen13=PhotoImage(file="camiseta1adidas.gif")
    #Creamos una etiqueta e indicamos la imagen que se encontrará dentro de la etiqueta
    camiseta1adidas=Label(v2, image=imagen13)
    #Definimos que en la etiqueta se va a msotrar la imagen antes especificada
    camiseta1adidas.image=imagen13
    #Utilizamos place para mostrar la etiqueta en la ventana
    camiseta1adidas.place(x=445, y=518)

    imagen14=PhotoImage(file="gorra1adidas.gif")
    #Creamos una etiqueta e indicamos la imagen que se encontrará dentro de la etiqueta
    gorra1adidas=Label(v2, image=imagen14)
    #Definimos que en la etiqueta se va a msotrar la imagen antes especificada
    gorra1adidas.image=imagen14
    #Utilizamos place para mostrar la etiqueta en la ventana
    gorra1adidas.place(x=670, y=518)

    #Creamos una etiqueta
    label_balón=Label(v2, text="Balón", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_balón.place(x=215, y=170)

    #Creamos una etiqueta
    label_camiseta=Label(v2, text="Camiseta", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_camiseta.place(x=450, y=170)

    #Creamos una etiqueta
    label_gorra=Label(v2, text="Gorra", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_gorra.place(x=682, y=170)

    #Creamos una etiqueta
    label_mochila=Label(v2, text="Mochila", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_mochila.place(x=208, y=312)

    #Creamos una etiqueta
    label_pants=Label(v2, text="Pants", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_pants.place(x=460, y=312)

    #Creamos una etiqueta
    label_sudadera=Label(v2, text="Chamarra", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_sudadera.place(x=672, y=312)

    #Creamos una etiqueta
    label_balón1=Label(v2, text="Balón", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_balón1.place(x=213, y=454)

    #Creamos una etiqueta
    label_mochila1=Label(v2, text="Mochila", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_mochila1.place(x=453, y=454)

    #Creamos una etiqueta
    label_tenis1=Label(v2, text="Tenis", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_tenis1.place(x=685, y=454)

    #Creamos una etiqueta
    label_sudadera1=Label(v2, text="Sudadera", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_sudadera1.place(x=202, y=596)

    #Creamos una etiqueta
    label_camiseta1=Label(v2, text="Camiseta", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_camiseta1.place(x=448, y=596)

    #Creamos una etiqueta
    label_gorra1=Label(v2, text="Gorra", bg='light blue')
    #Utilizamos place para mostrar la etiqueta en la ventana
    label_gorra1.place(x=685, y=596)

    #Creamos una entrada de texto
    entrypr=Entry(v2, bg='light blue')
    #Utilizamos place para mostrar la entrada de texto en la ventana
    entrypr.place(x=400, y=720)

    #Creamos una función para insertar una variable a nuestra entrada
    def click12 (event):
        entrypr.insert(0,text12)
    #Creamos nuestro botón
    button_balón=Button(v2, text="$499")
    #Le asignamos un valor a nuestra variable
    text12=("Balón = 499; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_balón.place(x=216, y=195)
    #Enlazamos el botón a la acción click12
    button_balón.bind("<Button-1>", click12)

    #Creamos una función para insertar una variable a nuestra entrada
    def click13 (event):
        entrypr.insert(0,text13)
    #Creamos nuestro botón
    button_camiseta=Button(v2, text="$599")
    #Le asignamos un valor a nuestra variable
    text13=("Camiseta = 599; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_camiseta.place(x=460, y=195)
    #Enlazamos el botón a la acción click13
    button_camiseta.bind("<Button-1>", click13)

    #Creamos una función para insertar una variable a nuestra entrada
    def click14 (event):
        entrypr.insert(0,text14)
    #Creamos nuestro botón
    button_gorra=Button(v2, text="$449")
    #Le asignamos un valor a nuestra variable
    text14=("Gorra = 449; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_gorra.place(x=684, y=195)
    #Enlazamos el botón a la acción click14
    button_gorra.bind("<Button-1>", click14)

    #Creamos una función para insertar una variable a nuestra entrada
    def click15 (event):
        entrypr.insert(0,text15)
    #Creamos nuestro botón
    button_mochila=Button(v2, text="$599")
    #Le asignamos un valor a nuestra variable
    text15=("Mochila = 599; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_mochila.place(x=216, y=337)
    #Enlazamos el botón a la acción click15
    button_mochila.bind("<Button-1>", click15)

    #Creamos una función para insertar una variable a nuestra entrada
    def click16 (event):
        entrypr.insert(0,text16)
    #Creamos nuestro botón
    button_pants=Button(v2, text="$949")
    #Le asignamos un valor a nuestra variable
    text16=("Pants = 949; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_pants.place(x=460, y=337)
    #Enlazamos el botón a la acción click16
    button_pants.bind("<Button-1>", click16)

    #Creamos una función para insertar una variable a nuestra entrada
    def click17 (event):
        entrypr.insert(0,text17)
    #Creamos nuestro botón
    button_sudadera=Button(v2, text="$1,399")
    #Le asignamos un valor a nuestra variable
    text17=("Sudadera = 1399; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_sudadera.place(x=681, y=337)
    #Enlazamos el botón a la acción click17
    button_sudadera.bind("<Button-1>", click17)

    #Creamos una función para insertar una variable a nuestra entrada
    def click18 (event):
        entrypr.insert(0,text18)
    #Creamos nuestro botón
    button_balón1=Button(v2, text="$499")
    #Le asignamos un valor a nuestra variable
    text18=("Balón = 499; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_balón1.place(x=215, y=479)
    #Enlazamos el botón a la acción click18
    button_balón1.bind("<Button-1>", click18)

    #Creamos una función para insertar una variable a nuestra entrada
    def click19 (event):
        entrypr.insert(0,text19)
    #Creamos nuestro botón
    button_mochila1=Button(v2, text="$599")
    #Le asignamos un valor a nuestra variable
    text19=("Mochila = 599; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_mochila1.place(x=460, y=479)
    #Enlazamos el botón a la acción click19
    button_mochila1.bind("<Button-1>", click19)

    #Creamos una función para insertar una variable a nuestra entrada
    def click20 (event):
        entrypr.insert(0,text20)
    #Creamos nuestro botón
    button_tenis1=Button(v2, text="$1,499")
    #Le asignamos un valor a nuestra variable
    text20=("Tenis = 1499; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_tenis1.place(x=680, y=479)
    #Enlazamos el botón a la acción click20
    button_tenis1.bind("<Button-1>", click20)

    #Creamos una función para insertar una variable a nuestra entrada
    def click21 (event):
        entrypr.insert(0,text21)
    #Creamos nuestro botón
    button_sudadera1=Button(v2, text="$599")
    #Le asignamos un valor a nuestra variable
    text21=("Sudadera = 599; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_sudadera1.place(x=215, y=621)
    #Enlazamos el botón a la acción click21
    button_sudadera1.bind("<Button-1>", click21)

    #Creamos una función para insertar una variable a nuestra entrada
    def click22 (event):
        entrypr.insert(0,text22)
    #Creamos nuestro botón
    button_camiseta1=Button(v2, text="$949")
    #Le asignamos un valor a nuestra variable
    text22=("Camiseta = 949; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_camiseta1.place(x=460, y=621)
    #Enlazamos el botón a la acción click22
    button_camiseta1.bind("<Button-1>", click22)

    #Creamos una función para insertar una variable a nuestra entrada
    def click23 (event):
        entrypr.insert(0,text23)
    #Creamos nuestro botón
    button_gorra1=Button(v2, text="$1,399")
    #Le asignamos un valor a nuestra variable
    text23=("Gorra = 1399; ")
    #Utilizamos place para mostrar el botón en la ventana
    button_gorra1.place(x=681, y=621)
    #Enlazamos el botón a la acción click23
    button_gorra1.bind("<Button-1>", click23)
    #Creamos una función para destruir una ventana con .destroy()
    def atrás5 (event):
        v2.destroy()
    #Creamos un botón
    button_atrás=Button(v2, text="Atrás")
    #Enlazamos el botón a la acción atrás5
    button_atrás.bind("<Button-1>", atrás5)
    #Utilizamos place para mostrar el botón en la ventana
    button_atrás.place(x=10, y=720)

    #Creamos una función para destruir una ventana e ir a otra
    def end1 (event):
        v2.destroy()
        v8 = Toplevel()
        v8.title ("Fast Delivery")
        v8.configure(background='light blue')
        v8.geometry("950x450")
        v8.resizable(0,0)

        #Creamos una etiqueta
        etiqueta_total=Label(v8, text="Tu orden está siendo enviada!", bg='light blue', font=("Helvetica", 35))
        #Utilizamos place para mostrar la etiqueta en la ventana
        etiqueta_total.place(x=215, y=150)

        #Creamos una función para destruir una ventana con .destroy()
        def kill1 (event):
                v8.destroy()
        #Creamos un botón
        button_kill=Button(v8, text="Salir")
        #Enlazamos el botón a la acción kill1
        button_kill.bind("<Button-1>", kill1)
        #Utilizamos place para mostrar el botón en la ventana
        button_kill.place(x=910, y=420)
    #Creamos un botón
    button_ordenar3=Button(v2, text="Ordenar")
    #Enlazamos el botón a la acción end1
    button_ordenar3.bind("<Button-1>", end1)
    #Utilizamos place para mostrar el botón en la ventana
    button_ordenar3.place(x=870, y=720)
#Para usar una imagen como botón, debemos definir el archivo a utilizar
imagen1=PhotoImage(file="marca3.gif")
#Creamos el botón y definimos la imagen a utilizar
button_marca3=Button(image=imagen1)
#Enlazamos el botón a la acción adidas
button_marca3.bind("<Button-1>", adidas)
#Utilizamos place para mostrar el botón en la ventana
button_marca3.place(x=505, y=325)

#Para usar una imagen como botón, debemos definir el archivo a utilizar
imagen2=PhotoImage(file="marca4.gif")
#Creamos el botón y definimos la imagen a utilizar
button_marca4=Button(image=imagen2)
#Utilizamos place para mostrar el botón en la ventana
button_marca4.place(x=695, y=325)
#Llamamos al proceso principal
v.mainloop()
