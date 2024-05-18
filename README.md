# Generador de Comandos PowerShell con GenerativeAI

Este proyecto consiste en un generador de comandos PowerShell que utiliza un modelo de inteligencia artificial de GenerativeAI para sugerir comandos basados en un prompt proporcionado por el usuario. El sistema presenta una interfaz gráfica de usuario (GUI) que facilita la interacción y la obtención de resultados de forma intuitiva.

## Funcionamiento

1. **Configuración de la API de GenerativeAI**:
   - Antes de usar el programa, es necesario configurar la API de GenerativeAI con una clave de API válida.

2. **Interfaz Gráfica de Usuario (GUI)**:
   - Al ejecutar el programa, se abrirá una ventana que solicitará al usuario ingresar un prompt en el área de texto proporcionada.

3. **Generación de Comandos**:
   - Una vez que el usuario ingresa el prompt y presiona el botón de aceptar, el programa enviará el prompt al modelo de GenerativeAI para que genere un comando en PowerShell relacionado con el prompt.

4. **Ejecución del Comando en PowerShell**:
   - Después de recibir la respuesta del modelo, el programa ejecutará el comando en PowerShell utilizando la función `execute_powershell_command_ise()`.

5. **Visualización de Resultados**:
   - El programa mostrará la respuesta generada por el modelo y la salida del comando en PowerShell en una ventana emergente para que el usuario pueda ver los resultados de forma clara.

## Requisitos

- Python 3.x instalado en el sistema.
- Biblioteca `tkinter` para la interfaz gráfica.
- Biblioteca `google.generativeai` para la interacción con GenerativeAI.
- Acceso a la API de GenerativeAI con una clave API válida.
- Entorno de PowerShell instalado en el sistema.

## Uso

1. Clona o descarga el repositorio en tu máquina local.
2. Abre el archivo `main.py` en tu editor de código Python.
3. Configura la clave API de GenerativeAI en la sección correspondiente del código.
4. Ejecuta el programa usando el comando `python main.py`.
5. Ingresa el prompt en la ventana emergente y presiona "Aceptar".
6. Observa la respuesta generada por el modelo y la salida del comando en PowerShell.

## Contribución

Si deseas contribuir a este proyecto, puedes hacerlo siguiendo estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube los cambios a tu repositorio (`git push origin feature/nueva-funcionalidad`).
5. Crea un pull request en el repositorio original.

## Agradecimientos

Este proyecto se basa en la API de GenerativeAI, que proporciona capacidades avanzadas de generación de texto mediante inteligencia artificial.
