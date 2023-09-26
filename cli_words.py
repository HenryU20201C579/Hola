import pandas as pd
import numpy as np
import lxml

import time
import random

from colorama import init, Fore
init(autoreset=True)

link = pd.read_html('https://www.berlitz.com/es-mx/blog/100-palabras-mas-usadas-en-ingles')
data = link[0]

data = data[[1, 2]]

en =  data[1]
esp = data[2]

# Duración en segundos del bucle (1 minuto = 60 segundos)
duracion_en_segundos = 30

# Tiempo de inicio del bucle
tiempo_inicio = time.time()

#variable random
ran = random.randint(1, len(en))

# Bucle while que se ejecutará durante 1 minuto
while (time.time() - tiempo_inicio) < duracion_en_segundos:
    ran = random.randint(1, len(en))
    print(en[ran].lower())
    rpt = input()
    if esp[ran].lower() == rpt:
        print(Fore.GREEN + "Correcto", "\n")
    else:
        print(Fore.RED + "Incorrecto -->",esp[ran], "\n")


