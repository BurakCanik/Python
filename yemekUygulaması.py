
def Lİstele():
    with open("YemekDosyası.txt", "r") as FILE:
        for YEMEK in FILE:
            print(YEMEK)


def YemekEkle():
    FN = input("Food Name: ")
    with open("YemekDosyası.txt", "a") as FILE:
        FILE.write(FN + '\n')


def YemekKaydet():
    with open('YemekDosyası.txt', "r") as FILE:
        liste = []

        for i in FILE:
            liste.append(i)

        with open('YemekDosyası.txt', "w") as file2:
            for i in liste:
                file2.write(i)


def MalzemeEkle():
    malzeme = input('Material Name: ')

    with open("YemekDosyası.txt", "a") as FILE:
        FILE.write(malzeme + '\n')


def MalzemeKaydet():
    with open('YemekDosyası.txt', "r") as FILE:
        liste = []

        for i in FILE:
            liste.append(i)

        with open('YemekDosyası.txt', "w") as file2:
            for i in liste:
                file2.write(i)


while True:
    Food = input('1- Listele \n 2- Yemek Ekle \n 3-Yemeği Kaydet \n 4-Malzeme Ekle \n 5-Malzemeleri Kaydet \n 6- Exit\n')

    if Food == '1':
        Lİstele()
    elif Food == '2':
        YemekEkle()
    elif Food == '3':
        YemekKaydet()
    elif Food == '4':
        MalzemeEkle()
    elif Food == '5':
        MalzemeKaydet()
    else:
        break

