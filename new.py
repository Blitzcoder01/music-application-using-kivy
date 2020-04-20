import kivy
from pygame import mixer
import threading
mixer.init()
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import ButtonBehavior
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
import pygame, sys
from kivy.core.audio import SoundLoader
import os
import random
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '500')
class ImageButton(ButtonBehavior, Image):
    pass
class mainscreen(Widget):
    pass
class winApp(App):
    musicctr=0
    ##M = SoundLoader.load('')
    def build(self):

        self.icon = "/home/riya/Downloads/gramophone.png"
        self.title = 'MuSiC MiX'
        self.ctr = 0
        path = "/home/riya/Music/"
        self.songs = []
        for filename in os.listdir(path):
            if filename.endswith('.mp3'):
                self.songs.append(os.path.join(path, filename))
        return mainscreen()

    def play(self):
        pygame.init()
        print(self.songs[self.ctr])
        mixer.music.load(self.songs[self.ctr])
        mixer.music.play(3)


    def pause(self):
        mixer.music.pause()

    def unpause(self):

        mixer.music.unpause()

    def next(self):
        pygame.init()
        if (len(self.songs)-1)==self.ctr:
            self.ctr=0
        else:
            self.ctr+=1
        print(len(self.songs))
        #for j in songs:
        print('ctr'+str(self.ctr))
        mixer.music.load(self.songs[self.ctr])
        print(self.songs[self.ctr])
        mixer.music.play(3)



    def previous(self):

        if self.ctr==0:
            self.ctr = len(self.songs)-1
        else:

            self.ctr -= 1


        mixer.music.load(self.songs[self.ctr])
        print('ctr' + str(self.ctr))
        mixer.music.play(3)


winApp().run()