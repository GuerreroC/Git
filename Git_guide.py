#Git 
#GIT
#Sistema de control de versiones: https://git-scm.com/docs
""" Etapas de Git

    Working directory:
        Donde trabajas con tus archivo
    Staging area:
        Donde agregas todos los archivos para el guardado(ver1, ver2)
    Repository:
        Proyecto guardados
"""

""" Commits
    Para que se pueda enviar el comando de commit necesitas dar de alta tu user name y tu correo, esto se hace con:
    $ git config --global user.name "cguerr28"
    $ git config --global user.email cguerr28@ford.com
    
    Agregando siguientes versiones en el Repository:
    git commit -m "Aqui metes el texto"
"""

""" Iconos de archivos
    ?? en rojo significa que no estan en staging area
    M en rojo es que esta modificado pero no en stagin area
    M de verde esque la modificacion esta en staging area
    
"""

""" Commandos
    git status -s               : ver status de los archivos de la carpeta
    git log --oneline           : Ver historial de tu brench master
    git reset --hard ffffff     : Regresar a la version fffffff
    git add .                   : Agrega todo los archivos de tu projecto a stagin area
    git git commit -m "name"    : Subir el archivo al repository
    git remote add origin url   : creas un remoto
    git push -u origin master   : Subir el archivo a Github
"""
