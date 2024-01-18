import time, math, random

player_attack = 1
player_defense = 0
player_health = 3
aantal_rupee = 0

sleutel_schatkist = ''
dekamerkeuze = ''
item = ''

print("# === [kamer 1] === #")
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

print("# === [kamer 7] === #")
print('Je stapt door de deur.')

geen_rupee = input('Kies een getal tussen de 1 en de 10: ')
geen_rupee_optie = random.randint(1, 10)
if geen_rupee == geen_rupee_optie:
    print('Helaas, de rupee is al meegenomen door iemand anders.')
    aantal_rupee = 0
elif  geen_rupee != geen_rupee_optie:
    print('Je ziet een rupee liggen en pakt het.')
    aantal_rupee = 1
print('')
time.sleep(1)

rechts_of_rechtdoor = input('Wil je rechts of rechtdoor? ')

print("# === [kamer 2] === #")
if rechts_of_rechtdoor == "rechts":
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een rupee vast.')
    print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')
    getal1 = random.randint(10, 25)
    getal2 = random.randint(-5, 75)
    som = f'{getal1} + {getal2}'
    antwoord_som = getal1 + getal2
    print(f'Daarboven zie je een som staan {som} = ?')
    antwoord = int(input('Wat toets je in? '))

    if antwoord == antwoord_som:
        print('Het standbeeld laat de rupee vallen en je pakt het op')
        aantal_rupee += 1
    else:
        print('Er gebeurt niets....')

    print('Je ziet een deur achter het standbeeld.')
    rechts_of_rechtdoor2 = input('Wil je rechts of rechtdoor? ')
    print('')
    time.sleep(1)

print("# === [kamer 6] === #")
if rechts_of_rechtdoor == "rechts":
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
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
    print('')
    time.sleep(1)
    dekamerkeuze = input('Wil je door naar kamer 3? (ja/nee)')

print("# === [kamer 8] === #")
if dekamerkeuze == "nee" or rechts_of_rechtdoor == "rechtdoor":
    dekamerkeuze = "kamer 3"
    print('Je loopt verder door de gang en komt in een lange kamer.')
    print('Aan het einde van de kamer zie je een glinsterende gokmachine.')

    gokmachine_gebruiken = input('Wil je de gokmachine gebruiken? (ja/nee) ')

    if gokmachine_gebruiken.lower() == "ja":
        print('Je gooit de dobbelstenen...')
        dobbelsteen1 = random.randint(1, 6)
        dobbelsteen2 = random.randint(1, 6)
        totaal = dobbelsteen1 + dobbelsteen2

        print(f'Je dobbelstenen tonen {dobbelsteen1} en {dobbelsteen2}. Totaal: {totaal}')

        if totaal > 7:
            aantal_rupee *= 2
            print(f'Gefeliciteerd! Je hebt gewonnen en het aantal rupees is verdubbeld. Je hebt nu {aantal_rupee} rupees.')
        elif totaal < 7:
            player_health -= 1
            print(f'Helaas, je hebt verloren. Je verliest 1 health. Je hebt nu {player_health} health.')
            if player_health <= 0:
                print('Je health is nu 0. Game over.')
                exit()
        else:
            aantal_rupee *= 2
            player_health -= 1
            print(f'Je hebt zowel gewonnen als verloren. Het aantal rupees is verdubbeld, maar je verliest ook 1 health. Je hebt nu {aantal_rupee} rupees en {player_health} health.')
    else:
        print('Je besluit de gokmachine niet te gebruiken en kijkt rond in de kamer.')
        print('Je ziet een volgende deur.')

    dekamerkeuze = input('Wil je door naar kamer 3? (ja/nee)')

print('')
time.sleep(1)

print("# === [kamer 9] === #")
if dekamerkeuze == "nee":
    print('Je opent de deur en loopt naar binnen.')
    betovering = random.choice(["defense", "health"])

    if betovering == "defense":
        player_defense += 1
        print('Je voelt een beschermende betovering om je heen. Je krijgt 1 verdedigingspunt erbij!')
    elif betovering == "health":
        player_health += 2
        print('Een helende betovering omringt je. Je krijgt 2 extra gezondheidspunten!')

    print('Je voelt de betovering en vervolgt je avontuur in de kamer.')

    kamer9klaar = "ja"


print('')
time.sleep(1)



print("# === [kamer 3] === #")
if dekamerkeuze == "ja" or kamer9klaar == "ja":
    print('Je duwt hem open en stapt een hele lange kamer binnen.')
    print(f'Je hebt {aantal_rupee} rupee.')
    if aantal_rupee == 1:
        item_antwoord = input('Wil je met de rupee een zwaard (1) of een schild (2) of een sleutel (3) kopen? ')
        if item_antwoord == "1":
                item = "zwaard"
                aantal_rupee = 0
                player_attack += 2
        elif item_antwoord == "2":
                item = "schild"
                aantal_rupee = 0
                player_defense += 1
        elif item_antwoord == "3":
            item = "niks"
            aantal_rupee = 0
            sleutel_schatkist = "ja"
    if aantal_rupee == 2:
        item_antwoord = input('Wil je met de twee rupees een zwaard en een schild kopen? (ja/nee/andere optie) ')
        if item_antwoord == "ja":
            item = "zwaard en schild"
            aantal_rupee = 0
            player_attack += 2
            player_defense += 1
        elif item_antwoord == "nee":
            item_antwoord = input('Wil je met de rupee een zwaard (1) of een schild (2) of een sleutel (3) kopen? ')
        if item_antwoord == "1":
                item = "zwaard"
                aantal_rupee = 0
                player_attack += 2
        elif item_antwoord == "2":
            item = "schild"
            aantal_rupee = 0
            player_defense += 1
        elif item_antwoord == "3":
            item = "niks"
            sleutel_schatkist = "ja"
            aantal_rupee = 0
        elif item_antwoord == "andere optie":
            item_antwoord = input('Wil je met de twee rupees een zwaard en een sleutel (1) of een schild en sleutel (2) kopen? ')
            if item_antwoord == "1":
                item = "zwaard"
                aantal_rupee = 0
                player_attack += 2
                sleutel_schatkist = "ja"
            elif item_antwoord == "2":
                item = "schild"
                aantal_rupee = 0
                player_defense += 1
                sleutel_schatkist = "ja"
    if aantal_rupee >= 3:
        item_antwoord = input('Wil je met de rupees een zwaard, een schild en een sleutel kopen? (ja/nee) ')
        if item_antwoord == "ja":
            item = "zwaard en schild"
            aantal_rupee = 0
            player_attack += 2
            player_defense += 1
            sleutel_schatkist = "ja"
        elif item_antwoord == "nee":
            item_antwoord = input('Wil je met de twee rupees een zwaard en een schild kopen? (ja/nee/andere optie) ')
            if item_antwoord == "ja":
                item = "zwaard en schild"
                aantal_rupee = 0
                player_attack += 2
                player_defense += 1
            elif item_antwoord == "nee":
                item_antwoord = input('Wil je met de rupee een zwaard (1) of een schild (2) of een sleutel (3) kopen? ')
                if item_antwoord == "1":
                        item = "zwaard"
                        aantal_rupee = 0
                        player_attack += 2
                elif item_antwoord == "2":
                    item = "schild"
                    aantal_rupee = 0
                    player_defense += 1
                elif item_antwoord == "3":
                    item = "niks"
                    sleutel_schatkist = "ja"
                    aantal_rupee = 0
            elif item_antwoord == "andere optie":
                item_antwoord = input('Wil je met de twee rupees een zwaard en een sleutel (1) of een schild en sleutel (2) kopen? ')
                if item_antwoord == "1":
                    item = "zwaard"
                    aantal_rupee = 0
                    player_attack += 2
                    sleutel_schatkist = "ja"
                elif item_antwoord == "2":
                    item = "schild"
                    aantal_rupee = 0
                    player_defense += 1
                    sleutel_schatkist = "ja"

    elif rechts_of_rechtdoor == "rechtdoor":
        dekamerkeuze = "kamer 3"
        

    elif dekamerkeuze == 'kamer 3':
        if item == "zwaard" or item == "schild" or item == "zwaard en schild":
            print(f'In deze kamer staat een tafel met daarop een {item}.')
            print(f'Je pakt het {item} op en houdt het bij je.')
            print('Op naar de volgende deur.')
    if item == "niks":
        print(f'In deze kamer staat een tafel met helaas {item} er op')
        print('Op naar de volgende deur.')

    print('')
    time.sleep(1)

print("# === [kamer 4] === #")
vijand_attack = 2
vijand_defense = 0
vijand_health = 3
print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
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

print("# === [kamer 10] === #")
dungeonboss_attack = 3
dungeonboss_defence = 1
dungeonboss_health = 5

dungeonboss_hit_damage = max(0, dungeonboss_attack - player_defense)  # Gebruik max(0, ...) om negatieve waarden te vermijden
if dungeonboss_hit_damage <= 0:
    print('Jij hebt een te goede verdediging voor de dungeonboss, hij kan je geen schade doen.')
else:
    dungeonboss_attack_amount = math.floor(player_health / dungeonboss_hit_damage)

    player_hit_damage = max(0, player_attack - dungeonboss_defence)  # Gebruik max(0, ...) om negatieve waarden te vermijden
    player_attack_amount = math.floor(dungeonboss_health / player_hit_damage)

    if player_attack_amount < dungeonboss_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de dungeonboss.')
        print(f'Je health is nu {player_health}.')
        if player_health <= 0:
            print('Game over.')
            exit()
    else:
        print('Helaas de dungeonboss is te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)

print("# === [kamer 5] === #")
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
if sleutel_schatkist == "ja":
    print('Je loopt ernaartoe.')
    print('Game over.')
else:
    print('Sorry, je hebt niet de sleutel om de schatkist te openen.')
    print('Game over.')