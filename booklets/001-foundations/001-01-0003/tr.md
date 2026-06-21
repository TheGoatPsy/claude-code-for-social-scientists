---
title_en: "Installation, First Session, and Sanity Checks"
title_tr: "Kurulum, İlk Oturum ve Sağlamlık Denetimleri"
booklet_id: "001-01-0003"
category: "001-foundations"
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
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.7 as of 2026-05-24
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "co-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 6
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Kurulum, İlk Oturum ve Sağlamlık Denetimleri

Bu kitapçık, önceki iki kitapçıktan daha operasyonel bir işlev taşır. İlk kitapçık Claude Code'u sosyal bilimci açısından kavramsal bir çerçeveye yerleştirmişti. İkinci kitapçık sohbet penceresi ile ajan tabanlı çalışma aracı arasındaki farkı, süreklilik ve denetlenebilirlik açısından ele almıştı. Bu üçüncü kitapçık ise araştırmacının aracı ilk kez kurarken ve ilk oturumu başlatırken hangi teknik ve yöntemsel kontrolleri yapması gerektiğini açıklar.

Buradaki temel iddia şudur. Kurulum yalnızca bir yazılım yükleme işlemi değildir. Sosyal bilimci açısından kurulum, sonraki araştırma iş akışının güvenilirliğini belirleyen ilk yöntemsel filtredir. Dosya erişimi, izin modeli, çalışma dizini, komut satırı ortamı ve ilk sağlamlık denetimleri doğru kurulmadığında, araç güçlü görünse bile akademik üretim için güvenilir biçimde kullanılamaz.

Bu nedenle bu kitapçık belirli komutları ezberletmeyi amaçlamaz. Komut satırı araçları ve resmi belgeler zaman içinde değişebilir. Kalıcı olan şey, araştırmacının bir kurulumun doğru çalışıp çalışmadığını hangi ilkelerle denetleyeceğini bilmesidir. Akademik kaynak doğrulamasında geçerli olan disiplin, teknik kurulumda da geçerlidir. Bir aracın nasıl çalıştığını anlamadan onu araştırma sürecine dahil etmek, yöntemi görünmez bir riske açmak anlamına gelir.

Bu kitapçığın amacı, Claude Code'un ilk kurulumunu ve ilk oturumunu sosyal bilimcinin gerçekten kontrol edebileceği bir sağlamlık denetimi protokolüne bağlamaktır. Böylece araştırmacı, aracın yalnızca açılıp açılmadığını değil, doğru klasörde çalışıp çalışmadığını, dosya okuyup okumadığını, yazma işlemlerini izinle yapıp yapmadığını ve çok adımlı bir görevi denetlenebilir biçimde yürütüp yürütemediğini sınayabilir.

## 1. Sistem Gereksinimleri

Claude Code'un çalışabilmesi için güncel bir işletim sistemi, işleyen bir komut satırı ortamı ve uygun bir paket yöneticisi gerekir. macOS ve Linux kullanıcıları için süreç görece doğrudandır. Bu sistemler Unix tabanlı kabuk yapısı ve komut satırı araçlarıyla birlikte geldiği için Claude Code'un beklediği çalışma düzenine daha yakındır.

Windows kullanıcıları için ek bir katman gündeme gelir. Windows üzerinde dosya sistemi ve terminal erişimini daha tutarlı biçimde kullanabilmek için WSL2 önerilir. WSL2, Windows içinde Linux tabanlı bir çalışma ortamı sağlayarak komut satırı araçlarını daha kararlı hâle getirir (Microsoft, 2026). Bu öneri, başka yapılandırmaların imkânsız olduğu anlamına gelmez. Ancak ilk kez kurulum yapan sosyal bilimciler için gereksiz teknik karmaşıklığı azaltır.

Sosyal bilimci açısından pratik kontrol listesi kısa tutulmalıdır. Güncel bir işletim sistemi, kararlı bir internet bağlantısı, birkaç gigabayt boş disk alanı ve temel terminal komutlarını çalıştırabilen bir ortam çoğu başlangıç senaryosu için yeterlidir. Claude Code yüksek yerel işlemci gücü ya da grafik kartı gerektirmez. Model çalıştırma işlemi yerel makinede değil, Anthropic altyapısı üzerinden gerçekleşir. Yerel bilgisayar esas olarak istemci, dosya sistemi ve komut satırı arayüzü işlevi görür.

Bu durum Türkiye ve Yunanistan gibi farklı kurumsal altyapılara sahip akademik ortamlarda önemlidir. Birkaç yıllık dizüstü bilgisayarlar ya da standart üniversite makineleri çoğu zaman başlangıç için yeterli olabilir. Ancak terminalin çalışıp çalışmadığı, komutların tanınıp tanınmadığı ve internet bağlantısının kararlı olup olmadığı ilk oturumdan önce kontrol edilmelidir.

Bu bölümün temel mesajı şudur. Kurulum için en güçlü makineye değil, doğru yapılandırılmış bir çalışma ortamına ihtiyaç vardır.

## 2. Hesap, Abonelik ve Faturalama

Claude Code'u kullanmak için bir Anthropic hesabı ve kullanım biçimine uygun bir erişim planı gerekir. Belirli fiyatlar vermek burada doğru değildir. Fiyatlandırma ve plan yapıları zaman içinde değişebilir. Bu nedenle kalıcı öneri fiyat bilgisi değil, bütçe değerlendirme ilkesidir.

Akademisyen için doğru plan, aracın hangi yoğunlukta kullanılacağına bağlıdır. Haftalık literatür taraması, veri düzenleme ve hakem yanıtı hazırlama gibi işlerde aracı düzenli kullanacak bir doktora öğrencisinin ihtiyacı ile yalnızca dönem dönem ders materyali ya da taslak metin düzenleme için kullanacak bir öğretim üyesinin ihtiyacı aynı değildir.

Başlangıçta düşük taahhütlü ve kontrollü bir kullanım düzeyi tercih edilebilir. Araştırmacı, bir ay boyunca gerçek kullanım örüntüsünü gözlemleyebilir. Hangi görevlerde araca başvurduğunu, hangi görevlerde gerçekten zaman kazandığını, hangi işlemlerde çıktının insan denetimi gerektirdiğini ve maliyetin hangi tür işlerde arttığını kaydedebilir. Daha sonra plan seçimi bu gerçek kullanım verisine göre yapılmalıdır.

Akademik bütçe açısından araç maliyeti, soyut bir abonelik gideri olarak değil, belirli araştırma görevlerinin emek maliyetiyle birlikte düşünülmelidir. Örneğin yüzlerce makalelik bir kaynak havuzunun ön sınıflandırması manuel yapılırsa günler ya da haftalar alabilir. Ancak burada dikkatli olmak gerekir. Her otomasyon zaman kazancı üretmez. Her zaman kazancı da bilimsel kalite anlamına gelmez. Bu nedenle maliyet değerlendirmesi yalnızca hız üzerinden değil, çıktının doğrulanabilirliği ve denetlenebilirliği üzerinden yapılmalıdır.

Faturalama aşamasında aylık kullanım sınırı belirlemek yararlı bir başlangıç stratejisidir. Bu sınır, özellikle ilk haftalarda deneme yaparken maliyetin kontrol dışına çıkmasını engeller. Araştırmacı için en sağlıklı yaklaşım, aracı önce küçük görevlerde denemek, gerçek ihtiyaç ortaya çıktıkça kullanım hacmini artırmaktır.

## 3. CLI Kurulumu

Claude Code'un kurulumu, farklı sistemlerde farklı yollarla yapılabilir. Bir dil paket yöneticisi, macOS için Homebrew benzeri bir sistem paket yöneticisi ya da doğrudan indirme seçenekleri kullanılabilir. Hangi yol seçilirse seçilsin kurulumun sonunda beklenen sonuç aynıdır. Terminalde çağrılabilir bir Claude Code komutu bulunmalıdır.

Bu kitapçık kesin kurulum komutunu sabitlemez. Bunun nedeni, komut satırı araçlarının ve resmi kurulum yollarının zaman içinde değişebilmesidir. Güncel komut ve resmi yönergeler her zaman Anthropic'in kendi belgelerinden kontrol edilmelidir (Anthropic, 2026a, 2026b). Sosyal bilimci için burada önemli olan şey, komutu ezberlemek değil, kurulumun doğrulanabilir biçimde tamamlanıp tamamlanmadığını anlayabilmektir.

Kurulumdan sonra en kritik denetim noktası PATH yapılandırmasıdır. Terminal komutu tanımıyorsa, sorun çoğu zaman aracın kurulmamış olmasından değil, kurulum dizininin sistemin arama yoluna eklenmemiş olmasından kaynaklanır. Bu durumda terminal "komut bulunamadı" anlamına gelen bir yanıt üretir.

macOS ve Linux kullanıcılarında çözüm çoğu zaman kabuk yapılandırma dosyasına ilgili dizinin eklenmesidir. Bu dosya kullanılan kabuğa göre .zshrc, .bashrc ya da benzeri bir profil dosyası olabilir. Windows kullanıcılarında aynı mantık WSL2 içindeki Linux ortamında geçerlidir. Terminal yeniden başlatıldıktan sonra komutun sürüm numarası döndürmesi, kurulumun temel düzeyde başarılı olduğunu gösterir.

Bu aşamada araştırmacının yapması gereken şey basittir. Komutun sistem tarafından tanınıp tanınmadığını kontrol etmek. Komut tanınıyorsa ilk eşik aşılmıştır. Komut tanınmıyorsa, araştırma sürecine geçmeden önce PATH sorunu çözülmelidir.

## 4. İlk Giriş ve İzin Onayı

Kurulum tamamlandıktan sonra ilk oturum genellikle hesap doğrulama adımıyla başlar. Araç kullanıcının hesabına bağlanır ve bundan sonra yerel çalışma dizini içinde işlem yapmaya hazır hâle gelir. Bu noktadan itibaren en önemli kavram izin modelidir.

Claude Code dosya okumak, dosya yazmak ya da terminalde komut çalıştırmak gibi işlemler için kullanıcıdan açık onay isteyebilir. Bu izin katmanı, sosyal bilimci için yalnızca teknik bir güvenlik özelliği değildir. Aynı zamanda araştırma sürecinin denetlenebilirliği açısından yöntemsel bir araçtır. Hangi dosyaya erişildiği, hangi değişikliğin önerildiği, hangi komutun çalıştırıldığı ve hangi çıktının üretildiği araştırmacı tarafından görülmelidir.

Bu izin modelini dil modeli güvenliği bağlamında düşünmek yararlıdır. Ouyang ve diğerlerinin insan geri bildirimiyle yönerge izleme üzerine çalışması, modellerin kullanıcı niyetlerine daha uygun yanıtlar üretmek üzere eğitilebileceğini göstermiştir. Bai ve diğerlerinin anayasal yapay zekâ yaklaşımı ise zarar azaltma ilkelerini model davranışına daha doğrudan yerleştirmeyi hedefler. Ancak modelin güvenli davranmaya eğitilmiş olması, araştırmacının izin denetimini gereksiz kılmaz (Bai ve diğerleri, 2022; Ouyang ve diğerleri, 2022).

İzin modeli, kullanıcı tarafındaki ikinci güvenlik katmanıdır. Model belirli bir eylemi önerebilir. Ancak araştırmacı, bu eylemin bağlamını, riskini ve uygunluğunu değerlendirmek zorundadır. Özellikle klinik veri, mülakat dökümü, kişisel tanımlayıcı içeren saha notu ya da etik kurul kapsamındaki materyaller söz konusu olduğunda otomatik onay verilmemelidir.

İlk hafta için önerilen strateji açıktır. Her eylem ayrı ayrı onaylanmalıdır. Bu yaklaşım başlangıçta yavaş görünebilir. Fakat araştırmacı böylece aracın hangi dosyalara dokunduğunu, hangi komutları çalıştırdığını, hangi dizinlerde hareket ettiğini ve hangi çıktıları nereye yazdığını öğrenir. Güven ancak bu gözlemden sonra kurulmalıdır.

## 5. Sağlamlık Denetimi 1. Dosya Okutma

İlk sağlamlık denetimi, aracın yerel dosya sistemiyle gerçekten çalışıp çalışmadığını sınar. Araştırmacı, Claude Code'dan belirli bir metin dosyasını okumasını istemelidir. Bu dosya gerçek içerik taşıyan, ancak hassas veri içermeyen bir belge olmalıdır. Örneğin bir okuma notu, sahte bir literatür listesi ya da anonim bir deneme dosyası kullanılabilir.

Sağlıklı bir yanıtın özellikleri nettir. Araç dosyayı okumadan önce gerekli izni ister. Dosyanın içeriğini okur. İçeriğin yapısını ya da kısa özetini raporlar. Dosyada herhangi bir değişiklik yapmaz. Çıktıda yalnızca o dosyadan gelebilecek somut ayrıntılar bulunur.

Bu test üç şeyi aynı anda sınar. Dosya sistemi erişimi çalışıyor mu? İzin modeli etkin mi? Araç okuma ile yazma arasındaki farkı koruyor mu?

Başarısızlık modları da öğreticidir. Araç dosyayı bulamıyorsa, oturum yanlış çalışma dizininden başlatılmış olabilir. İzin istemeden dosyayı okuyorsa, izin yapılandırması fazla gevşek olabilir. Dosyayı gerçekten okumadan, akla yatkın ama belgeyle örtüşmeyen bir özet üretiyorsa, bu ciddi bir uyarı işaretidir. Böyle bir durumda araç belgeye dayalı işlem yapmak yerine istatistiksel olarak olası bir metin üretmiş olur.

Akademik bağlamda en riskli hata türü budur. Çünkü çıktı biçimsel olarak makul görünür. Ancak kaynağa dayanmaz. Bu nedenle ilk dosya okutma testi, Claude Code'un araştırma arşiviyle gerçekten ilişki kurduğunu doğrulamak için vazgeçilmezdir.

## 6. Sağlamlık Denetimi 2. Dosya Düzenleme ve Diff Görüntüleme

İkinci denetim, okuma işleminden yazma işlemine geçer. Araştırmacı, araçtan küçük ve sınırlı bir değişiklik yapmasını istemelidir. Örneğin bir deneme dosyasına başlık eklemek, bir tarihi düzeltmek ya da tek bir cümleyi yeniden düzenlemek gibi düşük riskli bir görev seçilebilir.

Sağlıklı iş akışı şu sırayı izlemelidir. Araç önce önerilen değişikliği açıkça göstermelidir. Mümkünse değişikliği diff görünümünde sunmalıdır. Hangi satırın ekleneceği, hangi satırın çıkarılacağı ya da hangi ifadenin değişeceği görünür olmalıdır. Araç ancak araştırmacı onay verdikten sonra dosyaya yazmalıdır.

Diff görünümü, akademik üretimde kritik bir denetim aracıdır. Çünkü değişikliğin gerçekleşmesinden önce neyin değişeceğini görmeyi sağlar. Bir makale taslağında hangi cümlenin düzenlendiği, bir hakem yanıtında hangi ifadenin eklendiği ya da bir yöntem bölümünde hangi kavramın değiştirildiği izlenebilir hâle gelir.

Araç diff göstermeden doğrudan yazıyorsa, araştırmacı bu davranışı gözden geçirmelidir. Denetlenemeyen yazma işlemi, akademik çalışma için kabul edilebilir bir pratik değildir. Özellikle makale taslakları, veri sözlükleri, etik kurul metinleri ve hakem yanıtları gibi belgelerde her değişikliğin izlenebilir olması gerekir.

Bu test başarıyla tamamlandığında araç yalnızca okuyabilen değil, sınırlı ve denetimli biçimde yazma işlemine de katılabilen bir çalışma yardımcısı hâline gelir. Ancak burada önemli nokta şudur. Yazma yetkisi, araştırmacının denetiminden bağımsız olmamalıdır.

## 7. Sağlamlık Denetimi 3. Çok Adımlı Görev

Üçüncü denetim, Claude Code'un ajan tabanlı niteliğini sınar. Araştırmacı, araca birden fazla adımdan oluşan küçük bir görev vermelidir. Örneğin bir literatür notunu okuması, belirli bir kavramın geçtiği yerleri çıkarması ve bu çıkarımları kaynak dosyaya dokunmadan ayrı bir özet dosyasına aktarması istenebilir.

Bu testte sağlıklı çalışma birkaç ölçütle anlaşılır. Araç her adımı sırayla yürütür. Hangi dosyayı okuduğunu, hangi ölçüte göre seçim yaptığını ve çıktıyı hangi dosyaya yazacağını açıkça belirtir. Kaynak dosyanın üzerine yazmaz. Yeni özet dosyası, kaynakta gerçekten bulunan materyale dayanır. Modelin eğitim verisinden gelen ek yorumlar, varsayımlar ya da uydurulmuş çıkarımlar içermez.

Bu denetim, önceki kitapçıkta ele alınan ajanlı çalışma mantığının küçük ölçekli bir sınamasıdır. Araç tek bir yanıt üretmekle kalmaz. Bir görevi alt adımlara böler, ara işlemler yapar ve çıktıyı dosya sistemine kaydeder. Ancak bu kapasite, doğrulama gerekliliğini ortadan kaldırmaz.

Araştırmacı, son çıktıyı kaynak dosyayla karşılaştırmalıdır. Çıkarılan pasajlar gerçekten kaynakta var mı? Kavram bağlamından koparılmış mı? Araç yorum ile alıntıyı karıştırmış mı? Özet dosyası kaynak metnin sınırları içinde kalmış mı?

Bu karşılaştırma, akademik kaynak denetiminin teknik iş akışına taşınmış biçimidir. Bir alıntı makaleye girmeden önce nasıl orijinal kaynaktan doğrulanıyorsa, Claude Code'un ürettiği ara çıktı da kaynak dosyayla karşılaştırılmalıdır.

Üçüncü test başarıyla tamamlandığında araştırmacı şunu söyleyebilir. Araç yalnızca açılmıyor. Aynı zamanda dosya okuyor, izinle yazıyor, çok adımlı görev yürütebiliyor ve çıktısı kaynakla karşılaştırılarak denetlenebiliyor.

## 8. Başarısızlık Modları

İlk oturumda karşılaşılan sorunların çoğu birkaç temel örüntüye indirgenebilir. Bu örüntüleri bilmek, araştırmacının paniğe kapılmadan doğru müdahaleyi yapmasını sağlar.

| Sembol | Açıklama | Çözüm |
|---|---|---|
| Komut bulunamadı | Terminal kurulan komutu tanımıyor. | PATH yapılandırmasını kontrol edin, kabuğu yeniden başlatın. |
| Yetki hatası | İzin verilmemiş bir dosya ya da dizine erişim denendi. | İzin onayını verin ya da çalışma dizinini düzeltin. |
| Ağ hatası | Model çağrısı ağa ulaşamadı. | Bağlantıyı kontrol edin, gerekirse yeniden deneyin. |
| Model zaman aşımı | Yanıt beklenen sürede gelmedi. | Görevi daha küçük adımlara bölün, bağlantı kalitesini kontrol edin. |
| Bağlam limiti | Oturum modelin bağlam penceresini aştı. | Oturumu özetleyip yeniden başlatın, kalıcı bilgiyi dosyaya yazın. |

Bu başarısızlık modları kurulumun tamamen başarısız olduğu anlamına gelmez. Çoğu, ilk kullanım sürecinin doğal parçasıdır. Önemli olan, sorunun neye işaret ettiğini anlamaktır.

Bağlam limiti özellikle dikkat gerektirir. Çünkü bu sorun, kalıcı dosya temelli çalışma alışkanlığının neden gerekli olduğunu gösterir. Oturum bağlamı aşılırsa, dosyaya yazılmamış ara kararlar ve açıklamalar kaybolabilir. Bu nedenle araştırmacı, önemli çıktıları sohbet geçmişinde bırakmamalı, çalışma arşivine kaydetmelidir.

Başarısızlık modları yalnızca teknik sorunlar değildir. Aynı zamanda araştırmacıya çalışma disiplinini öğretir. İyi bir kurulum, hatasız çalışan sistem değil, hata ortaya çıktığında sorunun nerede olduğunu gösterebilen sistemdir.

## 9. Türkiye ve Yunanistan Bağlamında Özgül Noktalar

Kurulum süreci, her ülkede ve her kurumda aynı biçimde ilerlemez. Türkiye ve Yunanistan bağlamında özellikle iki başlık öne çıkar. Ödeme altyapısı ve bağlantı kalitesi.

Türkiye'de bazı uluslararası ödeme sistemleri doğrudan abonelik sürecinde sorun çıkarabilir. Bu durumda sanal kartlar, yurt dışı banka kartları, kurumsal hesaplar ya da araştırma merkezi üzerinden sağlanan erişimler gündeme gelebilir. Hangi seçeneğin işe yarayacağı, bireysel ve kurumsal koşullara göre değişir. Bu nedenle bu kitapçık belirli bir ödeme yolunu önermek yerine, araştırmacının alternatifleri önceden düşünmesini önerir.

Yunanistan'da Avrupa Birliği ödeme altyapısı nedeniyle standart abonelik süreçleri genellikle daha doğrudan ilerleyebilir. Ancak burada da kurum içi kütüphane erişimi, proxy ayarları ve bilgi işlem politikaları araştırmacının deneyimini etkileyebilir.

Bağlantı kalitesi ikinci önemli noktadır. Komotini gibi daha küçük şehirlerde ya da kırsala yakın bölgelerde bağlantı kalitesi her zaman kararlı olmayabilir. Kesintili bağlantı, model zaman aşımı hatalarını artırabilir. Bu durumda büyük görevleri tek seferde çalıştırmak yerine daha küçük adımlara bölmek daha güvenlidir.

Bu bölgesel ayrıntılar teknik gibi görünse de yöntemsel anlam taşır. Kurulum, evrensel bir prosedürün aynı biçimde uygulanması değildir. Bir aracı belirli bir kurumsal, altyapısal ve coğrafi bağlama yerleştirme sürecidir. Sosyal bilimci için sorumlu teknoloji kullanımı, bu bağlamı görmezden gelmeden başlamalıdır.

## 10. Sonraki Kategori

Bu kitapçık, Claude Code kurulumunu teknik bir başlangıç adımı olmaktan çok, akademik iş akışının ilk yöntemsel filtresi olarak ele aldı. Sistem gereksinimleri, hesap ve faturalama, CLI kurulumu, izin modeli, dosya okuma, dosya yazma, çok adımlı görev yürütme ve başarısızlık modları birlikte değerlendirildi.

Bu çerçevede araştırmacı için temel amaç, aracı yalnızca çalıştırmak değildir. Aracın doğru klasörde çalıştığını, dosyaları gerçekten okuduğunu, değişiklikleri izinle yaptığını, ara çıktıları ayrı dosyalara yazdığını ve çıktıların kaynakla karşılaştırılabildiğini görmektir.

Kurulum tamamlandıktan sonra sosyal bilimci için yeni soru akademik erişimdir. Türkçe ve Yunanca akademik kaynaklara, bölgesel indekslere ve kurumsal kütüphane altyapılarına güvenilir biçimde nasıl erişilecektir? Bir sonraki kategori bu soruya ayrılmıştır.

002-04-0001, DergiPark, ULAKBİM TR Dizin, HEAL Link ve Bölgesel İndeksleme, bu noktadan devam eder.

---

## Kaynakça

Atıflar APA 7 biçimindedir. İki arXiv ön baskısı (Bai ve diğerleri, 2022 ve Ouyang ve diğerleri, 2022) Crossref'te kayıtlı değildir. Her ikisi de 2026-05-24 tarihinde arXiv üzerinden doğrulanmıştır. Belge bağlantıları 2026-06-21 tarihinde Crossref ile doğrulanmıştır. Anthropic 2026a URL'si https://code.claude.com/docs adresine çözümlenmektedir, Microsoft 2026 URL'si ise https://learn.microsoft.com/en-us/windows/wsl/ adresine.

Anthropic. (2024). *Announcing our updated responsible scaling policy*. https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy

Anthropic. (2026a). *Claude Code documentation*. https://code.claude.com/docs

Anthropic. (2026b). *Claude Code best practices*. https://code.claude.com/docs/en/best-practices

Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McKinnon, C., Chen, C., Olsson, C., Olah, C., Hernandez, D., Drain, D., Ganguli, D., Li, D., Tran-Johnson, E., Perez, E., & Kaplan, J. (2022). *Constitutional AI: Harmlessness from AI feedback*. arXiv. https://arxiv.org/abs/2212.08073

Microsoft. (2026). *Windows Subsystem for Linux documentation*. https://learn.microsoft.com/windows/wsl/

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P., Leike, J., & Lowe, R. (2022). Training language models to follow instructions with human feedback. In *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)* (pp. 27730–27744). https://arxiv.org/abs/2203.02155

---

**Kitapçık kimliği.** `001-01-0003`
**Sürüm.** `0.2.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 2312 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 6
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`001-01-0002`](../001-01-0002/tr.md). Aracın Ötesine Geçiş: Sohbet Penceresinden İş Ortağına
**Sonraki kitapçık.** `002-04-0001`. DergiPark, ULAKBIM TR Dizin, HEAL-Link ve Bölgesel İndeksleme (Faz 2)
