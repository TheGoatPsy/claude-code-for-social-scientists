---
title_en: "Preparing Sensitive Data, Anonymization, Masking, and Local Preprocessing"
title_tr: "Hassas Veriyi Hazırlamak, Anonimleştirme, Maskeleme ve Yerel Ön İşleme"
booklet_id: "008-04-0001"
category: "008-data-analysis"
language: "tr"
version: "0.1.0"
date_published: "2026-06-21"
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
    model_dated: null  # Anthropic, Opus 4.8 için tarihli tanımlayıcı yayımlamadı (2026-06-21)
    role: "drafting, verification, citation lookup, bilingual authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 9
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Bu kitapçık Türkçe olarak kaleme alınmış, İngilizce sürüm (en.md) aynı argüman ve kaynak kümesiyle bağımsız olarak yeniden yazılmıştır. Atıflar her iki dilde özdeştir."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Hassas Veriyi Hazırlamak, Anonimleştirme, Maskeleme ve Yerel Ön İşleme

Sosyal bilimcinin çalışmasını en sık kilitleyen şey yanlış bir istatistiksel karar değildir. Ham verinin yanlış yere gitmesidir. Görüşme dökümleri, klinik notlar, saha günlükleri ve öğrenci metinleri, araştırmacıdan çok daha uzun yaşar ve çok daha geniş bir izleyici kitlesiyle buluşur. Bu kitapçık o malzemeyi yapay zekâ iş akışına sokulmadan önce nasıl güvenli çalışma verisine dönüştüreceğini ele alır. Temel kural nettir: önce anonimleştirme, sonra araç.

## 1. Ham veri, çalışma verisi, paylaşılabilir veri

Ham veri, katılımcının verdiği ya da araştırmacının topladığı ilk materyaldir. Sesi tam kaydeder, adı tam yazar, adresi tam bildirir. Çalışma verisi ise kimlik ve bağlam riski azaltılmış analiz kopyasıdır. Gerçek bir araştırma oturumunda kullanılan dosyadır. Paylaşılabilir veri, daha ileri bir süzgeçten geçmiş, etik kurul onayı ve hukuki uyumluluk çerçevesinde dışarı açılabilecek sürümdür.

Bu üç katmanı birbirinden ayıran tek şey kural değil, pratiğin kendisidir. Ham veriyi yanlışlıkla bir yapay zekâ oturumuna taşımak o ayrımı silip atar ve onarımı güçtür. Klasör yapısı bu ayrımı zaten kural hâline getirmelidir: ham arşiv ayrı, çalışma dizini ayrı, paylaşım klasörü ayrı. Claude Code yalnızca çalışma dizininde çalışır. Ham arşive hiçbir otomasyon bağlanmaz.

Üç katmanın karıştırılması hem etik hem hukuki sonuçlar doğurur. Türkiye'de 6698 sayılı KVKK ve Avrupa bağlamında GDPR, araştırmacının ham veriyi kişisel veri olarak işlemesini açık bir yasal çerçeveye bağlar (Kişisel Verileri Koruma Kurumu, 2016) (Avrupa Parlamentosu ve Konseyi, 2016). Katılımcı, onam formunda çalışma verisini ima eden bir sözleşme yapmıştır, ham veriyle yapılan her şeyi onaylamamıştır.

## 2. Anonimleştirme ve takma adlandırma

Bu iki kavram aynı şey değildir ve birbirine karıştırılması ciddi bir güvenlik açığı doğurur.

Takma adlandırma, doğrudan kimlik bilgisini bir kodla değiştirmektir. Mehmet yerine K7, Ankara Eğitim Araştırma Hastanesi yerine Hastane B. Bağlantı tablosu araştırmacının elindedir, istendiğinde geri dönüş mümkündür. GDPR ve KVKK bu yöntemi tam anonimleştirme saymaz. Takma adlandırılmış veri yine de kişisel veridir çünkü bir anahtarla yeniden bağlanabilir.

Anonimleştirme ise yeniden tanımlama riskini makul ölçüde ortadan kaldırmayı hedefler. İsim silmek yeterli değildir. Sweeney (2002), posta kodu, cinsiyet ve doğum tarihi gibi üç "zararsız" değişkenin bir araya geldiğinde ABD nüfusunun yüzde seksen yedisini tekil biçimde tanımladığını göstermiştir. Yeniden tanımlama saldırılarını inceleyen sistematik derleme bulgular açısından daha da çarpıcıdır: sağlık veri kümelerinde yüzde seksen beşe varan bireyin, göreceli olarak az bağlamsal bilgiyle yeniden tanımlanabildiği raporlanmıştır (El Emam ve diğerleri, 2011). Bu rakamlar, büyük veri tabanlarında anonimleştirmenin neden "yapıldı, tamamlandı" olarak değil, süregelen bir risk yönetimi süreci olarak ele alınması gerektiğini açıklar.

## 3. Doğrudan ve dolaylı kimlik bilgisi

Ad, soyad, telefon, e-posta ve kimlik numarası doğrudan kimlik bilgisidir. Bunlar genellikle tanınır ve silinir. Asıl risk dolaylı kimlik bilgisinde yatar.

Dolaylı kimlik bilgisi, tek başına kişiyi açıklamayan ama başka bilgilerle birleştiğinde açıklayan değişkenlerdir: yer, meslek, aile yapısı, nadir bir olay, belirli bir tarih. Küçük topluluklarda bir köy adı, okul, tanınmış bir hoca ve olay yılı bir araya gelince katılımcı tanınabilir hâle gelir. Nitel veri bu açıdan özellikle kırılgandır. Anlatının dramatik ayrıntıları kimlik bilgisi değeri taşır ve araştırmacı bunu bazen fark etmez.

NIST'in kişisel verilerin kimliksizleştirilmesine ilişkin teknik rehberi (Garfinkel, 2015), doğrudan ve dolaylı tanımlayıcılar arasındaki bu ayrımı sistematik hâle getirir ve her veri türü için hangi dönüşümlerin uygulanması gerektiğini adım adım belirler. Anonimleştirme raporu her iki tür bilgiyi ayrı ayrı ele almalıdır. Dolaylı tanımlayıcılar üzerinde bir kontrol listesi çalıştırılmadan anonimleştirme tamamlanmış sayılmaz.

## 4. Klinik veri protokolü

Klinik veri özel nitelikli veridir. KVKK'nın 6. maddesi ve GDPR'ın 9. maddesi sağlık verisini, biyometrik veriyi ve psikolojik değerlendirme kayıtlarını ayrı bir yasal koruma altına alır. Bu verilerle işlem yapılabilmesi için açık rıza ya da açıkça belirtilmiş yasal dayanak şarttır.

Vaka notları, tanı bilgisi, tedavi süreci, aile öyküsü ve psikometrik sonuçlar model erişimine kapalı bölgede tutulur. Bunların araştırma amacıyla incelenmesi gereken kısmı yalnızca gerekli en az bilgiyi taşıyan bir çalışma kopyasına aktarılır. Gereksiz klinik ayrıntı burada temizlenir, araştırma sorusunu yanıtlamayan her alan bu kopyadaki yerini kaybeder.

Klinik örnekler eğitim ya da yayın amacıyla kullanılacaksa kimliksizleştirme yeterli değildir. Bağlam azaltma da gerekir. Bir dava örneğinin hangi şehirde gerçekleştiği, hangi kurumda, yaklaşık hangi yıl aralığında, topluluğun büyüklüğü: bunların hepsi dolaylı tanımlayıcı işlev görebilir ve hepsi karara bağlanmalıdır. Bu karar araştırmacının değer yargısını, etik kurulun beklentisini ve yayının izleyici kitlesini birlikte içerir.

## 5. Mülakat ve saha notu protokolü

Mülakat dökümleri konuşanın kimliğini yalnızca adıyla değil, anlatının dokusundan geçirir. Bir katılımcı çocukluğundan söz ederken anlattığı köy, isimsizce "büyük bir kayıp" dediği olayın yılı, öğretmeninin ismi verilmeden tanımladığı özelliği, bulunduğu sınıfın kaç kişiden oluştuğunu ima eden cümlesi: bunların her biri ayrı bir tanımlayıcıdır. Saha notlarında ise yer ve ilişki ağı çok daha güçlü bir tanımlayıcı set kurar.

Bu nedenle dökümler önce maskeleme tablosundan geçirilir. Kişi, yer, kurum, olay ve tarih alanları ayrı işaretlenir. Her alan için karar verilir: genelleştirilecek mi, silinecek mi, yoksa bağlam kaybı yaratacağı için etiket değiştirilecek mi? Saunders ve diğerleri (2015), bu kararın neden tek bir kuralın uygulanmasına indirgenemeyeceğini göstermiştir. Araştırmacı her seferinde alıntının değeri ile kimlik riski arasında gerçek bir ödünleşim yapar. Mülakat dökümleri için standart bir komut dosyası yoktur. Her çalışmanın kendi maskeleme mantığı kendine özgüdür.

## 6. Yerel ön işleme

Yerel ön işleme, verinin üçüncü taraf bir modele veya bulut hizmetine gitmeden önce araştırmacının kendi cihazında temizlenmesidir. Bu adım teknik bir kolaylık değil, etik bir zorunluluktur.

Ohm (2010), anonimleştirme tekniklerinin kırılganlığını ayrıntılı biçimde belgelemiştir. Buna karşın yerel ön işleme, buluta yüklemeden önce riski en aza indirgeyen tek kontrol noktasıdır. Pratik akış şudur: ham dosyadan düz metin kopyası oluşturulur, kimlik alanları işaretlenir, maskeleme uygulanır, güvenli sürüm ayrı bir klasöre yazılır ve bu klasör Claude Code iş akışına açılır. Ham dosya klasörüne hiçbir otomasyon bağlanmaz.

Yerel ön işlemenin ek bir faydası vardır: araştırmacıyı veriyle doğrudan temasa sokar. Birinci kitapçıkta kurulan spesifikasyon günlüğü mantığıyla örtüşür. Araştırmacı verinin içinden geçer, neyin kalıp neyin silineceğini karar verir. Bu karar bilişsel bir sürtünme üretir ve bu sürtünme değerlidir.

## 7. Maskeleme tablosu

Maskeleme tablosu değiştirilen her öğenin kaydını tutar. Katılımcı kodu A, şehir kodu X, kurum kodu Y gibi. Her satır şu alanları içerir: orijinal değer, kullanılan etiket, değiştirme gerekçesi, uygulama tarihi.

Bu tablo çalışma verisiyle aynı yerde tutulmaz. Ayrı, erişimi sınırlı, şifreli bir alanda yaşar ve araştırmanın bütün yürütme süresince güvende kalır. İki uç senaryo tablonun neden bu kadar önemli olduğunu açıklar. Maskeleme tablosu olmadan geri dönüş gerekirse bağlam kaybolur ve araştırmacı hangi kodun hangi katılımcıya karşılık geldiğini hatırlamayabilir. Maskeleme tablosu açıkta kalırsa anonimleştirme boşa düşer. Tabloya erişen herkes anonimleştirme sürecini tersine işletir.

Narayanan ve Shmatikov (2008), büyük seyrek veri kümelerinde yeniden tanımlama saldırılarının gerçekte ne kadar başarılı olabileceğini göstermiştir. Rocher ve diğerleri (2019) aynı tehdidin tamamlanmamış veri kümelerinde de geçerliliğini koruduğunu ortaya koymuştur. Bu bulgular, maskeleme tablosunun neden yalnızca idari bir güzellik değil, gerçek bir güvenlik bileşeni olduğunu somutlaştırır.

## 8. Yapay zekâya asla verilmemesi gerekenler

Bu liste kısaldır, mutlaktır ve konforla değişmez.

Açık kimlik bilgisi, onam formu, ses ve görüntü kaydı (transkript değil, kaydın kendisi), biyometrik iz, ham klinik not, küçük toplulukta tanınabilir anlatı ve maskeleme tablosu yapay zekâ aracına verilmez. Araç güçlü olduğu için sınır esnetilmez. Araç yalnızca güvenli çalışma kopyasıyla karşılaşır.

Bu kural iki noktada ek dikkat ister. Birincisi, araştırmacının "bu kadar az bilgiyle tanımlanamazlar" diye düşündüğü ama gerçekte dolaylı tanımlayıcıların birleştiği alıntılar. İkincisi, görüntülü görüşme platformlarının otomatik olarak oluşturduğu katılımcı listeleri ya da katılımcı adlarını içeren toplantı notları. Bunlar bazen ham klinik not kadar açık kimlik bilgisi taşır ama görünürde belge formatında oldukları için göz ardı edilir.

## 9. Anonimleştirme sonrası denetim

Güvenli kopya oluşturulduktan sonra otomatik araçlara güvenmek yeterli değildir. İnsan denetimi zorunludur.

Denetim şu adımlardan oluşur: güvenli kopyadan rastgele örnekler seçilir ve okunur, yeniden tanımlama riski açısından değerlendirilir, özellikle dolaylı tanımlayıcılar gözden geçirilir. Bu okuma araştırmacı tarafından yapılır ve maskeleme tablosunu görmeden yapılır. Tanımak mümkün mü? Hangi bilgilerin birleşimi potansiyel bir riskti?

Anonimleştirme otomatik bir temizleme değil, etik bir karar sürecidir. Veri setinin büyüklüğü, topluluğun tanınabilirliği, araştırmanın açıklanacağı platform ve katılımcı nüfusunun homojenliği bu kararı etkiler. Rocher ve diğerleri (2019), bu değişkenleri dikkate alan istatistiksel bir yeniden tanımlama risk modelini klinik bağlamda uygulamıştır. Araştırmacı her araçtan yararlanır ama nihai yargı hep insana aittir.

## 10. Skill çıktıları

`/sensitive-data-anonymization-gate` dört çıktı üretir ve bunların her biri bir karar noktasına karşılık gelir. Anonimleştirme raporu, gerçekleştirilen dönüşümlerin ve gerekçelerinin kaydıdır. Maskeleme tablosu, değiştirilen her öğenin izlenebilir kümesidir. Dolaylı kimlik riski notu, gözden geçirme gerektiren alanların listesidir. Güvenli çalışma kopyası, modele açılacak tek veri dosyasıdır.

Skill bir hız aracı değil, kapıdır. Bu dört çıktıdan herhangi biri eksik ya da yetersiz görünüyorsa veri modele girmez. Anonimleştirme bir süreç içinde yaşar ve bu sürecin son adımı daima araştırmacının değerlendirmesidir.

## Kaynakça

Atıflar APA 7 biçimindedir. DOI'ler 2026-06-21 tarihinde Crossref ve doi.org üzerinden doğrulanmıştır. KVKK ve GDPR metinleri resmî yasal kaynaklar olup DOI sisteminde yer almaz. Bağlantılar kurumsal yayın adresleri üzerinden verilmiştir.

Avrupa Parlamentosu ve Konseyi. (2016). *Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation)*. https://eur-lex.europa.eu/eli/reg/2016/679/oj

El Emam, K., Jonker, E., Arbuckle, L., & Malin, B. (2011). A systematic review of re-identification attacks on health data. *PLOS ONE*, 6(12), e28071. https://doi.org/10.1371/journal.pone.0028071

Garfinkel, S. L. (2015). *De-identification of personal information* (NIST IR 8053). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.IR.8053

Kişisel Verileri Koruma Kurumu. (2016). *6698 sayılı Kişisel Verilerin Korunması Kanunu*. https://www.kvkk.gov.tr

Narayanan, A., & Shmatikov, V. (2008). Robust de-anonymization of large sparse datasets. *IEEE Symposium on Security and Privacy*, 111–125. https://doi.org/10.1109/SP.2008.33

Ohm, P. (2010). Broken promises of privacy: Responding to the surprising failure of anonymization. *UCLA Law Review*, 57, 1701–1777.

Rocher, L., Hendrickx, J. M., & de Montjoye, Y. A. (2019). Estimating the success of re-identifications in incomplete datasets using generative models. *Nature Communications*, 10, Article 3069. https://doi.org/10.1038/s41467-019-10933-3

Saunders, B., Kitzinger, J., & Kitzinger, C. (2015). Anonymising interview data: Challenges and compromise in practice. *Qualitative Research*, 15(5), 616–632. https://doi.org/10.1177/1468794114550439

Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal on Uncertainty, Fuzziness and Knowledge-Based Systems*, 10(5), 557–570. https://doi.org/10.1142/S0218488502001648

---

**Kitapçık kimliği.** `008-04-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1391 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 9
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`008-03-0001`](../008-03-0001/tr.md). Yapay Zekâ Yardımı ve İnsan Gözetimiyle Nitel Kodlama
**Sonraki kitapçık.** [`008-05-0001`](../008-05-0001/tr.md). Araştırma Protokolü ve Ön Kayıt, Analizden Önce Karar Vermek
