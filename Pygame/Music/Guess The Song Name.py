# Guess the Song name
import random
import pygame
import time
import datetime
songs = {"demo1.mp3" : "suyt nua thi",
         "demo2.mp3" : "nam ay",
         "demo3.mp3" : "dung quen ten anh",
         "demo4.mp3" : "da lo yeu e nhieu",
         "demo5.mp3" : "nao ca vang",
         "demo6.mp3" : "mong yu",
         "demo7.mp3" : "mot doi"
         }

list_song = list(songs.keys())


def display_answer(answer):
    print(answer)

def on_music(file_path, duration):

    pygame.mixer.init()
    pygame.mixer.music.load(file_path)

    print("🔊 Đang phát bài hát.....")
    pygame.mixer.music.play()
    time.sleep(duration) # nghe trong bao nhieu giay
    pygame.mixer.music.stop()



def display_hint(hint):
    print("".join(hint))
if __name__ == "__main__":

    is_running = True
    count = 1
    while is_running:
        file_path = random.choice(list_song)
        name_song = songs.get(file_path)

        is_start = True
        print(f"Bai hat thu {count}: ")
        print("*******************")
        hint = ['_'] * len(songs[file_path])
        for i in range(len(hint)):
            s = songs[file_path]
            if s[i] == " ":
                hint[i] = " "
        count += 1
        while is_start:
            guesses_wrong = 3 # được đoán 3 lần
            on_music(file_path, 10)
            guessed = set()
            s = input("Do you want to listen again (y/n) :").lower()
            if s == 'y' or s == 'Y':
                on_music(file_path, 10)
                continue
            elif s == 'n' or s == 'N': # nếu là no thì làm tiếp

                while guesses_wrong != 0:
                    display_hint(hint)
                    guess = input("Guess a letter: ")
                    if guess in guessed:
                        print("Letter is guessed")
                        continue
                    guessed.add(guess)
                    if len(guess) > 1 or not guess.isalpha():
                        print("Input Invalid")
                        continue
                    if guess in songs[file_path]:
                        for i in range(len(hint)):
                            s = songs[file_path]
                            if guess == s[i] and guess != ' ':
                                hint[i] = guess
                    else:
                        guesses_wrong -= 1

                    if "_" not in hint:
                        print(f"Dap an chinh la : {songs[file_path]}")
                        print("You Win")
                        is_start = False
                        break
                if "_" in hint:
                    print()
                    print("You have run out of 3 word guesses")
                    print(f"Dap an chinh la : {songs[file_path]}")
                    print("You Lose")
                    is_start = False
                    break













