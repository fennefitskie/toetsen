import time, math, random

player_attack = 1
player_defense = 0
player_health = 3

sleutel_schatkist = ''

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 7] === #
print('Je stapt door de deur.')
print('Je ziet een rupee liggen en pakt het.')
rupee = 1
print('')
time.sleep(1)

# === [kamer 2] === #
print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')
getal1 = random.randint(10, 25)
getal2 = random.randint(-5, 75)
som = f'{getal1} + {getal2}'
antwoord_som = getal1 + getal2
print(f'Daarboven zie je een som staan {som} = ?')
antwoord = int(input('Wat toets je in? '))

if antwoord == antwoord_som:
    print('Het standbeeld laat de sleutel vallen en je pakt het op')
else:
    print('Er gebeurt niets....')

print('Je ziet een deur achter het standbeeld.')
print('')
time.sleep(1)

dekamerkeuze = input("Wil jij naar kamer 3 of naar kamer 6? ")

# === [kamer 6] === #
if dekamerkeuze == 'kamer 6':
    zombie_attack = 1
    zombie_defense = 0
    zombie_health = 2
    print(f'Dapper met je handen loop je de kamer binnen.')
    print('Je loopt tegen een zombie aan.')

    zombie_hit_damage = (zombie_attack - player_defense)
    if zombie_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
    else:
        zombie_attack_amount = math.floor(player_health / zombie_hit_damage)

        player_hit_damage = (player_attack - zombie_defense)
        player_attack_amount = math.floor(zombie_health / player_hit_damage)

        if player_attack_amount < zombie_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            player_health -= zombie_attack_amount * zombie_hit_damage
            print(f'Je health is nu {player_health}.')
        else:
            print('Helaas is de zombie te sterk voor je.')
            print('Game over.')
            exit()

# === [kamer 3] === #

print('Je hebt een rupee.')
item_antwoord = input('Wil je met de rupee een zwaard of een schild kopen?  ')
if item_antwoord == "zwaard":
    player_attack += 2
elif item_antwoord == "schild":
    player_defense += 1

elif dekamerkeuze == 'kamer 3':
    print('Je duwt hem open en stapt een hele lange kamer binnen.')
    print(f'In deze kamer staat een tafel met daarop een {item_antwoord}.')
    print(f'Je pakt het {item_antwoord} op en houdt het bij je.')
    print('Op naar de volgende deur.')
    print('')
    time.sleep(1)

# === [kamer 4] === #
vijand_attack = 2
vijand_defense = 0
vijand_health = 3
print(f'Dapper met je nieuwe {item_antwoord} loop je de kamer binnen.')
print('Je loopt tegen de vijand aan.')

vijand_hit_damage = (vijand_attack - player_defense)
if vijand_hit_damage <= 0:
    print('Jij hebt een te goede verdediging voor de vijand, hij kan je geen schade doen.')
else:
    vijand_attack_amount = math.floor(player_health / vijand_hit_damage)

    player_hit_damage = (player_attack - vijand_defense)
    player_attack_amount = math.floor(vijand_health / player_hit_damage)

    if player_attack_amount < vijand_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de vijand.')
        player_health -= vijand_attack_amount * vijand_hit_damage
        print(f'Je health is nu {player_health}.')
        if player_health <= 0:
            print('Game over.')
            exit()
    else:
        print('Helaas is de vijand te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
if antwoord == antwoord_som:
    print('Je loopt ernaartoe.')
    print('Game over.')
else:
    print('Sorry, je hebt niet de sleutel om de schatkist te openen.')
    print('Game over.')
