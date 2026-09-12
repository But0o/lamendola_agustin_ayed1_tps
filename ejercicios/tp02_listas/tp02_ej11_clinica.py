def carda_pacientes() -> tuple[list[int], list[int]]:
    """
    contrato

    Registra a los pacientes que llegan a la clínica, separándolos
    según si vinieron por una urgencia o con turno, hasta que se
    indica que no hay más pacientes para cargar.

    pre: no recibe parametros, se ingresan por teclado numeros de afiliado (enteros de 4 digitos) y el tipo de atencion (0 urgencia, 1 turno), finalizando con -1
    post: devuelve una tupla con la lista de afiliados atendidos por urgencia y la lista de afiliados atendidos por turno, en el orden en que llegaron
    """
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

def busqueda_afiliado(resultados: tuple[list[int], list[int]]) -> None:
    """
    contrato

    Permite buscar, por número de afiliado, cuántas veces esa
    persona fue atendida por urgencia y cuántas por turno.

    pre: resultados es una tupla con la lista de afiliados atendidos por urgencia y la lista de afiliados atendidos por turno
    post: por cada numero de afiliado ingresado por teclado, informa cuantas veces fue atendido por urgencia y por turno; finaliza al ingresar -1
    """
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


def main() -> None:
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
