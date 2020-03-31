import os
class auta():

    marka = "Marka"
    model = "Model"
    rocznik = 0
    pojemnosc= 0
    przebieg = 0
    skrznia = 'B'

    def __init__(self, marka=None, model=None, rocznik=None, pojemnosc=None, przebieg=None, skrzynia=None):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.pojemnosc = pojemnosc
        self.przebieg = przebieg
        self.skrzynia = skrzynia

    def zapis(self):
         with open("dane.txt", "a") as plik:
            marka = input("podaj marke: ") + " "
            plik.write(marka)
            model = input("podaj model: ") + " "
            plik.write(model)
            rocznik = input("podaj rocznik: ") + " "
            plik.write(rocznik)
            pojemnosc = input("podaj pojemnosc: ") + " "
            plik.write(pojemnosc)
            przebieg = input("podaj przebieg: ") + " "
            plik.write(przebieg)
            skrzynia = input("podaj rodzaj skrzyni biegow: ") +" \n"
            plik.write(skrzynia)

            samochod=auta(marka, model, rocznik, pojemnosc, przebieg, skrzynia )
            samochody.append(samochod)

    def wyswietl(self,samochod):
                print(samochod.marka, end=" ")
                print(samochod.model, end= " ")
                print(samochod.rocznik, end= " ")
                print(samochod.pojemnosc, end= " ")
                print(samochod.przebieg, end=" ")
                print(samochod.skrzynia, end=" ")

def wysswietlw():
    print("Filtorwanie wedlug pojemnosci.")
    print("Wyswietl \n1.Wieksze od x \n2.Mniejsze od x\n")
    wybor =input()
    if (wybor == 1):
        p = (input("podaj x: "))
        for i in range(samochody.__len__()):
            if samochody[i].pojemnosc>p:
                print(samochody[i].marka, end=" ")
                print(samochody[i].model, end=" ")
                print(samochody[i].rocznik, end=" ")
                print(samochody[i].pojemnosc, end=" ")
                print(samochody[i].przebieg, end=" ")
                print(samochody[i].skrzynia, end=" ")

            else:
                p = input("podaj x: ")
                for i in range(samochody.__len__()):
                    if samochody[i].pojemnosc < p:
                        print(samochody[i].marka, end=" ")
                        print(samochody[i].model, end=" ")
                        print(samochody[i].rocznik, end=" ")
                        print(samochody[i].pojemnosc, end=" ")
                        print(samochody[i].przebieg, end=" ")
                        print(samochody[i].skrzynia, end=" ")

def wyswietlk():
   w = input("ktory samochod z kolei chcesz wyswietlic: ")
   print(samochody[w].marka, end=" ")
   print(samochody[w].model, end=" ")
   print(samochody[w].rocznik, end=" ")
   print(samochody[w].pojemnosc, end=" ")
   print(samochody[w].przebieg, end=" ")
   print(samochody[w].skrzynia, end=" ")


samochody=[]
samochod=auta()
z=input("Czy chcesz korzystac z istniejacego pliku?\n1.Tak\n2.Nie (wybranie tej opcji spowoduje usuniecie istniejacej bazy)\n")
if z == "1":
    with open('dane.txt') as plik:
        print(plik.read())
        samochody.append(samochod);
else:
    while z !="0":
        os.system('CLS')
        x=input("Co chcesz zrobic?\n1.Dodaj samochod\n2.Pokaz liste samochodow\n3.Odczytaj warunkowo\n4.Wyswietl konkretny samochod\n5.Usun konkretny samochod\n7.Posortuj Samochody po parametrze\n0. nic\n")

        if x=="1":
            os.system('CLS')
            samochod.zapis()



        if x=="2":
            print("lista samochodow:")
            for i in range(samochody.__len__()):
                samochod.wyswietl(samochody[i])


        if x=="3":
            wysswietlw()

        if x=="4":
            wyswietlk()


        if x=="5":
            i=input ("ktory samochod chcesz usunac:")
            i=int(i)
            samochody.pop(i)
            samochod.zapis()

        print("koniec")









