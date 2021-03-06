from Screen.Console.Battle.battle_screen import BattleScreen

class BattleMessageScreen(BattleScreen):
    """ View for the Battle """
    
    def __init__(self, battle):
        """ Builds the Battle View with the Battle """
        self.messageBox = None
        BattleScreen.__init__(self, battle)

    def getBottomLines(self):
        """ Returns the Message Box """
        messageBox, messageBoxSize = self.messageBox.draw()
        return messageBox