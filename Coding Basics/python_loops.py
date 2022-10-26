# Loops
from faulthandler import cancel_dump_traceback_later


for i in range(5): # Crear una secuencia
    print(i)


names = ['Angelica', 'Eliza', 'Peggy']
for name in names: # Recorrer una lista
    print(name)

# Iterate throug a Dictionary
# En este caso solo se muestran los keys.
card_suits = {"spades": 5, "diamonds": 2, "clubs": 8, "hearts": 9}
for suit in card_suits:
    print(suit)

# Para recorrer tanto los keys como los values, se usa el método .items()
for cardvalue in card_suits.items():
    print(cardvalue)    # Muestra una tupla: key:value.

# Si usted desea los keys en una variable y los valores en otra, entonces:
a, b, c = [1, 2, 3]
print(a, b, c)

# Unpacking the (key, value) in .items()
for suit, cardvalue in card_suits.items():
    print("You have a {} of {}.".format(cardvalue, suit))

# Ejemplo para un 'while' -> Conditional Loops
i = 0
while i < 5:
    print(i)
    i += 1