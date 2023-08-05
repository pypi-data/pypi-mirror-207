# ♾️Routing_flet -> Enrutamiento y protección de paginas facil con flet
## instalar
```
pip install Routing-flet
```
## Actualizar
```
pip install Routing-flet --upgrade
```
---
## Ejemplo:
En el archivo principal `./main.py` se implementa lo siguiente que sera la funcion principal que enrutara todas las paginasque tengra el sitio web.
```python
import flet as ft
from Routing_flet import RoutePage

def main(page: ft.Page):

    ruta = RoutePage(page)
    ruta.run()

ft.app(target=main, view=ft.WEB_BROWSER, port=9999, route_url_strategy='hash')
```
En las vistas de cada pagina se utiliza mediante clases que heredara de la clase `ViewPage`, en la clase de la vista que se creara y se encuentra ubicado en `./views/<archivo>.py` | tiene los siguientes metodos:
- Para configurar la url
```python
  def __init__(self) -> None:
        self.route = '/about/list/
```
- Configurar un ruta dinámica por defecto es estático | En consola se recibira los parametros como diccionario.
```python
def math_url(self):
        return ['id','name','edad']
```
- Para proteger una ruta | Por defecto no hay protección de ruta: 
- Al retornar `True` Se podra ingresar, en caso `False` se denegara el ingreso.
```python
def login_requi(self):
        return True
```
## Ejemplo de una pagina con enrutamiento estático y sin protección de ruta:
```python
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
```
## Sitio web con enrutamiento dinámico y protección de rutas
```python
import flet as ft
from Routing_flet import ViewPage

class View(ViewPage):
    def __init__(self) -> None:
        self.route = '/about/1/2'

    def math_url(self):
        return ['id','name','edad']
     
    def login_requi(self):
        return True

    def view(self, page: ft.Page):
        page.title = 'contact'

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
## Correr Flet (-w : Para ejecutar en la web) | ruta : `./`
```cmd
flet run main.py -r -w -p 9999
```
