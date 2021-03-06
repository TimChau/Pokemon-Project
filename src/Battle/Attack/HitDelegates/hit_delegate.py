import random

class HitDelegate(object):
    """ Represents an Attack's ability to hit an opponent """
    accMods = [1.0, 4/3.0, 5/3.0, 2.0, 7/3.0, 8/3.0, 3.0,
                    1/3.0, 3/8.0, 3/7.0, 1/2.0, 3/5.0, 3/4.0]
                    
    MISS = "Attack missed."
    STATUSMISS =  "But it failed."
    
    messages = [MISS, STATUSMISS]
  
    def __init__(self, parent, toHit):
        """ Build a core hit Delegate """
        self.parent = parent
        self.chanceToHit = toHit
    
    def hit(self, user, target, environment):
        """ Returns whether or not an attack hit its target """
        return not target.fainted() and not self.dodging(target)\
                   and self.hitGhost(target) and self.core(user, target),\
                   [self.messages[self.parent.isStatus()]]
        
    def core(self, user, target):
        """ Calculates a random #, compares to chanceToHit to determine if it
        lands or not """
        toHit = self.getChanceToHit(user, target)
        return self.checkHit(random.randint(0, 99), toHit)
        
    def getChanceToHit(self, user, target):
        """ Return the modified chance to hit """
        accuracy = user.getAbility().onAccuracy(self.chanceToHit)
        mod = self.getMod(user, target)
        return accuracy*mod
        
    def getMod(self, user, target):
        """ Return the mod based on the User's Acc mod and Target's Evasion mod """
        accLvl = user.statMods["ACC"]
        evasLvl = target.statMods["EVAS"]
        
        if accLvl*evasLvl >= 0:
            # They are countering each other, so subtract them
            mod = HitDelegate.accMods[accLvl-evasLvl]
        else:
            accMod = HitDelegate.accMods[accLvl]
            evasMod = HitDelegate.accMods[-evasLvl]
            mod = accMod*evasMod
        
        return mod
        
    def checkHit(self, rand, toHit):
        """ Return whether the target hits based on the hit chance
        and random value value passed """
        return rand < toHit
        
    def dodging(self, target):
        """ Returns if the opp is dodging """
        return target.dodge is not None
        
    def hitGhost(self, target):
        """ Return if the attack misses because the target is GHOST """
        if self.parent.isStatus():
            return True # Status moves can always hit GHOST Pkmn
        
        isGhost = "GHOST" in target.getTypes()
        normalAndFighting = self.parent.type in ["NORMAL", "FIGHTING"]
        
        return not (isGhost and normalAndFighting)
        