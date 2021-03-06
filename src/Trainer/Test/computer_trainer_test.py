import unittest
from Test.test_helper import BuildPokemonBattleWrapper

from Battle.Attack.attackfactory import AttackFactory
from Trainer.computer_trainer import ComputerTrainer


class pickAction(unittest.TestCase):
    """ Test cases of pickAction """
    
    def  setUp(self):
        """ Build the Trainer and Pokemon lists for use in tests """
        self.trainer = ComputerTrainer()
        self.battlePkmn = BuildPokemonBattleWrapper(trainer = self.trainer)
        self.targetPkmn  = BuildPokemonBattleWrapper()
        
        self.attack = AttackFactory.getAttackAsNew("TACKLE")
        self.battlePkmn.pkmn.battleDelegate.attacks = [self.attack]
        
    def actionIsAttack(self):
        """ Check that the attack returned by getAction is an attack the Pokemon has """
        attackAction = self.trainer.pickAction(self.battlePkmn, [self.targetPkmn], None, None, None)
        assert attackAction.attack is self.attack, "Should be the attack"
        
    def userIsBattlePkmn(self):
        """ Check the user is the Battle Pkmn """
        attackAction = self.trainer.pickAction(self.battlePkmn, [self.targetPkmn], None, None, None)
        assert attackAction.user is self.battlePkmn, "Should be the Battle Pkmn"

    def targetIsTargetPkmn(self):
        """ Check the target is the Target Pkmn """
        attackAction = self.trainer.pickAction(self.battlePkmn, [self.targetPkmn], None, None, None)
        assert attackAction.target is self.targetPkmn, "Should be the Target Pkmn"

# Collect all test cases in this class
testcasesPickAction = ["actionIsAttack",  "userIsBattlePkmn", "targetIsTargetPkmn"]
suitePickAction  = unittest.TestSuite(map(pickAction, testcasesPickAction))

##########################################################

class getHeader(unittest.TestCase):
    """ Test cases of getFirstPokemon """
    
    def  setUp(self):
        """ Build the Trainer and Pokemon lists for use in tests """
        self.trainer = ComputerTrainer()
        
    def headerIsCompHeader(self):
        """ Check that the attack returned by getAction is an attack the Pokemon has """
        assert self.trainer.getHeader() is ComputerTrainer.header, "Should be 'Enemy '"

# Collect all test cases in this class
testcasesGetHeader = ["headerIsCompHeader"]
suiteGetHeader   = unittest.TestSuite(map(getHeader , testcasesGetHeader ))

##########################################################
# Collect all test cases in this file
suites = [suitePickAction, suiteGetHeader]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()