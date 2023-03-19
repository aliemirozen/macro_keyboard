# macro_keyboard
 
**Bu projemde Raspberry Pi Pico kullanarak altı tuşlu programlanabilir makro klavye yaptım. Gerekli tüm dosyalar repo nun içerisinde mevcuttur.**

İlk olarak Raspberry Pi Pico'yu üzerindeki "BOOTSEL" tuşuna basılı tutarak bilgisayara bağlayın. Bilgisayarınıza bağladığınızda tıpkı bir USB bellek gibi açılacaktır. Açılan pencerenin içerisine repo'da bulunan "Gerekli Dosyalar" kısmındaki "adafruit-circuitpython-raspberry_pi_pico-tr-7.3.3.uf2" dosyasını atmanız gerekmektedir. Bu işlemi yaptıktan sonra Raspberry kendisini kapatıp tekrar açacaktır ve bunun gerçekleşmesi için bağlantıyı kopartmamanız gerekmektedir. Bu işlemden sonra aygıtınızın ismi "CIRCUITPY" olacaktır. Açılan ekrandaki "lib" klasörüne repo'da bulunan "Gerekli Dosyalar" kısmındaki "adafruit_hid" klasörünü yapıştırın. Böylece kod için gerekli tüm kütüphaneler hazır olacaktır. 

Kod kısmı için bir üst klasöre geçin ve oraya repo da bulunan "code.py" isimli python dosyanımızı atın. Bu dosya içerinde 6 farklı değişik komut var ancak onları kullanmak yerine başka komutlar kullanmak istersenizde kodun altına yorum satırı olarak bir kaç örnek ekledim ordanda bakabilirsiniz. Ayrıca yazının altına bir link ekledim ve oradan tuşların keycode larını inceleyebilirsiniz. Ben kodlama yaparken Thonny adlı IDE’yi kullandım ve Thonny IDE üzerinden anlatım gerçekleştireceğim. Sizde aşağıdaki linkten Thonny IDE'sini indirebilirsiniz. code.py dosyası içinde herhangi bir değişiklik yapmak isterseniz bu dosyayı birlikte aç seçeneğine basarak Thonny’yi seçin ardından kod Thonny IDE'sinde açılacaktır. Burda kodunuzu Raspberry'ye atmak için üst bardaki “Çalıştır” butonuna basmanız gerekmektedir. Eğer kod attıktan sonra kod üzerinde herhangi bir değişiklik yaptıysanız bu kodu Raspberry'ye atmanız için öncelikle üst bardaki “Durdur” butonuna basıp ardından “Çalıştır” butonuna basmanız gerekmektedir. Böylelikle Raspberry içerindeki kod güncellenecektir.

Kodunuzu Raspberry ye attıktan sonra eğer çalışıp çalışmadığını denemek isterseniz bir jumper yardımıyla bunu kontrol edebilirsiniz. Jumper’ın bir ucu 3V3 diğer ucunuda denemek istediğiniz giriş pinine bir kere değdirdiğinizde komut çalışacaktır. Her şey sorunsuzsa lehimleme işlemine geçebilirsiniz.

Bu koddaki bulunan giriş pinleri aşağıda verilen fotoğraftaki şemaya göre tasarlanmıştır. Dolayısıyla siz farklı giriş pinleri kullandıysanız kod üzerinde bağladığınız pinlere göre değişiklik yapmalısınız. Ben 6 tuşlu küçük bir klavye olduğundan GP0, GP2, GP4, GP6, GP8 ve GP10 pinlerini tercih ettim. Sizde istediğiniz pinleri kullanabilirsiniz. 


<img width="607" alt="Ekran Resmi 2023-03-19 15 17 30" src="https://user-images.githubusercontent.com/115935357/226174585-50af9c48-73fe-4787-9998-265f9eb250dd.png">


> Source code for adafruit_hid.keycode: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html

> Thonny IDE’yi indirebileceğiniz link: https://thonny.org 
