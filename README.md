# macro_keyboard
  Bu projemde Raspberry Pi Pico kullanarak altı tuşlu programlanabilir makro klavye yaptım. Gerekli tüm dosyalar repo nun içerisinde mevcuttur. Öncelikle Raspberry Pi Pico nuzu bilgisayarınıza bağladığınızda içine repo da bulunan "Gerekli Dosyalar" kısmındaki "adafruit-circuitpython-raspberry_pi_pico-tr-7.3.3.uf2" dosyayı atmanız gerekmektedir. Bu işlemi yaptıktan sonra raspberry kendisini kapatıp tekrar açacaktır ve bağlantıyı kopartmamanız gerekmektedir. Bu işlemden sonra ismi "CIRCUITPY" olacaktır. Açılan ekrandaki "lib" klasörüne repo da bulunan "Gerekli Dosyalar" kısmındaki "adafruit_hid" klasörünü yapıştırıyoruz. Böylece kod için gerekli tüm kütüphanelerimiz hazır olacaktır. Daha sonra bir üst klasöre geçiyoruz ve oraya repo da bulunan "code.py" isimli python dosyanımızı atıyoruz. Ben kodlama yaparken Thonny adlı IDE yi kullandım sizde tercih edebilirsiniz. şağıya Thonny IDE sini indirebileceğiniz linkide bıraktım. code.py dosyası içinde herhangi bir değişiklik yapmak isterseniz bu dosyayı birlikte aç seçeneğine basarak Thonny yi seçin ardından kod Thonny de açılacaktır. Burda kodunuzu çalıştırmak istediğinizde 
Devre şeması aşağıdaki gibidir.






<img width="607" alt="Ekran Resmi 2023-03-19 15 17 30" src="https://user-images.githubusercontent.com/115935357/226174585-50af9c48-73fe-4787-9998-265f9eb250dd.png">
