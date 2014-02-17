from Battle.battle_message import BattleMessage
from Screen.Pygame.screen import Screen

from Screen.Pygame.Menu.MainMenu.scrolling_map import map
from Screen.Pygame.Menu.TrainerMenu.trainer_menu_entry_view import TrainerMenuEntryView

from Screen.Pygame.MessageBox.message_box import MessageBox

from kao_gui.pygame.pygame_screen import PygameScreen

import pygame

class TrainerMenuScreen(PygameScreen):
    """ Trainer Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        self.font = pygame.font.SysFont("Times New Roman", 36)

        self.entries = []
        i = 0
        for entry in self.menu.entries:
            self.entries.append(TrainerMenuEntryView(entry, i))
            i += 1
            
        self.selectedIndex = 0
        self.buildMessageBox()
        
    def update(self):
        """ Update the screen """
        map.update()
        
        if not self.entries[self.selectedIndex].entry.selected:
            self.findNewSelectedIndex()
            self.buildMessageBox()
        
        self.messageBox.update()
        
    def drawSurface(self):
        """ Draw the surface """
        self.drawMap()
        
        for entry in self.entries:
            entrySurface = entry.draw()
            self.drawOnSurface(entrySurface, centerx=.5, centery=(entry.yRatio+.5)/TrainerMenuEntryView.HEIGHT_RATIO)
            
        text = self.messageBox.draw()
        self.drawOnSurface(text, centerx=.5, centery=.75)
        
    def drawMap(self):
        """ Draws the map to the window """
        mapSurface = map.draw()
        self.drawOnSurface(mapSurface, left=0, top=0)
        
    # Unnecessary MessageBox stuff
    def findNewSelectedIndex(self):
        """ Set the new Selected Index """
        for entry in self.entries:
            if entry.entry.selected:
                self.selectedIndex = self.entries.index(entry)
                break
    
    def buildMessageBox(self):
        """ Builds a Message Box """
        battleMessage = BattleMessage("{0}'s first Pkmn is {1}".format(self.entries[self.selectedIndex].entry.trainer.name, self.entries[self.selectedIndex].entry.trainer.beltPokemon[0].name))
        self.messageBox = MessageBox(battleMessage)