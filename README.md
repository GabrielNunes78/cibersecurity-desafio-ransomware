Como Utilizar o Programa
============================================================================
Passo 1: Preparação do Ambiente
Certifique-se de que você possui a biblioteca cryptography instalada no seu ambiente. Caso não tenha, instale-a utilizando o seguinte comando:

bash
pip install cryptography

---------------------------------------------------------------------------
Passo 2: Execução do Programa
Abrir o terminal e navegar até o diretório onde o programa Python está salvo.
Executar o programa:

bash
python programa.py

---------------------------------------------------------------------------
Passo 3: Fornecer a Chave de Criptografia
O programa solicitará que você forneça uma chave de criptografia de 32 bytes em formato hexadecimal. Você pode gerar uma chave hexadecima manualmente ou usar ferramentas online para isso.

Exemplo de chave válida de 32 bytes (64 caracteres hexadecimais):
Informe a chave de criptografia quando solicitado.

---------------------------------------------------------------------------
Passo 4: Escolher a Ação
O programa permitirá que você escolha entre duas opções:

1) Criptografar arquivos: Ao selecionar esta opção, todos os arquivos do diretório atual serão criptografados.
2) Descriptografar arquivos: Ao selecionar esta opção, todos os arquivos criptografados no diretório serão descriptografados de volta ao formato original.

---------------------------------------------------------------------------
Passo 5: Processo de Criptografia ou Descriptografia
Se você escolher a opção de criptografar, os arquivos serão processados e criptografados no formato base64. O conteúdo dos arquivos será alterado e o programa salvará os dados criptografados no próprio arquivo.
Se você escolher a opção de descriptografar, o programa irá reverter os arquivos criptografados para seus conteúdos originais.

---------------------------------------------------------------------------
Gera um IV aleatório de 16 bytes para garantir que a criptografia seja única a cada execução.
O arquivo a ser criptografado é lido e padronizado para múltiplos de 16 bytes, utilizando padding.
Os dados são criptografados com AES em modo CBC e codificados em base64.
O IV é adicionado no início do arquivo criptografado.
decrypt_file(filename, key):

Lê o arquivo criptografado, extrai o IV e os dados criptografados.
Decodifica os dados criptografados de base64 e descriptografa com a chave fornecida.
Remove o padding aplicado durante a criptografia e escreve o conteúdo original de volta ao arquivo.


Criptografando arquivos:
O programa solicitará a chave de encriptação.
Você escolhe a opção de criptografar.
Todos os arquivos no diretório são criptografados e o conteúdo dos arquivos será alterado para dados criptografados.

Descriptografando arquivos:
O programa solicitará a chave de encriptação.
Você escolhe a opção de descriptografar.
O programa descriptografa os arquivos criptografados de volta ao seu conteúdo original.
