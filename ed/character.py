#!/usr/bin/python
# -*- coding: utf-8 -*-

from spells import spellbook
from system import step_to_dice
from common import *

try:
    from mako.template import Template
    from mako.lookup import TemplateLookup
    mako_available = True
except ImportError:
    mako_available = False


class Character(object):
    def __init__(self, name):
        self.basic = {
            'name': name,
            'discipline': None,
            'circle': None,
            'race': None,
            'age': None,
            'hair': None,
            'eyes': None,
            'gender': None,

            'legends_all': None,
            'legends_current': None,
            'wealth_silver': None,
            'wealth_comment': None,
        }

        self.health = {
            'life': None,
            'consciousness': None,
            'wound': None,
            'health_tests': None,
            'comment': None
        }

        self.attribute_names = [
            'DEX', 'STR', 'TOU',
            'PER', 'WIL', 'CHA',
        ]

        self.attribute_values = {
            'DEX': None,
            'STR': None,
            'TOU': None,
            'PER': None,
            'WIL': None,
            'CHA': None,
            'comment': None,
        }

        self.attribute_steps = {
            'DEX': None,
            'STR': None,
            'TOU': None,
            'PER': None,
            'WIL': None,
            'CHA': None,
        }

        self.defense = {
            'physical': None,
            'spell': None,
            'social': None,
            'comment': None,
        }

        self.armor_stat = {
            'physical': None,
            'mystic': None,
            'comment': None,
        }

        self.karma = {
            'current': None,
            'max': None,
            'cost': None,
            'step': None,
            'dice': None,
            'comment': None
        }

        self.talents = []
        self.talent_extensions = []
        self.comments = []
        self.spells = []
        self.items = []
        self.skills = []

        self.weapons = []
        self.armors = []
        self.items = []

        # Code lookup for dice generation
        self.code_talents = {}

    def _update(self, category_name, data):
        d = getattr(self, category_name)
        for key in data.iterkeys():
            if key not in d and key != 'comment':
                print "Invalid key:", key, "for category", category_name
                raise Exception("Error")
        d.update(data)
        if 'comment' in data and data['comment']:
            d['comment'] = data['comment']


    def description(self, **kwargs):
        self._update('basic', kwargs)

    def set_health(self, life, consciousness, wound,
                   health_tests, comment=None):
        self._update('health', {
            'life': life,
            'consciousness': consciousness,
            'wound': wound,
            'health_tests': health_tests,
            'comment': comment
        })



    def legends(self, all, current=None):
        self.basic['legends_all'] = all
        if current:
            self.basic['legends_current'] = current

    def wealth(self, silver, comment=None):
        self.basic['wealth_silver'] = silver
        self.basic['wealth_comment'] = comment

    def add_comment(self, comment):
        self.comments.append(comment)

    def discipline(self, name, circle=1):
        self.basic['discipline'] = name
        self.basic['circle'] = circle

    def _update_attribute_steps(self):
        # value=10 -> step 5, then increment every 3
        for atr in self.attribute_names:
            value = self.attribute_values[atr]
            self.attribute_steps[atr] = 5 + (value-10)/3

    def attributes(self, **values):
        self._update('attribute_values', values)
        self._update_attribute_steps()

    def set_karma(self, current, max, cost, step, dice=None, comment=None):
        self._update('karma', {
            'current': current,
            'max': max,
            'cost': cost,
            'step': step,
            'dice': dice,
            'comment': comment
        })


    def set_defense(self, physical, spell, social, comment=None):
        self._update('defense', {
            'physical': physical,
            'spell': spell,
            'social': social,
            'comment': comment
        })

    def set_armor(self, physical, mystic, comment=None):
        self._update('armor_stat', {
            'physical': physical,
            'mystic': mystic,
            'comment': comment
        })


    def add_skill(self, ability, level=None):
        self.skills.append((ability, level))

    def add_talent(self, attribute, name, rank=None,
                   options='', circle=0, damage=0,
                   comment=None, code=None):
        talent = {
            'attribute': attribute,
            'name': name,
            'rank': rank,
            'comment': comment,
            'circle': circle,
            'damage': damage,

            'disciplinary': 'D' in options,
            'action': 'A' in options,
            'karma': 'K' in options,
        }

        self.talents.append(talent)
        if code:
            self.code_talents[code] = talent

    def add_talent_extension(self, name, comment=None):
        talent = {
            'name': name,
            'comment': comment,
        }

        self.talent_extensions.append(talent)


    def add_spell(self, spellname, discipline=None, comment=None):
        if not discipline:
            discipline = self.basic['discipline']

        spell = spellbook.get_spell(spellname, discipline)
        self.spells.append(spell)

    def add_spells(self, lst):
        for spell in lst:
            try:
                self.add_spell(spell)
            except UnknownSpellError:
                print "No such spell:", spell
                return


    def add_weapon(self, name, damage_step, talent_code=None, comment=None):
        weapon = {
            'name': name,
            'damage_step': damage_step,
            'talent_code': talent_code,
            'comment': comment
        }
        self.weapons.append(weapon)

    def add_armor(self, name, physical_mod, mystic_mod, comment=None):
        armor = {
            'name': name,
            'physical_mod': physical_mod,
            'mystic_mod': mystic_mod,
            'comment': comment
        }
        self.armors.append(armor)


    def add_item(self, name, comment=None):
        item = {
            'name': name,
            'comment': comment,
        }
        self.items.append(item)




    ##
    # Dice generation
    ##
    def get_talent(self, code):
        if code in self.code_talents:
            return self.code_talents[code]
        else:
            raise Exception("No such talent code")


    def get_talent_step(self, talent):
        atr = talent['attribute']
        rank = talent['rank']
        try:
            atr_step = self.attribute_steps[atr]
        except KeyError:
            raise Exception("Unknown attribute:", talent['attribute'])
        return atr_step + rank

    def get_step(self, code, mod=0):
        if code in self.attribute_steps:
            step = self.attribute_steps[code]
        elif code in self.code_talents:
            talent = self.code_talents[code]
            step = self.get_talent_step(talent)
        else:
            raise Exception("Unknown code:" + str(code))
        return step + mod


    def get_dice(self, code, mod=0):
        step = self.get_step(code, mod)
        return step_to_dice(step)

    def get_talent_dice(self, talent):
        step = self.get_talent_step(talent)
        return step_to_dice(step)


    ##
    # Printing
    ##
    def __unicode__(self):
        def formdict(d):
            pairs = ["%s=%s" % (key, unicode(value))
                     for key,value in d.iteritems()
                     if value is not None]
            return ", ".join(pairs) + "\n"

        def formentries(lst):
            s = []
            for entry in lst:
                s.append(formdict(entry))
            return "".join(s)


        s = "=== Character ===\n"
        s += formdict(self.basic)
        s += formdict(self.health)
        s += formdict(self.karma)
        s += formdict(self.attribute_steps)
        s += formdict(self.defense)
        s += formdict(self.armor_stat)

        s += "\n== Talents ==\n"
        s += formentries(self.talents)

        s += "\n== Talent extentions ==\n"
        s += formentries(self.talent_extensions)

        s += "\n== Weapons ==\n"
        s += formentries(self.weapons)

        s += "\n== Armors ==\n"
        s += formentries(self.armors)

        s += "\n== Items ==\n"
        s += formentries(self.items)

        s += "\n== Spells ==\n"
        for spell in self.spells:
            s += unicode(spell) + "\n"



        s += "\n== Comments ==\n"
        for comment in self.comments:
            s += unicode(comment) + "\n"


        return s

    def _render(self, filename, template_name, template_dir="templates/",
                title="Character chart"):
        if not mako_available:
            print "MAKO python templating is not installed"
            return
        lookup = TemplateLookup(directories=[template_dir])
        template = lookup.get_template(template_name)
        env = {
            'c': self,
            'title': title,

            'basic': self.basic,
            'health': self.health,
            'attribute_values': self.attribute_values,
            'attribute_steps': self.attribute_steps,
            'attribute_names': self.attribute_names,

            'defense': self.defense,
            'armor_stat': self.armor_stat,
            'karma': self.karma,

            'talents': self.talents,
            'talent_extensions': self.talent_extensions,

            'skills': self.skills,
            'spells': self.spells,
            'items': self.items,
            'weapons': self.weapons,
            'armors': self.armors,

            'comments': self.comments,

            'step_to_dice': step_to_dice,
        }
        html = template.render_unicode(**env)

        f = open(filename, 'w')
        f.write(html.encode('utf-8'))
        f.close()

        print html


    def render_spellbook(self, filename="spellbook.html"):
        template_dir='ed/templates/'
        template_name = 'spellbook.html'

        self._render(filename, template_name, template_dir, title="Spellbook")

    def render_basic(self, filename="basic.html"):
        template_dir='ed/templates/'
        template_name = 'basic.html'

        self._render(filename, template_name, template_dir, title="Basic data")
