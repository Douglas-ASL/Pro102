import os
import shutil

# Definindo os caminhos de origem e destino
from_dir = "Caminho/Para/Downloads"
to_dir = "Caminho/Para/Arquivos_Documentos"

# Obtendo a lista de arquivos no diretório de origem
list_of_files = os.listdir(from_dir)

# Exibindo os nomes de todos os arquivos no diretório de origem
print(list_of_files)

# Percorrendo a lista de arquivos
for file_name in list_of_files:
    # Capturando o nome e a extensão do arquivo
    name, ext = os.path.splitext(file_name)
    
    # Ignorando arquivos sem extensão
    if ext == "":
        continue
    
    # Verificando se a extensão está na lista desejada
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        # Criando os caminhos de origem, pasta temporária e destino
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, ext[1:].upper())  # Pasta temporária
        path3 = os.path.join(to_dir, "Arquivos_Documentos", file_name)
        
        # Verificando se a pasta temporária existe
        if os.path.exists(path2):
            print("Movendo", file_name)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Movendo", file_name)
            shutil.move(path1, path3)
