import flet as ft
from Routing_flet import RoutePage

def main(page: ft.Page):

    ruta = RoutePage(page)
    ruta.run()

ft.app(target=main, view=ft.WEB_BROWSER, port=9999, route_url_strategy='hash')