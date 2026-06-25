def menu():
    print("1. reserva cupo de python basico ")
    print("2. reserva cupo ciencias de datos")
    print("3. reserva cupos bases google cloud")
    print("4. ver cupos disponibles")
    print("5. salir ")

diccionario_python_basico={}
diccionario_google={}
diccionario_google_cloud={}

def validar_disponibilidad(taller,cupos):
    if len(taller) >= cupos:
        return False
    return True

def validacion_codigo(codigo,caracteres,cant_mayusculas,cant_numeros):
    if len(codigo)< caracteres:
        return False
    
    contador_mayusculas=0
    contador_numeros=0

    for caracteres in codigo:
        if caracteres.isupper():
            contador_mayusculas += 1
        if caracteres.isnumeric():
            contador_numeros += 1
    
    if contador_mayusculas < cant_mayusculas:
        return False
    if contador_numeros < cant_numeros:
        return False    
    
    return True

def reserva_python_basico():

    tipo_participacion=""
    nombre=""
    codigo_acceso=""
    registro_exitoso= True  # ✅ Bug 1: inicializar en True por defecto

    nombre=input("ingrese su nombre: ")
    if nombre in diccionario_python_basico:
        print("este usuario ya esta registrado ")
        registro_exitoso= False

    while tipo_participacion != "p" and tipo_participacion!="o":  # ✅ Bug 2: comparar en minúsculas
        tipo_participacion=input("ingrese el tipo de participacion (P/O): ").strip().lower()
        if tipo_participacion != "p" and tipo_participacion!="o":
            print("el tipo de participacion solo debe ser presencial o online ")
    while not validacion_codigo(codigo_acceso,6,1,2):
        codigo_acceso=input("ingrese el tipo de acceso:")
        if not validacion_codigo(codigo_acceso, 6, 1,2):
            print ("ingreso invalido: el codigo debe tener al menos 6 caracteres")

    if validar_disponibilidad(diccionario_python_basico,100):  # ✅ Bug 3: usar el diccionario
        if registro_exitoso :
            diccionario_python_basico[nombre]= [tipo_participacion, codigo_acceso]  # ✅ Bug 3
        else:
            print("este usuario ya se encuentra en el registro")
    else:
        print("no quedan cupos")

def reserva_bases_google():
    tipo_participacion=""
    nombre=""
    codigo_acceso=""
    registro_exitoso= True  # ✅ Bug 1 (misma corrección)

    nombre=input("ingrese su nombre: ")
    if nombre in diccionario_google:
        print("este usuario ya esta registrado ")
        registro_exitoso= False

    while tipo_participacion != "l" and tipo_participacion!="c":  # ✅ Bug 4: minúsculas
        tipo_participacion=input("ingrese el tipo de participacion (L/C): ").strip().lower()
        if tipo_participacion != "l" and tipo_participacion!="c":
            print("el tipo de participacion solo debe ser presencial o online ")
    while not validacion_codigo(codigo_acceso,7,2,1):
        codigo_acceso=input("ingrese el tipo de acceso:")
        if not validacion_codigo(codigo_acceso, 7,2,1):
            print ("ingreso invalido: el codigo debe tener al menos 7 caracteres")

    if validar_disponibilidad(diccionario_google,80):  # ✅ Bug 4
        if registro_exitoso :
            print("registro exitoso")
            diccionario_google[nombre]= ["0", codigo_acceso]  # ✅ Bug 4
        else:
            print("este usuario ya se encuentra en el registro")
    else:
        print("no quedan cupos")

def reserva_google_cloud():
    nombre=""
    codigo_acceso=""
    registro_exitoso= True  # ✅ Bug 1 (misma corrección)

    nombre=input("ingrese su nombre: ")
    if nombre in diccionario_google_cloud:  # ✅ Bug 5: diccionario correcto
        print("este usuario ya esta registrado ")
        registro_exitoso= False
    while not validacion_codigo(codigo_acceso,7,2,1):
        codigo_acceso=input("ingrese el tipo de acceso:")
        if not validacion_codigo(codigo_acceso, 7,2,1):
            print ("ingreso invalido: el codigo debe tener al menos 7 caracteres")

    if validar_disponibilidad(diccionario_google_cloud,40):  # ✅ Bug 5
        if registro_exitoso :
            diccionario_google_cloud[nombre]= ["0", codigo_acceso]  # ✅ Bug 5
        else:
            print("este usuario ya se encuentra en el registro")
    else:
        print("no quedan cupos ")
    
def consultar_cupos():
    print("cupos disponibles")
    print(f"python basico: {100-len(diccionario_python_basico)} cupos")   # ✅ Bug 6
    print(f"bases google: {80-len(diccionario_google)} cupos")            # ✅ Bug 6
    print(f"google cloud: {40-len(diccionario_google_cloud)} cupos")      # ✅ Bug 6

def salir():
    print("saliendo del programa")
    return False


progama_corriendo = True
while progama_corriendo:
    menu()
    opcion=input("ingrese una opcion: ")

    match opcion:
        case "1":
            reserva_python_basico()
        case "2":
            reserva_bases_google()
        case "3":
            reserva_google_cloud()
        case "4":
            consultar_cupos()
        case "5":
            progama_corriendo= salir()
        case others:
            print("opcion invalida")