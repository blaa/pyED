#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

class Dice(object):
    def __init__(self, level, times=1):
        # Do NOT change the values while dice has been created. Recreate
        # With new values each time.
        self.times = times
        self.level = level

    def __repr__(self):
        if self.times == 1:
            return "D%d" % self.level
        else:
            return "%dD%d" % (self.times, self.level)
        
    def __rmul__(self, times):
        return Dice(self.level, self.times * times)

    def __add__(self, dice):
        if isinstance(dice, Dice):
            r = Roll([self, dice])
        else:
            r = Roll([self]) + dice
        return r

    def __eq__(self, dice):
        # Compare only values, not times
        return self.level == dice.level

    def cast(self):
        result = 0
        times = self.times
        while times > 0:
            c = randint(1, self.level)
            result += c
            if c != self.level:
                times -= 1
            else:
                print "BONUS D%d" % self.level
        return result
        

class Roll(object):
    def __init__(self, dice=[]):
        self.dice = dice
        
    def __add__(self, roll_or_dice):
        if isinstance(roll_or_dice, Dice):
            try:
                idx = self.dice.index(roll_or_dice)
                lst = self.dice[:]
                lst[idx] = Dice(lst[idx].level, lst[idx].times + roll_or_dice.times)
                return Roll(lst)
            except ValueError:
                pass
            return Roll(self.dice + [roll_or_dice])
        else:
            return Roll(self.dice + roll_or_dice.dice)

    def __rmul__(self, times):
        return Roll([times * dice for dice in self.dice])

    def __repr__(self):
        def cmp(a, b):
            a = a.level * a.times
            b = b.level * b.times
            if a < b:
                return 1
            elif a > b:
                return -1
            else:
                return 0
        return "+".join(repr(dice) for dice in sorted(self.dice, cmp=cmp))

    def cast(self):
        results = [dice.cast() for dice in self.dice]
        return sum(results)

D4 = Dice(4)
D6 = Dice(6)
D8 = Dice(8)
D10 = Dice(10)
D12 = Dice(12)
D20 = Dice(20)
D100 = Dice(100)

cycle = [D4, D6, D8, D10, D12, 2*D6,
         D8 + D6, D10 + D6, D10 + D8,
         2*D10, D12 + D10]

def step_to_dice(step):
    if step < 3:
        raise NotImplementedError
    if step <= 13: # 3 - 13
        return cycle[step - 3]
    if step <= 24: # 14 - 24
        return D20 + cycle[step - 14]
    if step <= 35: # 25 - 35
        return D20 + D10 + D8 + cycle[step - 25]
    if step <= 40: # 36 - 40
        return 2*D20 + D10 + D8 + cycle[step - 36]
    
    raise NotImplementedError

if __name__ == "__main__":
    roll = D8 + (2*D6 + D20) + D8 + D8
    print roll
    result = roll.cast()
    print "You've rolled", result
    for i in range(3, 41):
        print "Step=%d --> %s" % (i, step_to_dice(i))
