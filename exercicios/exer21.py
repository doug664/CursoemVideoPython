#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#é preciso instalar esse modulo
#para instalar no windows
#1 - abra o cmd
#2 - digite pip install pygame
#3 - Ao final da instalação retorna successlly installed pygame-2.1.2
#4 - talvez seja preciso fechar e abrir o vscode para reconhecer a biblioteca

import pygame
pygame.init() # para iniciar o pygame
pygame.mixer.music.load('deserto.mp3')
pygame.mixer.music.play()
pygame.event.wait()
