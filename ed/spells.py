#!/usr/bin/python
# -*- coding: utf-8 -*-

from common import *

class Spell(object):

    def __init__(self, name, circle=None, threads=None, 
                 weaving=None, casting=None, range=None, effect=None,
                 duration=None, comment=None):
        self.name = name
        self.circle = circle
        self.threads = threads
        # Thread creation difficulty
        self.weaving = weaving
        # Casting difficulty
        self.casting = casting

        self.effect = effect
        self.range = range
        self.duration = duration
        self.comment = comment

    def __repr__(self):
        s = u"(%d) '%s' Threads=%s (%s): %s " % (self.circle, self.name, self.threads,
                                               self.weaving, self.effect)
        return s     

class Spellbook(object):
    def __init__(self):
        self.spells = {
            'wizard': {},
            'other': {}
        }

    def add_spells(self, spelllist, discipline):
        book = self.spells[discipline]        
        for spell in spelllist:
            book[spell.name.lower()] = spell

    def get_spell(self, name, discipline=None):
        name = name.lower()
        if discipline:
            if discipline not in self.spells:
                raise UnknownDisciplineError
            s = self.spells[discipline]
            if name not in s:
                raise UnknownSpellError(name)
            else:
                return s[name]

        # Any discipline
        for spells in self.spells.itervalues():
            if name in spells:
                return spells[name]

        raise UnknownSpellError(name)


wizard = [
    Spell(u"Badanie aury",1,1,'01/06/14',"obrona mag.",
          "25 m",u"Moc Woli + 5","5 + poziom minut","ED 158"),
    Spell(u"Chodzenie po ścianach",1,1,'01/06/14',"obrona mag.",
          "dotyk",u"Moc Woli ofiary+ +5","10 + poziom rund","ED 158"),
    Spell(u"Miażdżąca wola",1,1,'01/08/16',"obrona mag.",
          "120 m",u"Moc Woli + 5","1 runda","ED 158"),
    Spell(u"Ognisty atak",1,1,'01/07/15',"obrona mag.",
          "25 m",u"Moc Woli + 4","1 runda","ED 158"),
    Spell(u"Rozniecenie ognia",1,0,'-11',"obrona mag.",
          "5 m",u"rozpalenie łatwopalnych przedmiotów","1 runda","ED 158"),
    Spell(u"Rozproszenie magii",1,1,'01/06/13',2,
          "60 m",u"Moc Woli","1 runda","ED 158"),
    Spell(u"Umysłowy sztylet",1,0,'-7',"obrona mag.",
          "40 m",u"Moc Woli + 2","1 runda","ED 159"),
    Spell(u"Zmysł astralny",1,2,'01/05/15',"6(opis)",
          "60 m",u"Moc Woli + 6","10 + poziom min.","ED 159"),
    Spell(u"Żelazna dłoń",1,1,'01/05/13',"obrona mag.",
          "dotyk",u"zwiększone o 3 stopnie obrażenia przez b b",
          "10 + poziom rund","ED 159"),
    Spell(u"Cicha rozmowa",
          1,1,'01/05/13',4,"100 m","Moc Woli + 4","5 + poziom minut","AM 6"),
    Spell(u"Namierzanie",1,0,'-10',"obrona mag.",
          "500 m","opis","1 runda","AM 6"),
    Spell(u"Zdumiewający popis log. myslenia",1,0,'-7',"obrona mag.",
          "osobisty","Charyzma + 6","poziom minut","AM 6"),
    Spell(u"Astralna tarcza",2,0,'-7',"obrona mag.",
          "dotyk","+3 do obrony magicznej","7 + poziom rund","ED 159"),
    Spell(u"Drabina sznurowa",2,2,'01/06/14',2,
          "50 m","stworzenie drabinki sznurowej","poziom minut","ED 159"),
    Spell(u"Oczyszczenie",2,2,'01/05/13',"obrona mag.",
          "dotyk","Moc Woli + 4","1 minuta","ED 159"),
    Spell(u"Pnącza",2,1,'01/06/15',"obrona mag.",
          "50 m","Moc Woli + 4","3 + poziom rund","ED 160"),
    Spell(u"Pobudka",2,4,'01/06/15',"obrona mag.",
          "dotyk",u"ustawienie alarmu na odpowiednia porę","do 24 godzin","ED 160"),
    Spell(u"Rozrzutnik",2,1,'01/07/16',"obrona mag.",
          "10 m",u"-4 do obrony społecznej ofiary","3 + poziom minut","ED 160"),
    Spell(u"Ułatwienie uniku",2,0,'-8',"obrona mag.",
          "osobisty","+3 stopnie do uniku","5 + poziom rund","ED 160"),
    Spell(u"Zaplombowanie",2,1,'06/11/11',4,
          "20 m","Moc Woli + 6","8 + poziom minut","AM 6"),
    Spell(u"Forsowny marsz",3,2,'01/10/13',"obrona mag.",
          "dotyk","Moc Woli + 4","4 + poziom godz.","ED 160"),
    Spell(u"Lewitacja",3,1,'01/08/18',"obrona mag.(opis)",
          "100 m","wylewitowanie do 1000 kg","5 + poziom minut","ED 160"),
    Spell(u"Podskoki",3,0,'-9',"obrona mag.",
          "dotyk","Moc Woli + 7","5 + poziom rund","ED 160"),
    Spell(u"Strzaskanie zamka",3,2,'01/06/13',"obrona mag.",
          "5 m","Moc Woli + ","1 runda","ED 160"),
    Spell(u"Szał bitewny",3,1,'01/09/16',"obrona mag.",
          "dotyk",u"+4 stopnie do testu ataku i obrażeń","7 + poziom rund","ED 161"),
    Spell(u"Wycelowanie",3,1,'01/07/15',"obrona mag.",
          "dotyk",u"+ 3 stopnie do ataku bronią strzelecka","1 + poziom minut","ED 161"),
    Spell(u"Wyciszenie",3,1,'01/07/15',"obrona mag.",
          "dotyk",u"+ 3 stopnie do testów skradania","1 + poziom minut","ED 161"),
    Spell(u"Fałszywa aura",3,2,'07/12/11',"obrona mag.",
          "dotyk",u"Moc Woli + 6","13 + poziom min.","AM 6"),
    Spell(u"Koci chód",3,1,'07/12/11',"obrona mag.",
          "dotyk",u"+6 stopni do testów wspinaczki i równowagi","8 + poziom rund","AM 6"),
    Spell(u"Leczniczy sen",3,2,'07/12/11',"obrona mag.",
          "60 m",u"podwojenie liczby testów zdrow. i + 4 st","8 godzin","AM 7"),
    Spell(u"Rozpoznanie zaklęcia",3,0,'-12',"obrona mag.(opis)",
          "60 m",u"opis","1 runda","AM 7"),
    Spell(u"Uderzenie w aurę",3,1,'07/12/11',"obrona mag.",
          "40 m",u"Moc Woli + 8","1 runda","AM 7"),
    Spell(u"Wodne skrzydła",3,1,'01/07/15',"obrona mag.",
          "dotyk",u"skrzydła wietrzniaka stają się wodoodporne","poziom godzin","AM 7"),
    Spell(u"Znamię Czarodzieja ",3,2,'01/06/15',"obrona mag.",
          "40 m",u"Moc Woli + 6","1 + poziom godz.","AM 7"),
    Spell(u"Chmura pyłu",4,2,'01/09/13',"obrona mag.",
          "80 m",u"-2 st. do akcji wy. wzroku, słuchu i węchu",
          "5 + poziom rund","ED 161"),
    Spell(u"Inwentaryzacja",4,4,'01/09/18',"obrona mag. przed.",
          "25 m",u"Moc Woli + 8","1 minuta","ED 161"),
    Spell(u"Kłębek nici",4,3,'01/10/15',2,
          "zmienny","Moc Woli + 6","3 + pozim godzin","ED 161"),
    Spell(u"Odpoczynek",4,3,'01/09/13',"obrona mag.",
          "dotyk","Moc Woli + 2","1 runda","ED 161"),
    Spell(u"Ściana cierni",4,1,'01/11/13',2,
          "dotyk","Moc Woli + 2","7 + pozim rund","ED 161"),
    Spell(u"Zaufanie",4,1,'13/17',"obrona mag.",
          "50 m","Moc Woli +3","poziom minut","ED 162"),
    Spell(u"Dotyk kuglarza",4,2,'01/10/17',"2/obrona mag.(opis)",
          "30 m","Moc Woli + 6","poziom rund","AM 8"),
    Spell(u"Dryfowanie",4,1,'13/20',"obrona mag.",
          "osobisty",u"+ 2 do testów pływania","poziom godzin","AM 8"),
    Spell(u"Lodowe palce",4,1,'07/12/11',"obrona mag.",
          "osobisty",u"zmniejszenie obrażeń wywołanych ogniem","5 + poziom minut","AM 8"),
    Spell(u"Magiczne więzy",4,2,'01/10/17',"obrona mag.",
          "40 m","Moc Woli + 8","2 + poziom minut","AM 8"),
    Spell(u"Płaszcz Czarodzieja",4,2,'01/10/17',"obrona mag.",
          "dotyk","Moc Woli + 8","5 + poziom minut","AM 8"),
    Spell(u"Połączenie karmy",4,1,'01/10/17',"obrona mag.",
          "dotyk","Moc Woli + 10","1 runda","AM 8"),
    Spell(u"Rozpoznanie magii",4,1,'01/10/20',"obrona mag.",
          "80 m","opis","1 runda","AM 9"),
    Spell(u"Szalone włosy",4,0,'-20',"obrona mag.",
          "25 m","-2 do akcji","5 + poziom rund","AM 9"),
    Spell(u"Antymagia",5,1,'-11',"obrona mag.",
          "15 m","Moc Woli + 5","poziom minut","ED 162"),
    Spell(u"Latanie",5,2,'01/07/18',"obrona mag.",
          "osobisty",u"pozwala latać","15 + poziom min.","ED 162"),
    Spell(u"Magiczny pancerz",5,1,'01/12/16',"obrona mag.(opis)",
          "dotyk","+4 do fizycznego pancerza","7 + poziom minut","ED 162"),
    Spell(u"Prowizoryczny pocisk",5,1,'01/09/15',"opis",
          "dotyk","Moc Woli + 6","2 + poziom rund","ED 162"),
    Spell(u"Spowolnienie",5,2,'01/07/15',"obrona mag.",
          "dotyk",u"- 5 st. do testów Zręczności","5 + poziom rund","ED 162"),
    Spell(u"Wigor",5,2,'01/09/17',"obrona mag.",
          "dotyk",u"+ 5 st. do testów zdrowienia","1 + poziom godz.","ED 162"),
    Spell(u"Mistyczne porażenie",5,2,'01/11/21',"obrona mag.",
          "10 m","Moc Woli + 10","1 runda","AM 9"),
    Spell(u"Olbrzymi wzrost",5,2,'01/11/18',"obrona mag.",
          "dotyk",u"+ 5 st. do testów S. Fiz. i Żywotności","2 + poziom minut","AM 9"),
    Spell(u"Rozgrzanie metalu",5,2,'01/11/18',"obrona mag.",
          "10 m",u"Moc Woli + 5","7 + poziom rund","AM 9"),
    Spell(u"Schronienie",5,3,'01/11/18',6,
          "dotyk",u"Moc Woli + 6","10 + poziom min.","AM 9"),
    Spell(u"Zbadanie wątku",5,2,'01/11/15',"obrona mag.",
          "dotyk",u"Moc Woli + 5","poziom minut","AM 9"),
    Spell(u"Odcięcie karmy",6,2,'01/11/18',"obrona mag.",
          "100 m",u"Uniemożliwia wykorzystanie karmy","8 + poziom rund","ED162"),
    Spell(u"Pocisk zagłady",6,3,'01/10/21',"obrona mag.",
          "100 m",u"Moc Woli + 5","poziom rund","ED162"),
    Spell(u"Prowizoryczna broń",6,1,'01/10/15',"obrona mag.",
          "dotyk",u"Moc Woli + 8","5 + poziom rund","ED163"),
    Spell(u"Przemieszczenie",6,2,'01/09/16',"obrona mag.",
          "osobisty",u"Moc Woli + 7","5 + poziom rund","ED163"),
    Spell(u"Tnąca sfera",6,2,'01/11/19',"obrona mag.",
          "100 m",u"Moc Woli + 15","1 runda","ED163"),
    Spell(u"Uśpienie",6,2,'01/09/17',"obrona mag.",
          "60 m",u"Uśpienie tylu ofiar ile wynosi poziom","10 + poziom rund","ED163"),
    Spell(u"Biblioteka umysłu",6,3,'01/12/19',6,
          "osobisty",u"+ 10 do talenty Zapamiętanie Tekstu","poziom godzin","AM10"),
    Spell(u"Pożyczenie zaklęcia",6,2,'01/11/15',"obrona mag.",
          "dotyk",u"Czasowe przekazanie zaklęcia","4 + poziom rund","AM10"),
    Spell(u"Przechowanie zaklęcia",6,2,'01/12/19',6,
          "dotyk",u"Moc Woli + 6","poziom godzin","AM10"),
    Spell(u"Utrata krwi",6,3,'01/12/22',"obrona mag.",
          "dotyk",u"Ofiara nie może leczyć ran","1 + poziom dni","AM10"),
    Spell(u"Zwielokrotniony umysłowy sztylet", 6, u"różny",'01/09/22',"obrona mag.",
          "1 km",u"Moc Woli + 2","1 runda","MA135"),
    Spell(u"Burza błyskawic",7,4,'01/12/18',"obrona mag.",
          "120 m",u"Moc Woli + 10","5 + poziom rund","ED163"),
    Spell(u"Droga wolna",7,0,'-17',"obrona mag.",
          "120 m",u"Moc Woli + 4","1 runda","ED163"),
    Spell(u"Magiczna Klatka",7,3,'01/11/19',"obrona mag.",
          "100 m",u"- 5 do Rzucania Czarów i Tkania Wąt.","8 + poziom rund","ED163"),
    Spell(u"Rozproszenie wątków",7,1,'13/20',"obrona mag.",
          "60 m",u"Moc Woli + 3","1 runda","ED163"),
    Spell(u"Wrząca krew",7,3,'01/12/17',"obrona mag.",
          "60 m",u"Moc Woli + 9","4 rundy","ED164"),
    Spell(u"Astralny dar",7,3,'13/23',"obrona mag.",
          "30 m",u"Daje ofierze wzrok astralny","5 rund","AM11"),
    Spell(u"Mistyczna sieć",7,3,'13/20',"obrona mag.",
          "40 m",u"Moc Woli + 8","2 + poziom minut","AM11"),
    Spell(u"Płynne oczy",7,3,'13/23',"obrona mag.",
          "40 m",u"Oślepienie ofiary","poziom rund","AM11"),
    Spell(u"Usunięcie zaklęcia",7,1,'01/09/22',"obrona mag.",
          "60 m",u"Moc Woli + 10","1 runda","AM11"),
    Spell(u"Wiadomość",7,2,'01/10/17',"obrona mag.",
          "150 km",u"Przesłanie informacji","1 runda","AM11"),
    Spell(u"Bezpieczne otwarcie",8,2,'01/12/19',"obrona mag.",
          "5 m.",u"Moc Woli + 8","5 + poziom rund","ED164"),
    Spell(u"Dodatkowy atak",8,2,'14/20',"obrona mag.",
          "dotyk",u"Moc Woli + 15","10 + poziom rund","ED164"),
    Spell(u"Kocia kołyska",8,4,'01/12/20',"obrona mag.",
          "25 m.",u"Dzielenie rzucenia czarów","poziom minut","ED164"),
    Spell(u"Miażdżąca sfera",8,3,'15/22',"obrona mag.",
          "75 m.",u"Moc Woli + 10","7 + poziom rund","ED164"),
    Spell(u"Ochronna maska",8,3,'13/15',"obrona mag.",
          "dotyk",u"Moc Woli + 10","5 + poziom rund","ED164"),
    Spell(u"Narzucenie pokoju",8,3,'01/11/21',"obrona mag.",
          "dotyk",u"Moc Woli + 10","5 + poziom rund","AM12"),
    Spell(u"Porwanie zaklęcia",8,2,'14/24',"obrona mag.",
          "60 m",u"Moc Woli + 10","1 eunda","AM12"),
    Spell(u"Schwytanie zaklęcia",8,2,'14/21',"obrona mag.",
          "osobisty",u"Moc Woli + 12","poziom rund","AM12"),
    Spell(u"Nieożywiony świadewk",9,3,'01/12/15',"obrona mag.",
          "dotyk",u"Uzyskanie odpowiedzi przedmiotu","1 minuta","KW73"),
    Spell(u"Obronna kula",9,3,'13/19',"obrona mag.",
          "60 m",u"Moc Woli + 8","12 + poziom rund","KW73"),
    Spell(u"Przytwierdzenie kończyny",9,6,'15/15',"obrona mag.",
          "dotyk",u"Moc Woli","1 runda","KW74"),
    Spell(u"Trzecie oko",9,4,'14/15',"obrona mag.",
          "60 m",u"Moc Woli + 10","poziom minut","KW74"),
    Spell(u"Widzenie przeszłości",9,5,'14/15',"obrona mag.",
          "5 m",u"Moc Woli + 3","zmienny","KW74"),
    Spell(u"Świetlisty rój",9,4,'01/12/22',8,
          "10 m",u"Stworzenie roju świetlistych owadów","3 + poziom rund","MA12"),
    Spell(u"Ukierunkowanie surowej magii",9,2,'01/12/25',"obrona mag.",
          "25 m",u"Skierowanie energii astralnej na ofiarę","3 rundy","MA13"),
    Spell(u"Wyczyszczenie matryc",9,u"różna",'01/12/22',"obrona mag.",
          "60 m",u"Moc Woli + 12","1 runda","MA13"),
    Spell(u"Darcie ciała",10,4,'16/19',"obrona mag.",
          "100 m",u"Moc Woli + 6","poziom rund","KW74"),
    Spell(u"Przywrócenie życia",10,7,'14/15',"obrona mag.",
          "dotyk",u"Moc Woli + 15","poziom dni","KW75"),
    Spell(u"Śmiertelna przysięga",10,3,'13/22',"obrona mag.",
          "dotyk",u"Moc Woli + 10","poziom tygodni","KW75"),
    Spell(u"Utrzymanie wzorca",10,6,'14/23',2,
          "dotyk",u"Moc Woli + 8","poziom dni","KW76"),
    Spell(u"Wypaczenie przestrzeni astralnej",10,3,'17/23',15,
          "50 m",u"- 8 do stopnia Rzucania Czarów","5 + poziom rund","KW76"),
    Spell(u"Ćwiartowanie",10,4,'16/26',"obrona mag.",
          "dotyk",u"Moc Woli + 15","1 runda","AM14"),
    Spell(u"Połączenie zaklęć",10,4,'16/26',7,
          "40 m",u"Moc Woli + 3","3 rundy","AM14"),
    Spell(u"Blokada magii",11,4,'16/25',10,
          "40 m",u"- 10 do testów opartych na magii","3 + poziom minut","AM14"),
    Spell(u"Zmiana formy",12,8,'16/26',"obrona mag.",
          "dotyk",u"Opis","1 runda","AM14"),
    Spell(u"Oczyszczenie przestrzeni astralnej",13,5,'20/28',10,
          "dotyk",u"Moc Woli + 12","1 runda","AM15"),
    Spell(u"Miasto w butelce",15,8,'18/33',12,
          "40 km",u"Zagarniecie terenu","1 + poziom dni","AM15"),

    # Self-added
    Spell(u"Sanktuarium", 99, 3, "11/18", "?", u"100m²", "moc+8 do obrony",
          "10+poziom minut", "self-added"),
    Spell(u"Lodowy atak",1,1,'08/15',"obrona mag.",
          "20 m",u"Moc Woli + 5","1 runda","self-made"),
    Spell(u"Arkchin",99,0,'-/11',"obrona mag.",
          "30 m",u"Moc Woli + 3","2 runda","self-made"),
    Spell(u"Lustro",99,1,'9/17',"obrona mag.",
          "75 m",u"Tworzy lustro o pow. 25m²","5 min.","self-made"),
    Spell(u"Światło",1,1,'9/13',"obrona mag.",
          "15 m",u"Rozświetla teren wokół maga","5+poz. min.","self-made"),

    Spell(u"Kaerowa kołatka",1,0,'--',"--",
          "dotyk",u"Pozwala stukać do Kaerów","--","self-made"),

    Spell(u"Piktogram",1,0,'--',"--",
          "dotyk",u"Pozwala pisać do Kaerów","--","self-made"),

    Spell(u"Catch spell",99,2,'14/21',"obrona mag.",
          "osobisty",u"moc+12, jak wygram w teście mogę trzymać zaklęcie",
          "poz. rund.","self-made"),
    ]

spellbook = Spellbook()
spellbook.add_spells(wizard, 'wizard')


if __name__ == '__main__':
    for i, spell in enumerate(wizard):
        print "Spell", i, spell.name
        print unicode(spell)
    print "Getting spell:"
    s = spellbook.get_spell('Badanie aury')
    print s
