from setuptools import setup

with open("./README.md", "r", encoding="utf-8") as e:
    long_description = e.read()

print(long_description)


setup(
    name='Routing_flet', 
    version='0.0.3',
    author='Dxsxsx',
    description='Esta es la descripcion de mi paquete',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Dxsxsx/Routing_flet',
    download_url='https://github.com/Dxsxsx/Routing_flet',
    project_urls = {
        "Bug Tracker":"https://github.com/Dxsxsx/Routing_flet/issues"
    },
    install_requires=["typer[all]", "flet"],
    classifiers={
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    },
    packages=["Routing_flet"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["dxs=Routing_flet.cli:main"],
    },
    keywords=["python web template", "web application", "development"],
)

""" 
py -m pip install --upgrade build
py -m build

py -m pip install --upgrade twine
py -m twine upload --repository pypi dist/*
 """