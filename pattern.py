
import re

regex = r"^ES\d{22}$"

# Ejemplo de uso
cadena = "ES1234567890123456789012"
if re.match(regex, cadena):
    print("La cadena cumple con las características.")
else:
    print("La cadena no cumple con las características.")
