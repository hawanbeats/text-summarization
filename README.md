# Text Summarization Example

## Proje Özeti
Bu Python kodu, transformers kütüphanesindeki ``pipeline`` fonksiyonunu kullanarak metni özetler. Kullanıcıdan alınan metin, belirli bir uzunlukta (max_length, min_length) özetlenir. Bu işlem, büyük dil modelleri kullanarak metni anlamlı bir şekilde kısaltmak için yapılır.

## Çalıştırma Adımları
1. Python ve Gerekli Kütüphaneleri Yükleme
- Python'un yüklü olduğundan emin olun. Python 3.x sürümü önerilir.
- Hugging Face Transformers kütüphanesini yüklemek için terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:
``
pip install transformers
``
2. Kodun Çalıştırılması
- Bu kod, kullanıcıdan alınan metni özetlemek için Hugging Face Transformer modellerini kullanır. ``summarizer`` fonksiyonu, metnin özetini oluşturur.
3. Kodu Çalıştırma
- ``text`` değişkenine özetlemek istediğiniz metni girin. Program, girilen metni özetleyecek ve sonucu ekrana yazdıracaktır.

## Kod Açıklaması
```python
from transformers import pipeline

# Hugging Face özetleme pipeline'ını yükler
summarizer = pipeline("summarization")

# Kullanıcıdan metin al
text = input("Özetlemek istediğiniz metni girin: ")

# Metni özetler
summary = summarizer(text, max_length=30, min_length=10, do_sample=False)

# Özet sonucu ekrana yazdırılır
print("Özet:", summary[0]['summary_text'])
```
- ``pipeline("summarization")``: Bu fonksiyon, Hugging Face'in özetleme modeli olan bir pipeline oluşturur.
- ``max_length`` ve ``min_length``: Özetin maksimum ve minimum uzunluklarını ayarlamanızı sağlar.
- ``do_sample=False``: Özetin tutarlı ve deterministik olmasını sağlar.

## Örnek Çıktı
- Girdi:
```
Hugging Face, doğal dil işleme (NLP) alanında oldukça popüler bir kütüphanedir. Model eğitimi ve önceden eğitilmiş modelleri kullanarak çok çeşitli NLP görevlerini yerine getirebilirsiniz. Bu kütüphane, dil modeli oluşturma, metin sınıflandırma, özetleme, çeviri ve daha birçok NLP görevini kolaylaştırır.
```
- Çıktı:
```
Özet: Hugging Face, doğal dil işleme (NLP) alanında oldukça popüler bir kütüphanedir. Model eğitimi ve önceden eğitilmiş modelleri kullanarak çok çeşitli NLP görevlerini yerine getirebilirsiniz.
```
## Katkıda Bulunma
Katkıda bulunmak isterseniz, önerilerinizi veya hataları GitHub issues bölümünde paylaşabilir veya pull request gönderebilirsiniz.
