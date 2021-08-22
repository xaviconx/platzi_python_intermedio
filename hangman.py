import random
import os

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
    /|  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\ |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\ |
    /   |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\ |
    / \ |
        |
    =========''']


def read_data():
    words = []
    with open("./files/data.txt","r", encoding="utf-8") as f:
        for line in f:
            words.append(line[:-1])
    return words
    #print(words)


def draw(secret,lifes):
    os.system("clear")
    print("XaviConX hangman game! - Spanish version")
    print(HANGMANPICS[6-lifes])
    print("\n")
    for letter in secret:
        print(letter,end=" ")
    print("\n")
     

def normalize_word(word):
    new_word = ""
    for chr in word:
        if chr == "á":
            chr = "a"
        elif chr == "é":
            chr = "e"
        elif chr == "í":
            chr = "i"
        elif chr == "ó":
            chr = "o"
        elif chr == "ú":
            chr = "u"
        new_word = new_word + chr
    return new_word


def run():
    lifes = 6
    words=read_data()
    index = random.randint(1,len(words))
    word = words[index]
    norm_word = normalize_word(word)
    word_len = len(word)
    secret = ["-" for i in range( 1 , word_len + 1 ) ]
    draw(secret,lifes)
    char_left = word_len
    used_chars = [" "]
    while True:
        used_char = False
        right_choice = False
        in_char=input("Ingrese una letra: ")
        assert len(in_char) == 1, "Se ingresó más de una letra."
        assert len(in_char) > 0, "No se ingresó ningún caracter."
        for char in used_chars:
            if in_char == char:
                used_char = True
        used_chars.append(in_char)    

        if not used_char:
            norm_char = normalize_word(in_char)
            for i in range(0,word_len):
                if norm_char == norm_word[i]:
                    char_left = char_left - 1
                    secret[i] = word[i]
                    right_choice = True
        if not right_choice:
            lifes = lifes - 1 
        if char_left <= 0:
            draw(secret,lifes)
            print(""" 
    ____  ____                 ____      ____  _            _ 
   |_  _||_  _|               |_  _|    |_  _|(_)          | |
     \ \  / / .--.   __   _     \ \  /\  / /  __   _ .--.  | |
      \ \/ // .'`\ \[  | | |     \ \/  \/ /  [  | [ `.-. | | |
      _|  |_| \__. | | \_/ |,     \  /\  /    | |  | | | | |_|
     |______|'.__.'  '.__.'_/      \/  \/    [___][___||__](_)
            """)
            break

        if lifes == 0:
            draw(secret,lifes)
            print("""
    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
            """)
            break
        draw(secret,lifes)
        #print(word)
    print("Thank you for playing my game")
        

if __name__ == "__main__":
    run()