def carda_pacientes():
    urgencia = []
    turno = []

    afiliado = int(input("Ingrese un numero de afiliado: "))
    while afiliado != -1:
        atencion = int(input("Ingrese el tipo de atencion (Urgencia = 0 | Turno = 1): "))
        if atencion == 0:
            urgencia.append(afiliado)
        elif atencion == 1:
            turno.append(afiliado)
        afiliado = int(input("Ingrese un numero de afiliado ( Finalizar la carga = -1 ): "))

    return urgencia,turno

def busqueda_afiliado(resultados):
    buscar_afiliado = int(input("Ingrese un numero de afiliado: "))
    while buscar_afiliado != -1:
        atendido_turno = 0
        atendido_urgente = 0
        for afiliado in resultados[0]:
            if buscar_afiliado == afiliado:
                atendido_urgente += 1
        for afiliado2 in resultados[1]:        
            if buscar_afiliado == afiliado2:
                atendido_turno += 1

        print(f"El afiliado numero {buscar_afiliado} se atendio por Urgencia: {atendido_urgente} y por Turno: {atendido_turno}")

        buscar_afiliado = int(input("Ingrese un numero de afiliado(ingresar -1 para salir): "))


def main():
    """Puto A"""
    resultados = carda_pacientes()
    urgente = resultados[0]
    turno = resultados[1]
    print("Listado de los pacientes")
    print("Urgencia                  Turno")
    print(f'{urgente}                     {turno}')

    """Puto B"""
    busqueda_afiliado(resultados)

if __name__ == "__main__":
    main()