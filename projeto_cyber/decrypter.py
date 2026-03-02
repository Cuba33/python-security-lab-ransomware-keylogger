import os
from cryptography.fernet import Fernet

# 1. Carregar a chave que foi gerada pelo encrypter.py
with open("chave.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# 2. Descriptografar os arquivos na pasta alvo
pasta = "alvo"
for arquivo in os.listdir(pasta):
    if arquivo == "chave.key": # Não tentar descriptografar a própria chave
        continue
        
    caminho_completo = os.path.join(pasta, arquivo)
    
    with open(caminho_completo, "rb") as f:
        dados_criptografados = f.read()
    
    # Reverter a criptografia
    dados_originais = fernet.decrypt(dados_criptografados)
    
    with open(caminho_completo, "wb") as f:
        f.write(dados_originais)

print("Arquivos restaurados com sucesso!")