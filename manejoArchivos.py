cadenas_validas = []
cadenas_no_validas = []


def es_keyword(palabra):
    keywords = ["int", "char", "string"]
    return palabra in keywords


def agrega_cadena(tipo, ident, val):
    cad = {"Tipo": tipo, "Identificador": ident, "Valor": val}
    cadenas_validas.append(cad)


def mostrar_cadenas(contenido):
    found = False
    for cad in contenido:
        found = True
        print(cad)
    if not found:
        print("No se registraron valores.")


with open("Archivo1.txt", "r", encoding="UTF-8") as f:
    # Se lee el archivo línea por línea
    while True:
        linea = f.readline()

        # Si ya no hay más líneas, se termina
        if linea == "":
            break

        # Se eliminan espacios y saltos de línea ANTES de revisar el ';'
        contenido = linea.strip()

        if contenido == "":
            continue

        if contenido.endswith(';'):
            contenido = contenido[:-1].strip()
            partes = contenido.split()

            if len(partes) == 2:
                tipo, identificador = partes

                if es_keyword(tipo):
                    if identificador[0].isdigit():
                        cadenas_no_validas.append(contenido)
                    else:
                        print("Cadena valida")
                        agrega_cadena(tipo, identificador, None)
                else:
                    cadenas_no_validas.append(contenido)
            else:
                cadenas_no_validas.append(contenido)
        else:
            cadenas_no_validas.append(contenido)

print("Cadenas validas")
mostrar_cadenas(cadenas_validas)
print("Cadenas no validas")
mostrar_cadenas(cadenas_no_validas)
