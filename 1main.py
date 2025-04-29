#A package directory containing multiple modules and other sub packages.
''' [Module[boss.py]]-->[Module[player.py]]-->[package[characters]]--->[package[game]]<--package[weapons]<--[Module[gun.py]]<--[Module[knife.py]]'''
# pip is the standard pakage manager for python that heps to install and manage additional pakages thatare not available in the python standard library 
import game.characters.player
game.characters.player.get_player_info()

from game.characters import player
player.get_player_info()

from game.characters.boss import get_boss_info
get_boss_info()