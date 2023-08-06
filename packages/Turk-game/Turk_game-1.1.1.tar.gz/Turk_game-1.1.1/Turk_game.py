import pygame as pg
import threading as th
import keyboard as ky
import sys, os , time , random, math
import statistics

pg.init()
pg.font.init()
#pygame baslatiliyor

class EKRAN(pg.Surface):#ekran sinifi pygame ekranı olarak kullanılacak sınıf ve bazi özellikleri turkce
    def __init__(self, boyut):
        super().__init__(boyut)
        self.boyut = boyut
        self.x,self.y = self.boyut[0] , self.boyut[1]
        self.doldur = self.fill
        self.yerlestir = self.blit
        self.cevir = self.convert
        self.kopyala = self.copy
        self.cevir_alpha = self.convert_alpha


class MASKE(pg.Mask):
    def __init__(self,size,fill):
        super().__init__(size, fill)
        self.cakisma = self.overlap



class dikdortgen(pg.Rect):#dikdortgen sinifi pg.rect ozelliklerini alir ve bazi ozellikleri turkcedir
    def __init__(self,konum,boyut):
        super().__init__(konum,boyut)
        self.carpma_listesi = self.collidedict
        self.hareket = self.move
        self.carp = self.colliderect
        self.nokta_carpmasi = self.collidepoint



class Vektor2(pg.Vector2):
    def __init__(self,x,y):
        super().__init__(x,y)

    def dogrultu_al(self):
        return self.normalize()



class OYUN:#HER TURLU ISLEM BURADA YAPILIR
    def __init__(self):
        pass
    def ekran_olustur(self,x,y,baslik="Turk_game",ikon="",boyutlandirilabilir=False):
        self.boyutlandirilabilir = boyutlandirilabilir
        if self.boyutlandirilabilir:
            self.___ekran_altyapisi___ = pg.display.set_mode((x,y),pg.RESIZABLE)
        else:
            self.___ekran_altyapisi___ = pg.display.set_mode((x,y))
        if ikon != "":
            pg.display.set_icon(ikon)
        self.___ekran___ = EKRAN((x,y))
        pg.display.set_caption(baslik)
        self.update = pg.display.update
        self.flip = pg.display.flip
        self.ciz = pg.draw
        self.ciz.cizgi = self.ciz.line
        self.ciz.yay = self.ciz.arc
        self.ciz.daire = self.ciz.circle
        self.ciz.dikdortgen = self.ciz.rect
        self.font_size = 30
        self.yazi = pg.font.SysFont("calibri",self.font_size)  # 36 punto büyüklüğünde "calibri" fontu kullan
        self.resim = pg.image
        self.mask = pg.mask
        self.mask.yuzeyden = self.mask.from_surface
        self.all = pg
        self.events = {"MOUSE_BUTONU_İNDİ":self.all.MOUSEBUTTONDOWN,"MOUSE_BUTONU_KALKTI":self.all.MOUSEBUTTONUP,"DOSYA_ATILDI":self.all.DROPFILE}
        self.muzik_yoneticisi = self.all.mixer
        self.muzik_yoneticisi.ses = self.muzik_yoneticisi.music
        self.muzik_yoneticisi.ses.yukle = self.muzik_yoneticisi.ses.load
        self.muzik_yoneticisi.ses.oynat = self.muzik_yoneticisi.ses.play
        self.muzik_yoneticisi.ses.durdur = self.muzik_yoneticisi.ses.stop
        self.muzik_yoneticisi.ses.kaldir = self.muzik_yoneticisi.ses.unload
        self.is_parcasi = th.Thread
        self.fare = pg.mouse
        self.fare.konum_al = self.fare.get_pos
        self.fare.gorunurluk_ayarla = self.fare.set_visible
        self.bekle = time.sleep
        self.dosya_yoneticisi = os
        self.rastgele = random
        self.rastgele.tamsayi = self.rastgele.randint
        self.rastgele.rasyonel_sayi = self.rastgele.uniform
        self.rastgele.secim = self.rastgele.choice
        self.matematik = self.MATEMATIK()
        return self.___ekran___
    
    def resim_yukle(self,yol):#pygame image ile resim yukler ve convert_alpha ise resmin bozulmasi ihtimalini azaltmak icindir
        return pg.image.load(yol).convert_alpha()
    
    def basildi(self,tus:str):#Bu fonksiyon keyboard modulunu kullanarak belirli bir tusun basilip basilmadigini kontrol eder
        return ky.is_pressed(tus)
    
    def maske_al(self,resim):
        return pg.mask.from_surface(self.resim_yukle(resim))

    def yukle_ve_cal(self,music):
        try:
            self.muzik_yoneticisi.ses.kaldir()
        except:
            pass
        self.muzik_yoneticisi.ses.yukle(music)
        self.muzik_yoneticisi.ses.oynat()

    def dongu(self,baslangic_islem,normal_islem,event_islem,kapandi_islem,yenileme_cesidi):#Pygame icinde en cok satir yazdiran kisimdir.AMA BU FONKSİYON BUNUN ONUNE GECMEK ICINDIR
        baslangic_islem()
        while 1:
            self.___ekran_altyapisi___.blit(self.___ekran___,(0,0))
            normal_islem()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    kapandi_islem()
                    pg.quit()
                    sys.exit()
                if event.type == pg.VIDEORESIZE and self.boyutlandirilabilir:
                    x,y = event.w, event.h
                    self.___ekran___.boyut = [x,y]
                event_islem(event)
            yenileme_cesidi()

    class MATEMATIK:
        class UCGEN:
            class DIGER:
                def __init__(self):
                    pass
            class DIK_UCGEN:
                def __init__(self):
                    pass
                def hipotenus(x,y):
                    return math.sqrt((x**2)+(y**2))
                def ucgenin_diger_kenarini_hesapla(birinci_kose:list,dik_aciya_sahip_kose:list,diger_kose:list,x_al:bool,kenar_degeri):
                    y = birinci_kose[1] - diger_kose[1]
                    x = birinci_kose[0] - diger_kose[0]
                    if x_al:
                        return (x/y)*kenar_degeri
                    else:
                        return (y/x)*kenar_degeri
                    
            def __init__(self):
                self.dik = self.DIK_UCGEN()
        def __init__(self):
            self.ucgen = self.UCGEN()
        def aritmetik_ort(self,liste:list):
            return statistics.mean(liste)
        def mutlak_deger(self,deger):
            return abs(deger)
        def uyarla(self,sayi,en_buyuk,en_kucuk,yeni_en_buyuk,yeni_en_kucuk):
            return (((sayi - en_kucuk) * (yeni_en_buyuk - yeni_en_kucuk)) / (en_buyuk - en_kucuk)) + yeni_en_kucuk