# Pergunta 1
# A função create_python_script cria um novo script Python no diretório de trabalho atual, adiciona a linha de comentários declarada pela variável 'comments' e retorna o tamanho do novo arquivo. Preencha as lacunas para criar um script chamado "program.py".

# import os
# def create_python_script(filename):
#   comments = "# Start of a new Python program"
#   with open(filename, 'w') as file:
#     file.write(comments)
#   return(os.path.getsize(filename))

# print(create_python_script("program.py"))



# Pergunta 2
# A função new_directory cria um novo diretório dentro do diretório de trabalho atual, cria um novo arquivo vazio dentro do novo diretório e retorna a lista de arquivos nesse diretório. Preencha as lacunas para criar um arquivo "script.py" no diretório "PythonPrograms". 

# import os
# def new_directory(directory, filename):
#   # Before creating a new directory, check to see if it already exists
#   if os.path.isdir(directory) == False:
#     os.mkdir(directory)

#   # Create the new file inside of the new directory
#   os.chdir(directory)
#   with open (filename, 'w') as file:
#     pass

#   # Return the list of files in the new directory
#   return os.listdir('.')

# print(new_directory("PythonPrograms", "script.py"))

# Pergunta 4
# A função file_date cria um novo arquivo no diretório de trabalho atual, verifica a data em que o arquivo foi modificado e retorna apenas a parte da data do registro de data e hora no formato aaaa-mm-dd. Preencha as lacunas para criar um arquivo chamado "newfile.txt" e verifique a data em que ele foi modificado.

# import os
# import datetime

# def file_date(filename):
#   # Create the file in the current directory
#   open(filename, 'w').close()
    
#   timestamp = os.path.getmtime(filename)
#   # Convert the timestamp into a readable format, then into a string
#   date = datetime.datetime.fromtimestamp(timestamp).date()
#   # Return just the date portion 
#   # Hint: how many characters are in “yyyy-mm-dd”? 
#   return date

# print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd



# Pergunta 5
# A função parent_directory retorna o nome do diretório que está localizado logo acima do diretório de trabalho atual. Lembre-se de que "..." é um alias de caminho relativo que significa "ir até o diretório pai". Preencha as lacunas para concluir essa função.

import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), "..")

  # Return the absolute path of the parent directory
  return os.path.realpath(relative_parent)

print(parent_directory())