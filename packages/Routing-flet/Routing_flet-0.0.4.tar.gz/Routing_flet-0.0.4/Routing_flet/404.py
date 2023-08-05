import flet as ft

class View:
    def __init__(self):
        self.route = '/404'

    def view(self, page: ft.Page):

        page.title = 'page 404'
        page.theme = ft.PageTransitionsTheme.ios
        return ft.View(
            self.route,
            controls=[
                ft.Column(
                    [
                        ft.Text('404', size=90),
                        ft.Text('url no encontrada:'),
                        ft.FilledButton(
                            'ir a Home',
                            width=120,
                            height=40,
                            on_click=lambda e:e.page.go('/')
                        )
                    ]
                )
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )