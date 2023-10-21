import flet as ft
import random


def main(page: ft.Page):
    global turns
    file = open("solutions.txt", "r")
    answerList = file.readlines()
    word = answerList[random.randint(0, len(answerList) - 1)].upper()

    wordlist = open("words.txt", "r")
    wordlist = wordlist.readlines()
    wordlist = [x.strip() for x in wordlist]

    crrct = ft.Container(width=50, height=50, bgcolor=ft.colors.GREEN)
    wrng = ft.Container(width=50, height=50, bgcolor=ft.colors.GREY)
    prtl = ft.Container(width=50, height=50,
                        bgcolor=ft.colors.YELLOW, content=ft.Text("Hi", color="Black", size=20))

    txt = ft.TextField(label="Enter your word")
    turns = 0

    def button_clicked(e):
        grey = "grey"
        yellow = "yellow"
        green = "green"
        userGuess = txt.value
        remaining_letters_in_word = word
        guessColourCode = [grey, grey, grey, grey, grey]
        if len(txt.value) == 5 and userGuess.lower() in wordlist:
            for x in range(0, 5):
                if word[x] == userGuess[x]:
                    remaining_letters_in_word = remaining_letters_in_word.replace(
                        userGuess[x], "", 1
                    )
                    guessColourCode[x] = green

            for x in range(0, 5):
                if (userGuess[x] in remaining_letters_in_word) and (userGuess[x] != word[x]):
                    remaining_letters_in_word = remaining_letters_in_word.replace(
                        userGuess[x], "", 1
                    )
                    guessColourCode[x] = yellow

            def tiled(lst):
                tile = [0] * 5
                for i in range(len(lst)):
                    if lst[i] == grey:
                        print(i)
                        tile[
                            i] = 'ft.Container(width=50, height=50, bgcolor=ft.colors.GREY, content=ft.Text(f"{userGuess[i]}", color="Black", size=20))'
                    elif lst[i] == yellow:
                        print(i)

                        tile[
                            i] = 'ft.Container(width=50, height=50, bgcolor=ft.colors.YELLOW, content=ft.Text(f"{userGuess[i]}", color="Black", size=20))'
                    else:
                        print(i)
                        tile[
                            i] = 'ft.Container(width=50, height=50, bgcolor=ft.colors.GREEN, content=ft.Text(f"{userGuess[i]}", color="Black", size=20))'

                return tile

            print(tiled(guessColourCode))

        else:
            pass

    b = ft.ElevatedButton(text="Guess", on_click=button_clicked)

    page.add(
        ft.Row(
            [
                crrct, wrng, prtl
            ]
        ), txt, b
    )


ft.app(target=main)
