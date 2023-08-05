from flet import Page
from Routing_flet.config import routing
from Routing_flet import Params
from rich import print as pt

route_page = routing()


class RoutePage:

    """ 
    Uso de la clase:
    ```
    RoutePage(
        page=page # Clase Page de Flet que llega como referencia
        )
    ```
    -----
    Ejemplo:
    ```
    def main(page: ft.Page):
        ruta = RoutePage(page)
        ruta.run()

    ft.app(target=main, view=ft.WEB_BROWSER,port=9999, route_url_strategy='hash') 
    ```
    """

    def __init__(self, page: Page) -> object:
        self.page = page

    def route_change(self, route):
        self.page.views.clear()
        pg_404 = True

        for key, value in route_page.items():
            if key != '/404':
                if key == route.route[0:len(key)]:
                    if value.math_url() != None:
                        params_u = {}
                        k = 0
                        url_value = route.route.replace(key+'/', '').split('/')
                        if '' not in url_value:
                            url_ext = len(url_value)
                            if len(value.math_url()) == url_ext:
                                pg_404 = False
                                if value.login_requi() == None or value.login_requi() == True:
                                    params_u.clear()
                                    for i in value.math_url():
                                        params_u[i] = url_value[k]
                                        k += 1
                                    params = Params(params_u)
                                    self.page.views.append(
                                        value.view(self.page, params))
                                    break
                                else:
                                    self.page.go('/')
                                    break

                    elif route.route == key:
                        pg_404 = False
                        if value.login_requi() == None or value.login_requi() == True:
                            self.page.views.append(value.view(self.page))
                            break
                        else:
                            self.page.go('/')
                            break

        if pg_404:
            self.page.views.append(route_page['/404'].view(self.page))

        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

    def run(self):
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go(self.page.route)
        self.page.update()
        pt('[green]>> Reload[/green]')
