import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.add(ft.Text("Hello Flet!"))

ft.run(main)