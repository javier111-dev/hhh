#javier gajardo

compradores=[]
stock= {1:150, 2:100}

def mostrar_stock():
   print("\n--- mostrar stock---")
   print(f"funcion 1(viernes):{stock [1]}entrada disponible")
   print(f"funcion 2 (sabado):{stock[2]} entrada disponible")
    


def menu_principal(opciones):
    print("---AUTOATENCION---")
    print("1. comprar entradas cats")
    print("2. cambio de funcion")
    print("3.mostrar stock de funcioes")
    print("4.salir")

def comprar_entradas():
    print("n\--comprar entradas cat---")
    nombre= input("nombre del comprador").strip()

    if nombre in compradores:
        print("error: nombre ya registrado")
        return

    print("seleccione funcion:") 
    print ("1. cats dia viernes({}entradas").format(stock[1])
    print("2. cats dia sabado({}entradas").format(stock[2])

    try:
        funcion=int(input("funcion (1 o 2):"))
    except ValueError:
        print("error:opcion de funcion invalida")
        return

    if funcion not in [1,2]:
        print("opcion de funcion erronea")

    if stock[funcion]:    
        print("no hay stock disponible")

    compradores[nombre] = funcion
    stock[funcion] -=1
    print(f"entrada registrada en funcion{funcion}")
    print(f"entrada 1(viernes):{stock[1]}")
    print(f"entrada 2 (sabado):{stock[2]}")

def cambiar_funcion():
    print("n\---cambio de funcion")
    nombre= input("nombre del comprador:").strip()

    if nombre not in compradores:
        print("error: comprador no encontrado")
        return
    
    funcion_actual= compradores[nombre]
    funcion_nueva= 2 if funcion_actual ==1 else 1

    print(f"cambiar de funcion {funcion_actual} a { funcion_nueva} (S/N):", end="")
    confirmacion= input().strip().lower()

    if confirmacion !='s':
        print("cambio cancelado")
        return
    
    if stock[funcion_nueva]<=0:
        print("error: no hay stock disponible en la nueva funcion")
        return
    
    compradores[nombre]=funcion_nueva
    stock[funcion_actual] +=1
    stock[funcion_nueva] -=1
    print(f"cambio realizado exitosamente.nuevo stock:")
    print(f"funcion 1 (viernes):{stock[1]}entradas disponibles")
    print(f"funcion 2 (sabado):{stock[2]} entradas disponibles")

def main():
    while True:
        menu_principal()
        try:
            opcion= int (input)("seleccione una opcion")
        except ValueError:
            print("error: opcion invalida")
            continue 

        if opcion == 1:
            comprar_entradas
        elif opcion ==2:
            cambiar_funcion
        elif opcion==3:
            mostrar_stock()  
        elif opcion ==4:
            print ("saliendo de la pagina") 
            break
        else:
            print ("opcion invalida. intentelo mas tarde")

main()            
