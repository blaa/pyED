pyED
====

Character card generator for a (paper-based) RPG game Earthdawn as a declarative Python library.

Along with library for dice rolls, step/dice recalculation etc.

Uses Mako template engine for card generation.

Currently spells (ed/spells.py) are copied from a Polish game edition (I found
them on the web on some hobby-site I'm afraid I don't remember currently which
is a shame - I'd give the credit. Using Emacs/vim macros I converted them
easily from a table into a simple py-database. Feel free to create english
version or add just the ones you need).

Program license does not cover the data or the trademarks or some other s...tuff - just the code.

avalac.py has a definition for my long-running character - 9nth level mage. Running this script
should generate two files: basic.html and spellbook.html containing a character sheet.
