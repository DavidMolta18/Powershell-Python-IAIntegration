import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
import google.generativeai as genai
import subprocess
import os

# Configura la API de GenAI
genai.configure(api_key="CLAVE_API_GEMINI")

# Configuración del modelo de generación
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

# Configuración de seguridad
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])

# Función para ejecutar comandos en Powershell
def execute_powershell_command_ise(message):
    try:
        process = subprocess.Popen([r'C:\\WINDOWS\\system32\WindowsPowerShell\\v1.0\\powershell.exe', f'{message}'], cwd=os.getcwd(), stdout=subprocess.PIPE)
        output, _ = process.communicate()
        return output.decode("utf-8")
    except Exception as e:
        return f"Error al ejecutar el comando, por favor ingresa un comando válido o inténtalo nuevamente."

# Función para obtener el prompt del usuario mediante una ventana emergente
def obtener_prompt():
    root = tk.Tk()

    # Configuración de la ventana emergente
    root.title("GENERADOR DE COMANDOS POWERSHELL V.1.0.0")
    root.attributes("-fullscreen", False)  # Pantalla completa
    root.configure(bg="white")  # Color de fondo blanco

    # Etiqueta de título
    tk.Label(root, text="Introduce tu prompt:", font=("Arial", 36, "bold"), bg="white").pack(pady=50)

    # Entrada de texto para el prompt
    prompt_entry = tk.Text(root, font=("Arial", 24), width=50, height=5)
    prompt_entry.pack(pady=20)

    # Función para obtener el prompt y cerrar la ventana
    def get_prompt():
        prompt_value = prompt_entry.get("1.0", "end-1c")  # Obtener el texto del cuadro de texto
        root.destroy()  # Cerrar la ventana
        if prompt_value:
            proceso_generacion(prompt_value)

    # Botón para confirmar el prompt
    tk.Button(root, text="Aceptar", command=get_prompt, font=("Arial", 24)).pack()

    # Ejecutar el bucle de la ventana
    root.mainloop()

# Función para procesar el prompt y obtener la respuesta del modelo
def proceso_generacion(prompt):
    mensajeabuscar = f"Dame un comando en powershell para {prompt}" + "SOLO DAME EL COMANDO, no digas nada más. OMITE cualquier otro tipo de texto. solamente enviame el comando.No adornes la respuesta, solamente enviame el comando ya que estás siendo usado como generador de comandos automáticos. Intenta hacerlo lo más conciso posible, además de que corra en todos los powershells. NO PONGAS NINGUN OTRO TIPO DE TEXTO, SOLAMENTE ENVIAME EL COMANDO POR FAVOR. COMO SI FUESE A COPIAR Y PEGAR EN LA CONSOLA. QUITALE LO DE ```powershell."
    convo.send_message(mensajeabuscar)
    answer = convo.last.text

    # Ejecutar comando en Powershell
    output = execute_powershell_command_ise(answer)
    if output == "Error al ejecutar el comando, por favor ingresa un comando válido o inténtalo nuevamente.":
        answer = "Comando inválido, por favor ingresa tu prompt nuevamente"
        
    mostrar_respuesta(answer, output)

# Función para mostrar la respuesta del modelo y la salida del comando en una ventana emergente
def mostrar_respuesta(answer, output):
    root = tk.Tk()

    # Configuración de la ventana emergente
    root.title("Respuesta y salida del comando")
    root.attributes("-fullscreen", True)  # Pantalla completa
    root.configure(bg="white")  # Color de fondo blanco

    # Etiqueta con el título
    tk.Label(root, text="Respuesta del modelo y salida del comando en Powershell", font=("Arial", 30, "bold"), bg="white").pack(pady=(50, 20))

    # Frame para la tabla
    frame = tk.Frame(root, bg="white")
    frame.pack()

    # Etiqueta con la respuesta del modelo
    tk.Label(frame, text="Respuesta del modelo:", font=("Arial", 24, "bold"), bg="white").grid(row=0, column=0, sticky="w", padx=20, pady=10)
    tk.Label(frame, text=answer, font=("Arial", 18), bg="white", wraplength=1200, justify="left").grid(row=1, column=0, padx=20, pady=10, sticky="w")

    # Etiqueta con la salida del comando en Powershell
    tk.Label(frame, text="Salida del comando en Powershell:", font=("Arial", 24, "bold"), bg="white").grid(row=2, column=0, sticky="w", padx=20, pady=10)
    text_output = scrolledtext.ScrolledText(frame, width=80, height=20, wrap=tk.WORD)
    text_output.insert(tk.END, output)
    text_output.config(state="disabled")
    text_output.grid(row=3, column=0, padx=20, pady=10, sticky="w")

    # Botón para cerrar la ventana
    tk.Button(root, text="Cerrar", command=lambda: [root.destroy(), obtener_prompt()], font=("Arial", 18)).pack(pady=(20, 50))

    # Ejecutar el bucle de la ventana
    root.mainloop()

# Función principal para iniciar el proceso de interacción
def startmetodo():
    obtener_prompt()

# Inicia todo el programacion

startmetodo()
