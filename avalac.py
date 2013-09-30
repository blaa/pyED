#!/usr/bin/python
# -*- coding: utf-8 -*-

from ed import *

##
# Basics
##
c = Character("Avalac")
c.description(race='Elf', age=176, hair='gray', eyes='gray', gender='male')
c.discipline('wizard', circle=9)

c.attributes(
    DEX=15+1,
    STR=11,
    TOU=12+1,
    PER=20+2,
    WIL=16+3,
    CHA=10,
    comment="Podnoszone: DX, TOU, 2*PER, 3*WIL"
)

c.legends(all=237723, current=-2900)
c.wealth(44747, comment="+2 monety orichalkowe")

# Calculated from DEX
#c.initiative

c.set_karma(current=20, max=34, cost=10, step=5, dice=D8, comment="K8 for passion")

c.set_defense(physical=9+1+1,  # Wątek drużyny
              spell=12+1+2+3,  # +3 Agamemnon, +2 9circle, +1 ?
              social=7+1)

c.set_armor(physical=8+4,  # ?
            mystic=3+1+3,  # +1 Passion,  +3 armor, +1 Snake, +1 fire
            comment="mystic +1 more against fire")

c.set_health(life=78,
             consciousness=67,
             wound=12,
             health_tests=2+1,
             comment=u"35(71)[78], 27(61)[67], wytrzymałość + snake, "
                     u"rany 10+passion+snake, "
                     u"+1 health test for circle")

##
# Talents
##

# 'D' - Disciplinary, 'K' - requires Karma, 'A' - requires action,
# Attribute, name, rank, options (above), circle
talent = c.add_talent
talent('PER', u"Czytanie/pisanie",                    9, 'DA', 1)
talent('PER', u"Czytanie/pisanie znaków magicznych", 10, 'DA', 1)

talent('PER', u"Rzucanie czarów",                    10, 'D', 1)
talent('PER', u"Tkanie wątków",                      10, 'D', 1)

talent('PER', u"Spojrzenie astralne",                 9, '')
talent('WIL', u"Złowieszcze mamrotanie",              5, 'D')
talent('PER', u"Zapamiętanie/odtworzenie tekstu",     1, 'D')
talent('WIL', u"Moc woli",                           11, 'D',
       comment="+1 for snake", code='POWER')

talent('PER', u"Analiza śladów",                      6, 'DA', damage=1)
talent('PER', u"Znajomość języka",                    4, 'D')
talent('PER', u"Czytanie z ruchu warg",               6, 'D')
talent('PER', u"Przyzwanie duchowego mistrza",        3, 'D')

talent('DEX', u"Broń biała",         9, '', code="MELEE")
talent('WIL', u"Podtrzymanie wątku", 4, '')
talent('TOU', u"Drewniana skóra",    5, '')
talent('WIL', u"Zimna krew",         4, '', damage=1)

# ?
talent('WIL', u"Cios w matryce",            3, '')
talent('WIL', u"Wzorzec zasięgu czarów",    3, '')

talent(None,  u"Matryca", 9)
talent(None,  u"Matryca", 9)
talent(None,  u"Matryca", 6)
talent(None,  u"Matryca", 5)
talent(None,  u"Ulepszona matryca", 6)
talent(None,  u"Ulepszona matryca", 9)
talent(None,  u"Pancerna matryca", 6)

talent(None,  u"Rytuał karmiczny",                    6)
talent(None,  u"Wytrzymałość (4/3)",                  6)
talent(None,  u"Niska magia",                         5, comment="+1 for passion")


# Extensions
ext = c.add_talent_extension
ext(u'Łączenie talentów')
ext(u'Widzenie wątków')
ext(u'Tworzenie zaklęć x2')
ext(u'Utrzymanie wątków', u'Wyczerpanie')
ext(u'Zakotwiczenie czaru', u'(1 rana != próg ran)')
ext(u'Rozplecenie wątków')
ext(u'Maskowanie wątków')
ext(u'Bezpieczne spojrzenie astralne', u'Duży sukces przeciw 7 zwykłej, 2pkt wyczerp')
ext(u'Ciche rzucanie czarów', u'2pkt. wyczerpania')

##
# Skills
##
skill = c.add_skill
skill(u'Wyszywanie szat', 1)
skill(u'Alchemia', 1)
skill(u'Botanika', 2)
skill(u'Zoologia', 2)
skill(u'Wiedza o horrorach', 3)
skill(u'Wyszukiwanie informacji 2k6')
skill(u'Język ludzki')

# Race
skill(u'Widzenie w ciemnościach', 0)


##
# Spells
##
spells = [
    # Directly offensive
    u'Miażdżąca wola',
    u'Wrząca krew',
    u'Tnąca sfera',
    u'Pocisk zagłady',
    u'Burza błyskawic',
    u'Mistyczne porażenie',

    u'Ognisty atak',
    u'Umysłowy sztylet', # Multiple?
    
    # Indirectly offensive
    u'Odcięcie karmy',
    u'Magiczna klatka',    
    u'Prowizoryczny pocisk',
    u'Prowizoryczna broń',
    u'Zaufanie',
    u'Uśpienie',
    
    u'Pnącza',
    u'Chmura pyłu',
    u'Ściana cierni',
    u'Droga wolna',
    
    # Defensive
    u'Ułatwienie uniku',
    u'Astralna tarcza',
    u'Antymagia',
    u'Magiczny pancerz',
    u'Przemieszczenie',
    u'Obronna kula',
    u'Sanktuarium', # Self-included
    
    # Moving
    u'Podskoki', # Defensive as well
    u'Latanie',    
    u'Drabina sznurowa',
    u'Lewitacja',

    u'Wyciszenie',
    u'Chodzenie po ścianach',
    
    # Powerups
    u'Żelazna dłoń',
    u'Szał bitewny',
    u'Wycelowanie',
    
    # Vision
    u'Zmysł astralny',

    # Healing etc.
    u'Oczyszczenie',
    u'Wigor',
    u'Odpoczynek',
    u'Oczyszczenie przestrzeni astralnej',
    
    # Other
    u'Rozniecenie ognia',
    u'Rozproszenie magii',
    u'Rozproszenie wątków',
    
    u'Strzaskanie zamka',
    u'Pobudka',

    # Self-made, special
    u'Lodowy atak', u'Arkchin',    
    u'Lustro', u'Światło', u'Catch spell',
    u'Kaerowa kołatka', u'Piktogram'
]

c.add_spells(sorted(spells))


##
# Weapons, armors and items
##
c.add_weapon(u'Miecz +5', damage_step=10, talent_code="MELEE")
c.add_weapon(u'Laska matryc +2', damage_step=4, talent_code="MELEE",
             comment=u"Z prowizorycznym MOC+8=" + str(c.get_dice('POWER', mod=8)))

c.add_armor(u'Skórzana warstwowa', physical_mod=5, mystic_mod=3)

item = c.add_item
item(u"Księga czarów")
item(u"Kupiecka mapa Barsawii, mapa Scyty")
item(u"Tuba na zwoje")
item(u"Szary płaszcz, ubranie podróżne")
item(u"Atrament, pióra, papier")

item(u'Klucz do biblioteki z Landis')
item(u'Amulet ochrony przed Horrorami +2 +3')
item(u'Proszek na porost ogona (2 dawki)')
item(u"Honorowy znak domu V'strimon")
item(u"Sztylet +1 (3) St:8 2k6")

item(u"Moneta esencji ziemi",     "______") # 1
item(u"Moneta esencji ognia",     "______") # 0
item(u"Moneta esencji powietrza", "______") # 0
item(u"Moneta esencji wody",      "______") # 0
item(u"Moneta esencji światła",   "______") # 0

item(u"Ziarno esencji powietrza")
item(u"2x Grudka esencji ziemi")



##
# Various other
##
c.add_comment( \
u"""
Alchemia:
Uśmiech Garlen       1/2  koszt=2
El. leczenia chorób  1/2  koszt=10
El. zdrowienia       2/3  koszt=5
Okład kelixa         2/3  koszt=5
""")

c.add_comment(u"Max damage ever: 84, tnąca sfera w maga")




c.render_basic()
c.render_spellbook()

#print unicode(c)
