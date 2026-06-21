---
title_en: "When Things Go Wrong, A Working Troubleshooting Protocol"
title_tr: "İşler Ters Gittiğinde, Çalışan Bir Sorun Giderme Protokolü"
booklet_id: "012-01-0001"
category: "012-troubleshooting"
language: "tr"
version: "0.2.0"
date_published: "2026-05-24"
date_last_revised: "2026-06-21"
authors:
  - name: "Onour Impram"
    orcid: "0000-0003-1076-3928"
    role: "author, principal reviewer"
ai_assisted: true
ai_tools:
  - name: "Claude Code"
    vendor: "Anthropic"
    model_alias: "claude-opus-4-8"
    model_dated: null
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "co-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 7
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Türkçe kaynak metinden sıfırdan yeniden yazıldı, birebir çeviri değil. Tüm çalışılmış sorun giderme örnekleri gerçek bir olaydan türetilmemiş, arşiv sanitizasyon protokolüne uygun sentetik örneklerdir."
closing_booklet: true
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# İşler Ters Gittiğinde, Çalışan Bir Sorun Giderme Protokolü

Önceki kitapçık, hakem yanıt mektubunu akademik üretimin en yüksek bahisli metin türlerinden biri olarak ele almıştı. Bu kapanış kitapçığı, o üretim zincirinin en kırılgan anına geçer. Bir komut beklenmedik bir sonuç döndürdüğünde, bir model yanıtı bağlam sınırına takıldığında, bir atıf bir türlü doğrulanamadığında, bir dosya yanlış sürümle açıldığında ya da bir ajan yetkisiz bir karar verdiğinde araştırmacının ihtiyacı yalnızca komut satırı hata kodları listesi değildir.

Hata mesajları eskir. Sürümler değişir. Araçların yüzeyi kayar. Kalıcı olan başka bir şeydir. Sorunu kök nedenine doğru daraltan düşünme biçimi. Bu kitapçık, Claude Code ile çalışan sosyal bilim araştırmacısı için bu düşünme biçimini yedi adımlı bir protokol olarak sunar. Amaç panik anında ezberlenen komutları çoğaltmak değil, işler ters gittiğinde araştırmacının hangi katmana bakacağını, hangi kanıtı kaydedeceğini, hangi değişkeni izole edeceğini ve çözümü nasıl arşivleyeceğini göstermektir.

Bu kitapçık aynı zamanda v1.0 dizisinin kapanışıdır. Rehberin ilk kitapçığı Claude Code'u sosyal bilimcinin akademik üretim sürecine yerleştirmişti. Son kitapçık ise bu üretim sürecinin kaçınılmaz gerçeğiyle ilgilenir. Her sistem aksar. Her araç bir noktada yanlış anlaşılır. Her arşiv bir gün direnç gösterir. Akademik olgunluk, hiçbir şeyin bozulmayacağına inanmakta değil, bozulduğunda yöntemle ilerleyebilmekte yatar.

## 1. Sorun Gidermenin Katmanları

Claude Code ile çalışan bir araştırmacının karşılaştığı sorunların büyük bölümü dört katmanda toplanabilir. İlk katman araç katmanıdır. Komut satırı hata verir, model zaman aşımına uğrar, bağlam penceresi dolar, terminal beklenen komutu tanımaz. Bu durumda sorun aracın kendisinde, çalıştığı ortamda ya da ağ bağlantısında aranır.

İkinci katman bilgi katmanıdır. Bir DOI doğrulanamaz, bir kütüphane kaydı bulunamaz, bir kaynak erişilemez, bir PDF tam metin vermeyebilir. Bu sorunlar çoğu zaman sessizdir. Hata mesajı üretmezler. Tam da bu yüzden tehlikelidirler. Çünkü boş sonuç, çoğu zaman kaynak yok anlamına gelmez. Erişim yok, indeks kapsamıyor, DOI yanlış girildi ya da kayıt farklı bir veri tabanında duruyor anlamına gelebilir.

Üçüncü katman iletişim katmanıdır. Araştırmacı bir niyet aktarır, model başka bir şey anlar. Komut belirsizdir, kapsam açık değildir, başarı ölçütü yazılmamıştır. Model teknik olarak düzgün, ama araştırmacının istediği şeyden uzak bir çıktı üretir. Bu tür sorunlarda araç bozuk değildir. Veri de bozuk değildir. Niyet aktarımı yetersizdir.

Dördüncü katman belirsiz durumdur. Sorunun hangi katmandan geldiği ilk bakışta görülmez. Model boş yanıt döndürür, ancak bunun nedeni ağ kesintisi mi, kaynak erişimi mi, yoksa kötü kurulmuş bir komut mu belli değildir. Belirsiz durumda doğru hamle tahmin etmek değil, katmanları sırayla elemektir. Önce araç katmanı, sonra bilgi katmanı, sonra iletişim katmanı sınanır. Çünkü hızlı çözülen katman önce dışarıda bırakılmalıdır.

Reason (2000), insan hatasını bireysel yetersizlikten çok sistemin katmanları içinde ele alır. Bu çerçeve doğrudan yapay zekâ destekli araştırma için geliştirilmemiştir. Bununla birlikte aynı yapısal düşünme biçimi burada değerlidir. Sorun çoğu zaman tek bir kişinin dikkatsizliğinde değil, aracın çevreyle, bilginin erişim koşullarıyla ya da araştırmacının niyetiyle kurduğu temas noktasında ortaya çıkar. Bu rehberin katman modeli, Reason'ın sistem yaklaşımını sosyal bilim araştırmacısının Claude Code iş akışına uyarlayan bir uygulayıcı çerçevesidir.

| Katman | Belirti | İlk soru | İlk müdahale |
|---|---|---|---|
| Araç | Hata mesajı, zaman aşımı, bağlam limiti, izin hatası | Araç hangi varsayımı karşılayamadı? | Hata metnini kaydet, girdiyi küçült, ortamı denetle |
| Bilgi | DOI bulunmaz, kaynak erişilemez, kayıt boş döner | Kaynak gerçekten yok mu, yoksa erişim mi yok? | Crossref, yayıncı sayfası, alternatif indeks ve kütüphane kaydıyla doğrula |
| İletişim | Model yanlış görevi yapar, döngüye girer, kapsamı aşar | Niyet yeterince açık iletildi mi? | Komutu yeniden yaz, başarı ölçütünü ekle, kapsamı daralt |
| Belirsiz | Neden görünmez, belirtiler karışık görünür | Hangi katman en hızlı elenebilir? | Araç, bilgi ve iletişim katmanlarını sırayla sınırla |

## 2. Araç Sorunları, Hata Mesajından Bağlam Limitine

Araç sorunları en görünür sorunlardır, çünkü çoğu zaman ekranda bir iz bırakırlar. Terminal hata kodu döndürür, model yanıt vermez, dosya sistemi erişimi reddeder, komut beklenenden farklı çalışır. Bu sorunlarda ilk refleks hata mesajını kapatmak değil, yavaşça okumaktır. Bir araştırmacı geliştirici olmak zorunda değildir. Ama hata mesajını akademik bir belge gibi okuması gerekir. Çünkü o metin çoğu zaman sorunun kategorisini, dosya yolunu, satırını ve nedenini açıkça gösterir.

Model zaman aşımı, genellikle girdinin çok büyük olmasından, ağın yavaşlamasından ya da model çağrısının beklenenden uzun sürmesinden doğar. Çözüm çoğu zaman görevi küçültmektir. Tek seferde yüz sayfa işlemek yerine bölümü alt başlıklara ayırmak, uzun bir konuşmayı özetleyip yeni oturuma geçmek ya da yalnızca ilgili dosyaları bağlama almak daha güvenli bir yoldur.

Bağlam limiti daha sinsi bir araç sorunudur. Uzun oturumlarda modelin bağlam penceresi dolar. Eski mesajlar düşer. Araştırmacı, modelin hâlâ önceki kararları hatırladığını sanabilir. Oysa bağlam çoktan taşmıştır. Bu noktada çözüm modeli zorlamak değil, bağlamı dosyaya taşımaktır. Oturum özeti yazılır, kararlar arşive kaydedilir ve temiz bir oturumla devam edilir. Bağlam pencereye değil diske bağlandığında limit bir duvar olmaktan çıkar, iş akışı kararına dönüşür.

Ortam yapılandırması da sık görülen bir araç sorunudur. Yanlış dizinde çalışmak, eksik bağımlılık, bozuk yol tanımı, PATH hatası ya da izin sorunu, akademisyenin gözünde aracın bozulduğu izlenimini yaratabilir. Norman'ın (2013) tasarım ilkesi burada yararlıdır. Kullanıcı hatası diye görünen şey, çoğu zaman sistemin kullanıcıya açıkça göstermediği bir varsayımdan doğar. Araştırmacının sorması gereken soru şudur. Araç benden hangi koşulun zaten sağlanmış olduğunu varsaydı?

Somut senaryo şudur. Bir araştırmacı yüz sayfalık bir tez bölümünü tek oturumda modele okutmaya çalışır ve model bağlam hatası döndürür. İlk tepki aracın yetersiz olduğu düşüncesi olabilir. Oysa hata mesajı sorunu açıkça söylemektedir. Girdi pencereyi aşmıştır. Doğru çözüm iş akışını değiştirmektir. Bölüm arşive kaydedilir, alt başlıklara ayrılır, her alt bölüm ayrı oturumda işlenir ve sonuçlar merkezi bir özet dosyasında birleştirilir. Sorun giderme, aracı zorlamaz. İş akışını aracın gerçek sınırlarına göre yeniden düzenler.

| Belirti | Olası kök neden | Uygun müdahale |
|---|---|---|
| Komut bulunamadı | PATH ya da kurulum yolu eksik | Sürüm komutunu çalıştır, PATH ayarını kontrol et, terminali yeniden başlat |
| Zaman aşımı | Girdi büyük, ağ yavaş, işlem çok uzun | Görevi parçala, girdi hacmini azalt, kısa bir deneme çalıştır |
| Bağlam limiti | Oturum çok büyüdü | Özet çıkar, kararları dosyaya yaz, yeni oturum başlat |
| İzin hatası | Dosya ya da klasör erişimi kapalı | Çalışma dizinini kontrol et, yalnızca gerekli izinleri ver |
| Yanlış çıktı dosyası | Yanlış dizinde çalışma ya da belirsiz çıktı yolu | Çıktı dosyasını açıkça belirt, hedef klasörü sabitle |

## 3. Bilgi Sorunları, Sessiz Başarısızlıklar

Bilgi sorunları araç sorunlarından daha tehlikelidir, çünkü çoğu zaman sessiz gelirler. Bir DOI çözülmez, ama terminal bunu dramatik bir hata gibi sunmaz. Bir kütüphane kaydı bulunmaz, ama model bunu kaynak yok diye yorumlayabilir. Bir abonelik kapısı tam metne izin vermez, ama çıktı yalnızca boş döner. Bu sessizlik, araştırmacıyı hızlı ve yanlış bir sonuca iter.

Atıf doğrulama bağlamında temel kural değişmez. Bir kaynak doğrulanmadığı için uydurulmaz. DOI çözülmezse önce DOI kaynaktan yeniden kopyalanır. Ardından Crossref, yayıncı sayfası, PubMed, OpenAlex ya da kütüphane kaydı denenir. Kaynak bir kitap, tez, rapor ya da DOI öncesi bir makale ise başka bir kalıcı tanımlayıcıyla, ISBN, kurumsal URL ya da kütüphane kaydıyla doğrulanır. Doğrulanamayan kaynak kaynakçaya girmez. Bekletilir.

Kütüphane erişimi de bilgi sorunudur. Bir makaleye erişilememesi, makalenin olmadığı anlamına gelmez. Kurumsal abonelik yoktur, proxy çalışmıyordur, EZproxy oturumu düşmüştür ya da yayıncı sayfası yönlendirme değiştirmiştir. Claude Code, bu durumda tam metnin yokluğunu içerik yokluğu sanmamalıdır. Araştırmacı, erişim ile varlık arasında ayrım yapmalıdır.

Bu ayrım özellikle bölgesel akademik kaynaklarda önemlidir. DergiPark, ULAKBİM TR Dizin, HEAL Link ve YÖK Tez Merkezi gibi kaynaklar uluslararası ticari veri tabanlarıyla aynı biçimde davranmaz. Kaynak bulunamadığında ilk açıklama kaynağın yokluğu olmamalıdır. Önce veri tabanı kapsamı, erişim yolu ve künye biçimi denetlenmelidir.

### Çalışılmış örnek, DOI çözülmüyor

Bir araştırmacının elinde DOI olduğu sanılan bir karakter dizisi vardır. Crossref yanıt vermez. Bu durumda yapılacak ilk iş, DOI'yi el ile düzeltmeye çalışmak değildir. Kaynak PDF'ten, yayıncı sayfasından ya da makalenin künyesinden DOI yeniden kopyalanır. Hâlâ çözülmüyorsa başlıkla arama yapılır. Başlık yayıncı sayfasında bulunur ama DOI yoksa kaynak DOI'siz olarak kayda alınır. Başlık hiçbir yerde bulunamazsa kaynak şüpheli kabul edilir ve referans listesine eklenmez. Bu sürecin her adımı kaynak pasaportuna yazılır. Böylece karar hatırlamaya değil, kayda dayanır.

## 4. İletişim Sorunları, Niyet Aktarımının Çatladığı Yer

İletişim sorunları, araç da veri de çalışıyor görünürken ortaya çıkar. Araştırmacı bir şey istemiştir, model başka bir şey yapmıştır. Çıktı teknik olarak düzgün olabilir. Hatta akıcı ve ikna edici görünebilir. Ama hedefe hizmet etmez. Bu tür sorunlarda sorun çoğu zaman modelin kapasitesinde değil, komutun belirsizliğindedir.

Akademik bir meslektaşa verilen örtük talimatla modele verilen talimat aynı değildir. Meslektaş alan bağlamını, geçmiş konuşmaları, kurumun beklentilerini ve araştırmacının üslubunu kendiliğinden tamamlayabilir. Model bunu ancak yazıldıysa görür. Bu nedenle iyi komut, yalnızca ne yapılacağını değil, ne yapılmayacağını da belirtir. Hangi dosyalara dokunulacak, hangi dosyalar dışarıda kalacak, çıktı hangi biçimde verilecek, başarı nasıl ölçülecek. Bunlar yazılmadan verilen komut, iyi niyetli ama riskli bir kısa yoldur.

Ajan döngüsü iletişim sorunlarının en tipik biçimlerinden biridir. Model aynı adımı tekrar tekrar dener, her seferinde benzer bir hatayla karşılaşır. Yeniden denemek sorunu çözmez, çünkü sorun denenen adımda değil, o adımı mümkün sanan varsayımdadır. Schoenfeld'in (1985) matematiksel problem çözme üzerine çalışmasında vurguladığı üstbiliş burada devreye girer. Araştırmacı süreci dışarıdan görmeli ve şu soruyu sormalıdır. Model hangi varsayımı doğru sanıyor?

Beklenmedik ajan kararı ise ayrı bir risk taşır. Model ilgisiz bir dosyaya dokunur, çıktı yolunu değiştirir, kapsam dışı bir belgeyi düzenler ya da onaylanmamış bir varsayımla devam eder. Bu durumda sorun, ajanın eylem alanının fazla geniş bırakılmış olmasıdır. Çözüm kapsamı daraltmak, kritik dosyaları korumak, her değişikliği diff ile görmek ve yüksek riskli işlemleri açık onaya bağlamaktır.

Somut örnek şudur. Bir araştırmacı modele bir veri dosyasını yeniden biçimlendirmesini söyler. Model aynı dönüşümü tekrar tekrar dener ve hata alır. Sorun, modelin dosyanın virgülle ayrılmış olduğunu varsaymasıdır. Oysa dosya noktalı virgülle ayrılmıştır. Yeniden dene komutu hiçbir şeyi çözmez. Doğru soru şudur. Bu dosya neden bu dönüşüme direniyor? Varsayım görünür olduğunda döngü kırılır.

| Sorun tipi | Tipik belirti | Düzeltici hamle |
|---|---|---|
| Belirsiz komut | Çıktı düzgün ama istenenden farklıdır | Amaç, kapsam, biçim ve başarı ölçütünü yeniden yaz |
| Ajan döngüsü | Model aynı adımı tekrar eder | Döngüyü durdur, varsayımı adlandır, görevi yeniden çerçevele |
| Kapsam kayması | İlgisiz dosyalar ya da ek işler devreye girer | Çalışma dizinini, dokunulacak dosyaları ve yasak alanları açıkça belirt |
| Gizli varsayım | Model söylenmeyen bir şeyi doğru kabul eder | Ara kararları görünür kıl, varsayımları ayrı listelet |

## 5. Yedi Adımlı Muhakeme Çerçevesi

Üç katman sorunu yerleştirmeye yarar. Çözmek için ise bir muhakeme çerçevesi gerekir. Aşağıdaki yedi adımlı protokol, Pólya'nın klasik anla, planla, uygula ve geriye bak aşamalarının sosyal bilim yapay zekâ iş akışına uyarlanmış hâlidir (Pólya, 1945/2014). Bu uyarlama bu rehberin kendi uygulayıcı yorumudur. Belirli bir komuta bağlı değildir. Bu nedenle araç sürümü değişse de düşünme sırası değişmez.

Birinci adım şüpheci olmaktır. İlk açıklama çoğu zaman en kolay hikâyedir, en doğru olan değil. İkinci adım kaydı almaktır. Hata mesajı ya da beklenmedik çıktı hafızadan değil, kaynaktan alınır. Üçüncü adım çoğaltmaktır. Tekrarlanamayan bir sorunun çözüldüğü de güvenilir biçimde söylenemez.

Dördüncü adım daraltmaktır. Sorun en küçük örneğe indirilir. Beşinci adım izole etmektir. Tek bir değişken değiştirilir ve sonucu gözlenir. Altıncı adım düzeltmektir. Düzeltme, kök nedeni aşan geniş bir müdahale olmamalıdır. Yedinci adım belgelemedir. Dörner'in (1996) karmaşık sistemlerde hata üzerine çalışması, başarısızlıkların çoğu zaman yan etkileri ve gecikmeli sonuçları görmemekten doğduğunu gösterir. Belgeleme, aynı sorunun ikinci kez yabancı görünmesini engeller.

Bu yedi adımın değeri, panik anında araştırmacıya bir sıra vermesidir. Sorun giderme, bu sırayla duygusal bir tepki olmaktan çıkar. Kayda dayalı bir muhakeme sürecine dönüşür.

| Adım | Ad | Soru | Pólya aşaması |
|---|---|---|---|
| 1 | Şüpheci ol | İlk açıklama doğru mu, yoksa en kolay açıklama mı? | Anla |
| 2 | Kaydı al | Hata mesajı, log, ekran görüntüsü ya da çıktı tam olarak ne diyor? | Anla |
| 3 | Çoğalt | Sorun güvenilir biçimde yeniden üretilebiliyor mu? | Anla |
| 4 | Daralt | Sorunu açan en küçük örnek nedir? | Planla |
| 5 | İzole et | Hangi tek değişken sorunu açıyor ya da kapatıyor? | Planla |
| 6 | Düzelt | En küçük doğru değişiklik nedir? | Uygula |
| 7 | Belgele | Kök neden ve çözüm gelecekteki araştırmacı için nasıl kaydedilecek? | Geriye bak |

## 6. Kurtarma Kaydı ve Olay Günlüğü

Sorun giderme yalnızca sorunu çözmek değildir. Çözümün arşive girmesidir. Çünkü aynı hata çoğu zaman tek kez yaşanmaz. Bağlam limiti tekrar eder, DOI hatası tekrar eder, kütüphane erişimi tekrar eder, yanlış dizinde çalışma tekrar eder. Her seferinde sıfırdan düşünmek yerine, ilk çözümden bir kayıt üretmek gerekir.

Bu kayıt uzun olmak zorunda değildir. Hatta uzun olursa kullanılmaz. İyi bir olay günlüğü kısa, tarihli ve yeniden uygulanabilir olmalıdır. Sorunun ne olduğu, hangi katmana ait olduğu, nasıl çoğaltıldığı, kök nedenin ne olduğu, hangi çözümün çalıştığı ve hangi önleyici adımın eklendiği yazılır.

Bu olay günlüğü, arşivin sorun giderme hafızasıdır. Bir araç hatası çözüldüğünde yalnızca bugünkü oturum kurtulmaz. Gelecekteki araştırmacı da korunur. Çoğu zaman o gelecekteki araştırmacı, altı ay sonra aynı arşive geri dönen sizsinizdir.

## 7. Bölgesel Altyapı Sorunları

Bazı sorunlar aracın kendisinden değil, araştırmacının çalıştığı coğrafi ve kurumsal altyapıdan doğar. Türkiye'de bazı uluslararası servisler zaman zaman yavaşlayabilir, ödeme ve erişim kanalları kesintili olabilir, kurumsal kütüphane proxy'leri farklı üniversitelerde farklı biçimde çalışabilir. Yunanistan'da, özellikle Komotini ve çevresindeki kurumlarda, kampüs dışı erişim, HEAL Link, proxy yapılandırması ve bağlantı kalitesi araştırma deneyimini doğrudan etkileyebilir.

Bu durumlarda araç sorunu gibi görünen şey aslında ağ sorunudur. Model zaman aşımına uğrar, ama asıl neden bağlantıdır. Katalog boş döner, ama asıl neden kurum dışı erişimin düşmesidir. Tam metin indirilemez, ama sorun Claude Code değil, yayıncı erişim duvarıdır.

Bölgesel sorunlarda ilk yapılacak şey, aracı suçlamadan önce bağlantı ve erişim katmanını sınamaktır. Aynı işlem farklı bir ağdan çalışıyor mu? Kurumsal VPN açık mı? EZproxy oturumu düşmüş mü? Katalog tarayıcıdan açılıyor mu? Bu sorular cevaplanmadan model davranışı hakkında hüküm vermek erken olur.

## 8. GitHub Issue Şablonu, Başkasına Yardımcı Olmak

Sorun giderme yalnızca kendi sorununu çözmek değildir. İyi belgelenmiş bir sorun, aynı başarısızlıkla karşılaşacak başka bir araştırmacıya da yardımcı olur. Açık kaynak ekosisteminde iyi bir issue, bireysel bir aksaklığı ortak bilgiye dönüştürür. Sorunu yalnız taşımak yerine kayda geçirmek, hem daha hızlı hem daha akademik bir davranıştır.

Vaughan (1996), Challenger kararını incelerken sistemik başarısızlıkların çoğu zaman tek bir büyük hatadan değil, görünür ama paylaşılmayan küçük sapmaların birikiminden doğduğunu gösterir. Perrow (1999) yüksek riskli teknolojilerde benzer bir yapıyı tartışır. Claude Code ile çalışan bir sosyal bilimcinin arşivinde bu ölçekte bir risk yoktur. Ancak ilke yine geçerlidir. Küçük sapmalar görünür kılınmazsa, topluluk aynı hatayı tekrar tekrar yaşar.

Önerilen issue şablonu:

Sorun başlığı. Kısa, tek satır.

Versiyon. Claude Code sürümü, işletim sistemi, kurulum yolu.

Beklenen. Ne olmasını umuyordunuz?

Gerçekleşen. Ne oldu?

Çoğaltma adımları.

1. ...

2. ...

3. ...

İlgili log ya da hata mesajı.

Hata logu buraya.

Daha önce denenenler. Hangi çözümler işe yaramadı?

Sorunun kategorisi. Araç, bilgi, iletişim ya da belirsiz.

Gizlilik kontrolü. Loglarda kişisel veri, klinik veri ya da anahtar bulunmadığı doğrulandı.

Bu şablonun gücü, onu dolduran kişiyi düşünmeye zorlamasında yatar. Beklenen ile gerçekleşen arasındaki farkı yazmak sorunu netleştirir. Çoğaltma adımlarını sıralamak, sorunun gerçekten yeniden üretilebilir olup olmadığını sınar. Daha önce denenenleri yazmak, yardım edecek kişinin aynı çıkmaz yolları tekrar yürümesini önler. Gizlilik kontrolü ise klinik ve insan katılımcılı araştırma bağlamlarında vazgeçilmezdir. Hiçbir log, hiçbir ekran görüntüsü, hiçbir hata mesajı kişisel veri sızdırmamalıdır.

## 9. Çalışılmış Sorun Giderme Senaryoları

Bu bölümdeki örnekler gerçek olaylardan alınmamıştır. Arşiv sanitizasyon protokolüne uygun sentetik senaryolardır. Ama her biri sosyal bilim araştırmacısının Claude Code ile karşılaşabileceği gerçek sorun sınıflarını temsil eder.

### Senaryo 1. Hakem yanıtı dosyası yanlış sürümle açıldı

Belirti şudur. Yazar, revizyon dosyasını açar ve bazı değişikliklerin kaybolduğunu görür. İlk açıklama dosyanın bozulduğu olabilir. Yedi adımlı protokol daha sakin ilerler. Önce kayıt alınır. Dosya adı, tarih, klasör yolu, son değiştirilme zamanı ve varsa bulut senkronizasyon geçmişi kaydedilir. Sonra sorun çoğaltılır. Aynı dosya farklı cihazda da eski sürüm mü görünüyor? Ardından daraltılır. Sorun dosyada mı, bulut senkronizasyonunda mı, yoksa yanlış klasörde mi? Kök neden çoğu zaman aynı dosyanın iki klasörde iki farklı sürümle durmasıdır. Çözüm, tek ana dosyayı belirlemek, diğerini arşivlemek ve revizyon klasörüne sürüm adı sözleşmesi eklemektir.

### Senaryo 2. Atıf doğrulama akışı sessizce yanlış künye üretiyor

Belirti şudur. Kaynakça biçimsel olarak düzgün görünür, ama bir dergi adı beklenenden farklıdır. İlk açıklama, APA biçiminde küçük bir stil farkı olabilir. Protokol bunu kabul etmez. Girdi ve çıktı kaydedilir. Aynı kaynak yeniden işlenir ve aynı hata üretilirse sorun tekrarlanabilir. Tek bir kaynakla deneme yapılır. Dergi adı alanı izole edilir. Kök neden, API'den dönen container title alanının yanlış ya da eksik alınması olabilir. En küçük doğru düzeltme, künye eşleştirme adımına yayıncı sayfasıyla karşılaştırma kontrolü eklemektir.

### Senaryo 3. Model aynı dönüşümü tekrar tekrar deniyor

Belirti şudur. Bir veri dosyası temizlenecektir. Model komutu çalıştırır, hata alır, aynı dönüşümü yeniden dener. Döngü ilerlemez. Sorun modelin çabasında değildir. Varsayım yanlıştır. Dosya beklenen biçimde değildir. Araştırmacı döngüyü durdurur ve komutu değiştirir. Dönüştürmeyi deneme. Önce dosyanın yapısını tanı, ayırıcıyı, kodlamayı ve başlık satırını raporla. Bu hamle döngüyü kırar. Araştırmacı tekrar etmesini değil, bakmasını istemiştir.

### Senaryo 4. Konferans sunumu sahnede açılmıyor

Belirti şudur. Sunum dosyası projektör bilgisayarında bozulmuş görünür. Bu da sorun giderme protokolünün konusudur. Önce kayıt alınır. Dosya hangi formatta, hangi sürümde, hangi cihazda açılmadı? Sonra daraltılır. PDF sürümü açılıyor mu? Yerel kopya açılıyor mu? Bulut bağlantısı mı çalışmıyor? Çözüm çoğu zaman önceden hazırlanmış üçlü yedektir. PPTX, PDF ve tek sayfalık özet. Sunum canlı performanstır. Canlı performansta sorun giderme, teknik beceri kadar önceden kurulan yedek düzenidir.

## 10. Kapanış, Dizinin Son Satırı

Bu kitapçık, v1.0 manifestosunun kapanış kitapçığıdır. Rehber boyunca tek bir tez işlendi. Claude Code, sosyal bilimci için akademik üretimin yöntemsel ortağı olarak ancak bir çerçeve, bir disiplin ve bir etik içinde anlam kazanır. İlk kitapçık aracın ne olduğunu sordu. Son kitapçık, araç aksadığında ne yapılacağını soruyor.

Bu kapanış bilinçli bir tercihtir. Çünkü bir rehberin gerçek değeri, her şey yolundayken değil, bir şeyler ters gittiğinde anlaşılır. Kurulum çalışırken herkes kendini yetkin hisseder. Arşiv düzenliyken herkes düzenlidir. Kaynaklar doğrulanırken herkes titizdir. Asıl sınav, hata mesajı geldiğinde, kaynak bulunmadığında, model döngüye girdiğinde ve süre azaldığında başlar.

Sorun gidermenin bir hata listesi değil bir muhakeme çerçevesi olması, rehberin baştan sona savunduğu yaklaşımın son uzantısıdır. Liste eskir. Çerçeve kalır. Bu dizinin bütün kitapçıkları birlikte okunduğunda sosyal bilim araştırmacısının elinde her sorunu çözecek bir büyü değil, daha değerli bir şey bulunur. Araçla çalışırken neyi devredebileceğini, neyi devredemeyeceğini, neyi kaydetmesi gerektiğini ve sorun çıktığında nereden başlayacağını gösteren bir akademik çalışma disiplini.

Geri kalanı pratiğin sınavıdır.

## Kaynakça

Atıflar APA 7 biçimindedir. Tüm referanslar 2026-06-21 tarihinde Crossref üzerinden doğrulanmıştır. Tüm kitap ISBN'leri yayıncı kayıtlarına göre teyit edilmiştir.

Dörner, D. (1996). *The logic of failure: Why things go wrong and what we can do to make them right*. Metropolitan Books. ISBN 978-0-8050-4160-6

Norman, D. A. (2013). *The design of everyday things* (Revised and expanded ed.). Basic Books. ISBN 978-0-465-05065-9

Perrow, C. (1999). *Normal accidents: Living with high-risk technologies* (Updated ed.). Princeton University Press. ISBN 978-0-691-00412-9

Pólya, G. (2014). *How to solve it: A new aspect of mathematical method*. Princeton University Press. (Orijinal eser 1945 yılında yayımlanmıştır). ISBN 978-0-691-16407-6

Reason, J. (2000). Human error: Models and management. *BMJ*, *320*(7237), 768–770. https://doi.org/10.1136/bmj.320.7237.768

Schoenfeld, A. H. (1985). *Mathematical problem solving*. Academic Press. ISBN 978-0-12-628870-4

Vaughan, D. (1996). *The Challenger launch decision: Risky technology, culture, and deviance at NASA*. University of Chicago Press. ISBN 978-0-226-85176-1

---

**Kitapçık kimliği.** `012-01-0001`
**Sürüm.** `0.2.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 3021 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 7
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`010-01-0001`](../../010-peer-review/010-01-0001/tr.md). İzlenebilirlik Matrisleri ile Hakem Yanıt Mektupları
**Sonraki kitapçık.** Yok. Bu, v1.0 manifestosunun kapanış kitapçığıdır. Yol haritası, kategori 005 (Hooks), 006 (MCP) ve 008 (Veri Analizi) ile v1.5 ve v2.0 sürümlerinde genişler.
