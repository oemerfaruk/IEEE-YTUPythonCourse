import sqlite3


# Ana Sınıf (Base Class)
class BankaHesabi:
    def __init__(self, ad, bakiye = 0):
        self.ad = ad
        self.bakiye = bakiye

# Türetilmiş Sınıf: Bireysel (TC Kimlik No ile)
class BireyselHesap(BankaHesabi):
    def __init__(self, ad, tc_no, bakiye=0):
        super().__init__(ad, bakiye)
        self.tc_no = tc_no
        self.tip = "Bireysel"

# Türetilmiş Sınıf: Tüzel (Vergi No ile)
class TuzelHesap(BankaHesabi):
    def __init__(self, ad, vergi_no, bakiye=0):
        super().__init__(ad, bakiye)
        self.vergi_no = vergi_no
        self.tip = "Tuzel"


class BankaSistemi:
    def __init__(self):
        self.conn = sqlite3.connect("banka.db")
        self.cursor = self.conn.cursor()

        self.kurulum_yap()

    def kurulum_yap(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS musteriler 
            (id INTEGER PRIMARY KEY, ad TEXT, tip TEXT, kimlik_no TEXT, bakiye REAL)
        """)

        self.conn.commit()

    def musteri_ekle(self, hesap_objesi):
        kimlik = hesap_objesi.tc_no if hesap_objesi.tip == "Bireysel" else hesap_objesi.vergi_no

        self.cursor.execute("INSERT INTO musteriler (ad, tip, kimlik_no, bakiye) VALUES (?,?,?,?)",
                            (hesap_objesi.ad, hesap_objesi.tip, kimlik, hesap_objesi.bakiye))
        
        self.conn.commit()

    def para_islem(self, m_id, miktar):
        # miktar pozitifse para yatırma, miktar negatifse para çekme
        self.cursor.execute("UPDATE musteriler SET bakiye = bakiye + ? WHERE id = ?", (miktar, m_id))

        self.conn.commit()

    def ozet_rapor_al(self):
        self.cursor.execute("SELECT * FROM musteriler")
        veriler = self.cursor.fetchall()

        with open("ozet_rapor.txt", "w", encoding="utf-8") as f:
            f.write("--- Banka Müşteri Özet Listesi ---\n")

            for veri in veriler:
                satir = f"ID: {veri[0]} | Tip: {veri[2]} | Ad: {veri[1]} | Bakiye {veri[4]}\n"
                f.write(satir)
        
        print("\n[!] Özet Rapor başarıyla oluşturuldu")

def main():
    sistem = BankaSistemi()

    while True:
        print("\n--- IEEE Banka Yönetim Paneli ---")
        print("1. Bireysel Müşteri Ekle")
        print("2. Tüzel Müşteri Ekle")
        print("3. Para Yatır / Çek")
        print("4. Özet Bilgileri Dosyaya Yazdır")
        print("5. Çıkış")

        secim = input("İşleminiz: ")

        if secim == "1":
            ad = str(input("Ad Soyad: "))
            tc = str(input("TC No: "))
            sistem.musteri_ekle(BireyselHesap(ad, tc))
            print("Bireysel hesap açıldı.")
        elif secim == "2":
            ad = str(input("Ad Soyad: "))
            v_no = str(input("Vergi No: "))
            sistem.musteri_ekle(TuzelHesap(ad, v_no))
            print("Tüzel hesap açıldı.")
        elif secim == "3":
            m_id = int(input("Müşteri ID: "))
            tutar = float(input("Tutar (çekmek için eksi değer girin): "))
            sistem.para_islem(m_id, tutar)
            print("İşlem tamamlandı.")

        elif secim == "4":
            sistem.ozet_rapor_al()

        elif secim == "5":
            break


if __name__ == "__main__":
    main()