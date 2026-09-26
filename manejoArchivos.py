
cadenas_validas = []
cadenas_no_validas = []


def es_keyword(palabra):
    keywords = ["int", "char", "string"]
    if palabra in keywords:
        return True
    else:
        return False
    
def agrega_cadena(tipo,ident,val):
    cad = {"Tipo":tipo, "Identificador":ident, "Valor":val}
    cadenas_validas.append(cad)
    
    # Mostrar cadenas válidas
def mostrar_cadenas(contenido):
    found = False
    for cad in contenido:
        found = True
        print("Los datos de las cadenas validas son: ", cad)
    # PENDIENTE
    if found == False :
        print("No se registraron valores válidos.")

with open("Archivo1.txt", "r", encoding="UTF-8") as f:
    
    while True:
        contenido = f.read()
        if contenido == "":
            continue
        
        if contenido.endswith(';'):
            # Se utiliza para eliminar caracteres específicos
            # devolviendo una nueva cadena sin modificar la original. 
            contenido = contenido[:-1].strip()
            #Split separa las cadenas
            partes = contenido.split()

            if len(partes) == 2:
                tipo = partes[0]
                identificador = partes[1]
                # verificamos que el tipo de dato sea permitido 
                if es_keyword(tipo):
                    #Aqui se verifica que no se inicie con un digito
                    if identificador[0].isdigit():
                        cadenas_no_validas.append(contenido)
                    else:
                        print("cadena valida")
                        #Aqui se agrega la cadena, se deja en None porque puede llevar un valor o no.
                        agrega_cadena(tipo, identificador, None)
                else:
                    cadenas_no_validas.append(contenido)
            else:
                cadenas_no_validas.append(contenido)        
            
                    
                    
# Cuando termina el codigo se muestran las cadenas validas
mostrar_cadenas("Las cadenas valias son: ", cadenas_validas)
mostrar_cadenas("Las cadenas no validas son: ", cadenas_no_validas)
