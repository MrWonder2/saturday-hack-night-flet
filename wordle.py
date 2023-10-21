import flet as ft
import random


def main(page: ft.Page):
    global turns
    file = open("solutions.txt", "r")
    answerList = file.readlines()
    word = answerList[random.randint(0, len(answerList) - 1)].lower()
    print(word)

    wordlist = open("words.txt", "r")
    wordlist = wordlist.readlines()
    wordlist = [x.strip() for x in wordlist]

    crrct = ft.Container(width=50, height=50, bgcolor=ft.colors.GREEN)
    wrng = ft.Container(width=50, height=50, bgcolor=ft.colors.GREY)
    prtl = ft.Container(width=50, height=50,
                        bgcolor=ft.colors.YELLOW, content=ft.Text("Hi", color="Black", size=20))

    txt = ft.TextField(label="Enter your word")
    turns = 0
    grey = "grey"
    yellow = "yellow"
    green = "green"

    def button_clicked(e):

        userGuess = str(txt.value).lower()
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
            print("clr code")
            print(guessColourCode)

            def tiled(lst):
                tile = [0] * 5
                for i in range(len(lst)):

                    print(lst)
                    if lst[i] == grey:
                        tile[
                            i] = f'ft.Container(width=50, height=50, bgcolor=ft.colors.GREY, content=ft.Text("{userGuess[i]}", color="Black", size=20))'
                    elif lst[i] == yellow:

                        tile[
                            i] = f'ft.Container(width=50, height=50, bgcolor=ft.colors.YELLOW, content=ft.Text("{userGuess[i]}", color="Black", size=20))'
                    else:
                        tile[
                            i] = f'ft.Container(width=50, height=50, bgcolor=ft.colors.GREEN, content=ft.Text("{userGuess[i]}", color="Black", size=20))'

                print(tile)
                page.add(

                    ft.Row(
                        controls=[
                            eval(tile[0]),
                            eval(tile[1]),
                            eval(tile[2]),
                            eval(tile[3]),
                            eval(tile[4]),

                        ]
                    )
                )
            tiled(guessColourCode)

    b = ft.ElevatedButton(text="Guess", on_click=button_clicked)

    page.add(
        ft.Row(controls=[
        ]
        ), txt, b
    )


ft.app(target=main)
