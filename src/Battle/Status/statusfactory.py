from Battle.Status.burn import Burn
from Battle.Status.faint import Faint
from Battle.Status.freeze import Freeze
from Battle.Status.paralysis import Paralysis
from Battle.Status.poison import Poison
from Battle.Status.sleep import Sleep
from Battle.Status.toxic_poison import ToxicPoison

class StatusFactory:
    """ Builds status objects """
    statuses = {Burn.abbr:Burn, Faint.abbr:Faint,
                     Freeze.abbr:Freeze,
                     Paralysis.abbr:Paralysis, 
                     Poison.abbr:Poison, Sleep.abbr:Sleep,
                     ToxicPoison.abbr:ToxicPoison}
    
    @staticmethod
    def buildStatusFromAbbr(abbr):
        """ Builds a status from the status' abbreviation"""
        status = StatusFactory.statuses[abbr]()
        return status, status.start