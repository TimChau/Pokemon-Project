from Battle.battle_environment import BattleEnvironment
from Battle.battle_side import BattleSide
from Battle.pkmn_battle_wrapper import PkmnBattleWrapper
from Battle.Actions.battle_action import BattleAction
from Battle.Actions.attack_action import AttackAction
from Battle.Actions.action_lock import ActionLock
from Battle.Attack.attackfactory import AttackFactory
from Battle.Attack.EffectDelegates.effect_delegate import EffectDelegate
from Battle.FaintHandlers.faint_handler_factory import FaintHandlerFactory
from Trainer.trainer import Trainer
from Pokemon.pokemon_factory import PokemonFactory


def BuildFaintHandler(type = "REGULAR"):
    """ Builds a faint handler of the given type """
    return FaintHandlerFactory.buildFromType(type)

def BuildPokemon(pkmn = "BULBASAUR"):
    """ Builds a Pokemon """
    return PokemonFactory.buildStarter(pkmn)
    
def BuildTrainer(pkmn="BULBASAUR", count=1):
    """Builds a trainer with count pokmen of type pkmn """
    trainer = Trainer()
    pokemon = BuildPokemon(pkmn = pkmn)
    trainer.beltPokemon = [pokemon]
    return trainer
    
def BuildBattleSide():
    """ Builds a Battle Side """
    trainer = BuildTrainer()
    side = BattleSide(trainer)
    side.sendOutPkmnAtStart()
    return side

def BuildPokemonBattleWrapper(pkmn = "BULBASAUR",  trainer = Trainer()):
    """  Builds a Pokemon Battle Wrapper """
    pokemon = BuildPokemon(pkmn = pkmn)
    trainer.beltPokemon = [pokemon]
    
    side = BattleSide(trainer)
    wrapper = PkmnBattleWrapper(side)
    wrapper.setPkmn(pokemon)
    
    return wrapper
    
def BuildEffectDelegate():
    """ Builds an Effect Delegate """
    delegate = EffectDelegate()
    delegate.faintHandler = BuildFaintHandler(FaintHandlerFactory.REGULAR)
    return delegate
    
def BuildAttack(attack = "TACKLE"):
    """ Builds an Attack """
    return AttackFactory.getAttackAsNew(attack)
    
def BuildBattleAction(user = BuildPokemonBattleWrapper(), priority = 0):
    """ Builds a Battle Action """
    return BattleAction(user, priority)
    
def BuildAttackAction(user = BuildPokemonBattleWrapper(), target = BuildPokemonBattleWrapper(), attack = "TACKLE"):
    """ Builds an Attack Action """
    attack = BuildAttack(attack = attack)
    environment = BattleEnvironment()
    return AttackAction(attack, user, target, environment)
    
def BuildActionLock(user = BuildPokemonBattleWrapper(), attackAction = BuildAttackAction(user = BuildPokemonBattleWrapper())):
    """ Builds an Action Lock """
    attackAction.user = user
    turns = 3
    return ActionLock(user, attackAction, turns)
    
    