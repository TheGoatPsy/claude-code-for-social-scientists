---
title_en: "Material Passport: Tracking Sources Across Sessions"
title_tr: "Kaynak Pasaportu: Kaynakları Oturumlar Arası İzlemek"
booklet_id: "003-03-0001"
category: "003-memory-system"
language: "tr"
version: "0.1.0"
date_published: "2026-06-12"
date_last_revised: "2026-06-20"
authors:
  - name: "Onour Impram"
    orcid: "0000-0003-1076-3928"
    role: "author, principal reviewer"
ai_assisted: true
ai_tools:
  - name: "Claude Code"
    vendor: "Anthropic"
    model_alias: "claude-fable-5"
    model_dated: null  # no dated identifier published by Anthropic for Fable 5 as of 2026-06-12
    role: "drafting, verification, citation lookup"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-20"
verified_citations_count: 6
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Kaynak Pasaportu: Kaynakları Oturumlar Arası İzlemek

Bu kategorinin ilk kitapçığı hafızayı arşive dönüştürmenin ilkelerini kurdu. Bu kitapçık o arşivin en hareketli sakinine, kaynağa, bir kimlik düzeni getirir. Mühendislikte malzeme pasaportu, bir yapıya giren her bileşenin nereden geldiğini ve hangi özellikleri taşıdığını belgeleyen kayıttır. Aynı fikir araştırma arşivine taşındığında kaynak pasaportu doğar. Arşive giren her makale, kitap ve rapor, nereden bulunduğunu, hangi sorguyla geldiğini, doğrulanıp doğrulanmadığını ve hangi taslakta kullanıldığını söyleyen bir kimlik satırı taşır. Bu kitapçık o satırın alanlarını, ne zaman yazılacağını ve Claude Code ile nasıl zahmetsiz tutulacağını anlatır.

## 1. Pasaport Metaforu

Bir kaynağın yaşamı bulunduğu anda bitmez, orada başlar. Bugün bir katalog taramasında bulunan makale, üç hafta sonra bir taslağın tartışma bölümünde, üç ay sonra bir hakem yanıtında yeniden sahneye çıkar. Her sahnede aynı sorular döner. Bu kaynağı nereden bulmuştum? Künyesi doğrulanmış mıydı? Hangi iddiayı destekliyordu? Pasaport, bu soruların yanıtını kaynağın kendisine iliştirir. Soru her doğduğunda arşivde aranan şey bir anı değil, bir kayıttır.

Metaforun gücü taşınabilirliğindedir. Pasaport kaynağa aittir ve kaynak nereye giderse onunla gider. Oturumlar değişir, projeler değişir, taslaklar el değiştirir. Kimlik satırı yerinde durur.

## 2. Neden Defter Gerekir

Sorunun kökü, bulmak ile bulunur tutmak arasındaki farktadır. Jones (2007), kişisel bilgi yönetimi alanını derlediği çalışmada, asıl zorluğun bilgiyi bulmak değil, bulunmuş bilgiyi yeniden bulunur kılmak olduğunu ortaya koyar. Araştırmacı her hafta onlarca kaynağa dokunur ve dokunulan her kaynak, kayıt düşülmediyse, birkaç oturum sonra yeniden yabancıdır. Yeniden bulma maliyeti sessizce birikir. Aynı makale ikinci kez aranır, aynı özet ikinci kez okunur, aynı karar ikinci kez verilir.

Defter bu maliyeti tek seferlik bir kayıt zahmetiyle değiştirir. Kaynak bulunduğu anda bir satır yazılır ve o satır, gelecekteki bütün yeniden bulmaların yerine geçer. Hafıza kitapçığının ilkesi burada en somut hâlini alır. Akılda tutulacak her şey, akıldan dosyaya taşınır.

## 3. Pasaportun Alanları

Bir pasaport satırı altı alanı yanıtlar. Künye ve DOI. Nereden ve hangi sorguyla bulunduğu. Bulunma tarihi. Erişim yolu, açık erişim mi, kurumsal abonelik mi, basılı kopya mı. Doğrulama durumu, künye hangi tarihte hangi katalogla teyit edildi. Kullanım yeri, hangi taslağın hangi bölümünde hangi iddiayı taşıyor.

Aşağıdaki örnek sentetiktir ve biçimi göstermek için kurulmuştur.

> **Kaynak.** Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. https://doi.org/10.1371/journal.pcbi.1003285
> **Bulunma.** PubMed araması, "reproducible research rules", 2026-06-12.
> **Erişim.** Açık erişim.
> **Doğrulama.** Crossref, 2026-06-12, künye eşleşti.
> **Kullanım.** Yöntem bölümü taslağı, köken kaydı paragrafı.
> **Not.** Köken izleme kuralı bu makaleden.

Altı alan kasıtlı olarak azdır. Doldurulması bir dakikadan kısa süren bir kayıt yazılır. Doldurulması çeyrek saat süren bir form yazılmaz.

## 4. FAIR İlkeleriyle Hizalanma

Bu kişisel düzenin, veri yönetiminin kurumsal katmanında bir karşılığı vardır. Wilkinson ve diğerleri (2016), bilimsel veri yönetimi için FAIR ilkelerini ortaya koydu. Bulunabilirlik, erişilebilirlik, birlikte çalışabilirlik ve yeniden kullanılabilirlik. İlkelerin omurgası, her nesnenin zengin üstveriyle ve kalıcı tanımlayıcıyla donanmasıdır. Kaynak pasaportu, bu omurganın kişisel arşiv katmanına indirilmiş hâli olarak okunabilir. DOI kalıcı tanımlayıcıdır, pasaport alanları üstveridir ve defterin kendisi arşiv içi bulunabilirliği kurar.

Benzetme bilinçli sınırlarıyla kullanılmalıdır. FAIR, kurumların ve depoların ölçeğinde tanımlanmış bir çerçevedir. Pasaport ise tek araştırmacının defteridir. Ortak olan ilke şudur. Kimliği olmayan nesne, ölçek fark etmeksizin, kaybolmaya adaydır.

## 5. Oturum İçinde Kayıt

Pasaportun yazılma anı, değerinin yarısıdır. Doğru an, kaynağın arşive girdiği andır. Katalog köprüsünden dönen bir kayıt işe yarar göründüyse pasaport satırı o oturumda açılır. Sonraya bırakılan kayıt, çoğu zaman hiç yazılmayan kayıttır, çünkü bulunma bağlamı, hangi sorgu, hangi amaç, oturum kapanınca buharlaşır.

Önceki kitapçıkların altyapısı burada birleşir. Köprüden gelen kaynağın sorgusu ve tarihi zaten bellidir, model bu alanları kendiliğinden doldurabilir. Oturum kapanış ritüeline eklenen tek bir denetim, sistemi mühürler. Bu oturumda taslağa giren ve pasaportu olmayan kaynak var mı? Varsa kapanıştan önce satırı yazılır.

## 6. Tekrarlanabilir Tarama Kaydı

Sistematik derleme geleneği, tarama belgelemenin en olgun örneğini sunar. Bramer ve diğerleri (2017), sistematik derlemeler için veri tabanı bileşimlerini inceledikleri çalışmada, hangi katalogların hangi sorgularla tarandığının kayıt altına alınmasını sürecin kurucu parçası olarak ele alır. Tam ölçekli bir sistematik derleme yapmayan araştırmacı için bile ders açıktır. Tarama, sorgusu ve tarihi kaydedildiğinde tekrarlanabilir bir işleme dönüşür.

Pasaport defteri bu disiplinin gündelik ölçeğe uyarlanmasıdır. Her satırdaki sorgu ve tarih alanları, aylar sonra aynı taramanın yeniden koşulmasına izin verir. Yöntem bölümünde tarama stratejisi sorulduğunda yanıt, hatırlamaya değil deftere dayanır.

## 7. Sürüm ve Yeniden Üretim

Sandve ve diğerleri (2013), tekrarlanabilir hesaplamalı araştırmanın kurallarını derlerken ilk sıraya köken kaydını koyar. Her sonucun nasıl üretildiği izlenebilir olmalıdır. Taslaktaki bir iddianın kökeni, onu taşıyan kaynaktır ve pasaportun kullanım alanı tam bu izi kurar. İddia sorgulandığında zincir hazırdır. Cümle, kaynak, künye, doğrulama tarihi.

Noble (2009), hesaplamalı projelerin düzenlenmesi üzerine kılavuzunda her şeyin bir gün yeniden yapılmak zorunda kalacağını ve düzenin bu yeniden yapmayı yabancılar için bile mümkün kılması gerektiğini söyler. Buradaki yabancı çoğu zaman gelecekteki sizsinizdir. Altı ay sonra revizyona dönen yazar, pasaport defteri sayesinde kendi kararlarının arkeolojisini yapmak zorunda kalmaz.

## 8. Uydurmaya Karşı Pasaport

Defterin bütünlük katmanındaki işlevi en serttir. Walters ve Wilder (2023), ChatGPT üretimi kaynakçalardaki uydurma künyelerin ölçeğini belgeledi. Bu rehberin atıf disiplini her künyenin katalogda doğrulanmasını şart koşar ve pasaport, bu şartın arşivdeki uygulayıcısıdır. Kural tek cümledir. Pasaportu olmayan kaynak, kaynakçaya giremez.

Kuralın gücü mekanikleşebilir olmasındadır. Taslağın kaynakçası ile pasaport defteri yan yana konduğunda üç liste düşer. Pasaportlu ve kullanılmış kaynaklar, sağlıklı çekirdek. Pasaportsuz atıflar, doğrulama kuyruğu. Kullanılmamış pasaportlar, ileride işe yarayabilecek yedekler. İlk liste büyüdükçe kaynakçanın güvenilirliği yapısal hâle gelir.

## 9. Claude Code ile Pasaport Defteri

Defterin bakımı, modelin en iyi yaptığı iş türündendir. Pasaport satırını biçimine uygun eklemek, köprüden gelen kaynağın sorgu ve tarih alanlarını doldurmak, kaynakça ile defteri karşılaştırıp üç listeyi raporlamak. Tartışma bölümünü hangi kaynaklar taşıyor sorusu, defter varken bir arama komutudur.

Sınır her zamanki yerindedir. Kaynağın işe yarayıp yaramadığına, hangi iddiayı taşıyacağına ve nota ne yazılacağına araştırmacı karar verir. Model defteri tutar, defterin söylediğini araştırmacı söyletir. Kayıt mekanikleştikçe yargıya kalan zaman büyür ve düzenin asıl getirisi budur.

## 10. Köprü, Defterin Evine

Pasaport defteri arşivin bir dosyasıdır ve her dosya gibi bir adrese ihtiyaç duyar. Defter nerede yaşar, günlük kayıtlarla ilişkisi nasıl kurulur, içerik haritasında nereye bağlanır? Bu soruların sistemi klasör disiplinidir. Bir sonraki kitapçık arşivin klasör mimarisini ve Maps of Content kalıbını kurar. Pasaportun evi orada hazırdır.

## Kaynakça

Atıflar APA 7 biçimindedir. DOI'ler 2026-06-12 tarihinde Crossref üzerinden doğrulanmıştır.

Bramer, W. M., Rethlefsen, M. L., Kleijnen, J., & Franco, O. H. (2017). Optimal database combinations for literature searches in systematic reviews: A prospective exploratory study. *Systematic Reviews*, 6(1), Article 245. https://doi.org/10.1186/s13643-017-0644-y

Jones, W. (2007). Personal information management. *Annual Review of Information Science and Technology*, 41(1), 453–504. https://doi.org/10.1002/aris.2007.1440410117

Noble, W. S. (2009). A quick guide to organizing computational biology projects. *PLoS Computational Biology*, 5(7), e1000424. https://doi.org/10.1371/journal.pcbi.1000424

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, 9(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, 13, Article 14045. https://doi.org/10.1038/s41598-023-41032-5

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.-W., da Silva Santos, L. B., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., … Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, Article 160018. https://doi.org/10.1038/sdata.2016.18

---

**Kitapçık kimliği.** `003-03-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-20
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1015 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 6
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`003-01-0001`](../003-01-0001/tr.md). Hafızayı Arşive Dönüştürmek, İlkesel Bir Giriş
**Sonraki kitapçık.** [`004-01-0001`](../../004-vault-architecture/004-01-0001/tr.md). Klasör Disiplini ve Maps of Content (MOC) Kalıbı
