import random
import os
from time import sleep
import sys

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('Abeja,Alce,Asno,Avestruz,Buey,Caballo,Cabra,Camello,Cerdo,Chinchilla,Codorniz,Conejo,Gallina,Ganso,Gato,Hamster,Huron,Iguana,Llama,Mula,Oveja,Paloma,Pavo,Perro,Raton,Reno,Serpiente,Tortuga,Vaca').split(',')


def main():
    try:
        word = random.choice(words).lower()

        spaces = ('_ ' * len(word)).split(' ')[:-1]

        used_letters = []
        user_letter = ''
        cantidad_fallos = 0

        while True:

            texto = f""" AHORCADO CON ANIMALES DOMESTICOS
        {HANGMANPICS[cantidad_fallos]}

        {' '.join(spaces)}

        Letras usadas: {' '.join(used_letters).upper()}
        """

            os.system('cls')
            print(texto)
            
            if cantidad_fallos >= len(HANGMANPICS) - 1:
                print(f'\nLa palabra era {word}')
                print('\nPerdiste!\n')
                break
            elif not '_' in spaces:
                print('\nGanaste!\n')
                break

            user_letter = input('Ingrese una letra: ')

            if user_letter in used_letters:
                cantidad_fallos += 1
                continue


            used_letters.append(user_letter)

            correct_letters = []
            for i in range(len(word)):
                if word[i] == user_letter:
                    correct_letters.append(i)
                    
            
            if len(correct_letters) == 0:
                cantidad_fallos += 1
            else:
                for i in correct_letters:
                    spaces[i] = user_letter
    except KeyboardInterrupt:
        print('\n\n--------------\nADIOS.')
        sleep(2)
        os.system('cls')
        sys.exit()

if __name__ == '__main__':
    main()