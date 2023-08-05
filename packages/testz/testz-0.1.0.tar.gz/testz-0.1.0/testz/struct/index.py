import flet as ft
from Routing_flet import ViewPage

class View(ViewPage):
    def __init__(self):
        self.route = '/'

    def view(self, page: ft.Page):
        page.title = 'Index'

        return ft.View(
            self.route,
            controls=[
                ft.Column(
                    [
                        ft.Container(
                            content=ft.Text('index page', size=50),
                            width=450,
                            height=450,
                            bgcolor='blue800',
                            alignment=ft.alignment.center,
                        ),
                        ft.FilledButton(
                            'ir a contact',
                            width=120,
                            height=40,
                            on_click=lambda e:e.page.go('/contact')
                        ),
                    ]
                )
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )