# TP02 — Programación I: controlador de misiones

**Alumnos:** Pedro Zarza | Lisandro Tosini
**Comisión:** Jueves Noche
**Robot:** Unitree Go2  
**Entorno utilizado:** WSL sobre Windows.

## Objetivo
Desarrollar un controlador modular que reciba misiones como listas de tuplas, valide sus comandos, ejecute las acciones permitidas y registre los resultados en una lista de diccionarios para generar un reporte final.

## Arquitectura
`mi_tp02.py` utiliza la clase `Robot` de `robot.py`. Este puente conecta mediante un socket local en `127.0.0.1` con el simulador MuJoCo y el modelo Go2. El SDK oficial de Unitree y CycloneDDS no son necesarios para esta versión del laboratorio. `robot.py` no debe modificarse.

## Diseño Top-Down
| Función | Entrada | Salida y responsabilidad |
|---|---|---|
| `main()` | Sin parámetros | Conecta, inicia la misión, genera el reporte y cierra la conexión. |
| `comando_es_valido(comando)` | Tupla de comando | Booleano: verifica estructura, nombre, cantidad y tipos de parámetros, valores finitos y tiempo no negativo. |
| `ejecutar_comando(robot, comando)` | Robot y comando validado | Texto de resultado; ejecuta el método correspondiente y captura `ErrorDeSeguridad`. |
| `ejecutar_mision(robot, mision, historial)` | Robot, lista de tuplas y lista mutable | Modifica el historial; recorre con `for` y omite inválidos con `continue`. |
| `generar_reporte(historial)` | Lista de registros | Imprime cantidades, distancia, tiempo y motivos de rechazo. |

Este esquema documenta la estructura del código desarrollado; no se presenta como evidencia de un diagrama realizado antes de programar.

## Ejecución en WSL
Desde `05LaboratoriosTPs/TP02_Programacion_I`, preparar el entorno según `INSTALACION.md` y `LEEME_ESTUDIANTE.md`. Secuencia de referencia:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install mujoco
python -c "import mujoco; print(mujoco.__version__)"
bash INICIAR_SIMULADOR.sh
```

Seleccionar `2 - Go2`. En otra terminal, desde la misma carpeta:

```bash
source .venv/bin/activate
python mi_desarrollo/mi_tp02.py
```

En `main()`, cambiar la misión pasada a `ejecutar_mision`. Cada ejecución comienza con `historial = []`. La misión cambia como dato, sin modificar las cuatro funciones.

## Límites informados por el puente durante las pruebas
- Velocidad lineal máxima: **0,2 m/s**.
- Velocidad angular máxima: **0,5 rad/s** en magnitud.
- Tiempo máximo por orden: **10 s**.

Estos son los límites observados en los reportes actuales; no los valores del ejemplo antiguo del PDF.

## Resultados obtenidos
| Misión | Recibidos | Ejecutados | Rechazados | Distancia planificada ejecutada | Tiempo de movimientos ejecutados |
|---|---:|---:|---:|---:|---:|
| `MISION_BASICA` | 4 | 4 | 0 | 0,8 m | 7,14 s |
| `MISION_CON_ERRORES` | 11 | 4 | 7 | 0,4 m | 5,14 s |
| `MISION_CUADRADO` | 9 | 9 | 0 | 1,6 m | 20,56 s |

Los resultados provienen de las salidas de consola aportadas por el alumno. La distancia se calcula como `abs(velocidad) * tiempo` para avances aceptados. El tiempo suma las duraciones de avances y giros aceptados: no mide la duración real completa ni incluye el saludo. La distancia tampoco constituye una medición de la trayectoria física del modelo.

### Misión básica
Se aceptaron dos avances, un giro y una detención. Cada avance representa `0,2 × 2 = 0,4 m`; la suma es 0,8 m. El tiempo es `2 + 3,14 + 2 = 7,14 s`.

### Misión cuadrado
Se aceptaron cuatro avances, cuatro giros y una detención. La distancia planificada suma 1,6 m. Cada giro representa `-0,5 × 3,14 = -1,57 rad`, aproximadamente 90 grados hacia la derecha. La secuencia planifica un cuadrado; la consola por sí sola no verifica el cierre geométrico de la trayectoria.

### Misión con errores
Se aceptaron un avance, un giro, el saludo y la detención. Los siete rechazos fueron:

| Comando | Motivo identificado |
|---|---|
| `('avanzar', 0.9, 2.0)` | Supera 0,2 m/s; rechazado por el puente. |
| `('avanzar', 0.2, 50.0)` | Supera 10 s por orden; rechazado por el puente. |
| `('girar', 3.0, 2.0)` | Supera 0,5 rad/s; rechazado por el puente. |
| `('volar', 0.2, 1.0)` | Nombre de comando desconocido. |
| `('avanzar', 'rapido', 2.0)` | Velocidad de tipo texto. |
| `('avanzar', 0.2)` | Falta un parámetro. |
| `('avanzar', 0.2, -3.0)` | Tiempo negativo. |

La validación de formato devuelve un mensaje general en el programa. La tabla detalla la causa de cada entrada. La ejecución posterior de `saludar` y `detenerse` demuestra que los rechazos no abortaron la misión.

## Archivos y pendientes de entrega
- `BITACORA.md`: reconstrucción del proceso confirmado.
- `PROBLEMAS.md`: análisis de rechazos y datos aún no informados.
- `CONCLUSIONES.md`: reflexión técnica.
- Agregar el código final real, las capturas y la URL del repositorio de entrega.
- Completar versiones del entorno y comisión.
- Crear y ejecutar una misión propia con al menos cinco comandos y uno inválido; incorporar su resultado. No se aportó todavía esa ejecución.

## Fuentes de la actividad
- `TP02_Programacion_I.pdf`.
- `Orientador_TP02_Robot_Unitree_Programacion_I.pdf`.
- Material de cátedra: https://github.com/tsamaan/UadeRobotLab
