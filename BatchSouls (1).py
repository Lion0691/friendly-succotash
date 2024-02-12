import random

def lancer_de(min_value, max_value):
    return random.randint(min_value, max_value)

def afficher_combat(nom_personnage, points_de_vie, points_de_vie_boss, nom_boss):
    print(f"\n{nom_personnage} {points_de_vie} X {points_de_vie_boss} {nom_boss}")

def combat_boss(nom_personnage, points_de_degats, nom_boss, points_de_vie_boss_initial):
    points_de_vie = 20
    points_de_vie_boss = points_de_vie_boss_initial
    
    while points_de_vie > 0 and points_de_vie_boss > 0:
        afficher_combat(nom_personnage, points_de_vie, points_de_vie_boss, nom_boss)

        action = input("Souhaitez-vous attaquer ou vous soigner? (A, S): ").upper()

        if action == 'A':
            degats_infliges = lancer_de(1, 10) + points_de_degats
            points_de_vie_boss -= degats_infliges
            print(f"Vous attaquez ! Vous avez infligé {degats_infliges} points de dégâts.")
        elif action == 'S':
            soin = lancer_de(1, 5)
            print(f"Vous vous soignez ! Vous récupérez {soin} points de vie.")
            points_de_vie += soin

        if points_de_vie_boss > 0:
            degats_subis = lancer_de(1, 5)
            points_de_vie -= degats_subis
            print(f"Votre ennemi attaque ! Il vous inflige {degats_subis} points de dégâts.")

    if points_de_vie_boss <= 0:
        print("!!! VICTOIRE !!!")
        return True
    else:
        print("!!! DEFAITE !!!")
        return False

def ranking(nom_personnage, points_de_degats):
    print("\n--- RANKING ---")
    print(f"{nom_personnage}: {points_de_degats} points de dégâts")

def jouer():
    print("BATCH SOULS\n")
    nom_personnage = input("Choisissez le nom de votre personnage : ")
    points_de_degats = 10

    while True:
        if combat_boss(nom_personnage, points_de_degats, "BOSS1", 50):
            points_de_degats += 1
        else:
            points_de_degats = max(10, points_de_degats - 1)

        choix = input("Voulez-vous procéder au niveau suivant ou rester à ce niveau ? (P, R): ").upper()
        if choix == 'R':
            ranking(nom_personnage, points_de_degats)
        elif choix != 'P':
            break

        if combat_boss(nom_personnage, points_de_degats, "BOSS2", 50):
            points_de_degats += 1
        else:
            points_de_degats = max(10, points_de_degats - 1)

        choix = input("Voulez-vous procéder au niveau suivant ou rester à ce niveau ? (P, R): ").upper()
        if choix == 'R':
            ranking(nom_personnage, points_de_degats)
        elif choix != 'P':
            break

        if combat_boss(nom_personnage, points_de_degats, "BOSS3", 50):
            points_de_degats += 1
        else:
            points_de_degats = max(10, points_de_degats - 1)

        choix = input("Voulez-vous procéder au niveau suivant ou rester à ce niveau ? (P, R): ").upper()
        if choix == 'R':
            ranking(nom_personnage, points_de_degats)
        elif choix != 'P':
            break

        if combat_boss(nom_personnage, points_de_degats, "FINAL BOSS \"XXX\"", 100):
            points_de_degats += 1
        else:
            points_de_degats = max(10, points_de_degats - 1)

        ranking(nom_personnage, points_de_degats)

if __name__ == "__main__":
    jouer()
