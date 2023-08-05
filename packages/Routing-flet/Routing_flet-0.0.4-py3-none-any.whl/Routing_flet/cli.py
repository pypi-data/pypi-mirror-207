import typer
from rich import print
from pathlib import Path

app = typer.Typer()
struct_app = typer.Typer()
app.add_typer(struct_app, name='init')


@struct_app.command(help='Crea una estructura: [views,controllers,models]')
def mvc():
    # creacion archivo main.pypip
    file_path_main = Path('./') / 'main.py'
    file_path_main.touch()

    source_path = Path(__file__).parent / 'main.py'

    with open(source_path, 'r') as source_file:
        content = source_file.read()

    with open(file_path_main, 'w') as file:
        file.write(content)

    # creacion de las vistas/archivos.py
    Path('views').mkdir(exist_ok=True)
    Path('controllers').mkdir(exist_ok=True)
    Path('models').mkdir(exist_ok=True)
    file = Path('views') / '__init__.py'
    file.touch()

    file_list = ['index.py', '404.py']

    for file_name in file_list:
        file = Path('views') / file_name
        file.touch()

        source_path = Path(__file__).parent / file_name

        with open(source_path, 'r') as source_file:
            content = source_file.read()

        with open(file, 'w') as file:
            file.write(content)

    print(
        f"[green]> Directorio [bold green]'controllers'[/bold green] creado\n> Directorio [bold green]'models'[/bold green] creado\n> Generado {len(file_list)} archivos en el directorio [bold green]'views'[/bold green] y  el archivo [bold green]'main.py'[/bold green]:[/green]")
    for files in file_list:
        print(f"[blue]● {files}[/blue]")

# views
@struct_app.command(help='Crea una estructura: main.py [views]')
def v():
    # creacion archivo main.pypip
    file_path_main = Path('./') / 'main.py'
    file_path_main.touch()

    source_path = Path(__file__).parent / 'main.py'

    with open(source_path, 'r') as source_file:
        content = source_file.read()

    with open(file_path_main, 'w') as file:
        file.write(content)

    # creacion de las vistas/archivos.py
    Path('views').mkdir(exist_ok=True)
    file = Path('views') / '__init__.py'
    file.touch()

    file_list = ['index.py', '404.py']

    for file_name in file_list:
        file = Path('views') / file_name
        file.touch()

        source_path = Path(__file__).parent / file_name

        with open(source_path, 'r') as source_file:
            content = source_file.read()

        with open(file, 'w') as file:
            file.write(content)

    print(
        f"[green]> Generado {len(file_list)} archivos en el directorio [bold green]'views'[/bold green] y  el archivo [bold green]'main.py'[/bold green]:[/green]")
    for files in file_list:
        print(f"[blue]● {files}[/blue]")

@app.command()
def version():
    print('[bold green]version:[/bold green] 0.0.3 [green]beta[/green]')

#------
main = app

if __name__ == "__main__":
    main()