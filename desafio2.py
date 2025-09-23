def possible_words(string):
  vocales = ["a", "i", "u", "e", "o"]  # defining vowels

  Stuart_words = []  # initialising lists
  Kevin_words = []

  words = string.strip().split()  # if multiple words are entered we process them one by one

  for string in words:
    for i, ch in enumerate(string):  # tomamos cada ch en la palabra processed by the .split() y le damos un index i de referencia
      if ch in vocales:  # si comienza con una vocal
        for j in range(i + 1, len(string) + 1):  # desde la posicion de la letra que estamos analizando (i+1) hasta el final del string (len(string) + 1)
          Kevin_words.append(string[i:j])  # anadimos todas las posibles combinaciones (banana --> b, ba, ban, ...)
      elif ch not in vocales:  # si no comienza con una vocal
        for k in range(i + 1, len(string) + 1):
          Stuart_words.append(string[i:k])
  return Stuart_words, Kevin_words

S = input("Palabra: ").strip()  # user input de la palabra pal juego
Stuart_words, Kevin_words = possible_words(S)  # encontrando las combinaciones de cada uno x

if len(Stuart_words) > len(Kevin_words):
  print(f"Winner: Stuart with {len(Stuart_words)} points")
elif len(Kevin_words) > len(Stuart_words):
  print(f"Winner: Kevin with {len(Kevin_words)} points")
else:
  print(f"Both players tied with {len(Kevin_words)} points!")
