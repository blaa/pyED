pyED
====

Character card generator for a (paper-based) RPG game Earthdawn as a declarative Python library.
Along with library for dice rolls, step/dice recalculation etc.
Based on 1st edition (polish version), might require tweaks for newer versions.

Uses Mako template engine for card generation.

Currently spells (ed/spells.py) are copied from a Polish game edition (I found
them on the web on some hobby-site. I'm afraid I don't remember currently which
site, which is a shame - I'd give the credit. Using Emacs/vim macros I converted them
easily from a table into a simple py-database. Feel free to create english
version or add just the ones you need).

Program license does not cover the data or the trademarks or some other s...tuff - just the code.

avalac.py has a definition for my long-running character - 9nth circle mage. Running this script
should generate two files: basic.html and spellbook.html containing a character sheet.


This is how it works:

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
        comment="Some comment on what got incremented: DX, TOU, 2*PER, 3*WIL"
    )
    
    c.legends(all=237723, current=-2900)
    c.wealth(44747, comment="+2 monety orichalkowe")
    
    # Calculated from DEX
    #c.initiative
    
    c.set_karma(current=20, max=34, cost=10, step=5, dice=D8, comment="K8 for passion")
    
    c.set_defense(physical=9+1+1,  # Wątek drużyny
                  spell=12+1+2+3,  # +3 Agramon, +2 9circle, +1 ?
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
    
    (...)
    
    # Talent extensions, name + comment
    ext = c.add_talent_extension
    ext(u'Łączenie talentów')
    ext(u'Widzenie wątków')
    ext(u'Tworzenie zaklęć x2')
    ext(u'Zakotwiczenie czaru', u'(1 rana != próg ran)')
    ext(u'Ciche rzucanie czarów', u'2pkt. wyczerpania')
    (...)
    
    ##
    # Skills
    ##
    skill = c.add_skill
    skill(u'Wyszywanie szat', 1)
    skill(u'Alchemia', 1)
    skill(u'Botanika', 2)
    (...)
    
    skill(u'Widzenie w ciemnościach', 0)
     
    
    ##
    # Spells
    ##
    spells = [
        u'Miażdżąca wola',
        u'Wrząca krew',
        u'Tnąca sfera',
        (...)
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
    
    
    c.add_comment(u"Max damage ever: 84, tnąca sfera w maga")
    
    c.render_basic()
    c.render_spellbook()
  
