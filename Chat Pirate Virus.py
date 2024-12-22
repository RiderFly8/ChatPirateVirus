import subprocess

# Chemin complet vers le fichier VBScript
chemin_vbs = "disclaimer.vbs"

# Exécutez le fichier VBScript en utilisant l'interpréteur WSH
subprocess.call(["cscript.exe", chemin_vbs], shell=True)
