from alwayshit_delegate import AlwaysHitDelegate
from crash_delegate import CrashDelegate
from hit_delegate import HitDelegate
from hitself_delegate import HitSelfDelegate
from piercedodge_delegate import PierceDodgeDelegate
from statushit_delegate import StatusHitDelegate


from Battle.Attack.EffectDelegates.effect_delegatefactory import EffectDelegateFactory

from resources.tags import Tags
from resources.sqlite.pokemon_sqlite_helper import GetParameters

class HitDelegateFactory:
    """ Builds HitDelegates """
    MISS = "Attack missed."
    STATUSMISS =  "But it failed."
    
    @staticmethod
    def loadFromAttackDex(attackdex, parent):
        """ Builds a HitDelegate from a file of the designated type """
        delegateType = attackdex.readline().strip()
        
        if delegateType == "CORE":
            accuracy = int(attackdex.readline().strip())
            return HitDelegate(parent, accuracy, "Attack missed.")
            
        elif delegateType == "STATUS CORE":
            accuracy = int(attackdex.readline().strip())
            return HitDelegate(parent, accuracy, "But it failed.")
            
    @staticmethod
    def loadFromXML(element, parent):
        """ Builds a HitDelegate from XML """
        delegateType = element.find(Tags.typeTag).text
        
        if delegateType == "ALWAYS":
            return AlwaysHitDelegate(HitDelegateFactory.MISS)
        
        elif delegateType == "CORE":
            accuracy = int(element.find(Tags.hitTag).text)
            return HitDelegate(parent, accuracy)
            
        elif delegateType == "CRASH":
            accuracy = int(element.find(Tags.hitTag).text)
            element = element.find(Tags.effectDelegateTag)
            delegate = EffectDelegateFactory.loadFromXML(element, parent)
            return CrashDelegate(parent, accuracy, HitDelegateFactory.MISS, delegate)
            
        elif delegateType == "PIERCE DODGE":
            accuracy = int(element.find(Tags.hitTag).text)
            pierce = element.find(Tags.pierceTag).text
            return PierceDodgeDelegate(parent, accuracy, pierce)
            
        elif delegateType == "SELF":
            return HitSelfDelegate()
            
        elif delegateType == "STATUS ALWAYS":
            return AlwaysHitDelegate(HitDelegateFactory.STATUSMISS)
            
        elif delegateType == "STATUS CORE":
            accuracy = int(element.find(Tags.hitTag).text)
            return StatusHitDelegate(parent, accuracy)
        
    @staticmethod
    def loadFromDB(cursor, parent):
        """ Builds a HitDelegate from database"""
        type, id = HitDelegateFactory.GetTypeAndID(cursor, parent.name)
        
        if type == "ALWAYS":
            return AlwaysHitDelegate(HitDelegateFactory.MISS)
        
        elif type == "CORE":
            accuracy = GetParameters(cursor, "accuracy", "CoreHitDelegate", id)
            return HitDelegate(parent, accuracy)    
            
        elif type == "CRASH":
            accuracy = int(element.find(Tags.hitTag).text)
            element = element.find(Tags.effectDelegateTag)
            delegate = EffectDelegateFactory.loadFromXML(element, parent)
            return CrashDelegate(parent, accuracy, HitDelegateFactory.MISS, delegate)
            
        elif type == "PIERCE DODGE":
            accuracy = int(element.find(Tags.hitTag).text)
            pierce = element.find(Tags.pierceTag).text
            return PierceDodgeDelegate(parent, accuracy, pierce)
            
        elif type == "SELF":
            return HitSelfDelegate()
            
        elif type == "STATUS ALWAYS":
            return AlwaysHitDelegate(HitDelegateFactory.STATUSMISS)
            
        elif type == "STATUS CORE":
            accuracy = GetParameters(cursor, "accuracy", "CoreHitDelegate", id)
            return StatusHitDelegate(parent, accuracy)
            
    @staticmethod
    def GetTypeAndID(cursor, name):
        """ Returns the type and id of the Hit Delegate for the attack """
        cursor.execute("SELECT HitDelegateVariants.type, Attack.hit_id from Attack, HitDelegateVariants where HitDelegateVariants.id = Attack.hit_type and name = ?", (name,))
        return cursor.fetchone()
            
    @staticmethod
    def buildNull():
        """ Returns a Null hit delegate """
        """ May not need """
        return None