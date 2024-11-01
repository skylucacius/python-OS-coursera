# Pergunta 1
# A função create_python_script cria um novo script Python no diretório de trabalho atual, adiciona a linha de comentários declarada pela variável 'comments' e retorna o tamanho do novo arquivo. Preencha as lacunas para criar um script chamado "program.py".
import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename) as file:
    filesize = file.seek(0, os.SEEK_END)
  return(filesize)

print(create_python_script("program.py"))


# import os
# def parent_directory():
#   # Create a relative path to the parent 
#   # of the current working directory 
#   relative_parent = os.path.join(os.getcwd(), "..")

#   # Return the absolute path of the parent directory
#   return os.path.abspath(relative_parent)

# print(parent_directory())

# # A função retorna o seguinte:
# # print(os.path.realpath((os.path.join(os.getcwd(), ".."))))