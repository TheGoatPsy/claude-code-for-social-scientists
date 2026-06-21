---
title_en: "Rebuttal Letters with Traceability Matrices"
title_tr: "İzlenebilirlik Matrisleri ile Hakem Yanıt Mektupları"
booklet_id: "010-01-0001"
category: "010-peer-review"
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
    role: "drafting, verification, citation lookup"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 8
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# İzlenebilirlik Matrisleri ile Hakem Yanıt Mektupları

## Giriş

Önceki kitapçık, etik çerçeveyi araştırmanın başında kurulan bir iş akışı belgesi olarak tanımlamıştı. Bu kitapçık, o çerçevenin sınandığı en kritik anlardan birine geçer: hakem yanıt mektubu. Yanıt mektubu, akademik üretimde sonucu en doğrudan etkileyen metin türlerinden biridir. İlk gönderimdeki emek çoğu zaman bu metinde sınanır. Atlanan bir yorum, gerekçesiz bir kısmi yanıt ya da karşılıksız bırakılan bir çelişki, ikinci turda reddi kolaylaştırabilir.

Bu kitapçığın temel iddiası şudur. Hakem yanıtı yalnızca iyi niyetli bir açıklama metni değildir. İzlenebilir, denetlenebilir ve editörün işini kolaylaştıracak biçimde yapılandırılması gereken bir revizyon belgesidir. İzlenebilirlik matrisi, her hakem yorumunu, verilen yanıtı ve makalede yapılan değişikliği tek bir satırda birleştirerek bu yapıyı kurar. Claude Code bu süreçte biçimi, ayrıştırmayı ve tutarlılık denetimini destekleyebilir. Yanıtın bilimsel içeriği ise araştırmacının sorumluluğunda kalır.

## 1. Hakem Yanıt Mektubunun Yapısı

Hakem yanıt mektubu birkaç temel bileşenden oluşur. Editöre yönelik açılış, revizyona teşekkür eder, ana değişiklikleri özetler ve mektubun nasıl okunacağını belirtir. Ardından hakem yorumları tek tek ele alınır. Her yorum görünür biçimde aktarılır, hemen altında yazarın yanıtı verilir ve makalede yapılan değişikliğin konumu sayfa, satır ya da bölüm düzeyinde gösterilir. Mektup, açık kalan noktaların dürüst biçimde belirtilmesiyle tamamlanır.

Bu yapı, ilk bakışta basit görünür. Ancak pratikte ciddi bir disiplin gerektirir. Provenzale ve Stanley, hakem yorumlarının yöntem, kuramsal çerçeve, biçim, yorum ve kanıt gibi farklı kategorilere ayrılabileceğini gösterir. Her kategori aynı tür yanıtı gerektirmez. Yöntemsel bir itiraz, yalnızca cümle sıkıştırma talebiyle aynı düzeyde ele alınamaz. Noble'ın hakemlere yanıt yazmaya ilişkin kuralları da aynı noktayı vurgular: her yoruma açıkça, ayrı ayrı ve izlenebilir biçimde yanıt verilmelidir.

Birden fazla yorumu tek yanıt altında eritmek ya da küçük görünen bir yorumu atlamak, editörde revizyonun eksik olduğu izlenimini yaratabilir. Bu izlenim ikinci turda kolay düzelmez. Belcher'ın akademik yayın sürecine ilişkin yaklaşımı da revizyon aşamasını makalenin kaderini belirleyen temel aşamalardan biri olarak konumlandırır. Bordage'ın hakem ret gerekçelerine ilişkin çalışması, önceki eleştirilere yetersiz yanıtın tekrar eden bir sorun olduğunu gösterir. Bu nedenle yanıt mektubu, savunma refleksiyle değil, belge disipliniyle yazılmalıdır.

## 2. İzlenebilirlik Matrisi Nedir?

İzlenebilirlik matrisi, her hakem yorumunu, o yoruma verilen yanıtı ve makalede yapılan değişikliği aynı yapıda bir araya getiren tablodur. Matrisin amacı, yazarın hiçbir yorumu atlamadığını ve her değişikliğin izlenebilir olduğunu göstermektir. Editör bu matrise baktığında hangi yorumun nasıl ele alındığını tek bakışta görebilmelidir.

Matrisin gerekliliği revizyonun aritmetiğinden doğar. Bir makale çoğu zaman iki ya da üç hakemden değerlendirme alır. Her hakemin beş ila on yorumu olduğunda, yazarın yanıtlaması gereken yorum sayısı kolayca yirmi ya da otuza ulaşabilir. Yapılandırılmamış bir düz yazı içinde bazı yorumların gözden kaçması olağandır. Bu ihmal çoğu zaman kötü niyetten değil, karmaşık bir hakem diyaloğunu düz yazıyla takip etmenin güçlüğünden doğar.

Matris bu sorunu yapısal olarak azaltır. Her yorum bir satırdır. Her satırın bir yanıtı, bir değişiklik kaydı ve bir karar kategorisi olmalıdır. Bu düzen kabul garantisi vermez. Ancak önlenebilir bir başarısızlık biçimini ortadan kaldırır: yanıtsız kalan ya da görünmez hâle gelen yorum.

## 3. Claude Code ile Matris Oluşturma

İzlenebilirlik matrisi Claude Code ile yarı otomatik kurulabilir. Hakem raporları önce arşive düz metin olarak alınır. Ardından her yorum hakem kimliği, yorumun yeri, yorumun özeti ve gerekiyorsa ilgili makale bölümüyle birlikte ayrı bir satır hâline getirilir. Model, uzun hakem raporlarını ayrıştırma ve tekrar eden biçimsel yapıları düzenleme konusunda yararlı olabilir.

Burada sınır açık tutulmalıdır. Claude Code matrisin yapısını, yorumların ayrıştırılmasını, dilbilgisel düzeni ve tutarlılık denetimini destekler. Ancak yanıtın özünü, hangi değişikliğin yapılacağını, hangi eleştirinin kabul edileceğini, hangi itirazın bilimsel gerekçeyle reddedileceğini yazar belirler. Hosseini ve diğerleri, bilimsel yayınlarda yapay zekâ kullanımını tartışırken biçim desteği ile içerik üretimi arasındaki ayrımın bulanıklaştırılmaması gerektiğini vurgular. Hakem yanıt mektubunda bu ayrım özellikle önemlidir.

İyi işleyen bir süreçte Claude Code şu işleri üstlenebilir: hakem yorumlarını numaralandırmak, yorumları kategoriye ayırmak, yanıtların eksik olduğu satırları işaretlemek, sayfa ve satır bilgilerini standart biçime getirmek, kısmi kabul ve ret kararlarını görünür kılmak. Yazarın işi ise her satırdaki bilimsel cevabı kurmak ve makaledeki gerçek değişikliği yapmaktır.

## 4. Yapay Zekâ İzinin Etik Tartışması

Yapay zekâ yardımıyla hazırlanmış revizyon metinlerinde iki ayrı soru birbirine karıştırılmamalıdır. Birinci soru üslup sorusudur. Metin yapay zekâ destekli bir taslakla başladıysa, yazar bu metni kendi akademik sesine ve derginin üslubuna göre yeniden kurabilir. Bu meşru bir editoryal işlemdir. İkinci soru katkı sorusudur. Yapay zekâ metnin hangi aşamasında, hangi amaçla ve hangi düzeyde kullanıldı? Bu soru beyan alanına aittir.

Else, yapay zekâ tarafından yazılmış özetlerin deneyimli bilim insanlarını bile yanıltabildiğini gösterdiğinde, sorun yalnızca metnin yapay zekâ izi taşıyıp taşımaması değildi. Asıl sorun, metnin nasıl üretildiğinin okura açıkça söylenmemesiydi. Bu nedenle bütünlük, yapay zekâ izinin görünür olup olmamasından çok katkının şeffaf biçimde beyan edilmesine bağlıdır.

Bu kitapçığın yaklaşımı nettir. Üslup yazarın alanıdır. Yazar metni yeniden kurabilir, yapay zekâya özgü mekanik tekrarları azaltabilir, cümleleri kendi akademik sesine uygun hâle getirebilir. Ancak yapay zekâ katkısını saklayamaz. Beyan korunuyorsa üslup bakımı meşrudur. Beyan kaldırılıyorsa mesele artık üslup değil, okuru yanıltmadır.

## 5. Örnek Bir R&R Matrisinin Kurulması

Aşağıdaki örnek, gerçek bir hakem değerlendirmesinden değil, sosyal kaygı üzerine varsayımsal bir çalışmadan türetilmiş sentetik bir senaryodur. Amaç matris mantığını göstermektir.

| No | Hakem | Yorum | Yapılan işlem | Konum ve durum |
|---|---|---|---|---|
| 1 | H1 | Örneklem küçük | Sınırlamalara eklendi, ek güç analizi raporlandı | s.18, s.5-12, kabul |
| 2 | H1 | Ölçek geçerliği belirsiz | Cronbach alfa ve önceki geçerlik çalışmaları eklendi | s.9, s.15, kabul |
| 3 | H1 | Analiz yöntemi gerekçesiz | Yöntem seçimi kuramsal ve istatistiksel gerekçeyle açıklandı | s.11, s.1-8, kabul |
| 4 | H2 | Kuramsal çerçeve dağınık | Yeni alt bölüm yazıldı, kavram sırası yeniden düzenlendi | s.5-7, yeniden yazım |
| 5 | H2 | Bulgular abartılı | İddialar bulgu düzeyiyle uyumlu hâle getirildi | s.13-14, kabul |
| 6 | H2 | Sınırlamalar yetersiz | Üç yeni sınırlama eklendi | s.19, s.3-18, kabul |
| 7 | H2 | Başlık yanıltıcı | Hakemin kaygısı kabul edildi, başlık kısmen düzenlendi | s.1, kısmi |
| 8 | H1 | Bir kaynak eski | Kaynak güncel literatürle desteklendi | s.8, s.5, kabul |

Bu matris, sekiz yorumun hiçbirinin atlanmadığını gösterir. Kategori sütunu özellikle önemlidir. Kabul edilen yorumlar revizyonun kapsamını, kısmi kabul edilen yorumlar ise ek gerekçe gerektiren alanları gösterir. Editörün dikkati çoğu zaman tam da bu kısmi ya da reddedilen satırlara yönelir. Bu nedenle her kısmi yanıt, mektupta ayrıca açık ve kanıta dayalı biçimde gerekçelendirilmelidir.

## 6. Hakem Yanlış Olduğunda

Her hakem yorumu doğru değildir. Bazı yorumlar makalenin yanlış okunmasından, bazıları kapsam dışı beklentilerden, bazıları da hakemler arasındaki çelişkilerden doğar. Buna rağmen hiçbir yorum sessizce geçiştirilmemelidir. Yazar bir öneriyi uygulamayacaksa bunu açıkça, saygılı biçimde ve bilimsel gerekçeyle belirtmelidir.

Yanıtın odağı hakemin kişisi değil, bilimsel gerekçe olmalıdır. Doğru yaklaşım "hakem yanılıyor" demek değildir. Doğru yaklaşım, literatürün, yöntemsel sınırlılığın ya da çalışmanın kapsamının neden farklı bir çözümü gerektirdiğini göstermektir. Williams ve Bizup'ın açıklık ve argümantasyon üzerine yazdıkları ilke burada da geçerlidir. Bir argümanın gücü sertliğinde değil, kanıtında yatar.

İki hakem doğrudan çelişen taleplerde bulunuyorsa ya da bir yorum makalenin temel tasarımıyla çözülemeyen bir çatışma yaratıyorsa editöre kısa ve açık bir not düşülmelidir. Bu, sorumluluğu editöre bırakmak değildir. Çelişkiyi görünür kılmak ve editoryal yönlendirme istemektir.

## 7. Editör ile Etkili İletişim

Editör, hakemlerle yazar arasında yer alır. Bu nedenle yanıt mektubuna eşlik eden kısa bir editör notu, sürecin akışını kolaylaştırır. Bu not üç ya da dört cümleyi geçmemelidir. Ana değişiklikleri özetler, hakemler arası çelişki varsa işaret eder ve ayrıntılı matrisin nasıl okunacağını belirtir.

Sword, üretken akademisyenlerin yazma pratiklerinde netlik ve doğrudanlığın önemli bir rol oynadığını gösterir. Editöre yazılan not, bu netliğin yoğun bir örneğidir. Not savunma metni değildir. Editöre bir harita sunar. Editör bu nottan şunu anlayabilmelidir: yazar revizyonu ciddiye almıştır, ana kaygılar ele alınmıştır ve ayrıntılı matris dikkatle okunmayı hak etmektedir.

## 8. Etik Sınırlar ve Beyan

Hakem yanıt sürecinde yapay zekâ yardımı kullanıldıysa bu kullanım açıkça beyan edilmelidir. Beyan, yapay zekânın sürecin neresinde yer aldığını somut olarak göstermelidir.

Bu yanıt mektubunun yapılandırılmasında yapay zekâ destekli bir araç kullanılmıştır. Araç, izlenebilirlik matrisinin biçimlendirilmesini ve metnin dilbilgisel düzenlemesini desteklemiştir. Hakem yorumlarına verilen bilimsel yanıtların özü, eklenen argümanlar ve nihai kararlar yazarlar tarafından oluşturulmuştur. Yapay zekâ kullanımı yazarlık iddiası oluşturmaz.

| Durum | Beyan |
|---|---|
| Dilbilgisi ve biçim düzenleme | Beyan edilir |
| Matris formatının oluşturulması | Beyan edilir |
| Analitik yanıtın özü | Yazarın üretimidir. Yapay zekâ bilimsel karar sahibi değildir |
| Bilimsel argümanın geliştirilmesi | Yazarın sorumluluğundadır |
| Kaynak doğrulama desteği | Yapay zekâ destekli yapıldıysa beyan edilir |

Bu beyan, yalnızca varlığıyla değil, somutluğu ile anlam taşır. Okur, yapay zekânın ne yaptığını ve ne yapmadığını açıkça görebilmelidir. Böyle bir beyan mektubu zayıflatmaz. Aksine yazarın bütünlük disiplinini görünür kılar.

## 9. Yanıt Süre Yönetimi

Revizyon daveti çoğu zaman otuz, altmış ya da doksan günlük sürelerle gelir. Bu süre baştan bir plana bağlanmazsa hızla tükenir. Doksan günlük bir planda ilk bölüm hakem raporlarının okunmasına, yorumların matrise işlenmesine ve büyük yapısal değişikliklerin belirlenmesine ayrılabilir. Orta bölümde makale üzerinde değişiklikler yapılır ve her satır için yanıt metni yazılır. Son bölümde matris tamamlanır, revize metin bütünlük okumasından geçirilir ve editör notu hazırlanır.

Daha kısa sürelerde plan sıkışır, ancak matris mantığı değişmez. Revizyon süresinin her günü matristeki görünür bir satıra bağlanmalıdır. Sürenin ortasında tamamlanmış satır oranına bakmak, ilerlemenin hissinden daha değerlidir. Yazar kaç yorumun kapandığını, kaçının açık kaldığını ve hangi yorumların ek analiz gerektirdiğini somut biçimde görür.

## 10. Köprü, Sorun Giderme Protokolüne

Hakem yanıt mektubu hazırlanırken iş akışı bozulabilir. Bir komut beklenmedik sonuç verebilir, bir dosya yanlış sürümle açılabilir, bağlam sınırı aşılabilir ya da model bir yorumu yanlış ayrıştırabilir. Bu nedenle revizyon sürecinde sorun giderme protokolü gerekir.

Bir sonraki kitapçık, işler ters gittiğinde panik yerine yöntemle ilerleyen bir sorun giderme çerçevesi kurar. Hakem yanıt mektubu, arşiv, atıf doğrulama ve yapay zekâ beyanı aynı anda çalıştığında, sistematik sorun giderme araştırmacının en önemli güvencelerinden biridir.

## Kaynakça

Atıflar APA 7 biçimindedir. DOI'ler 2026-06-21 tarihinde Crossref üzerinden doğrulanmıştır.

Belcher, W. L. (2019). *Writing your journal article in twelve weeks: A guide to academic publishing success* (2nd ed.). University of Chicago Press. ISBN 978-0-226-49991-8

Bordage, G. (2001). Reasons reviewers reject and accept manuscripts: The strengths and weaknesses in medical education reports. *Academic Medicine*, *76*(9), 889–896. https://doi.org/10.1097/00001888-200109000-00010

Else, H. (2023). Abstracts written by ChatGPT fool scientists. *Nature*, *613*(7944), 423. https://doi.org/10.1038/d41586-023-00056-7

Hosseini, M., Rasmussen, L. M., & Resnik, D. B. (2023). Using AI to write scholarly publications. *Accountability in Research*, *31*(7), 715–723. https://doi.org/10.1080/08989621.2023.2168535

Noble, W. S. (2017). Ten simple rules for writing a response to reviewers. *PLOS Computational Biology*, *13*(10), e1005730. https://doi.org/10.1371/journal.pcbi.1005730

Provenzale, J. M., & Stanley, R. J. (2005). A systematic guide to reviewing a manuscript. *American Journal of Roentgenology*, *185*(4), 848–854. https://doi.org/10.2214/AJR.05.0782

Sword, H. (2017). *Air & light & time & space: How successful academics write*. Harvard University Press. https://doi.org/10.4159/9780674977617

Williams, J. M., & Bizup, J. (2016). *Style: Lessons in clarity and grace* (12th ed.). Pearson. ISBN 978-0-13-408041-3

---

**Kitapçık kimliği.** `010-01-0001`
**Sürüm.** `0.2.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1616 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 8
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`009-01-0001`](../../009-ethics-irb/009-01-0001/tr.md). Yapay Zekâ Destekli Araştırmada Etik, İlkeden Davranışa
**Sonraki kitapçık.** [`012-01-0001`](../../012-troubleshooting/012-01-0001/tr.md). İşler Ters Gittiğinde, Çalışan Bir Sorun Giderme Protokolü
