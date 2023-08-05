from flet import Page, View, Column, Text, MainAxisAlignment, CrossAxisAlignment

class Params:
    def __init__(self, params: list = None) -> list:
        self.params = params
    
    def get_all(self):
        return self.params

    def get(self, key: str):
        return self.params[key]


class ViewPage:
    """ 
    Usar el siguiente metodo dentro de la clase si se requiere un login requerido a la página (True: para acceder | None: Por defecto) o denegar (False: Renvia a la ruta -> '/' )
    ```
    def login_requi(self):
        return None
    ```
    ---
    El metodo que se hereda en la clase -> def math_url(self): si no se desea una url dinámica no se agrega a la nueva clase creada, ya que por defecto es None.
    ```
    def math_url(self):
        return None
    ```
    ---
    Ejemplo de un enrutamiento dinámico:
    ```
    import flet as ft
    from Routing_flet import ViewPage

    class View(ViewPage):
        def __init__(self) -> None:
            self.route = '/about/1/2'

        def math_url(self):
            return ['id', 'name', 'edad']

        def view(self, page: ft.Page, params:Params): # Params: para acceder a los parametros enviados en la url
            page.title = 'contact'
            print('Mi params:' params.get_all())
            return ft.View(
                self.route,
                controls=[
                    ft.Column(
                        [
                            ft.Container(
                                content=ft.Text('index about', size=50),
                                width=450,
                                height=450,
                                bgcolor='green800',
                                alignment=ft.alignment.center,
                            ),
                            ft.FilledButton(
                                'ir a index',
                                width=120,
                                height=40,
                                on_click=lambda e:e.page.go('/')
                            ),
                        ]
                    )
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
    ``` 
    """

    def __init__(self) -> None:
        self.route = '/'

    def math_url(self) -> list:
        return None

    def route(self) -> str:
        return self.route

    def login_requi(self) -> bool:
        return None

    def view(self, page: Page, params: Params = None) -> object:
        page.title = 'WiewPage'
        print('parametro:', params.get('id'))
        return View(
            self.route,
            controls=[
                Column(
                    Text('View Page', size=90)
                )
            ],
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )