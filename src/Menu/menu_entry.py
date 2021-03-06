
class MenuEntry:
    """ Represents an entry in the menu.
        Intended to be sub-classed. """
    
    def __init__(self, callback):
        """ Builds a menu entry with its callback function to call when finished """
        self.callback = callback
        self.selected = False
        
    def call(self):
        """ Calls the function """
        self.callback(self)
        
    def select(self):
        """ Select this entry """
        self.selected = True
        
    def deselect(self):
        """ Deselect this entry """
        self.selected = False
        
    def getTextLength(self):
        """ Return the printable length of the Entry's Text """
        return 0

    def getText(self):
        """ Return the text of the Menu Entry """
        return ""