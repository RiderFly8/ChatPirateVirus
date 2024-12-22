import pygame

# Initialisez pygame
pygame.init()

# Chemin vers votre fichier audio (remplacez le chemin par le vôtre)
musique = "music.mp3"

# Chargez la musique
pygame.mixer.music.load(musique)

# Définissez la boucle infinie pour jouer la musique en boucle
pygame.mixer.music.play(-1)  # L'argument -1 signifie de jouer en boucle

# Attendez jusqu'à ce que vous souhaitiez arrêter la lecture
input("Appuyez sur Entrée pour arrêter la musique...")

# Arrêtez la musique lorsque vous avez terminé
pygame.mixer.music.stop()

# Quittez pygame
pygame.quit()
