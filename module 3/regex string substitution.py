import re

# regex para substituir um trecho de uma string semelhante a um endereço de e-mail
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))