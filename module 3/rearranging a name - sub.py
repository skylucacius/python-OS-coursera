# Rearranging a name using re.sub() function
import re

# Um nome pode conter:
# "\w" - qualquer caractere alfanumérico: a-z , A-Z, 0-9 ou _
# " " - um espaço vazio
#  "." - um ponto
#  "-" - um hífen

# Logo, a regex [\w.-] poderá aparecer 0 ou mais vezes tanto no nome, quanto no sobrenome

print(re.sub(r"^([\w.-]*), ([\w.-]*)$", r"\2 \1", "Lovelace, Ada"))