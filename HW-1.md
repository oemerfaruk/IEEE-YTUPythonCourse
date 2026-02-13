🎯 Proje Ödev - Sezar Şifreleme Algoritması (Python)

### 🧩 Konu:

Bu ödevde, **C++ dilini kullanarak Sezar (Caesar) Şifreleme algoritmasını** uygulayacaksınız.  
Kullanıcıdan bir **metin (string)** ve bir **anahtar (integer)** değeri alınacak.  

Girilen metin, anahtar yardımıyla şifrelenip ekrana yazdırılacak ve ardından bu şifre çözülerek orijinal metin geri elde edilecektir.

---

### 📘 Görev Tanımı:

1. Kullanıcıdan bir metin (örneğin: `"HELLO"`) alın.
2. Kullanıcıdan bir anahtar değeri (örneğin: `3`) alın.
3. Aşağıdaki iki fonksiyonu **kendiniz tanımlayın ve kullanın:**
    - `string encrypt(string text, int key)`  
        → Metni verilen anahtar kadar kaydırarak **şifrelenmiş metni döndürür.**
    - `string decrypt(string encryptedText, int key)`  
        → Şifrelenmiş metni aynı anahtar değeriyle çözerek **orijinal metni döndürür.**
    - Aşağıda verilen `main()` fonksiyonu yapısını tamamla.
	    - Yorum satırlarını ( `...` ) kendi kodunla doldur.
	    - Program kullanıcıdan metin ve anahtar almalı, ardından şifreleme ve çözme sonuçlarını göstermelidir.
4. Programın sonunda ekrana şu bilgiler sırasıyla yazdırılmalıdır:
    - Orijinal metin
    - Şifrelenmiş metin
    - Çözülmüş metin

---

### 🧠 İpucu:

- Şifreleme işlemi için karakterleri ASCII tablosunda kaydırabilirsiniz.
- Sadece harfleri kaydırmak istiyorsanız `isalpha()` fonksiyonunu kullanabilirsiniz.
- Harf büyük/küçük farkını korumak için `isupper()` veya `islower()` fonksiyonlarını kullanabilirsiniz.
- Karakterleri döngü içinde `char(int(mes[i]) + key)` gibi dönüştürebilirsiniz.

## 🧭 **Önerilen orta yol (en verimli yöntem):**

> “Aşağıda **programın ana yapısı** verilmiştir.  
> Sizden beklenen, `encrypt()` ve `decrypt()` fonksiyonlarını kendiniz tanımlayıp `main` içinde çağırmaktır.”

```cpp
int main() {
	// Değişkenleri tanımla
    string text, encryptedText, decryptedText;
    int key;

    // 1. Kullanıcıdan metin al
    ...

    // 2. Anahtar al
    ...

    // 3. Şifreleme fonksiyonunu çağır
    ...

    // 4. Şifre çözme fonksiyonunu çağır
    ...

    // 5. Sonuçları ekrana yazdır
    ...

    return 0;
}

```

### ✅ Teslim Koşulları:

- Dosya adı: `caesar_cipher.cpp`
- Dosyanın en başında **yorum satırı olarak** aşağıdaki bilgileri ekleyin:
 ```cpp
// Öğrenci Adı: [Adınızı Yazın]
// Öğrenci Soyadı: [Soyadınızı Yazın]
// Ödev: Sezar Şifreleme (Caesar Cipher)
```

- GitHub hesabınızda bir depo (repository) oluşturun.
- Bu deponun içinde **`odev`** adlı bir klasör açın ve `.py` dosyanızı buraya yükleyin.
- Hazırladığınız GitHub repo linkini ve `.py` dosyanızı ödev teslim sistemine ekleyin.
- Kod kullanıcıdan veri almalı ve çıktıyı ekranda göstermelidir.
- Kodunuzu açıklayıcı **yorum satırları** (`#`) ile zenginleştirin.
#### Kod derlenip çalıştırıldığında aşağıdaki örneğe benzer bir çıktı üretmelidir:
```
Enter your text:
HELLO WORLD
Enter your key: 3

Original Text: HELLO WORLD
Encrypted Text: KHOOR#ZRUOG
Decrypted Text: HELLO WORLD
```

### 🧾 Değerlendirme Ölçütleri:
|Kriter|Açıklama|Puan|
|---|---|---|
|Doğru şifreleme ve çözme işlemi|Metin doğru şekilde şifrelenip çözülebilmeli|40|
|Fonksiyon yapılarının doğru kullanımı|`encrypt` ve `decrypt` fonksiyonları tanımlanmalı|25|
|Kullanıcı etkileşimi ve çıktı düzeni|Kullanıcıdan veri alma ve sonuç gösterimi düzenli olmalı|20|
|Kodun okunabilirliği ve açıklama satırları|Yorum satırları, değişken adları ve biçimlendirme|15|
|**Toplam**||**100**|
