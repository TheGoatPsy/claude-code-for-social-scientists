---
title_en: "When Things Go Wrong, A Working Troubleshooting Protocol"
title_tr: "İşler Ters Gittiğinde, Çalışan Bir Sorun Giderme Protokolü"
booklet_id: "012-01-0001"
category: "012-troubleshooting"
language: "tr"
version: "0.1.0"
date_published: "2026-05-24"
date_last_revised: "2026-06-04"
authors:
  - name: "Onour Impram"
    orcid: "0000-0003-1076-3928"
    role: "author, principal reviewer"
ai_assisted: true
ai_tools:
  - name: "Claude Code"
    vendor: "Anthropic"
    model_alias: "claude-opus-4-7"
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.7 as of 2026-05-24
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "co-drafting"
human_review: "complete"
human_review_date: "2026-06-04"
verified_citations_count: 7
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Türkçe kaynak metinden sıfırdan şampiyonluk yeniden yazımı, birebir çeviri değil. Tüm çalışılmış sorun giderme örnekleri gerçek bir olaydan türetilmemiş, kasa sanitizasyon protokolüne uygun sentetik örneklerdir."
closing_booklet: true
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# İşler Ters Gittiğinde, Çalışan Bir Sorun Giderme Protokolü

Önceki broşür, hakem yanıt mektubunu akademik üretimin en yüksek bahisli metin türü olarak ele almış ve son cümlesinde bir işaret bırakmıştı: o mektup yazılırken Claude Code akarken işler ters gidebilir. Bu broşür tam o ana geçer. Bir komut beklenmedik bir sonuç döndürdüğünde, bir model yanıtı bağlam sınırına takıldığında, bir atıf bir türlü doğrulanamadığında ya da bir ajan yetkisiz bir karar verdiğinde, sosyal bilim araştırmacısının ihtiyacı komut satırı hata kodlarından oluşan bir liste değildir. Hata mesajları eskir. Sürümler değişir. Araçların yüzeyi sürekli kayar. Eskimeyen şey başkadır: bir sorunu kök nedenine doğru daraltan düşünme biçimi. Bu kapanış broşürü o düşünme biçimini yedi adımlı bir protokol olarak sunar ve rehberin bütününü bağlar.

## 1. Sorun Gidermenin Üç Kategorisi: Araç, Bilgi, İletişim

Bir akademisyenin Claude Code ile çalışırken karşılaştığı sorunların büyük çoğunluğu üç kategoriye girer. Bir sorunu doğru kategoriye yerleştirmek çözümün yarısıdır. Çünkü araç sorunu için bakılacak yer, bilgi sorunu için bakılacak yerden farklıdır. İletişim sorununa sorulan soru her ikisinden de ayrıdır.

Birinci kategori araç sorunlarıdır: komut satırı bir hata kodu döndürür, model yanıt vermeden zaman aşımına uğrar, bağlam penceresi dolar. Sorunun kökü aracın kendisinde, çalıştığı ortamda ya da ağ bağlantısındadır. İkincisi bilgi sorunlarıdır: bir kütüphaneye erişilemez, bir atıf doğrulanamaz, bir DOI bulunamaz. Bu sorunlar verinin erişilebilirliğiyle ve doğruluğuyla ilgilidir. Uyarı mesajıyla kendini ilan etmedikleri için sessiz başarısızlıklardır. Üçüncüsü iletişim sorunlarıdır: verilen komut model tarafından yanlış anlaşılır, ajan bir döngüde sıkışır ya da beklenmedik bir karar verir. Bu başarısızlıklar ne araçta ne veride, araştırmacı ile araç arasındaki dilde yatar, niyet aktarımının çatladığı yerlerdir.

Reason (2000), insan hatasının modellenmesi üzerine yazdığı kısa ama etkili makalesinde, hataların bireysel yetersizlikten çok sistemin yapısal katmanlarından doğduğunu gösterir. Bu çerçeve klinik ve endüstriyel ortamlar için kurulmuştur. Bu rehberin çıkardığı çıkarım, aynı yapısal mantığın yapay zekâ destekli araştırma iş akışlarına da uzandığıdır: başarısızlıklar benzer biçimde katmanlar arasındaki sınırda belirir: araç ile çevresi arasında, bilgi tabanı ile erişim koşulları arasında, araştırmacının niyeti ile modelin yorumu arasında. Bu çıkarım bu rehberin kendi yorumudur, Reason'ın doğrudan kurduğu bir iddia değildir. Üç kategori, bu katmanları okumanın haritasıdır.

Ne var ki üç kategoriye temiz oturmayan bir dördüncü durum da vardır: belirsiz durum. Sorun ilk bakışta hangi katmandan geldiğini ele vermez. Model boş bir yanıt döndürür ama bunun nedeni bir ağ kesintisi mi, erişilemeyen bir kaynak mı, yoksa yanlış anlaşılmış bir komut mu, belli değildir. Belirsiz durumda doğru hamle kategori tahmin etmeye çalışmak değil, üç kategoriyi en ucuz testten en pahalıya doğru sırayla elemektir. Önce araç katmanı sınanır, çünkü bir hata mesajı en hızlı okunan kanıttır. Sonra bilgi katmanı: kaynak gerçekten erişilebilir mi? En son iletişim katmanı, çünkü komutu yeniden yazmak en fazla emek isteyen adımdır. Belirsizlik bir kategori değildir. Henüz daraltılmamış bir sorundur. Daraltma ise protokolün beşinci adımının işidir.

## 2. Araç Sorunları: CLI Hatası, Model Zaman Aşımı, Bağlam Limiti

Araç sorunları en görünür kategoridir, çünkü çoğunlukla açık bir hata mesajıyla gelir. Komut satırı bir hata kodu döndürür, ekrana bir uyarı düşer, bir işlem yarıda kesilir. Burada ilk refleks hata mesajını okumak olmalıdır. Yavaşça. Bir akademisyen, geliştirici olmadığı için hata metnini teknik gürültü olarak algılayıp gözünü kaçırabilir. Oysa hata mesajı çoğunlukla sorunun kategorisini ve yerini doğrudan söyler. Dosya adı, satır numarası, durum kodu: mesajın içindeki şeyi fark etmek çözümün başladığı yerdir.

En sık karşılaşılan üç araç sorunu şunlardır. Model zaman aşımı, modelin yanıt üretmeden önce ayrılan sürenin dolmasıdır. En yaygın nedeni fazla büyük bir girdi ya da geçici bir ağ yavaşlamasıdır. Girdiyi küçülterek, isteği bölerek ya da kısa bir süre bekleyip yeniden deneyerek çözülür. Bağlam limiti, modele verilen toplam metnin pencereyi aşmasıdır: uzun bir oturumda biriken konuşma bağlamı sessizce büyür ve bir noktada model en eski kısımları yitirmeye başlar. Çözüm, oturumu özetleyip yeniden başlatmak ya da bağlamı kasaya yazıp temiz bir oturumla devam etmektir. Bu, üçüncü broşürde anlatılan kasa olarak hafıza ilkesinin pratik karşılığıdır: bağlam pencereye değil diske bağlandığında, limit bir engel olmaktan çıkar, bir iş akışı kararına dönüşür. Üçüncü sorun ortam yapılandırmasıdır: yanlış bir dizinde çalışmak, eksik bir bağımlılık, hatalı bir yol tanımı. Norman (2013), *Gündelik Şeylerin Tasarımı* adlı eserinde, kullanıcı hatası diye etiketlediğimiz şeyin çoğunlukla bir tasarım hatası olduğunu gösterir: aracın yaptığı ve kullanıcının karşılayacağını bilmediği bir varsayım. Araç sorunuyla karşılaşan araştırmacı kendini suçlamak yerine şunu sormalıdır: aracın hangi varsayımı karşılanmadı? Bu soru, suçlamadan her zaman daha üretkendir.

Somut bir örnek kalıbı netleştirir. Bir araştırmacı yüz sayfalık bir tez bölümünü tek bir oturumda modele okutmaya çalışır ve model yarıda bağlam hatası döndürür. İlk refleks aracı suçlamak olabilir. Oysa hata mesajı sorunu açıkça söyler: girdi pencereyi aşmıştır. Çözüm farklı bir araç aramak değil, iş akışını değiştirmektir. Bölüm kasaya kaydedilir, alt başlıklarına bölünür, her alt başlık ayrı bir oturumda işlenir. Bağlam diske bağlandığında limit bir duvar olmaktan çıkıp yapıyı farklı kurmanın sinyaline dönüşür.

## 3. Bilgi Sorunları: Kütüphane Erişimi, Atıf, DOI Bulunamıyor

Bilgi sorunları araç sorunlarından daha sessizdir, çünkü hata mesajıyla gelmezler. Bir kütüphaneye erişim engellendiğinde abonelik kapısı sessizce devreye girer ve model boş bir sonuç döndürür. Bir DOI bulunamadığında atıf doğrulama akışı sonuç vermeden durur. Asıl tehlike tam da bu görünmezliktir: araç sorunu çığlık atar, bilgi sorunu fısıldar. Dolayısıyla bilgi sorunlarına karşı en güçlü savunma, yedinci broşürde anlatılan atıf doğrulama disiplinidir. Üç dizinli üçgenleme, bir kaynağın tek bir veri tabanında bulunamamasının onun var olmadığı anlamına gelmediğini kabul eder.

Bir DOI bulunamadığında üç olasılık sırayla işlenmeye değer. Birincisi: DOI gerçekten yoktur, çünkü kaynak bir kitaptır ya da DOI atanmamış eski bir makaledir. Bu durumda kaynak DOI olmadan, ISBN ya da kararlı bir URL ile künyelenir. İkincisi: DOI vardır ama bir yazım hatası olmuştur, bir basamak eksik ya da fazladır. Bu durumda DOI yeniden, kaynaktan kopyalanarak girilir. Üçüncüsü: veri tabanı geçici olarak erişilemezdir. Bu durumda alternatif bir dizin denenir: Crossref yanıt vermiyorsa OpenAlex, o da vermiyorsa yayıncının kendi sayfası.

Her durumda kritik kural aynıdır: bir kaynağı bulunamadığı için uydurmamak gerekir. Bir DOI doğrulanamıyorsa, bu başarısızlık dürüstçe belirtilir ve kaynak doğrulanana kadar bekletilir. Bilgi sorunu, boşluğu doldurma dürtüsü disiplinin önüne geçtiği anda bir bütünlük sorununa dönüşür. Somut bir örnek: bir araştırmacı bir makaleye atıf yapmak ister ama elindeki DOI Crossref'te çözülmez. Boş sonuç, makalenin var olmadığı anlamına gelmez. Önce DOI kaynaktan yeniden kopyalanır, çünkü hataların büyük bölümü bir basamağın eksik ya da fazla girilmesinden gelir. Çözülmezse makale başlığıyla alternatif bir dizinde, OpenAlex'te ya da yayıncının sayfasında aranır. Hâlâ bulunamazsa en olası açıklama, makalenin DOI atanmamış eski bir kaynak olmasıdır. Bu durumda kaynak kararlı bir URL ya da basılı künye ile atıflanır. Hiçbir aşamada eksik künye uydurulmaz. Bu örnekte çözüm farklı bir araç değil, bir disiplin gerektirir: doğrulanana kadar bekletme disiplini.

## 4. İletişim Sorunları: Komut Anlaşılmaz, Ajan Döngüde, Beklenmedik Karar

İletişim sorunları, üç kategorinin en incesidir. Ne araçta ne veride yatarlar. Araştırmacı ile araç arasındaki dilde, niyet aktarımının çatladığı yerde yatarlar. İlk tip, komutun yanlış anlaşılmasıdır: araştırmacı bir şey ister, model başka bir şey anlar ve teknik olarak kusursuz ama niyetten uzak bir sonuç üretir. Bunun nedeni neredeyse her zaman belirsizliktir. Bir akademisyen, güvendiği bir meslektaşına verdiği gibi örtük bir talimat verir ama modelin o örtük bağlamı paylaşmadığını unutur. Çözüm komutu açık kılmaktır: ne istendiğini, hangi biçimde istendiğini ve başarının nasıl ölçüleceğini söylemek. Bu özgüllük, yanlış anlamayı başlamadan keser.

İkinci tip, ajanın bir döngüde sıkışmasıdır. Model aynı adımı tekrar tekrar dener, her seferinde benzer bir başarısızlıkla, ve ilerleme durur. Bu, modelin altındaki bir varsayımın yanlış olduğunu fark edemediği durumlarda olur. Başarısızlığı görür ama neden başarısız olduğunu görebilecek kadar geri çekilemez. Schoenfeld (1985), matematiksel problem çözme üzerine yaptığı çalışmada, başarılı sorun çözücüleri başarısızlardan ayıran şeyin metabiliş olduğunu gösterir: kişinin kendi düşünme sürecini izleyip bir yolun çıkmaz olduğunu fark ederek geri dönmesi. Ajan döngüde sıkıştığında, modelin sağlayamayacağı bu metabilişsel müdahaleyi araştırmacı sağlamalıdır. Döngü durdurulur. Temel varsayım sorgulanır. Yanlış olabilecek varsayım adlandırılır.

Üçüncü tip, ajanın beklenmedik bir karar vermesidir: model söylenmemiş bir dosyayı değiştirir ya da varsayılan bir davranışa kayar. Bu, ikinci broşürde anlatılan ajanlık dönüşümünün öbür yüzüdür. Bir araç ne kadar çok özerklik taşırsa, o özerkliği istenilmedik yönlerde kullanma fırsatı da o kadar artar. Çözüm kapsamı sınırlamaktır: kritik aksiyonları açık onaya bağlamak ve her oturumu neyin devrede olduğu, neyin olmadığının açık bir tanımıyla başlatmak. İletişim sorunları, araştırmacı aracı bağlamı önceden paylaşan bir meslektaş gibi değil, niyetin tam ve açık biçimde aktarılması gereken yetenekli bir ortak gibi gördüğünde azalır.

Somut bir örnek döngü tipini gösterir. Bir araştırmacı modelden bir veri dosyasını yeniden biçimlendirmesini ister ama dosyanın gerçek yapısı modelin varsaydığından farklıdır. Model aynı dönüşümü tekrar tekrar dener, her seferinde aynı hatayla. Dönüşümün başarısız olduğunu görür ama temel varsayımının yanlış olduğunu göremez. Araştırmacının metabilişsel müdahalesi gerekir: döngü durdurulur ve soru değiştirilir. "Yeniden dene" değil, "bu dosya neden bu dönüşüme direniyor?" Çoğunlukla yanıt, dosyanın beklenenden farklı bir kodlamada ya da yapıda olmasıdır. Araştırmacı bu farkı açıkça bildirdiğinde döngü kırılır. Çözüm daha fazla deneme değildir. Varsayımı yeniden ifade etmektir.

## 5. Yedi Adımlı Muhakeme Çerçevesi

Üç kategori sorunu yerleştirmeye yarar. Onu çözmek için bir muhakeme çerçevesi gerekir. Aşağıdaki yedi adımlı protokol, Pólya'nın (1945/2014) klasik dört aşamalı çerçevesinin, yani anla, planla, uygula ve geriye bak aşamalarının, sosyal bilim yapay zekâ iş akışına bu rehber tarafından genişletilmiş halidir. Bu genişletme bu rehberin kendi yorumudur, Pólya'nın yapay zekâ araçları hakkında doğrudan kurduğu bir iddia değildir. Çerçeve üç kategorideki sorunların büyük çoğunluğu için işler, çünkü genel bir düşünme disiplinidir. Belirli bir komuta bağlı değildir.

| Adım | Ad | Soru | Pólya aşaması |
|---|---|---|---|
| 1 | Şüpheci ol | İlk açıklama doğru mu, yoksa en kolay açıklama mı | Anla |
| 2 | Kaydı al | Hata mesajı, log, ekran görüntüsü tam olarak ne diyor | Anla |
| 3 | Çoğalt | Sorun güvenilir biçimde yeniden üretilebiliyor mu | Anla |
| 4 | Daralt | Sorunu en küçük örneğe indirgeyebilir miyim | Planla |
| 5 | İzole et | Hangi tek değişken sorunu açıyor | Planla |
| 6 | Düzelt | En küçük doğru değişiklik nedir | Uygula |
| 7 | Belgele | Kök neden ve çözüm gelecekteki ben için nasıl kaydedilir | Geriye bak |

Birinci adım şüpheci olmaktır: ilk yüzeylenen açıklama çoğunlukla en kolay olandır, en doğru olan değil. Bir sorunu kabul edilen ilk hikayeyle kapatmak kök nedeni gölgede bırakır. İkinci adım kaydı almaktır. Hata mesajının, logun ya da beklenmedik sonucun tam metni bellekten değil kaynaktan alınır. Üçüncü adım çoğaltmaktır: bir sorun güvenilir biçimde yeniden üretilemiyorsa, çözüldüğü de doğrulanamaz. Bu üç adım Pólya'nın anlama aşamasına karşılık gelir.

Dördüncü adım daraltmaktır: sorun onu açan en küçük örneğe indirgenerek gereksiz değişkenler elenir. Beşinci adım izole etmektir: tek bir değişken değiştirilip etkisi gözlemlenerek nedensellik rastlantıdan ayrılır. Bu iki adım, herhangi bir şeye dokunmadan önce doğru kaldıracı bulmayı amaçlar. Planlama aşamasıdır.

Altıncı adım düzeltmektir. Buradaki kısıtlama önemlidir: çözüm en küçük doğru değişiklik olmalıdır. Tanımlanmış kök nedenin ötesinde daha geniş bir müdahale, gereksiz dokunduğu yerlerde yeni sorunlar üretir. Yedinci adım belgelemektir: kök neden ve çözüm kasaya kısa bir not olarak yazılır, böylece aynı sorun ikinci kez karşımıza çıktığında çözüme giden yol hazırdır. Dörner (1996), karmaşık durumlarda insan karar vermesini çözümlediği eserinde, başarısızlığın en tutarlı biçimde yan etkileri ve gecikmeli sonuçları göz ardı etmekten doğduğunu gösterir. Belgeleme, bu körlüğe karşı doğrudan bir savunmadır: hataları önlemez, ama onlardan nasıl toparlanılacağını bilen kalıcı bir bilgi yaratır.

Çerçeveyi tek bir örnekte yürütmek onu somutlaştırır. Bir araştırmacının atıf doğrulama akışı sessizce hatalı bir künye üretmektedir. Birinci adımda araştırmacı şüpheci olur, çünkü künye doğru görünse de akış son zamanlarda güncellenmiştir. İkinci adımda akışın girdisi ve çıktısı tam olarak kaydedilir. Üçüncü adımda sorun çoğaltılır: aynı kaynak yeniden işlenince aynı hatalı künye çıkar, demek ki sorun rastlantısal değildir. Dördüncü adımda sorun daraltılır, tek bir kaynakla denenir ve hata sürer. Beşinci adımda değişkenler izole edilir: yıl alanı boşaltılınca hata kaybolur, yani sorun yıl ayrıştırmasındadır. Altıncı adımda en küçük doğru değişiklik yapılır, yıl alanının ayrıştırma kuralı düzeltilir, akışın geri kalanına dokunulmaz. Yedinci adımda kök neden ve çözüm kasaya yazılır. Aynı ayrıştırma hatası bir daha karşımıza çıktığında çözüm hazırdır. Yedi adım, bir sezgiyi bir yönteme dönüştürür.

## 6. Türkiye ve Yunanistan Özgüllüğü

Bazı sorunlar bölgeseldir. Türkiye'de, özellikle büyük şehirler dışındaki illerde, internet bağlantısı zaman zaman kesintili olabilir ve bazı dış servislere erişim kısıtlanabilir. Yunanistan'ın kuzey şehirlerinde, Komotini ve çevresinde, fiber altyapısının değişkenliği benzer bir koşuldur. Bu durumlarda araç sorunu gibi görünen şey aslında bir ağ sorunudur. Aracın kendisinde aranan çözüm boşa çıkar.

Sorun ağ kaynaklı göründüğünde birkaç pratik adım denenebilir: alternatif bir DNS sunucusu, bağlantının kararlı olduğu bir saat dilimine işi kaydırmak ya da kurumsal bir ağ üzerinden çalışmak. Ayrıntılı ağ yapılandırması bu broşürün kapsamı dışındadır ve rehberin ilerleyen sürümlerine bırakılır. Buradaki kritik nokta, bölgesel bir altyapı koşulunu araç kusuruyla karıştırmamaktır. Çevre bir ilden ya da değişken bir hattan çalışan araştırmacı, ağ katmanını sorun giderme protokolünün ilk adımlarından birine dahil etmeli, sonradan akla gelen bir düşünce olarak bırakmamalıdır.

## 7. GitHub Issue Şablonu: Başkasına Yardımcı Olmak

Sorun giderme yalnızca kendi sorununu çözmek değildir. İyi belgelenmiş bir sorun, aynı başarısızlıkla karşılaşacak olan bir sonraki araştırmacıya da yardımcı olur. Açık kaynak topluluğunun kurucu jesti budur. Bir sorunu GitHub issue olarak bildirmek, onu paylaşılabilir bir bilgiye dönüştürür. İyi bir issue, yedi adımlı çerçevenin ikinci ve üçüncü adımlarının yazılı karşılığıdır: kaydı almanın ve çoğaltmanın.

Önerilen yapı aşağıdadır.

```
**Sorun başlığı.** kısa, tek satır
**Versiyon.** Claude Code sürümü ve işletim sistemi
**Beklenen.** ne olmasını umduğunuz
**Gerçekleşen.** ne oldu
**Çoğaltma adımları.**
1. ...
2. ...
**İlgili log ya da hata mesajı.**
```

```
hata logu buraya
```

```
**Daha önce denenenler.** hangi çözümler işe yaramadı
**Sorunun kategorisi.** araç, bilgi, iletişim ya da belirsiz
```

Bu şablonun gücü, onu dolduran kişiyi sorunu düşünmeye zorlamasında yatar. Beklenen ile gerçekleşen arasındaki farkı yazmak sorunun ne olduğunu netleştirir. Çoğaltma adımlarını sıralamak, sorunun gerçekten yeniden üretilebilir olup olmadığını sınar. Daha önce denenenleri belgelemek, yardım eden kişinin aynı çıkmaz yolları tekrar yürümesini önler.

Vaughan (1996), NASA'nın Challenger kararını incelediği çalışmasında, ve Perrow (1999), yüksek riskli teknolojilerde normal kazaları çözümlediği eserinde, her ikisi de şunu gösterir: sistemik başarısızlıklar tek bir yıkıcı hatadan değil, küçük ve görünüşte zararsız sapmaların birikmesinden doğar. Bu sapmalar birine görünürdü ama paylaşılmadı. İyi belgelenmiş bir issue, bu sapmaları topluluk genelinde görünür kılar ve ortak hafızaya ekler. Bir sorunu paylaşmak, onu yalnız taşımaktan hem daha hızlı hem daha onurludur.

## 8. Kapanış: Dizinin Son Satırı

Bu, on broşürlük v1.0 manifestosunun son broşürüdür. Bu bölüm dizinin kapanışıdır.

Rehber boyunca tek bir tez işlendi. Claude Code, sosyal bilimci için yalnızca bir komut satırı aracı değil, akademik üretimin metodolojik bir ortağıdır. Bu ortaklık ancak bir çerçeveyle, bir disiplinle ve bir etikle anlam kazanır. İlk broşür Claude Code'un epistemolojik düzeyde ne olduğunu tanımladı. Yöntemsel omurga broşürleri hafızayı, kasa mimarisini ve bölgesel akademik erişimi kurdu. Üretim çevrimi broşürleri yazımı, etiği ve hakem değerlendirmesini ele aldı. Bu son broşür, işler ters gittiğinde başvurulacak muhakeme çerçevesini verdi.

Sorun gidermenin bir hata listesi değil bir muhakeme çerçevesi olması, rehberin baştan sona savunduğu tezin son ve tutarlı uzantısıdır. Liste eskir. Çerçeve kalır. On broşürün hepsi okunduğunda, sosyal bilim araştırmacısının elinde, Claude Code ile akademik üretime başlamak için her şey olmasa bile, doğru yöne ilk adımı atmak için yeterli bir çerçeve vardır. Geri kalanı pratiğin kendi sınavı olacaktır.

## Kaynakça

Atıflar APA 7 biçimindedir. Reason (2000) DOI'si 2026-06-04 tarihinde Crossref üzerinden doğrulanmıştır. Tüm kitap ISBN'leri yayıncı kayıtlarına göre teyit edilmiştir.

Dörner, D. (1996). *The logic of failure: Why things go wrong and what we can do to make them right*. Metropolitan Books. ISBN 978-0-8050-4160-6

Norman, D. A. (2013). *The design of everyday things* (Revised and expanded ed.). Basic Books. ISBN 978-0-465-05065-9

Perrow, C. (1999). *Normal accidents: Living with high-risk technologies* (Updated ed.). Princeton University Press. ISBN 978-0-691-00412-9

Pólya, G. (2014). *How to solve it: A new aspect of mathematical method*. Princeton University Press. (Orijinal eser 1945 yılında yayımlanmıştır). ISBN 978-0-691-16407-6

Reason, J. (2000). Human error: Models and management. *BMJ*, 320(7237), 768–770. https://doi.org/10.1136/bmj.320.7237.768

Schoenfeld, A. H. (1985). *Mathematical problem solving*. Academic Press. ISBN 978-0-12-628870-4

Vaughan, D. (1996). *The Challenger launch decision: Risky technology, culture, and deviance at NASA*. University of Chicago Press. ISBN 978-0-226-85176-1

---

**Broşür kimliği.** `012-01-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-04
**Sözcük sayısı (yaklaşık).** 2270 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 7
**Halüsinasyon atıf sayısı.** 0
**Önceki broşür.** [`010-01-0001`](../../010-peer-review/010-01-0001/tr.md). İzlenebilirlik Matrisleri ile Hakem Yanıt Mektupları
**Sonraki broşür.** Yok. Bu, v1.0 manifestosunun kapanış broşürüdür. Yol haritası, kategori 005 (Hooks), 006 (MCP) ve 008 (Veri Analizi) ile v1.5 ve v2.0 sürümlerinde genişler.
