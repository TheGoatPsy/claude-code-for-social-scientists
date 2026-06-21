---
title_en: "Material Passport. Tracking Sources Across Sessions"
title_tr: "Kaynak Pasaportu. Kaynakları Oturumlar Arasında İzlemek"
booklet_id: "003-03-0001"
category: "003-memory-system"
language: "tr"
version: "0.2.0"
date_published: "2026-06-12"
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
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.8 as of 2026-06-21
    role: "drafting, verification, citation lookup"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 6
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Kaynak Pasaportu. Kaynakları Oturumlar Arasında İzlemek

## Giriş

Bu kategorinin ilk kitapçığı hafızayı arşive dönüştürmenin temel ilkelerini kurmuştu. Bu kitapçık ise o arşivin en hareketli öğesine, yani kaynağa, izlenebilir bir kimlik düzeni kazandırmayı amaçlar.

Mühendislikte malzeme pasaportu, bir yapıya giren her bileşenin nereden geldiğini, hangi özellikleri taşıdığını ve hangi kullanım geçmişine sahip olduğunu belgeleyen kayıttır. Aynı fikir araştırma arşivine taşındığında kaynak pasaportu ortaya çıkar. Arşive giren her makale, kitap, rapor ya da tez, nereden bulunduğunu, hangi sorguyla geldiğini, doğrulanıp doğrulanmadığını ve hangi taslakta kullanıldığını gösteren bir kimlik satırı taşır.

Bu kitapçığın temel amacı, kaynak pasaportunun alanlarını, ne zaman yazılacağını ve Claude Code ile nasıl sürdürülebilir biçimde tutulacağını açıklamaktır. Çünkü kaynak yönetiminde asıl sorun yalnızca kaynağı bulmak değildir. Bulunmuş kaynağı aylar sonra yeniden bulunur, doğrulanır ve kullanılabilir hâlde tutmaktır.

## 1. Pasaport Metaforu

Bir kaynağın akademik yaşamı bulunduğu anda bitmez. Tam tersine orada başlar. Bugün bir katalog taramasında bulunan makale, üç hafta sonra bir taslağın giriş bölümünde, üç ay sonra tartışma bölümünde, altı ay sonra hakem yanıtında yeniden karşımıza çıkabilir.

Her yeniden kullanımda aynı sorular ortaya çıkar. Bu kaynağı nereden bulmuştum? Künyesi doğrulanmış mıydı? Hangi sorguyla gelmişti? Hangi iddiayı destekliyordu? Daha önce hangi taslakta kullanmıştım? Eğer bu soruların yanıtı yalnızca araştırmacının hafızasındaysa, kaynak yönetimi kırılgan hâle gelir.

Kaynak pasaportu, bu soruların yanıtını kaynağın kendisine iliştirir. Böylece kaynak yalnızca bir PDF, DOI ya da künye olmaktan çıkar. Bulunma bağlamı, doğrulama durumu ve kullanım geçmişiyle birlikte arşivde yaşar.

Metaforun gücü taşınabilirliğindedir. Pasaport kaynağa aittir ve kaynak nereye giderse onunla birlikte gider. Oturumlar değişir, projeler değişir, taslaklar el değiştirir. Kimlik satırı yerinde kalır.

## 2. Neden Defter Gerekir?

Sorunun kökü, bulmak ile bulunur tutmak arasındaki farktadır. Jones (2007), kişisel bilgi yönetimi alanını değerlendirirken asıl güçlüğün çoğu zaman bilgiyi ilk kez bulmak değil, bulunmuş bilgiyi yeniden bulunur kılmak olduğunu gösterir. Bu tespit, akademik kaynak yönetimi için doğrudan geçerlidir.

Bir araştırmacı her hafta çok sayıda kaynağa dokunur. Bazılarını yalnızca gözden geçirir, bazılarını derinlemesine okur, bazılarını taslağa alır, bazılarını daha sonra dönmek üzere kenara koyar. Eğer bu temaslar kayda geçirilmezse, aynı makale yeniden aranır, aynı özet yeniden okunur, aynı karar yeniden verilir.

Kaynak pasaportu bu sessiz maliyeti azaltır. Kaynak bulunduğu anda kısa bir kayıt açılır. Bu kayıt gelecekteki yeniden bulmaların, doğrulamaların ve kullanım kararlarının temelini oluşturur. Hafızayı arşive dönüştürme ilkesinin kaynak düzeyindeki karşılığı tam olarak budur. Akılda tutulacak şey dosyaya taşınır.

## 3. Pasaportun Alanları

Bir kaynak pasaportu gereğinden fazla ayrıntılı olmamalıdır. Aksi hâlde araştırmacı onu sürdüremez. Bu nedenle pasaport satırı altı temel soruya yanıt verecek kadar kısa tutulmalıdır.

Künye ve DOI nedir?

Kaynak nereden ve hangi sorguyla bulundu?

Kaynak hangi tarihte bulundu?

Erişim yolu nedir? Açık erişim, kurumsal abonelik, basılı kopya ya da başka bir yol.

Künye hangi tarihte ve hangi katalogla doğrulandı?

Kaynak hangi taslakta, hangi bölümde, hangi iddiayı taşımak için kullanıldı?

Aşağıdaki örnek sentetiktir ve yalnızca biçimi göstermek için verilmiştir.

Kaynak. Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. https://doi.org/10.1371/journal.pcbi.1003285

Bulunma. PubMed araması, reproducible research rules, 2026-06-12.

Erişim. Açık erişim.

Doğrulama. Crossref, 2026-06-12, künye eşleşti.

Kullanım. Yöntem bölümü taslağı, köken kaydı paragrafı.

Not. Köken izleme kuralı bu makaleden.

Bu alanların az tutulması bilinçli bir tercihtir. Bir dakikadan kısa sürede doldurulamayan kayıt, zamanla terk edilir. Pasaport defterinin sürdürülebilirliği, kısa ve işlevsel olmasına bağlıdır.

## 4. FAIR İlkeleriyle Hizalanma

Kaynak pasaportu kişisel bir arşiv pratiğidir. Bununla birlikte daha geniş veri yönetimi literatürüyle uyumludur. Wilkinson ve diğerleri (2016), bilimsel veri yönetimi için FAIR ilkelerini ortaya koymuştur. Bu ilkeler bulunabilirlik, erişilebilirlik, birlikte çalışabilirlik ve yeniden kullanılabilirlik üzerine kuruludur.

FAIR ilkeleri kurumlar, veri depoları ve bilimsel veri altyapıları için geliştirilmiştir. Kaynak pasaportu ise tek araştırmacının arşivine uygulanır. Ölçek farklıdır. Ancak temel sezgi benzerdir. Kimliği, üst verisi ve kalıcı tanımlayıcısı olmayan bir nesne, ister kurumsal depoda ister kişisel arşivde olsun, kaybolmaya adaydır.

DOI, kaynağın kalıcı tanımlayıcısıdır. Pasaport alanları ise kaynağın üst verisidir. Defterin kendisi de arşiv içi bulunabilirliği kurar. Bu nedenle kaynak pasaportu, FAIR mantığının kişisel araştırma arşivi düzeyindeki sadeleştirilmiş bir uyarlaması olarak düşünülebilir.

## 5. Oturum İçinde Kayıt

Kaynak pasaportunun değeri yalnızca hangi alanları içerdiğine bağlı değildir. Ne zaman yazıldığı da en az o kadar önemlidir. Doğru zaman, kaynağın arşive girdiği andır.

Bir katalog taramasından dönen kayıt işe yarar görünüyorsa, pasaport satırı aynı oturumda açılmalıdır. Sonraya bırakılan kayıt çoğu zaman hiç yazılmaz. Çünkü kaynağın hangi sorguyla, hangi amaçla ve hangi bağlamda bulunduğu oturum kapandıktan sonra hızla bulanıklaşır.

Önceki kitapçıklarda kurulan altyapı burada birleşir. Bibliyografik köprüden gelen kaynağın sorgusu, tarihi ve erişim yolu çoğu zaman bellidir. Claude Code bu alanları taslak olarak doldurabilir. Araştırmacı ise kaynağın gerçekten kullanılabilir olup olmadığını, hangi iddiayı taşıyacağını ve hangi notun düşüleceğini belirler.

Oturum kapanışına tek bir soru eklemek çoğu zaman yeterlidir. Bu oturumda taslağa giren ve pasaportu olmayan kaynak var mı? Varsa kapanıştan önce pasaport satırı yazılmalıdır.

## 6. Tekrarlanabilir Tarama Kaydı

Sistematik derleme geleneği, kaynak taramasının belgelendirilmesi konusunda en gelişmiş örneklerden birini sunar. Bramer ve diğerleri (2017), sistematik derlemelerde veri tabanı bileşimlerini incelerken hangi katalogların hangi sorgularla tarandığının kayıt altına alınmasını sürecin temel parçası olarak ele alır.

Tam ölçekli bir sistematik derleme yürütmeyen araştırmacı için bile bu ilke değerlidir. Bir tarama ancak sorgusu, tarihi, veri tabanı ve seçim gerekçesi kaydedildiğinde yeniden üretilebilir bir işleme dönüşür.

Kaynak pasaportu bu disiplini gündelik akademik çalışmaya taşır. Her satırdaki sorgu ve tarih alanları, aylar sonra aynı taramanın yeniden yürütülmesine imkân verir. Yöntem bölümünde tarama stratejisi sorulduğunda yanıt araştırmacının hafızasına değil, pasaport defterine dayanır.

## 7. Sürüm ve Yeniden Üretim

Sandve ve diğerleri (2013), tekrarlanabilir hesaplamalı araştırma için köken kaydının önemini vurgular. Her sonucun nasıl üretildiği izlenebilir olmalıdır. Akademik yazıda bir iddianın kökeni, onu taşıyan kaynaktır. Kaynak pasaportunun kullanım alanı bu izi kurar.

Bir cümle sorgulandığında zincir görünür olmalıdır. Cümle hangi iddiayı kuruyor? Hangi kaynağa dayanıyor? Kaynağın künyesi doğrulanmış mı? Hangi tarihte ve hangi katalogla doğrulanmış? Bu soruların yanıtı pasaport defterinde bulunmalıdır.

Noble (2009), hesaplamalı projelerin düzenlenmesine ilişkin kılavuzunda, her şeyin bir gün yeniden yapılmak zorunda kalabileceğini hatırlatır. Bu yeniden yapma görevini üstlenecek kişi çoğu zaman gelecekteki araştırmacının kendisidir. Altı ay sonra revizyona dönen yazar, pasaport defteri sayesinde kendi kararlarının arkeolojisini yapmak zorunda kalmaz.

## 8. Uydurma Atfa Karşı Pasaport

Kaynak pasaportunun en sert işlevi, kaynak bütünlüğünü korumasıdır. Walters ve Wilder (2023), ChatGPT tarafından üretilen bibliyografik künyelerde uydurma ve hatalı kaynakların ciddi bir sorun oluşturduğunu göstermiştir. Bu risk, yapay zekâ destekli akademik yazımda pasaport defterini daha da önemli hâle getirir.

Bu rehberin kuralı açıktır. Pasaportu olmayan kaynak, kaynakçaya giremez. Bu kural mekanikleştirilebilir olduğu için güçlüdür. Taslağın kaynakçası ile pasaport defteri karşılaştırıldığında üç liste ortaya çıkar.

Pasaportlu ve kullanılmış kaynaklar. Sağlıklı çekirdek.

Pasaportsuz atıflar. Doğrulama kuyruğu.

Kullanılmamış pasaportlar. Daha sonra işe yarayabilecek yedek kaynaklar.

İlk liste büyüdükçe kaynakçanın güvenilirliği kişisel dikkatle sınırlı kalmaz, yapısal bir güvenceye dönüşür.

## 9. Claude Code ile Pasaport Defteri

Pasaport defterinin bakımı, Claude Code'un iyi destekleyebileceği görev türlerinden biridir. Pasaport satırını belirlenen biçime göre eklemek, bibliyografik araçtan gelen kayıtları ilgili alanlara yerleştirmek, kaynakça ile pasaport defterini karşılaştırmak ve eksikleri raporlamak yapılandırılmış görevlerdir.

Örneğin araştırmacı tartışma bölümünde kullanılan kaynakları pasaport defteriyle karşılaştırmasını isteyebilir. Araç pasaportlu kaynakları, doğrulama gerektiren kaynakları ve henüz kullanılmamış kayıtları ayrı ayrı raporlayabilir. Böylece kaynak denetimi yalnızca son aşamada yapılan yorucu bir temizlik olmaktan çıkar, yazım sürecinin doğal parçası hâline gelir.

Sınır yine aynıdır. Kaynağın hangi iddiayı taşıyacağına, metinde hangi ağırlıkla kullanılacağına ve not alanına hangi değerlendirmenin yazılacağına araştırmacı karar verir. Model defteri tutmaya yardım eder. Bilimsel yargı araştırmacıda kalır.

## 10. Köprü. Defterin Evine

Kaynak pasaportu arşivin bir dosyasıdır. Her dosya gibi onun da bir evi olmalıdır. Pasaport defteri nerede yaşar? Günlük kayıtlarla ilişkisi nasıl kurulur? İçerik haritasında hangi başlığa bağlanır? Bu sorular klasör disiplinini gerektirir.

Bir sonraki kitapçık, arşivin klasör mimarisini ve Maps of Content kalıbını ele alır. Kaynak pasaportunun evi, bu mimarinin içinde anlam kazanacaktır.

## Kaynakça

Atıflar APA 7 biçimindedir. DOI'ler 2026-06-21 tarihinde Crossref üzerinden doğrulanmıştır.

Bramer, W. M., Rethlefsen, M. L., Kleijnen, J., & Franco, O. H. (2017). Optimal database combinations for literature searches in systematic reviews: A prospective exploratory study. *Systematic Reviews*, 6(1), Article 245. https://doi.org/10.1186/s13643-017-0644-y

Jones, W. (2007). Personal information management. *Annual Review of Information Science and Technology*, 41(1), 453–504. https://doi.org/10.1002/aris.2007.1440410117

Noble, W. S. (2009). A quick guide to organizing computational biology projects. *PLoS Computational Biology*, 5(7), e1000424. https://doi.org/10.1371/journal.pcbi.1000424

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, 9(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, 13, Article 14045. https://doi.org/10.1038/s41598-023-41032-5

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.-W., da Silva Santos, L. B., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., … Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, Article 160018. https://doi.org/10.1038/sdata.2016.18

---

**Kitapçık kimliği.** `003-03-0001`
**Sürüm.** `0.2.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1267 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 6
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`003-01-0001`](../003-01-0001/tr.md). Hafızayı Arşive Dönüştürmek. İlkesel Bir Giriş
**Sonraki kitapçık.** [`003-04-0001`](../003-04-0001/tr.md). Açık Bilim Paketi, Veri, Kod, Ek Dosya ve Kalıcı DOI
