import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import hashlib
import sys

# Função para gerar chave a partir de uma senha fornecida
def derive_key(password):
    # A chave derivada será de 32 bytes (256 bits)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b'some_salt', iterations=100000, backend=default_backend())
    return kdf.derive(password.encode())

# Função para criptografar um arquivo
def encrypt_file(filename, key):
    # Gerar o IV (Initialization Vector) para CBC
    iv = os.urandom(16)
    
    # Inicializar o algoritmo de criptografia (AES CBC)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Abrir o arquivo a ser criptografado
    with open(filename, 'rb') as f:
        file_data = f.read()
    
    # Padronizar o tamanho dos dados para ser múltiplo de 16 bytes
    padding = 16 - len(file_data) % 16
    file_data += bytes([padding] * padding)
    
    # Criptografar os dados
    encrypted_data = encryptor.update(file_data) + encryptor.finalize()
    
    # Codificar os dados criptografados em base64
    encrypted_data_base64 = base64.b64encode(encrypted_data).decode('utf-8')
    
    # Salvar o arquivo criptografado
    with open(filename, 'wb') as f:
        f.write(iv + encrypted_data_base64.encode())
    
    print(f'Arquivo {filename} criptografado com sucesso.')

# Função para descriptografar um arquivo
def decrypt_file(filename, key):
    # Abrir o arquivo criptografado
    with open(filename, 'rb') as f:
        encrypted_data = f.read()
    
    # Extrair o IV (primeiros 16 bytes)
    iv = encrypted_data[:16]
    encrypted_data_base64 = encrypted_data[16:]
    
    # Decodificar os dados base64
    encrypted_data = base64.b64decode(encrypted_data_base64)
    
    # Inicializar o algoritmo de criptografia (AES CBC)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Descriptografar os dados
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Remover o padding
    padding = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding]
    
    # Salvar o arquivo descriptografado
    with open(filename, 'wb') as f:
        f.write(decrypted_data)
    
    print(f'Arquivo {filename} descriptografado com sucesso.')

# Função principal
def main():
    # Solicitar a chave de encriptação
    key = input('Digite a chave de encriptação (32 bytes hex): ')
    key = bytes.fromhex(key)
    
    # Verificar se a chave tem o comprimento correto
    if len(key) != 32:
        print("Chave inválida! A chave deve ter 32 bytes.")
        sys.exit(1)
    
    # Escolha de ação
    print("Escolha a ação:")
    print("1) Criptografar")
    print("2) Descriptografar")
    choice = input("Digite a opção: ")
    
    if choice == '1':
        # Criptografar arquivos
        for filename in os.listdir('.'):
            if filename != 'programa.py':
                encrypt_file(filename, key)
    elif choice == '2':
        # Descriptografar arquivos
        for filename in os.listdir('.'):
            if filename != 'programa.py':
                decrypt_file(filename, key)
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
