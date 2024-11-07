import json
import os
import subprocess

# Leer el archivo JSON
with open('bots.json', 'r') as file:
    data = json.load(file)

# configuracion de carpeta padre donde esta cada carpeta para cada bot (e.g. /home/mac/botrsi) si las carpetas son /home/mac/botrsi/ada o /home/mac/botrsi/doge
base_path = "" 
# configuracion de entorno virtual (e.g. /home/mac/rsi/bin/activate) - Activar entorno virtual --> echo $VIRTUAL_ENV --> agregar '/bin/activate' al final al resultado
venv_path = "" 

# Iterar sobre cada bot en el JSON
for bot in data['bots']:
    folder_name = bot['name']
    is_active = bot['active']
    script_path = os.path.join(base_path, folder_name, 'botrsi_bybit.py')
    folder_path = os.path.join(base_path, folder_name)

    # Solo proceder si la carpeta está activa
    if is_active:
        # Comprobar si la carpeta existe y si el script está presente
        if os.path.isdir(folder_path) and os.path.isfile(script_path):
            # Comando para crear una nueva sesión tmux, cambiar al directorio y ejecutar el script
            session_name = folder_name
            command = f"tmux new-session -d -s {session_name} 'cd {folder_path} && source {venv_path} && python3 {script_path}'"

            # Ejecutar el comando
            subprocess.run(command, shell=True)
            print(f"Sesión tmux '{session_name}' creada y ejecutando '{script_path}' en el directorio '{folder_path}' en el entorno virtual.")
        else:
            print(f"Carpeta '{folder_name}' no existe o no se encontró 'botrsi_bybit.py'.")
    else:
        print(f"Sesión tmux para '{folder_name}' no se creará (inactiva).")

print("Todas las sesiones tmux activas han sido iniciadas.")
