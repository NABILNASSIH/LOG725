from settings import PLAYER_SPEED
from commands import MoveBatUpCommand, MoveBatDownCommand
from pgzero.keyboard import keyboard    
def p1_controls(bat):
    if keyboard.z or keyboard.down:
        MoveBatDownCommand(bat).execute()
        return PLAYER_SPEED  # Ou la valeur appropriée
    elif keyboard.a or keyboard.up:
        MoveBatUpCommand(bat).execute()
        return -PLAYER_SPEED  # Ou la valeur appropriée
    return 0  # Retourner 0 si aucune touche n'est pressée


def p2_controls(bat):
    if keyboard.m:  # Supposons que la touche 'm' fait descendre la raquette du joueur 2
        MoveBatDownCommand(bat).execute()
        return PLAYER_SPEED  # Retourne la vitesse positive pour un mouvement vers le bas
    elif keyboard.k:  # Supposons que la touche 'k' fait monter la raquette du joueur 2
        MoveBatUpCommand(bat).execute()
        return -PLAYER_SPEED  # Retourne la vitesse négative pour un mouvement vers le haut
    return 0  # Retourner 0 si aucune touche n'est pressée
