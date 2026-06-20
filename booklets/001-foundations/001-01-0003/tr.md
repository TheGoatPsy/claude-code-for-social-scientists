---
title_en: "Installation, First Session, and Sanity Checks"
title_tr: "Kurulum, İlk Oturum, Sağlık Testleri"
booklet_id: "001-01-0003"
category: "001-foundations"
language: "tr"
version: "0.1.0"
date_published: "2026-05-24"
date_last_revised: "2026-06-20"
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
human_review_date: "2026-06-20"
verified_citations_count: 6
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Kurulum, İlk Oturum, Sağlık Testleri

Bu kitapçık önceki ikisinden farklı bir karakter taşır. İlk iki kitapçık kavramsal zemini kuruyordu: aracın ne olduğunu, hangi arayüz üzerinden çalıştığını ve ajan mantığının sosyal bilim için ne anlam ifade ettiğini ortaya koyuyordu. Bu kitapçık ise operasyoneldir. Claude Code'un kurulumunu ve ilk oturumunu, sosyal bilim akademisyeninin gerçekten kontrol edebileceği bir sağlık testi protokolüyle birlikte anlatır. Temel iddia şudur: kurulum, sosyal bilim akademisyeni için yöntemsel bir filtredir. İlk oturumda neyin doğru yapılandırıldığı, sonraki on iki haftanın geri dönüş maliyetini belirler. İyi yapılandırılmış bir kurulum araştırmacının onlarca saatini kazandırır. Dikkatsiz bir kurulum ise hiçbir şey öğretmez ve aracı boşta bırakır.

Baştan bir notu açık kılmak gerekir. Komut satırı araçları sık güncellenir. Bu kitapçık kavramsal kontrolü kurmayı hedefler. Belirli komutların ezberlenmesi bu hedefin dışındadır. Kesin komut sözdizimi için her zaman güncel resmi belge esas alınmalıdır (Anthropic, 2026a). Bu bilinçli bir tercihtir. Araştırmacı için kalıcı değer, bir kurulumun neden ve nasıl çalıştığını kavramaktadır. Literatür taramasında kaynak doğrulamasını yöneten disiplinin ta kendisidir bu.

## 1. Sistem Gereksinimleri

Claude Code macOS, Linux ve Windows üzerinde çalışır. Her ortamda temel gereksinim ortaktır: güncel bir komut satırı ortamı ve bir paket yöneticisi. macOS ve Linux, Unix kabuğuyla birlikte geldiğinden bu sistemlerde kurulum görece doğrudan ilerler. Windows kullanıcıları için ek bir katman devreye girer. Windows'ta dosya sistemi ve terminale tam erişim en sorunsuz biçimde WSL2 üzerinden sağlanır. Bu Linux alt sistemi, Windows makinesinde eksiksiz bir Ubuntu ortamı açarak aracın beklediği Unix araçlarını hazır eder (Microsoft, 2026). Rehber Windows kullanıcıları için bu yolu öneriyor. Alternatif yapılandırmalar mümkündür, ancak ilk oturumda boşuna üstlenilecek bir karmaşıklık yükü taşırlar.

Sosyal bilim akademisyeni için pratik kontrol listesi kısadır: güncel bir işletim sistemi sürümü, birkaç gigabayt boş disk alanı (oturum belleği ve arşiv dosyaları zamanla büyür) ve kararlı bir internet bağlantısı. Donanım açısından rahatlatıcı olan şudur: araç yüksek yerel işlemci gücü ya da grafik kartı gerektirmez. Hesaplama Anthropic'in altyapısında yapılır, yerel makine yalnızca bir istemcidir. Bu mimari yapıdan çıkan pratik sonuç şudur: Türkiye ve Yunanistan'daki birçok üniversite makinesinin, hatta birkaç yıllık dizüstü bilgisayarların, aracı sürtünmesiz çalıştırmaya yeterli olduğu söylenebilir. Yapılması gereken tek ön kontrol, terminalin açıldığını ve temel bir komuta yanıt verdiğini doğrulamaktır.

## 2. Hesap, Abonelik ve Faturalama

Kurulumdan önce bir hesap gerekir. Anthropic, farklı kullanım hacimlerine göre kalibre edilmiş birkaç plan katmanı sunar. Akademisyen için doğru katman, aracı ne yoğunlukla kullanacağına bağlıdır: hafta hafta sürekli literatür taraması yürüten bir doktora öğrencisinin ihtiyacı, ders tasarımı için aracı zaman zaman kullanan bir öğretim üyesinden farklıdır. Bu kitapçık belirli fiyat rakamları vermez, çünkü plan fiyatlandırması bu rehberin sürümleri arasında değişir. Bunun yerine bir ilke önerir: en düşük taahhütlü seçenekle başlayın, gerçek kullanım örüntünüzü bir tam ay boyunca gözlemleyin, ardından planı buna göre ayarlayın.

Akademik bütçe bağlamında şu çerçevelemeyi açık kılmak yerindedir. Araç maliyeti, soyut bir abonelik gideri olarak değil, aynı görevi yapacak bir araştırma asistanının saatlik ücreti ile karşılaştırılarak değerlendirilmelidir. İki haftalık manuel çalışmayı kurtaran iki yüz makalenin tek bir oturumda taranması, aylık bir ücreti fazlasıyla karşılar. Gerçek değer görev türüne ve kullanım hacmine göre değişeceğinden bu oran bir başlangıç çerçevesi olarak okunmalıdır. Kullanım çoğu zaman işlenen metin miktarına göre ölçüldüğünden maliyet öngörülebilir biçimde ölçeklenir: küçük keşif görevleri neredeyse maliyetsizdir, büyük taramalar ise orantılı ve tahmin edilebilir bir gidere bağlıdır. Faturalama yapılandırmasında aylık bir kullanım üst sınırı belirlemek pratik bir başlangıç adımıdır. Bu sınır, araştırmacının ilk haftalarda maliyet kaygısı olmadan özgürce denemesini sağlar.

## 3. CLI Kurulumu

Kurulumun yaygın yolları arasında bir dil paket yöneticisi (en sık başvurulan seçenek), macOS'ta Homebrew gibi bir sistem paket yöneticisi ve doğrudan indirme sayılabilir. Hangi yol seçilirse seçilsin varılan nokta aynıdır: terminalde çağrılabilir bir komut. Kurulumun ardından kritik adım, bu komutun sistemin arama yolunda (PATH) görünür olmasıdır. Terminal komutu tanımıyorsa sorun neredeyse her zaman PATH yapılandırmasındadır, başarısız bir kurulumda değil.

Bu kitapçık kesin kurulum komutunu burada sabitlemez, çünkü araç sürümü sık değişir ve sabitlenmiş bir komut hızla eskir. Güncel ve doğru kurulum komutu resmi belgede tutulur ve oradan alınmalıdır (Anthropic, 2026a). Önerilen başlangıç akışı ve iyi uygulama kalıpları da resmi belgenin ayrı bir bölümünde yer alır (Anthropic, 2026b). Bir teknik araç kurarken birincil belgeye gitmek, üçüncü taraf bir blogdan kopyalanan bir komutu denemekten çok daha güvenlidir. Literatür taramasında kaynak doğrulamasını yöneten disiplin kurulum adımında da geçerliliğini korur.

PATH sorununun pratik belirtisi nettir: komutu çağırdığınızda terminal "komut bulunamadı" yanıtı verir. Çözüm çoğu zaman iki adıma indirgenir: kurulum dizininin kabuk yapılandırma dosyasına eklenmesi ve terminalin yeniden başlatılması. macOS ve Linux kullanıcıları için bu kabuk profil dosyası anlamına gelir (`.zshrc`, `.bashrc` ya da eşdeğeri). Windows WSL2 kullanıcıları için aynı mantık Ubuntu ortamı içinde geçerlidir. İlk oturumda en sık karşılaşılan engel budur ve bir kez çözüldükten sonra bir daha karşıya çıkmaz. Kurulumun başarılı olduğunun en basit doğrulaması, komutun sürüm numarası sorulduğunda bir sürüm numarası döndürmesidir.

## 4. İlk Giriş ve İzin Onayı

Kurulumun ardından ilk oturum bir kimlik doğrulama ile başlar: araç hesabınıza bağlanır. Bu noktadan itibaren her etkileşimi yöneten kavram izin modelidir. Claude Code, dosya okumak, dosya yazmak ya da terminalde komut çalıştırmak gibi işlemleri gerçekleştirmeden önce açık izin talep eder. Güvenli kullanımın yapısal temeli bu mekanizmadır.

Bu izin katmanının neden var olduğunu bir an için anlamak aydınlatıcıdır. Dil modelleri, insan geri bildirimiyle yönergeleri takip edecek biçimde eğitilir. InstructGPT paradigması, modelin insanların hangi çıktıları tercih ettiğini öğrendiğini ve bu eğitimin sonraki yönergelere verdiği yanıtları şekillendirdiğini ortaya koymuştur (Ouyang ve diğerleri, 2022). Ama bir yönergeyi takip etmek, her yönergenin güvenli olduğu anlamına gelmez. Anthropic'in modelleri, zarar kaçınma ilkelerini bir öz-eleştiri döngüsü üzerinden doğrudan model davranışına kodlayan anayasal hizalama yaklaşımıyla eğitilir (Bai ve diğerleri, 2022). İzin modeli, bu hizalama katmanının kullanıcı tarafındaki tamamlayıcısıdır: model güvenli davranmaya eğitilmiştir, araştırmacı ise hangi eylemlere izin verdiğini açıkça denetler. Her iki taraf da tek başına yeterli değildir. İkisi birlikte tutunmalıdır.

Pratikte bu, her duyarlı eylemden önce bir onay isteminin ekrana gelmesi demektir. Araç ne yapmak istediğini bildirir, siz onaylar ya da reddedersiniz. Sosyal bilim akademisyeni için önerilen başlangıç stratejisi, ilk oturumda her eylemi ayrı ayrı onaylamaktır. İlk haftalarda bu "her seferinde sor" yaklaşımı, aracın her adımda gerçekte ne yaptığını öğrenmenin en güvenilir yoludur: hangi dosyalara dokunduğunu, komutların tam olarak ne döndürdüğünü, dizin geçişlerinin nerede ve neden gerçekleştiğini. Güven arttıkça ve tanıdık örüntüler tekrar ettikçe, düşük riskli belirli işlemler için kalıcı onay verilebilir. Klinik veri, mülakat dökümü ya da kişisel tanımlayıcı içeren dizinlere erişim ise hiçbir zaman otomatik onaya bağlanmamalıdır. Sorumlu kullanım çerçevesi bu tür sınırların açıkça çizilmesini ve korunmasını zorunlu kılar (Anthropic, 2024), ancak bu politika kurumsal düzeyde bir çerçeve sunar, operasyonel izin ayarlarının kendisini değil.

## 5. Sağlık Testi 1: Dosya Okutma

İlk sağlık testi en basit ama en bilgilendirici olanıdır. Araçtan bir metin dosyasını okumasını isteyin: arşivinizdeki gerçek içerik taşıyan herhangi bir dosya, örneğin bir okuma notu ya da literatür listesi. Sağlıklı bir yanıtın görünümü bellidir: araç dosyanın içeriğini okur, içeriğin bir özetini ya da yapısını size geri raporlar, hiçbir değişiklik yapmaz ve okuma öncesinde izin istediğini belli eder. Yalnızca o dosyadan gelebilecek somut ayrıntılar çıktıda yer alıyorsa, yerel dosya sistemine bağlantının gerçek olduğunun kanıtı budur. Bu tek test hem dosya sistemi erişimini hem izin modelinin etkinliğini hem de okuma ile yazma arasındaki ayrımın sağlam tutulduğunu doğrular.

Başarısızlık modları öğreticidir. Araç dosyayı bulamıyorsa çalışma dizini yanlış ayarlanmıştır: oturumu doğru klasörün içinden başlatın. İzin istemeden okuyorsa izin yapılandırması fazla gevşektir ve daha fazla çalışmadan önce sıkılaştırılmalıdır. Dosyayı okumak yerine akla yatkın görünen ama dosyayla örtüşmeyen içerik üretiyorsa bu ciddi bir uyarı işaretidir: araç, belgeyi gerçekten okumak yerine kendi istatistiksel örüntülerinden metin üretmiştir. Bu son başarısızlık modu, rehberin değerlendirmesine göre, akademik bağlamdaki en tehlikeli olanıdır. Çünkü üretilen içerik sözdizimsel açıdan gerçekten okunan içerikten ayırt edilemez ve yüzeysel bir incelemede fark edilmez. Bu ilk testin sağlıklı sonucu araştırmacıya aracın gerçekten yerel dosyalarla çalıştığı güvenini verir. Bu güven, sonraki tüm iş akışlarının temelidir.

## 6. Sağlık Testi 2: Dosya Düzenletme ve Diff Görüntüleme

İkinci test okumadan bir adım ileri gider. Araçtan bir dosyada küçük ve sınırlı bir değişiklik yapmasını isteyin: bir nota başlık eklemek, bir tarihi düzeltmek, bir cümle eklemek. Sağlıklı bir yanıt şu sırayla açılır: araç önce önerilen değişikliği bir fark (diff) görünümünde gösterir, tam olarak hangi satırların ekleneceğini ya da kaldırılacağını ortaya koyar, onayınızı ister ve ancak onayladıktan sonra dosyaya yazar. Bu sıralama seçime bırakılmış değildir. Denetim izinin ta kendisidir.

Diff görünümü akademik üretim için kritik bir araçtır. Değişiklik gerçekleşmeden önce neyin değişeceğini görürsünüz, sonrasında değil. Bir makale taslağı revizyonunda aracın tam olarak hangi cümleyi değiştirdiğini görebilirsiniz. Bir hakem yanıtında düzenlemenin yalnızca o yoruma karşılık verdiğini ve başka hiçbir şeye dokunmadığını doğrulayabilirsiniz. Diff görünümüyle çalışmak bu izlenebilirliği oturumun en başından kurar: sonradan değil, en baştan. Araç değişikliği diff göstermeden doğrudan yazıyorsa izin yapılandırması gözden geçirilmelidir: denetlenemeyen bir yazma, kaydın bütünlüğünün pazarlık konusu olmadığı akademik çalışmada meslek etiği açısından kabul edilemez. Bu test başarıyla tamamlandığında araç okuyuculuktan yazım ortaklığına terfi etmiştir: değişiklik yapabilen, ama yalnızca her adımda sizin açık denetiminiz altında.

## 7. Sağlık Testi 3: Çok Adımlı Görev

Üçüncü test Claude Code'u bir sohbet penceresinden ayıran ajan tabanlı niteliği sınar. Araca zincirleme bir görev verin: bir literatür dosyasını okusun, belirli bir kavramın geçtiği bölümleri çıkarsın ve bu çıkarımları kaynağa dokunmadan ayrı bir özet dosyasına aktarsın. Her adım bir öncekine bağlıdır ve her biri farklı bir dosyaya dokunur.

Sağlıklı bir çalışma şöyle görünür: araç her adımı sırayla yürütür, her adımda ne yaptığını raporlar ve son çıktıyı kaynağın üzerine yazmak yerine ayrı bir dosyaya yazar. Özet dosyası, kaynakta gerçekten bulunan materyali içerir. Çıkarımlar, yorumlar ya da modelin eğitim verisinden ürettiği içerik yoktur. Önceki kitapçıkta (001-01-0002) anlatılan eylem döngüsünün gerçek dosyalar üzerinde gerçek bir oturumda doğru çalıştığındaki görünümü budur.

Bu testte en yaygın başarısızlık modu, aracın bir ara adımı atlamasıdır ya da daha ciddisi, kaynak belge yerine kendi belleğinden içerik üretmesidir. Bu nedenle doğrulama adımı zorunludur: son çıktıyı kaynak dosyayla, pasaj pasaj karşılaştırın. Bu karşılaştırma, akademik disiplinin teknik akışa taşınmış halidir. Tıpkı bir alıntının bir makaleye girmeden önce orijinal kaynaktan doğrulanması gibi. Bu üçüncü test başarılıysa kurulum tamamlanmış, araç akademik üretim için hazır demektir.

## 8. Başarısızlık Modları

İlk oturumda karşılaşılan sorunların büyük bölümü, az sayıda tanınabilir örüntüye indirgenir. Her birinin net bir nedeni ve net bir çözümü vardır.

| Sembol | Açıklama | Çözüm |
|---|---|---|
| Komut bulunamadı | Terminal, kurulan komutu tanımıyor | PATH yapılandırmasını kontrol edin, kabuğu yeniden başlatın |
| Yetki hatası | İzin verilmemiş bir dosya ya da dizine erişim denendi | İzin onayını verin ya da çalışma dizinini düzeltin |
| Ağ hatası | Model çağrısı ağa ulaşamadı | Bağlantıyı kontrol edin, gerekirse yeniden deneyin |
| Model zaman aşımı | Yanıt beklenen sürede gelmedi | Görevi daha küçük adımlara bölün, bağlantı kalitesini kontrol edin |
| Bağlam limiti | Oturum modelin bağlam penceresini aştı | Oturumu özetleyip yeniden başlatın, kalıcı bilgiyi dosyaya yazın |

Bu modların hiçbiri kurulumun başarısız olduğu anlamına gelmez. Hepsi ilk oturumun normal öğrenme eğrisinin parçasıdır. Önemli olan her örüntüyü hızla tanımak ve paniğe kapılmadan uygun çözüme ulaşmaktır. Bağlam limiti moduna özel dikkat gerekir: arşiv alışkanlığını en doğrudan pekiştiren başarısızlık bu moddur. Oturum modelin bağlam penceresini aştığında, dosyaya yazılmamış her şey gider. Araştırmacı, kalıcı dosya temelli belgelemenin gerçek bir zorunluluk olduğunu tam da o an öğrenir. Bu modu erken karşılaşmak, herhangi bir araştırma akışı oturum sürekliliğine bağlanmadan önce dersi almak demektir.

## 9. Türkiye ve Yunanistan Özgüllüğü

Bölgesel gerçekler kurulum sürecinde iki noktada belirir.

Ödeme bu noktaların ilkidir. Türkiye'de belirli uluslararası ödeme altyapıları, doğrudan aboneliği engelleyebilecek kısıtlamalar getirir. Bu durumda alternatif yollar devreye girer: yerli bir fintek sağlayıcısının sunduğu sanal kart, yurt dışı banka kartı ya da bir üniversite veya araştırma merkezi üzerinden yapılandırılmış kurumsal hesap. Bu kitapçık yalnızca bu alternatiflerin haritasını çıkarır. Hangi seçeneğin işe yarayacağı kurumsal bağlama ve bireysel erişim koşullarına göre değişir. Yunanistan AB üyeliği nedeniyle standart ödeme akışını izler. Türkiye'ye özgü kısıtlamalar bu coğrafyada geçerli değildir.

Bağlantı kalitesi ikinci noktadır. Komotini gibi küçük şehirlerde fiber bağlantı her zaman güçlü olmayabilir. Kesintili bağlantı, model zaman aşımı modunun sıklığını artırır. Pratik çözüm her yerde aynıdır: görevleri daha küçük adımlara bölün ve büyük görevleri kararsız bir bağlantıya zorlamak yerine kararlı bağlantı pencerelerinde çalışın. Bu iki bölgesel ayrıntı teknik bir noktanın ötesine geçen yöntemsel bir anlam taşır: kurulum, her yerde aynı biçimde uygulanan evrensel bir prosedür değildir. Bir aracı özgül bir kurumsal, altyapısal ve coğrafi bağlama oturtma eylemidir.

## 10. Sonraki Kategori

Bu kitapçık kurulumun yöntemsel bir filtre olduğunu, sağlık testlerinin ise araştırmacıya aracın yerel dosyalarda gerçekten çalıştığına dair kanıta dayalı bir güven verdiğini ortaya koydu. Kurulum tamamlandıktan sonra akademisyenin önüne gelen ilk önemli soru şudur: Türkçe ve Yunanca akademik dergilere araç üzerinden nasıl güvenilir biçimde erişilir? Bir sonraki kategori akademik erişim altyapısına ayrılmıştır: DergiPark, ULAKBIM TR Dizin, HEAL-Link ve bunları çalışan bir araştırma oturumuna bağlayan EZproxy yapılandırmaları. Bu altyapı uluslararası rehberlerde yoktur ve bu rehberin en yüksek değerli katkılarından birini oluşturur. Kitapçık 002-04-0001 bu noktadan devam eder.

---

## Kaynakça

Atıflar APA 7 biçimindedir. İki arXiv ön baskısı (Bai ve diğerleri, 2022 ve Ouyang ve diğerleri, 2022) Crossref'te kayıtlı değildir. Her ikisi de 2026-05-24 tarihinde arXiv üzerinden doğrulanmıştır. Belge bağlantıları 2026-06-04 tarihinde canlı erişim ile doğrulanmıştır. Anthropic 2026a URL'si https://platform.claude.com/docs/en/claude-code adresine çözümlenmektedir, Microsoft 2026 URL'si ise https://learn.microsoft.com/en-us/windows/wsl/ adresine.

Anthropic. (2024). *Responsible scaling policy*. https://www.anthropic.com/news/anthropics-responsible-scaling-policy

Anthropic. (2026a). *Claude Code documentation*. https://docs.claude.com/en/docs/claude-code

Anthropic. (2026b). *Claude Code best practices*. https://code.claude.com/docs/en/best-practices

Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McKinnon, C., Chen, C., Olsson, C., Olah, C., Hernandez, D., Drain, D., Ganguli, D., Li, D., Tran-Johnson, E., Perez, E., ... Kaplan, J. (2022). *Constitutional AI: Harmlessness from AI feedback*. arXiv. https://arxiv.org/abs/2212.08073

Microsoft. (2026). *Windows Subsystem for Linux documentation*. https://learn.microsoft.com/windows/wsl/

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P., Leike, J., & Lowe, R. (2022). Training language models to follow instructions with human feedback. In *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)* (pp. 27730-27744). https://arxiv.org/abs/2203.02155

---

**Kitapçık kimliği.** `001-01-0003`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-20
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 2094 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 6
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`001-01-0002`](../001-01-0002/tr.md). Aracın Ötesine Geçiş: Sohbet Penceresinden İş Ortağına
**Sonraki kitapçık.** `002-04-0001`. DergiPark, ULAKBIM TR Dizin, HEAL-Link ve Bölgesel İndeksleme (Faz 2)
