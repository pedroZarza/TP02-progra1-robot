# Bitácora técnica — TP02

**Alumnos:** Pedro Zarza | Lisandro Tosini **Fecha:** 15/10/2026.

## Entorno de trabajo

| Elemento | Información |
|---|---|
| Plataforma | WSL sobre Windows |
| Distribución | Ubuntu 24.04.4 LTS (Noble Numbat) |
| Arquitectura | x86_64 (64 bits) |
| Shell | zsh |
| Python | 3.12.3 |
| pip | 24.0 |
| Git | 2.43.0 |
| MuJoCo | 3.16.0 |
| Entorno virtual | `.venv`, dentro de la carpeta del TP |
| Robot utilizado | Unitree Go2 |
| IDE | VSCODE  Cursor |

## Análisis de documentación
El laboratorio requiere Python, MuJoCo y los modelos del robot. La versión mínima exacta aplicable debe confirmarse en la documentación actual del repositorio; el PDF original indica Python 3.10 o superior. No requiere instalar CycloneDDS ni el SDK oficial de Unitree. La versión actual emplea `robot.py` como puente y movimientos definidos por velocidad y tiempo, mientras el PDF original utiliza una interfaz diferente.

## Acciones confirmadas
| Nº | Acción | Resultado | Problema / tratamiento | Estado |
|---:|---|---|---|---|
| 1 | Configuración y verificación del entorno | Ubuntu 24.04.4 LTS en WSL, arquitectura x86_64; Python 3.12.3, pip 24.0, Git 2.43.0 y MuJoCo 3.16.0 | Entorno virtual `.venv` activado y versiones verificadas en terminal | Completado |
| 2 | Desarrollo del controlador sobre la plantilla | Se completaron las cuatro funciones | Separación de validación, ejecución, historial y reporte | Implementado según código compartido |
| 3 | Ejecución de `MISION_BASICA` | 4 recibidos, 4 ejecutados, 0 rechazados | Sin rechazos en el reporte | Completado |
| 4 | Ejecución de `MISION_CON_ERRORES` | 11 recibidos, 4 ejecutados, 7 rechazados | Rechazos controlados; la misión continuó | Completado |
| 5 | Ejecución de `MISION_CUADRADO` | 9 recibidos, 9 ejecutados, 0 rechazados | Sin rechazos en el reporte | Completado |
| 6 | Ejecución de `MISION_GUARDIAN` (misión propia) | 10 recibidos, 10 ejecutados, 0 rechazados; distancia planificada de 1,2 m y tiempo de movimientos de 18,56 s | Avance, inspección lateral, retroceso al punto inicial aproximado y repetición de la inspección | Completado |

## Misión propia: El perro guardián

El robot avanzó 0,6 m, realizó giros para inspeccionar ambos lados
y recuperó su orientación inicial. Luego retrocedió 0,6 m para
regresar aproximadamente al punto de partida, repitió la inspección,
saludó y se detuvo.

Los diez comandos fueron aceptados. La distancia planificada total
fue de 1,2 m y el tiempo acumulado de avances y giros fue de 18,56 s.
El regreso se calculó mediante velocidad y tiempo, sin medir la
posición real del modelo.
