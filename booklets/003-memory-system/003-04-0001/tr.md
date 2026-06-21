---
title_en: "Open Science Package, Data, Code, Supplementary Files, and Persistent DOI"
title_tr: "Açık Bilim Paketi, Veri, Kod, Ek Dosya ve Kalıcı DOI"
booklet_id: "003-04-0001"
category: "003-memory-system"
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
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.8 as of 2026-06-21
    role: "drafting, verification, citation lookup"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 9
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Açık Bilim Paketi, Veri, Kod, Ek Dosya ve Kalıcı DOI

Bir makale yayımlandığında çalışma bitmez. Bulgu anlatılmıştır, ama bulgunun nasıl üretildiği henüz gösterilmemiştir. Veri sözlüğü hazırlanmamış, analiz kodu belgelenmemiş, ek materyal düzenlenmemiş, lisans seçilmemiş, kalıcı tanımlayıcı atanmamışsa araştırma paketi eksiktir. Bu eksiklik yalnızca bir şeffaflık sorunu değildir. Beş yıl sonra kendi arşivine dönen araştırmacı da o paketi çözemeyebilir.

Bu kitapçığın merkezi iddiası şudur: sosyal bilimci, makalesini tek başına değil, yeniden okunabilir ve yeniden denetlenebilir bir araştırma paketiyle birlikte düşünmelidir. Açık bilim, sorumsuz ifşa değildir. Açılabilecek olanı düzenli açmak, açılamayacak olanın neden açılamadığını dürüstçe belgelemektir. Bu iki sorumluluk birbirinin rakibi değil, bütünleyicisidir.

## 1. Makale ile araştırma paketi arasındaki fark

Makale bulguyu anlatır. Araştırma paketi bulgunun nasıl üretildiğini gösterir. Bu iki şey aynı değildir ve biri diğerinin yerini tutamaz.

Makalede birkaç paragrafla özetlenen süreç, pakette somut dosyalar olarak görünür hale gelir: veri temizleme adımları, dönüşüm kararları, analiz sırası, kaynak doğrulama protokolü, etik sınırlar. Bu görünürlük yalnızca okurun erişimi için değildir. Kitzes ve diğerleri (2018), veri-yoğun bilimlerdeki yeniden üretim deneyimlerini incelerken şunu vurgular: araştırmacılar kendi çalışmalarının en sık yeniden üreticileridir. İyi bir araştırma paketi, beş yıl sonra kendi arşivine dönen araştırmacıya ne yaptığını yeniden öğretir. Hangi veri sürümü kullanılmış, hangi kod çalışmış, hangi kaynak nereden gelmiş, hangi değişken nasıl tanımlanmış. Bunlar hatırlanmaz. Kaydedilir.

Paket olmadan makale bir sonuca işaret eder. Paketli makale ise o sonuca giden yolu açık tutar. İkisi arasındaki fark, araştırmanın gelecekte sorgulanabilir olup olmayacağını belirler.

## 2. Açık veri ne zaman mümkündür

Açık veri her araştırma için mümkün değildir ve bu normaldir. Katılımcı hakları, etik kurul koşulları, onam kapsamı ve bağlamdan koparıldığında zarar üretme riski, paylaşım kararını belirleyen gerçek sınırlardır.

Anonimleştirilmiş, yeniden tanımlama riski taşımayan, onam kapsamıyla uyumlu ve bağlamından koparıldığında zarar üretmeyecek veri paylaşılabilir. Klinik veri, küçük topluluk verisi ve hassas mülakat dökümü çoğu zaman bu koşulları karşılamaz. Ama bu, araştırmacının elleri boş kalacağı anlamına gelmez.

Doğrudan paylaşılamayan durumlarda alternatif biçimler devreye girer. Sentetik örnek veri, değişken sözlüğü, analiz kodu, özet istatistikler, erişim başvuru kılavuzu ve etik sınırlama notu bunların başında gelir. Bu alternatifler, araştırmanın doğrulanamaz olduğu anlamına gelmez. Araştırmanın hangi koşullar altında doğrulanabileceğini belgeler. Açıklık, sorumsuz ifşanın değil, dürüst belgelemenin adıdır.

Nosek ve diğerleri (2015), açık araştırma kültürünün yalnızca erişim değil, şeffaflık, metodolojik doğruluk ve yeniden üretim üzerine kurulu olduğunu ortaya koyar. Bu çerçevede kısıtlı veriyle yapılan araştırma da açık olabilir: kısıtlamanın gerekçesi açıkça belgelendiğinde.

## 3. Veri sözlüğü ve kod kitabı

Araştırma paketinin en çok ihmal edilen ama en yararlı bileşeni veri sözlüğüdür. Sözlük olmadan bir veri dosyası, bağlamını bilmeyene anlamsız sayılar dizisidir.

İyi bir veri sözlüğü her değişken için şu bilgileri içerir: değişken adı ve açıklaması, ölçüm düzeyi, değer aralığı ve olası kodlar, eksik veri kodu ve bu kodun anlamı, dönüşüm bilgisi, analizdeki rolü ve kaynağa bağlantısı. Bu bilgiler bir sayfayı geçmeyebilir. Ama o sayfa olmadan veriyi başkası okuyamaz. Beş yıl sonra araştırmacının kendisi de okuyamayabilir.

Nitel çalışmada kod kitabı benzer işlevi görür. Kod etiketi, tanım, dahil etme ve dışlama ölçütleri, örnek alıntı ve sürüm notu birarada tutulur. Yapay zekâ destekli kodlama yapıldıysa modelin rolü, hangi metin parçalarında kullanıldığı ve analist denetimi nasıl yürütüldüğü ayrıca belirtilir. Yapay zekâ katkısı hem teknik şeffaflık hem de hakem yanıtı açısından giderek daha kritik bir belgeleme noktasına dönüşmektedir.

Sandve ve diğerleri (2013), tekrarlanabilir hesaplamalı araştırma için on kural arasında köken kaydını öne çıkarır. Değişkenin nerede, ne zaman ve hangi kararla tanımlandığı bir kök izleme meselesidir. Veri sözlüğü bu izi kurar.

## 4. Analiz kodu ve ortam yakalama

Kod tek başına yeterli değildir. Kodun çalıştığı ortam da kaydedilmelidir. R paketleri, Python kütüphaneleri, sürüm numaraları ve işletim sistemi ortamı sonuçları doğrudan etkileyebilir. Aynı kod farklı paket sürümlerinde farklı çıktılar üretebilir ya da hiç çalışmayabilir.

Bu nedenle pakete ortam dosyası eklenir: R için `renv.lock`, Python için `requirements.txt` veya `environment.yml`, Julia için `Project.toml`. Bu dosyalar hesaplamalı ortamı dondurur. İleride aynı ortamı yeniden kurmak mümkün hale gelir.

Noble (2009), hesaplamalı projelerin düzenlenmesine ilişkin kılavuzunda dosya yapısının, betiğin ve ortamın kayıt altına alınmasını temel pratiğin bir parçası olarak ele alır. Her şeyin bir gün yeniden yapılmak zorunda kalabileceğini hatırlatır. Bu yeniden yapma görevini çoğunlukla gelecekteki araştırmacının kendisi üstlenir. Ortam dosyası kaydedilmemişse o görev çok daha ağırlaşır.

Claude Code bu süreçte kodu düzenleyebilir, çalıştırma notu hazırlayabilir, eksik bağımlılıkları tespit edebilir ve yorumları standardize edebilir. Bununla birlikte kodun yöntemsel uygunluğu, analizin araştırma sorusuna doğru yanıt verip vermediği ve yorumun alan bilgisine dayandığı araştırmacı tarafından denetlenmelidir.

## 5. Ek materyal düzeni

Ek materyal, makalenin çöplüğü değildir. Makalede yer almayan ama okura gerekli olduğunda sunulması gereken belgelenmiş bir katmandır.

Bu katmanda neler bulunmalıdır? Ölçek maddeleri ve puanlama kılavuzları, sistematik tarama protokolü ve PRISMA akış şeması, dışlama gerekçe tablosu, ek analizler ve duyarlılık kontrolleri, güç analizi, etik onay belgesi ve arama dizgeleri bunların başında gelir. Her ek dosya kısa bir üst bilgi taşır: dosyanın ne olduğu, ne zaman üretildiği, makalenin hangi bölümüne bağlandığı ve nasıl okunacağı.

Bezjak ve diğerleri (2018), Açık Bilim Eğitim El Kitabı'nda ek materyalin net bir hiyerarşi ve adlandırma düzeniyle sunulmasını önerir. Ek-1, Ek-2 gibi numaralandırma yerine içerik tanımlayıcı dosya adları tercih edilmelidir: `ek-a-olcek-maddeleri.pdf`, `ek-b-prisma-akisi.pdf` gibi. Böylece ek dosya ne içerdiğini adından belli eder.

Piwowar ve Vision (2013), verilerin paylaşılmasının atıf oranlarını artırdığını göstermiştir. Aynı etki büyük olasılıkla eksiksiz ek materyal için de geçerlidir. Paylaşılan belge, araştırmayı denetlenebilir kılar ve denetlenebilir araştırma daha sık atıf alır.

## 6. OSF, Zenodo ve kurumsal arşiv

Platform seçimi araştırmanın yapısına ve hedeflerine göre değişir. OSF, araştırma sürecini kayıt altına almak, ön kayıt yapmak ve proje bileşenlerini düzenli tutmak için kullanışlıdır. Canlı çalışma alanı olarak kullanılabilir. Süreci şeffaf kılmak isteyen araştırmacılar için güçlü bir seçenektir.

Zenodo ise kalıcı DOI ve sürüm arşivleme için öne çıkar. CERN tarafından işletilir, Avrupa Komisyonu'nun Horizon araştırma altyapısıyla entegre çalışır ve ücretsizdir. Her sürüme ayrı bir DOI atandığından hangi verinin veya kodun hangi makalede kullanıldığı kayıt altına alınmış olur. Bu ayrım editoryal dürüstlük ve bilimsel kayıt açısından önemlidir.

Kurumsal arşivler üniversitenin uzun vadeli kayıt sistemine bağlanır. Bazı fon sağlayıcılar belirli bir arşiv kullanımını zorunlu kılar. Birden fazla arşiv aynı anda kullanılabilir. Önemli olan kayıtların birbirine bağlanmasıdır: makale DOI, veri DOI, kod deposu ve ek dosya DOI birbirini işaret etmelidir. Klump ve Huber (2017), yirmi yıllık kalıcı tanımlayıcı tarihini incelerken başarılı sistemlerin teknik üstünlük kadar kurumsal sürdürülebilirlik ve sosyal sözleşme üzerine kurulduğunu gösterir.

## 7. Concept DOI ve version DOI

Zenodo gibi platformlarda iki ayrı DOI türü bulunur. Concept DOI tüm projenin kalıcı kimliğini taşır. Yayın yapıldıkça güncellenir ve her zaman en güncel sürüme yönlendirir. Version DOI ise belirli bir sürümün sabit kimliğini taşır. Bir kez atandıktan sonra değişmez.

Bu ayrım görünürde teknik bir ayrıntı gibi görünebilir. Ama bilimsel kayıt açısından kritiktir. Makale yöntem bölümünde kullanılan sürüm açıkça belirtilmelidir. Aksi halde ileride güncellenen veri veya kod, yayımlanan makaledeki sonuçlarla karışabilir ve bağımsız doğrulama güçleşir.

Fenner ve diğerleri (2019), veri atıf yol haritasında veri depolarının hem kavram hem sürüm düzeyinde atıfı desteklemesini önerir. Bu altyapının araştırmacı tarafından kullanılabilmesi için iki DOI arasındaki farkın anlaşılmış olması gerekir. Makale kaynakçasında her zaman version DOI kullanılmalıdır. Concept DOI ise projenin genel referansı olarak ayrıca verilebilir.

## 8. Lisans seçimi

Lisans, paylaşım ahlakının hukuk dilidir. Kullanıcının ne yapabileceğini, ne yapamayacağını ve hangi koşullarda atıf göndermesi gerektiğini açıklaştırır. Lisanssız paylaşım belirsizlik üretir ve bu belirsizlik çoğu zaman kaynağın kullanılmamasıyla sonuçlanır.

Kod ve düzyazı farklı lisansları hak eder. Kod için MIT veya Apache 2.0 tercih edilir. Bu lisanslar yeniden kullanıma izin verir, türev çalışmaları destekler ve bağımlılık zincirinde sorun yaratmaz. GPL ise kodu kullanan her türevin de aynı lisansla paylaşılmasını zorunlu kılar. Hassas kararların nasıl alındığını projenin başında netleştirmek, ileride uyuşmazlık riskini azaltır.

Düzyazı ve prosedürel metin için Creative Commons lisansları daha uygundur. CC BY atıf yükümlülüğüyle özgür kullanıma açar. CC BY-NC ticari kullanımı sınırlar. CC BY-SA türev çalışmanın aynı lisansla yayımlanmasını gerektirir. Hangi kombinasyonun seçileceği araştırmanın bağlamına, fon sağlayıcı koşuluna ve kurumsal politikaya bağlıdır.

Hassas veya kişisel veri açık lisansla paylaşılmaz. Bu durumda verinin neden açık lisans taşımadığı paket README'sinde belgelenir. Açıklanamaz kısıtlama da bir tür şeffaflıktır.

## 9. FAIR ilkeleri ve README

Wilkinson ve diğerleri (2016), bilimsel veri yönetimi için FAIR ilkelerini ortaya koymuştur. Bulunabilirlik, erişilebilirlik, birlikte çalışabilirlik ve yeniden kullanılabilirlik olarak özetlenen bu ilkeler önce kurumsal depolar ve büyük ölçekli veri altyapıları için geliştirilmiştir. Ama aynı mantık bireysel araştırma paketlerine de uygulanabilir.

Paket README'si FAIR mantığının paket düzeyindeki karşılığıdır. Kapsamlı bir README şu başlıkları içermelidir: projenin amacı ve kapsamı, veri ve kod bileşenlerinin listesi, ortam kurulum adımları, analizin hangi sırayla çalıştırılacağı, lisans bilgileri, katkı beyanı ve iletişim bilgisi. README olmadan en iyi belgelenmiş paket bile yabancı bir araştırmacı için kapalı bir kutu olarak kalır.

Sosyal bilimler için bu gereklilik özellikle anlamlıdır. Nicel analizden nitel yoruma, arşiv çalışmasından deney tasarımına uzanan geniş bir yöntem yelpazesi, paket bileşenlerinin de aynı çeşitlilik içinde hazırlanmasını gerektirir. Tek bir README şablonu her projeye uymayabilir. Ama hangi bileşenin hangi soruya yanıt verdiğini açıklayan bir başlangıç belgesi her projede zorunludur.

## 10. Yayın öncesi kontrol listesi

Paket yayınlanmadan önce şu sorular sorulur. Veri paylaşımı etik kurul kararı ve katılımcı onamıyla uyumlu mu? Paylaşılamayan veri için gerekçe belgesi hazırlandı mı? Veri sözlüğü her değişkeni kapsıyor mu? Kodun temiz ortamda çalıştığı doğrulandı mı? Ek dosyalar makaledeki iddialarla eşleşiyor mu? Concept DOI ile version DOI ayrımı yapıldı mı? Makale kaynakçası version DOI'yi mi gösteriyor? Lisans seçimi kod ve düzyazı için ayrı ayrı yapıldı mı? README paketin bütününü bağımsız bir araştırmacıya anlatabilir durumda mı? Yapay zekâ katkı beyanı pakette yer alıyor mu?

Bu kontrol listesi `/open-science-release-packager` skill'inin çerçevesini oluşturur. Skill paketi hazırlar. Araştırmacı son kararı verir. Etik uygunluk, yöntemsel doğruluk ve atıf bütünlüğü hiçbir araçla devredilemez.

## 11. Skill çıktıları

`/open-science-release-packager` şu çıktıları üretir: README taslağı, veri sözlüğü şablonu, kod kitabı şablonu, analiz yeniden üretim notu, ek materyal dizini, lisans özeti, Zenodo ve OSF hazırlık listesi, concept DOI ile version DOI notu ve yapay zekâ katkı beyanı.

Bu çıktılar araştırmayı gösteriye değil, sürdürülebilir bilimsel kayda bağlar. Bir araştırmacı bu paketi tamamladığında yalnızca bir makale yayımlamış olmaz. Araştırmayı geleceğe taşıyacak bir arşiv bırakmış olur.

## Kaynakça

Atıflar APA 7 biçimindedir. DOI'ler 2026-06-21 tarihinde Crossref ve DataCite üzerinden doğrulanmıştır. Kitzes ve diğerleri (2018) ISBN ile tanımlanmıştır. DOI bulunmamaktadır.

Bezjak, S., Clyburne-Sherin, A., Conzett, P., Fernandes, P., Görögh, E., Helbig, K., Kramer, B., Labastida, I., Niemeyer, K., Psomopoulos, F., Ross-Hellauer, T., Schneider, R., Tennant, J., Verbakel, E., Brinken, H., & Heller, L. (2018). *Open science training handbook*. FOSTER/Zenodo. https://doi.org/10.5281/zenodo.1212496

Fenner, M., Crosas, M., Grethe, J. S., Kennedy, D., Hermjakob, H., Rocca-Serra, P., Durand, G., Berjon, R., Karcher, S., Martone, M., & Clark, T. (2019). A data citation roadmap for scholarly data repositories. *Scientific Data*, *6*, Article 28. https://doi.org/10.1038/s41597-019-0031-8

Kitzes, J., Turek, D., & Deniz, F. (Eds.). (2018). *The practice of reproducible research: Case studies and lessons from the data-intensive sciences*. University of California Press. ISBN 978-0-520-29673-3

Klump, J., & Huber, R. (2017). 20 years of persistent identifiers: Which systems are here to stay? *Data Science Journal*, *16*, Article 9. https://doi.org/10.5334/dsj-2017-009

Noble, W. S. (2009). A quick guide to organizing computational biology projects. *PLoS Computational Biology*, *5*(7), e1000424. https://doi.org/10.1371/journal.pcbi.1000424

Nosek, B. A., Alter, G., Banks, G. C., Borsboom, D., Bowman, S. D., Breckler, S. J., Buck, S., Chambers, C. D., Chin, G., Christensen, G., Contestabile, M., Dafoe, A., Eich, E., Freese, J., Glennerster, R., Goroff, D., Green, D. P., Hesse, B., Humphreys, M., … Yarkoni, T. (2015). Promoting an open research culture. *Science*, *348*(6242), 1422–1425. https://doi.org/10.1126/science.aab2374

Piwowar, H. A., & Vision, T. J. (2013). Data reuse and the open data citation advantage. *PeerJ*, *1*, e175. https://doi.org/10.7717/peerj.175

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, *9*(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.-W., da Silva Santos, L. B., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., … Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, *3*, Article 160018. https://doi.org/10.1038/sdata.2016.18

---

**Kitapçık kimliği.** `003-04-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1632 (Türkçe gövde metni)
**Doğrulanmış atıf sayısı.** 9
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`003-03-0001`](../003-03-0001/tr.md). Kaynak Pasaportu, Kaynakları Oturumlar Arasında İzlemek
**Sonraki kitapçık.** [`004-01-0001`](../../004-vault-architecture/004-01-0001/tr.md). Klasör Disiplini ve Maps of Content (MOC) Kalıbı
