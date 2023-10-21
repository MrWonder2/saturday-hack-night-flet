import flet as ft
from names import *


def main(page: ft.Page):

    page.title = "Random Name Generator"
    page.add(
        ft.Text("The Random Name Artisan", size=30,
                color="blue600", italic=True)
    )

    def dropdown_changed(e):
        tempi.value = f"You would like to generate {limit.value} {dd_sex.value} name(s), with the origins of {dd_fname.value, dd_lname.value}, if so Generate"
        tempi.size = 20
        page.update()

    def button_clicked(e):
        t.value = ""
        t.size = 20
        gender = dd_sex.value
        fname = dd_fname.value
        lname = dd_lname.value
        lm = limit.value

        if gender.lower() == 'male':
            prefix = 'get_random_male'
        elif gender.lower() == 'female':
            prefix = 'get_random_female'
        elif gender.lower() == 'unisex':
            prefix = 'get_random_unisex'
        else:
            return "Invalid gender."

        for i in range(int(lm)):
            command_1 = f'{prefix}_first_name("{fname}")'
            command_2 = f'{prefix}_last_name("{lname}")'
            try:
                pg_fname = eval(command_1)
                pg_lname = eval(command_2)
                # print(x)
            except Exception as e:
                print(f"An error occurred: {e}")

            t.value = t.value + \
                f"The generated name is: {pg_fname} {pg_lname} \n"
        page.update()

    b = ft.ElevatedButton(text="Generate", on_click=button_clicked)
    tempi = ft.Text()
    t = ft.Text()
    dd_sex = ft.Dropdown(
        on_change=dropdown_changed,
        width=200,
        hint_text="Gender",
        options=[
            ft.dropdown.Option("Male"),
            ft.dropdown.Option("Female"),
            ft.dropdown.Option("Unisex"),
        ],
    )

    dd_fname = ft.Dropdown(
        on_change=dropdown_changed,
        width=200,
        hint_text="First Name Origin",
        options=[
            ft.dropdown.Option("English"),
            ft.dropdown.Option("Italian"),
            ft.dropdown.Option("French"),
            ft.dropdown.Option("German"),
            ft.dropdown.Option("Russian"),
            ft.dropdown.Option("Indian"),


        ],

    )

    dd_lname = ft.Dropdown(
        on_change=dropdown_changed,
        width=200,
        hint_text="Last Name Origin",
        options=[
            ft.dropdown.Option("English"),
            ft.dropdown.Option("Italian"),
            ft.dropdown.Option("French"),
            ft.dropdown.Option("German"),
            ft.dropdown.Option("Russian"),
            ft.dropdown.Option("Indian"),



        ],
    )

    limit = ft.Dropdown(
        on_change=dropdown_changed,
        width=200,
        hint_text="Limit",
        options=[
            ft.dropdown.Option(1),
            ft.dropdown.Option(2),
            ft.dropdown.Option(3),
            ft.dropdown.Option(4),
            ft.dropdown.Option(5),

        ],
    )

    page.add(dd_sex, dd_fname, dd_lname, limit, b, t, tempi)


ft.app(target=main)
