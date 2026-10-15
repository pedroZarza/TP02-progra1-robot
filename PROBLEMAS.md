# Problemas y validaciones — TP02

## Instalación y configuración
No se aportaron mensajes de error de instalación ni soluciones aplicadas. Esto no permite afirmar que no hubo problemas. Completar esta sección si existieron, incluyendo comando, salida, interpretación, hipótesis, prueba y resultado.

## Diferencias entre documentos
El PDF original menciona `unitree_sdk_sim.py` y parámetros distintos para los movimientos. El orientador establece que prevalecen la plantilla y API actuales: `robot.py`, velocidad y tiempo. Se siguió esta interfaz en el código. El laboratorio no necesita el SDK oficial de Unitree ni CycloneDDS.

## Prueba deliberada de entradas incorrectas
Los siguientes son casos de prueba intencionales, no fallas de instalación:

| Entrada | Resultado esperado | Resultado observado | Estado |
|---|---|---|---|
| Velocidad lineal 0,9 m/s | Rechazar por superar 0,2 m/s | `ErrorDeSeguridad` capturado y registrado | Correcto |
| Duración de 50 s | Rechazar por superar 10 s | `ErrorDeSeguridad` capturado y registrado | Correcto |
| Velocidad angular 3 rad/s | Rechazar por superar 0,5 rad/s | `ErrorDeSeguridad` capturado y registrado | Correcto |
| Comando `volar` | Rechazar nombre desconocido | Validación devolvió falso | Correcto |
| Velocidad `rapido` | Rechazar tipo texto | Validación devolvió falso | Correcto |
| Avance sin tiempo | Rechazar cantidad de parámetros | Validación devolvió falso | Correcto |
| Tiempo de -3 s | Rechazar tiempo negativo | Validación devolvió falso | Correcto |

Después de los siete rechazos, se ejecutaron `saludar` y `detenerse`. No fue necesario corregir esas entradas de la misión provista: su finalidad era comprobar que el controlador las detectara y continuara.

## Mejora identificada
La validación de formato utiliza un mensaje común. Una mejora futura sería producir motivos específicos para cada error de estructura, tipo o rango. La distancia y el tiempo reportados son cálculos de los comandos aceptados, no mediciones de la simulación.
