import pathlib
ejemplo_dir = '/pyos/'
directorio = pathlib.Path(ejemplo_dir)
for fichero in directorio.iterdir():
    print(fichero.name)