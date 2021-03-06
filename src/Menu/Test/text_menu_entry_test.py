import unittest
from Test.test_helper import *

from Menu.menu import Menu
from Menu.text_menu_entry import TextMenuEntry


class changeSelected(unittest.TestCase):
    """ Test cases of changeSelected """
    
    def  setUp(self):
        """ Build the Menu and Entries for the test """
        self.menu = Menu()
        self.firstEntry = TextMenuEntry("1", None)
        self.secondEntry = TextMenuEntry("2", None)
        self.thirdEntry = TextMenuEntry("3", None)
        self.menu.entries = [self.firstEntry, self.secondEntry, self.thirdEntry]
        self.menu.selectEntry()
        
    def selectedChanged(self):
        """ Test that the selected Entry Changed """
        current = self.menu.current
        assert self.firstEntry.selected, "First Entry should be selected"
        self.menu.changeSelected(1)
        
        assert self.menu.current == current + 1, "Current Entry should have increased by one"
        assert not self.firstEntry.selected, "First Entry should be deselected"
        assert self.secondEntry.selected, "Second Entry should be selected"
        
    def wrapAround(self):
        """ Test that the selection can wrap around by going negative """
        current = self.menu.current
        assert self.firstEntry.selected, "First Entry should be selected"
        self.menu.changeSelected(-1)
        
        assert self.menu.current == (current - 1)% len(self.menu.entries), "Current Entry should have increased by one"
        assert not self.firstEntry.selected, "First Entry should be deselected"
        assert self.thirdEntry.selected, "Third Entry should be selected"
        
    def fullRotationBackwards(self):
        """ Test that the selection can be fully rotated through all possible actions and return to the start """
        current = self.menu.current
        assert self.firstEntry.selected, "First Entry should be selected"
        self.menu.changeSelected(-1*len(self.menu.entries))
        
        assert self.menu.current == current, "Current Entry should have be the same"
        assert self.firstEntry.selected, "First Entry should be selected"
        
    def fullRotationForwards(self):
        """ Test that the selection can be fully rotated through all possible actions and return to the start """
        current = self.menu.current
        assert self.firstEntry.selected, "First Entry should be selected"
        self.menu.changeSelected(len(self.menu.entries))
        
        assert self.menu.current == current, "Current Entry should have be the same"
        assert self.firstEntry.selected, "First Entry should be selected"

# Collect all test cases in this class
testcasesChangeSelected = ["selectedChanged", "wrapAround", "fullRotationForwards", "fullRotationForwards"]
suiteChangeSelected = unittest.TestSuite(map(changeSelected, testcasesChangeSelected))

##########################################################

# Collect all test cases in this file
suites = [suiteChangeSelected]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()