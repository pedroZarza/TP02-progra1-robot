# =====================================================================
# TP02 - Programacion I
# Controlador de misiones
#
# Nombre y apellido: Pedro Zarza, Lisandro Tosini
# Comision: .....................................
#
# Antes de ejecutar, abrir el simulador y seleccionar Go2.
# =====================================================================

from robot import ErrorDeSeguridad, Robot
from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO, MISION_GUARDIAN


# =====================================================================
# PARTE 1 - Validar un comando
# =====================================================================
def comando_es_valido(comando):
    """Verifica el formato y los parametros. Devuelve True o False."""

    if not isinstance(comando, tuple) or len(comando) == 0:
        return False

    tipo = comando[0]

    if tipo not in ("avanzar", "girar", "detenerse", "saludar"):
        return False

    if tipo in ("detenerse", "saludar"):
        return len(comando) == 1

    if len(comando) != 3:
        return False

    velocidad, tiempo = comando[1], comando[2]

    # Evita aceptar textos y booleanos como parametros numericos.
    if type(velocidad) not in (int, float):
        return False

    if type(tiempo) not in (int, float):
        return False

    # Rechaza valores infinitos y NaN.
    if not (-float("inf") < velocidad < float("inf")):
        return False

    return 0 <= tiempo < float("inf")


# =====================================================================
# PARTE 2 - Ejecutar un comando
# =====================================================================
def ejecutar_comando(robot, comando):
    """Ejecuta un comando y devuelve un texto con el resultado."""

    tipo = comando[0]

    try:
        if tipo == "avanzar":
            robot.avanzar(velocidad=comando[1], tiempo=comando[2])

        elif tipo == "girar":
            robot.girar(velocidad=comando[1], tiempo=comando[2])

        elif tipo == "detenerse":
            robot.detenerse()

        elif tipo == "saludar":
            robot.saludar()

        return "OK: comando ejecutado"

    except ErrorDeSeguridad as error:
        return f"RECHAZADO: {error}"


# =====================================================================
# PARTE 3 - Recorrer la mision entera
# =====================================================================
def ejecutar_mision(robot, mision, historial):
    """Procesa la mision y registra comandos ejecutados y rechazados."""

    for comando in mision:
        if not comando_es_valido(comando):
            motivo = (
                "Formato invalido: se requiere una tupla con un comando "
                "conocido, cantidad correcta de parametros, velocidad "
                "numerica y tiempo numerico no negativo."
            )

            historial.append({
                "comando": comando,
                "ejecutado": False,
                "motivo": motivo,
                "distancia": 0,
                "tiempo": 0,
            })

            print(f"[RECHAZADO] {comando}: {motivo}")
            continue
        
        resultado = ejecutar_comando(robot, comando)
        ejecutado = resultado.startswith("OK:")

        distancia = 0
        tiempo = 0

        if ejecutado and comando[0] in ("avanzar", "girar"):
            tiempo = comando[2]

            if comando[0] == "avanzar":
                distancia = abs(comando[1]) * tiempo

        historial.append({
            "comando": comando,
            "ejecutado": ejecutado,
            "motivo": "" if ejecutado else resultado,
            "distancia": distancia,
            "tiempo": tiempo,
        })

        print(f"{comando}: {resultado}")


# =====================================================================
# PARTE 4 - El reporte final
# =====================================================================
def generar_reporte(historial):
    """Muestra cantidades, distancia, tiempo y motivos de rechazo."""

    ejecutados = 0
    distancia = 0
    tiempo = 0

    for registro in historial:
        if registro["ejecutado"]:
            ejecutados += 1

        distancia += registro["distancia"]
        tiempo += registro["tiempo"]

    print("\n========== REPORTE ==========")
    print(f"Comandos recibidos: {len(historial)}")
    print(f"Comandos ejecutados: {ejecutados}")
    print(f"Comandos rechazados: {len(historial) - ejecutados}")
    print(f"Distancia planificada ejecutada: {round(distancia, 2)} m")
    print(f"Tiempo de movimientos ejecutados: {round(tiempo, 2)} s")

    for registro in historial:
        if not registro["ejecutado"]:
            print(f"- {registro['comando']}: {registro['motivo']}")

    print("=============================\n")


# =====================================================================
# PROGRAMA PRINCIPAL
# =====================================================================
def main():
    robot = Robot()
    robot.conectar()

    historial = []

    try:
        ejecutar_mision(robot, MISION_GUARDIAN , historial)
        generar_reporte(historial)
    finally:
        try:
            robot.detenerse()
        finally:
            robot.desconectar()


if __name__ == "__main__":
    main()