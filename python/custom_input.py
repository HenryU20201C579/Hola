import keyboard

def custom_input():
    input_text = ""

    while True:
        event = keyboard.read_event()
        
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "enter":
                # Si se presiona Enter, rompe el bucle y devuelve el texto ingresado
                break
            elif event.name == "space":
                # Si se presiona Space, agrega un espacio al texto
                input_text += " "
            else:
                # Agrega la tecla presionada al texto
                input_text += event.name

    return input_text

# Llama a la función personalizada para obtener la entrada
input_data = custom_input()

# Imprime la entrada recopilada
print("Entrada ingresada:", input_data)
