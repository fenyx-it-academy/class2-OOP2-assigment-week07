# class2-OOP2-assigment-week06

- Bir savaş oyunu yazılacak. Bu oyunda iki askeri birlik birbiri ile savaşacak.
- Birlikler; Bir albay(Colonel), yüzbaşılar(Captain) ve erlerden(Private) oluşacak.
-Savaş argümanları; Birlik, bölük, Saldırı gücü, savunma gücü, mermi, el bombası ve
siperler.
- Savaşın amacı düşman birliğinin albayını öldürmek.
- Albay;
- Savaş komutanı.
- Albay attribute; künye, ordusunun ismi, emrindeki yüzbaşı listesi,1000
savunma gücü(savunma gücü sıfırlanınca savaş kaybedilir) , 50 mermi
- Albay method;
- Yeni birlik kur(Albay yeni bir bölük kurabilir, her yeni birlik bir yüzbaşı ve
erlerden oluşur. Er sayısı 5 ile 10 arasında olabilir. Albayın oluşturacağı
bir yüzbaşı için 50, bir er için 25 savunma gücü azalır. )
- Bir bölüğe saldırı emri (Albay emrindeki bir yüzbaşıya saldırı
emri verir. Hagi mevziye saldıracağını belirtir.)
- Mevzi değiştir (Albay savunma amaçlı mevzi değiştirebilir)
- Bölükleri incele(Albay tüm bölüklerin komutanlarının raporlarını
inceleyebilir)
- Oyun sırası kendine gelen bir albay mevzi değiştir, saldır veya yeni bir bölük
kur hamlelerinden sadece birini yapabilir. 'Bölükleri incele' methodu hamle
hakkını kaybettirmez.
- Yüzbaşı;
- Bölük komutanı
- Yüzbaşı attribute; künye, komutan ismi, bölüğündeki asker sayısı, savunma
gücü(savunma gücü 40-50 arası random bir değerdir ve savunma gücü
sıfırlanan yüzbaşının kendiside dahil tüm birliği savaş dışı kalır) ,50 mermi, bir el
bombası
- Yüzbaşı method;
- Albaya rapor verme (bulunulan mevzi, saldırı ve savunma
gücü ve eğer saldırı olmuşsa SOS kodu, savaşılan mevziler )
- Saldır;
-Askere saldırı emri(Tüm askerlerle birlikte emredilen mevziye
saldırma. Saldırı kaç mermi ile yapılacağını belirler ve tüm asker o
sayıda mermi ile saldırır. Kaç mermi ile saldırı yapıldıysa o sayıda
saldırı yapan askerin mermi sayısı azalır ve saldırılan askerin
savunma gücü aynı sayıda azalır.)
-El bombası(Her yüzbaşının bir el bombası var ve bomba atılan
mevzideki tüm askerler öldürür)
-Er
-Savaştaki en aktif asker
- Er attribute; künye, komutan ismi, savunma gücü(25-40 arası random bir
değerdir ve savunma gücü sıfırlanan asker savaş dışı kalır), mermi sayısı (50
mermi vardır ve mermi sayısı sıfırlanan asker oyun dışı kalır.)
- Er method;
- Saldır; Komutanın belirttiği mermi sayısınca saldırı gerçekleştirilir, aynı
sayıda mermi sayısı azalır ve aynı sayıda saldırılan askerin
savunma gücü azalır.
- Mevziler:
toplam 10 adet mevzi olsun(5 tanesi bir birliğe, diğer 5 tanesi diğer birliğe ait
olacak). Albay bölükleri mevzilere yerleştirecek ve savaşa bulundukları
mevzilerden başlayacaklar.)
KOD:
- Bu oyun için üç class olacak(Private, Captain, Colonel ).
- Captain ve Colonel Private classının alt classı olacak
- Tüm sınıflardaki ilgili attribute ve method isimeri aynı olacak(overriding
yapılacak)
- getattr,issubclass, isinstance, setattr gibi yöntemlerini araştırıp kodunuz için
uygun olanlarını kullanınız.
- Tüm methodları en az bir defa uygulayacak şekilde kodunuzu oluşturunuz.:

!!Yazdığınız kodu iki oyuncunun oynayabilieceği veya bilgisayara karşı bir oyuna
dönüştürünüz.(Bonusa kadar işin %90 bitmiş oluyor zaten. Çok basit While döngüleri
ile bir oyuna dönüştürebilceğinizi düşünüyorum.)
