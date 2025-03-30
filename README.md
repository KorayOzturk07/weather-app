
# Hava Durumu Uygulaması

Bu Python uygulaması, kullanıcının girdiği şehir adı ile hava durumu bilgisini gösterir. OpenWeatherMap API'si kullanılarak hava durumu verisi alınır ve Tkinter kütüphanesi ile görsel bir kullanıcı arayüzü (GUI) oluşturulmuştur.

## Özellikler
- Şehir adı girildiğinde hava durumu bilgisini gösterir.
- Uygulama, sıcaklık bilgilerini Celsius (°C) cinsinden gösterir.
- Hava durumu açıklamaları Türkçe dilinde sunulur.
- Kullanıcı dostu bir Tkinter GUI'si ile hava durumu bilgileri görsel olarak sunulur.

## Gereksinimler
Bu uygulama için aşağıdaki Python kütüphanelerine ihtiyaç vardır:
- `requests` (API ile veri almak için)
- `tkinter` (GUI oluşturmak için)

Aşağıdaki komutla gerekli kütüphaneleri yükleyebilirsiniz:

```
pip install -r requirements.txt
```

**Not**: Tkinter, Python ile birlikte gelir, ancak bazı sistemlerde ayrıca yüklenmesi gerekebilir. Tkinter'ı yüklemek için aşağıdaki komutu kullanabilirsiniz:
```
sudo pacman -S tk
```

## Kurulum

1. **API Anahtarını Alın**:
   OpenWeatherMap API anahtarınızı [OpenWeatherMap](https://openweathermap.org/api) üzerinden alabilirsiniz.

2. **API Anahtarını Projeye Ekleyin**:
   `weather.py` dosyasındaki `API_KEY` değişkenine aldığınız API anahtarını ekleyin.

3. **Gerekli Kütüphaneleri Yükleyin**:
   Aşağıdaki komutu kullanarak gerekli kütüphaneleri yükleyin:
   ```
   pip install requests
   ```

4. **Uygulamayı Çalıştırın**:
   Ana uygulamayı başlatmak için aşağıdaki komutu kullanın:
   ```
   python main.py
   ```

## Kullanım

1. Uygulama başladığında bir Tkinter penceresi açılacaktır.
2. Şehir adı girin ve **"Hava Durumunu Getir"** butonuna tıklayın.
3. Şehir hakkındaki hava durumu bilgileri pencerenin altında görünecektir.

## Lisans

MIT Lisansı altında dağıtılmaktadır.
