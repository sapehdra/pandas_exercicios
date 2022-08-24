# -*- coding: utf-8 -*-
"""
Created on Fri May  6 22:15:01 2022

@author: sapeh
"""

#Questão 1 - Arquivos baixados e colocados na mesma pasta do arquivo python

#Questão 2 - A extensão dos arquivos é csv.

#Questão 3 - Os arquivos contêm informações referentes a arquivos de música, como: nome do artista, nome da faixa, popularidade, gênero e etc.

import pandas as hayanny

#Questão 4 - Código abaixo:
    
alternative = hayanny.read_csv('alternative_music_data.csv')
blues = hayanny.read_csv('blues_music_data.csv')
hiphop = hayanny.read_csv('hiphop_music_data.csv')

print (f'Música alternativa:\n{alternative}\nBlues:\n{blues}\nHiphop:\n{hiphop}\n\n')

#Questão 5 - Código abaixo:
    
print (f'Música alternativa:\n{alternative.shape}\nBlues:\n{blues.shape}\nHiphop:\n{hiphop.shape}\n\n')

#Questão 6 - Código abaixo:
    
print (f'Música alternativa:\n{alternative.columns}\nBlues:\n{blues.columns}\nHiphop:\n{hiphop.columns}\n\n')

#Questão 7 - Código abaixo:
    
print (f'Música alternativa:\n{alternative.dtypes}\n\nBlues:\n{blues.dtypes}\n\nHiphop:\n{hiphop.dtypes}\n\n')

#Questão 8 - Código abaixo:
    
#alternative.insert(2160,"hay", 1, 'true')
alternative = alternative.assign(hay = 1)

print (f'Musicas alternativas:\n{alternative}\n\n')

#Questão 9 - Código abaixo:

blues = blues.assign(hay = 2)

print (f'Blues:\n{blues}\n\n')

#Questão 10 - Código abaixo:

hiphop.loc[:,'hay'] = 3

print (f'Hiphop:\n{hiphop}\n\n')

#Questão 11 - Código abaixo:
    
playlist = hayanny.merge(alternative, blues, how = 'outer')
playlistmix = hayanny.concat([playlist, hiphop], axis = 0)

print (f'Playlistmix:\n{playlistmix}\n\n')

#Questão 12 - Código abaixo:
    
cade_ur_nan = playlistmix.isnull()
print (f'Se houver algum nan aparecerá true, caso contrário aparecerá false:\n{cade_ur_nan}\n\nNão existe nenhuma linha com valor nan!\n\n')
    
#Questão 13 - Código abaixo:
    
playlistmix = playlistmix.dropna()

print (f'Playlistmix:\n{playlistmix}\n\n')
#print (f'Não existem linhas com valor nan para desconsiderar!\n\n')

#Questão 14 - Código abaixo:
    
playlistmix = playlistmix.select_dtypes(exclude = ['object'])

print (f'Playlistmix:\n{playlistmix}\n\n')

