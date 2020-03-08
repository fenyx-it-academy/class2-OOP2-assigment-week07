from random import randint

class Player():

    # Savaş argümanları; Birlik, bölük, Saldırı gücü, savunma gücü, mermi, el bombası ve siperler.
    def __init__(self, birlik, boluk, saldiri_gucu, savunma_gucu, mermi, el_bombasi, siperler):
        self.abirlik = birlik
        self.aboluk = boluk
        self.asaldiri_gucu = saldiri_gucu
        self.asavunma_gucu = savunma_gucu
        self.amermi = mermi
        self.ael_bombasi = el_bombasi
        self.asiperler = siperler

# birlikler erlerden olusacak
class Private(Player):
    
    # Er attribute; künye, komutan ismi, savunma gücü
    # (25-40 arası random bir değerdir 
    # ve savunma gücü sıfırlanan asker savaş dışı kalır),
    #  mermi sayısı (50 mermi vardır ve mermi sayısı sıfırlanan asker oyun dışı kalır.)
    def __init__(self, kunye, komutan_ismi, savunma_gucu = randint(25,40), mermi = 50 ):
        self.akunye = kunye
        self.akomutan_ismi = komutan_ismi
        self.asavunma_gucu = savunma_gucu
        self.amermi = mermi

    # Saldır; Komutanın belirttiği mermi sayısınca saldırı
    #  gerçekleştirilir, aynı sayıda mermi sayısı azalır 
    # ve aynı sayıda saldırılan askerin savunma gücü azalır.
    def Saldir(self):
        pass


    # Mevziler: toplam 10 adet mevzi olsun(5 tanesi bir birliğe, diğer 5 tanesi diğer birliğe ait olacak). Albay bölükleri mevzilere yerleştirecek ve savaşa bulundukları mevzilerden başlayacaklar.)
    def Mevziler(self):
        pass

# birlikler yuzbasilar- Bölük komutanı
class Captain(Private):

    # Yüzbaşı attribute; künye, komutan ismi,
    #  bölüğündeki asker sayısı, savunma gücü
    # (savunma gücü 40-50 arası random bir değerdir 
    # ve savunma gücü sıfırlanan yüzbaşının kendiside
    #  dahil tüm birliği savaş dışı kalır) ,50 mermi, bir el bombası
    def __init__(self, kunye, komutan_ismi, asker_sayisi, savunma_gucu = randint(40,50), mermi = 50, elbombasi = 1 ):
        self.akunye = kunye
        self.akomutan_ismi = komutan_ismi
        self.aasker_sayisi = asker_sayisi
        self.asavunma_gucu = savunma_gucu
        self.amermi = mermi
        self.aelbombasi = elbombasi 

    # Albaya rapor verme (bulunulan mevzi,
    #  saldırı ve savunma gücü ve eğer saldırı olmuşsa 
    # SOS kodu, savaşılan mevziler )
    def AlbayaRaporVer(self):
        pass

    # Saldır; -Askere saldırı emri
    # (Tüm askerlerle birlikte emredilen mevziye saldırma.
    #  Saldırı kaç mermi ile yapılacağını belirler 
    # ve tüm asker o sayıda mermi ile saldırır.
    #  Kaç mermi ile saldırı yapıldıysa o sayıda saldırı 
    # yapan askerin mermi sayısı azalır 
    # ve saldırılan askerin savunma gücü aynı sayıda azalır.)
    #  -El bombası(Her yüzbaşının bir el bombası var 
    # ve bomba atılan mevzideki tüm askerler öldürür) 
    # -Er -Savaştaki en aktif asker    
    def AskereSaldirEmriVer(self):
        pass    

# birlikler 1 albay - savas komutani - olurse savas biter kaybeder
class Colonel(Private):
    # Albay attribute; künye, ordusunun ismi, 
    # emrindeki yüzbaşı listesi,1000 savunma gücü
    # (savunma gücü sıfırlanınca savaş kaybedilir) ,
    #  50 mermi
    def __init__(self, kunye, ordu_ismi, yuzbasi_list = [], savunma_gucu = 1000,mermi = 50):
       self.akunye = kunye
       self.aordu_ismi = ordu_ismi
       self.ayuzbasi_list = yuzbasi_list
       self.asavunma_gucu = savunma_gucu
       self.amermi = mermi 

    # Yeni birlik kur(Albay yeni bir bölük kurabilir,
    #  her yeni birlik bir yüzbaşı ve erlerden oluşur.
    #  Er sayısı 5 ile 10 arasında olabilir.
    #  Albayın oluşturacağı bir yüzbaşı için 50,
    #  bir er için 25 savunma gücü azalır. )
    def YeniBirlikKur(self):
        pass

    # Bir bölüğe saldırı emri (Albay emrindeki bir yüzbaşıya 
    # saldırı emri verir. Hagi mevziye saldıracağını belirtir.)
    def SaldiriEmri(self):
        pass

    # Mevzi değiştir (Albay savunma amaçlı mevzi değiştirebilir)
    def MevziDegistir(self):
        pass

    # Bölükleri incele(Albay tüm bölüklerin komutanlarının raporlarını inceleyebilir)
    def BolukleriNcele(self):
        pass




