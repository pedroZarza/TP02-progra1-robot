# Conclusión técnica — TP02

El controlador separa la validación de comandos, su ejecución, el recorrido de la misión y la generación del reporte. Esta descomposición Top-Down permite cambiar la misión sin reescribir las funciones: únicamente se sustituye la lista pasada a `ejecutar_mision`.

La misión se representa como una lista de tuplas y el historial como una lista de diccionarios. En Python los parámetros reciben referencias a objetos. Al agregar registros con `append`, la función modifica la misma lista mutable que conserva `main`, por lo que no es necesario retornarla. Los números son inmutables: reasignar un parámetro numérico dentro de una función no modifica la variable del llamador. Se emplean, entre otras, las funciones de biblioteca `len` y `round`.

Las tres misiones provistas se procesaron con los resultados esperados: la básica ejecutó sus cuatro comandos, la cuadrada sus nueve comandos y la misión con errores ejecutó cuatro y rechazó siete sin abortar. Los rechazos respondieron tanto a errores de formato como a límites de seguridad aplicados por el puente. Esto demuestra la continuidad del procesamiento y el registro de resultados.

La versión actual utiliza `robot.py` para comunicarse mediante un socket local con MuJoCo y el modelo Go2. No requiere el SDK oficial de Unitree ni CycloneDDS. Los movimientos se expresan con velocidad y tiempo, y los límites observados fueron 0,2 m/s, 0,5 rad/s y 10 s por orden.

Los reportes respaldan los hitos funcionales de conexión, ejecución de la misión básica, procesamiento de errores y reporte final, correspondientes a los niveles 7 a 10 del orientador. Para acreditar íntegramente el proceso faltan evidencias de las etapas previas y de la ventana gráfica. Tampoco se aportaron datos para identificar una dificultad principal de instalación, un intento fallido o una solución específica.

El próximo paso es ejecutar una misión propia con al menos cinco comandos y uno inválido, incorporar sus resultados y completar las evidencias y los datos del entorno. Para ejecutarla solo debe cambiarse la lista de comandos suministrada al controlador. Como mejora futura, se pueden detallar los motivos de validación y medir por separado el tiempo real total de ejecución.
