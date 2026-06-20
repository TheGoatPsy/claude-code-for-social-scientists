---
title_en: "Rebuttal Letters with Traceability Matrices"
title_tr: "İzlenebilirlik Matrisleri ile Hakem Yanıt Mektupları"
booklet_id: "010-01-0001"
category: "010-peer-review"
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
    role: "drafting, verification, citation lookup"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-20"
verified_citations_count: 8
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# İzlenebilirlik Matrisleri ile Hakem Yanıt Mektupları

Önceki kitapçık, etik çerçeveyi baştan kurulan bir iş akışı belgesi olarak tanımlamıştı. Bu kitapçık, o çerçevenin sınandığı en kritik ana geçer: hakem yanıt mektubuna. Yanıt mektubu, profesyonel akademik üretimin en yüksek bahisli metin türüdür. Tek bir yapısal hata kapıyı ikinci kez kapatabilir: atlanan bir yorum, gerekçesiz kısmi yanıt ya da karşılıksız bırakılmış bir çelişki. Yapılandırılmamış bir mektup çoğunlukla tam buradan kırılır ve ikinci bir redde açılan yolu genişletir. Bir izlenebilirlik matrisi ise her yorumu görünür, her yanıtı izlenebilir kılarak bu riski yönetir. Buradaki amaç, Claude Code ile bu matrisi yarı otomatik kuran ve yapay zekâ beyan etiğini koruyan bir iş akışını göstermektir.

## 1. Hakem Yanıt Mektubunun Yapısı

Hakem yanıt mektubunun bileşenleri birbirini zorunlu olarak önceler. Editöre yönelik açılış, revizyona teşekkür cümlesini, ana değişikliklerin kısa özetini ve mektubun yapısına tek satırlık bir yönelimi barındırır. Ardından her hakem yorumuna tek tek yanıt verilir: önce yorumun kendisi, hemen altında yazarın yanıtı, sonra makalede yapılan değişikliğin tam konumu. Değişiklikler sayfa ve satır düzeyinde açıkça işaretlenir. Mektup, kalan açık noktaların dürüst bir kabulüyle kapanır.

Bu yapı, araştırmacıların çoğunun ilk revizyona getirmediği bir disiplin ister. Provenzale ve Stanley (2005), el yazması değerlendirmenin sistematik kılavuzunda, hakem yorumlarının belirlenebilir kategorilere ayrıldığını ortaya koyar. Bir yorum yönteme ilişkin olabilir, bir diğeri kavramsal çerçeveye, bir başkası biçime. Her yanıtın tonu ve ağırlığı, hitap ettiği kategoriye uygun olmalıdır. Yöntemsel bir itiraz, bir paragrafı sıkıştırma talebinden farklı bir argümantasyon gerektirir. Noble (2017), hakemlere yanıt yazmanın on kuralında en kritik olanını doğrudan söyler: her yoruma açıkça ve ayrı ayrı yanıt vermek. İki yorumu tek yanıtta birleştirmek ya da önemsiz göründüğü için birini atlamak, editörde revizyonun eksik olduğu izlenimini yaratır. Bu izlenim ikinci turda nadiren düzeltilir. Belcher (2019), akademik yayın sürecini on iki haftalık bir yapıya oturttuğu rehberinde, revizyonun makalenin kaderini belirleyen aşama olduğunu açıkça koyar. İlk gönderim değil, revizyon. Bordage (2001), hakemlerin makaleleri neden reddedip kabul ettiğini inceleyen sistematik çalışmasında, önceki eleştirilere yetersiz yanıtı tekrarlayan bir red gerekçesi olarak saptamıştır.

## 2. İzlenebilirlik Matrisi Nedir

Bir izlenebilirlik matrisi, her hakem yorumunu, ona verilen yanıtı ve makalede yapılan değişikliği tek bir tabloda birbirine bağlayan yapıdır. Matris, yazarın hiçbir yorumu atlamadığını ve her değişikliğin izlenebilir olduğunu kanıtlar. Bir editör matrise baktığında, hangi yorumun nasıl ele alındığını tek bakışta görür.

Matrisin gerekliliği, revizyonun aritmetiğinden doğrudan çıkar. Bir makale çoğunlukla iki ya da üç hakemden, her birinde beş ila on yorum barındıran değerlendirmeler alır. Bu, on beş ila otuz ayrı yoruma yanıt vermek demektir. Yapılandırılmamış bir mektupta o yorumların bir kısmı kaçar. İhmalden değil, karmaşık ve çok hakemli bir diyalogu yalnızca düz yazıyla takip etmenin güçlüğünden. Matris bu kaçışı yapısal olarak olanaksız kılar: her yorum bir satırdır ve her satırın bir yanıtı olmak zorundadır. Matris, kabulün garantisi değildir. Önlenebilir bir başarısızlık biçimini ortadan kaldıran bir düzen aracıdır. Kapsamlı bir yanıtın editoryal kararı etkileyip etkilemeyeceği, araştırmacının kendi değerlendirmesiyle yapacağı bir yargıdır. Matrisin sağladığı, en azından yanıtın eksiksiz ve okunabilir olmasıdır.

## 3. Claude Code ile Bir Matris Oluşturma

Bir izlenebilirlik matrisi, Claude Code ile yarı otomatik kurulabilir. İş akışı birkaç aşamada ilerler. Hakem raporları önce arşive düz metin olarak alınır. Ardından her yorum, hakem kimliği ve yorumun makaledeki konumuyla birlikte ayrı bir satır olarak çıkarılır. Model bu çıkarma işlemini destekler: uzun bir hakem raporunu ayrı ve ayrıştırılmış yorumlara böler. Bu işlem, hakemlerin tamamı için tek başına yapılsaydı saatlerce sürerdi. Yazar daha sonra her satıra kendi yanıtını ve planlanan değişikliği ekler.

Burada kesin olarak belirtilmesi gereken kritik bir sınır vardır. Model, matrisin yapısını ve dilbilgisel düzenini destekler. Yanıtın özünü, ne yanıt verileceğini, karşı argümanın nasıl kurulacağını, hangi değişikliğin yapılacağını, yazar üretir. Bu karar her zaman ve yalnızca araştırmacıya aittir. Hosseini ve diğerleri (2023), bilimsel yayınlarda yapay zekâ kullanımını incelerken, aracın metnin biçimini düzenlemesi ile metnin içeriğini üretmesi arasındaki ayrımın belirsizleşmeden korunması gerektiğini vurgular. İzlenebilirlik matrisinde bu ayrım sürecin içine işlenmiştir: biçim modelin desteğiyle, içerik yazarın kalemiyle.

## 4. Yapay Zekâ İzinin Etik Tartışması

Yapay zekâ yardımıyla yazılan metinlerin izini gizleme tartışması, dikkatli bir ayrım gerektiriyor. Bu ayrım kolayca yanlış okunur. Yapay zekâ desteğiyle şekillenen bir metin ile yapay zekânın doğrudan ürettiği bir metin aynı eşikte değerlendirilemez. Aralarında kökten bir mesafe vardır. Bir araştırmacının kendi analizini bu destekle daha açık ifade etmesi meşru bir pratiğin içindedir. Yapay zekânın ürettiği içeriği ise kendi entelektüel çıktısı gibi sunmak ayrı bir soruyu doğurur: katkı kime aittir?

Bu ayrım, "anti-yapay-zekâ-izi yazımı" kavramının neden etik açıdan çetrefilli bir alan olduğunu açıklar. Else (2023), yapay zekâ tarafından yazılan özetlerin deneyimli bilim insanlarını bile yanıltabildiğini gösterdiğinde, ortaya çıkan sorun izin görünmezliği değildi. Beyan eksikliğiydi. Bir metnin yapay zekâ izi taşıyıp taşımaması ikincil bir sorudur. Birincil soru şudur: yapay zekâ katkısı beyan edilmiş mi? Bu kitapçığın amacı beyan zorunluluğunu korumaktır. Yapay zekâ yardımının bir revizyon iş akışında dürüstçe nasıl belirtileceğini gösterir. Bütünlük, izin görünürlüğünde değil, katkının şeffaflığındadır.

## 5. Örnek Bir R&R'dan Matris Geliştirme

Somut bir örnek kalıbı netleştirir. Aşağıdaki matris sentetik bir senaryodan türetilmiştir, gerçek bir hakem değerlendirmesinden değil. Bir sosyal kaygı çalışmasının iki hakemden aldığı varsayımsal yorumlar üzerine kurulmuştur.

| # | Hakem | Yer | Yorum (özet) | Yanıt | Değişiklik | Kategori |
|---|---|---|---|---|---|---|
| 1 | H1 | s.4 s.12 | Örneklem küçük | Sınırlamalara eklendi, güç analizi yapıldı | s.18 s.5-12 | Kabul |
| 2 | H1 | s.7 s.3 | Ölçek geçerliği belirsiz | Cronbach alfa eklendi | s.9 s.15 | Kabul |
| 3 | H1 | s.10 s.20 | Analiz yöntemi gerekçesiz | Yöntem seçimi gerekçelendirildi | s.11 s.1-8 | Kabul |
| 4 | H2 | genel | Kuramsal çerçeve dağınık | Yeni alt bölüm 2.1 yazıldı | s.5-7 | Yeniden yazım |
| 5 | H2 | s.13 s.4 | Bulgular abartılı | İddialar ölçüldü, dil yumuşatıldı | s.13-14 | Kabul |
| 6 | H2 | s.16 s.9 | Sınırlamalar yetersiz | Üç yeni sınırlama eklendi | s.19 s.3-18 | Kabul |
| 7 | H2 | s.2 s.1 | Başlık yanıltıcı | Hakemin önerisi tartışıldı, kısmen uygulandı | s.1 | Kısmi |
| 8 | H1 | s.8 s.5 | Bir kaynak eski | Kaynak güncel literatürle desteklendi | s.8 s.5 | Kabul |

Bu matris, yazarın sekiz yorumun hiçbirini atlamadığını kanıtlar. Her satır, editöre yanıtın izlenebilir bir kaydını sunar. Kategori sütunu yorumların ne ölçüde kabul edildiğini özetler ve kısmi ya da reddedilen yanıtlar için eşlik eden mektupta ayrı bir gerekçe gerektiğini işaret eder.

Kategori sütunu aynı zamanda editörün eleme aracıdır. Bir editör matrise baktığında, kabul edilen yorumların çoğunlukta olduğunu görür ve revizyonun ciddiyetine güvenir. Asıl dikkat, kısmi ve reddedilen satırlara döner. Tam da dönmesi gereken yer orası. Yukarıdaki yedinci satır, başlık önerisinin kısmen uygulandığı bir kısmi kabuldür. Yazar burada açıkça yazmalıdır: hakemin kaygısı neden tam karşılanmadı ve bunun yerine hangi orta yol bulundu? Kısmi bir kabul geçiştirilirse ikinci turda yeniden masaya gelir. Açık ve kanıta dayalı bir gerekçeyle sunulursa editör çoğunlukla yazarın tarafını tutar. Matris bu kritik satırları görünür kılar. Yazarın görevi, onlara hak ettikleri ağırlığı vermektir.

## 6. "Hakem Yanlış" Protokolü

Her hakem yorumu doğru ya da uygulanabilir değildir. Bir yorum makalenin yanlış okunmasından kaynaklanıyor olabilir. Bir diğeri belirtilen kapsamın dışına düşebilir. Zaman zaman iki hakem birbirine doğrudan karşıt değişiklikler talep eder. Bu durumların her birinin bir protokolü vardır.

Temel kural nettir: hiçbir yorum yanıtsız geçiştirilmez. Yazar bir yorumu uygulamayacaksa, bu kararı açıkça ve gerekçesiyle belirtmek zorundadır. Gerekçe, hakemin güvenilirliğine değil, bilimsel argümana dayanmalıdır. Doğru formülasyon şudur: "Bu noktada literatür şu konumu önermektedir." Tonun ötesinde, bu yapısal bir tercih meselesidir. Williams ve Bizup (2016), açıklık ve argümantasyon üzerine yazım derslerinde genel bir ilke olarak şunu koyar: bir argümanın gücü, ne kadar kararlı söylendiğinde değil, kanıtında yatar. Bu ilke, okuyucunun zaten kuşkuya yatkın olduğu bir yanıt bağlamında özellikle geçerlidir. Hakem yanlış olduğunda bile yanıt saygılı ve kanıta dayalı kalır.

Editöre yükseltme eşiği şudur: iki hakem birbiriyle doğrudan çeliştiğinde ya da bir yorum makalenin temel tasarımıyla çözülemez bir çatışma yarattığında, yazar editöre doğrudan ve kısa bir not yazarak çatışmayı işaret eder ve yönlendirme ister. Bunu yalnız çözmeye çalışıp editörün fark etmemesini ummak yerine bu yola gitmek hem daha güvenli hem de daha mesleki bir tavırdır.

## 7. Editör ile Etkili İletişim

Editör, hakem ile yazar arasında durur. Bu konum ayrı bir iletişim stratejisi gerektirir. Yanıt mektubuna eşlik eden kısa bir editör notu, sürecin akışını önemli ölçüde kolaylaştırır. Bu not üç ya da dört cümlede ana değişiklikleri özetler, varsa hakemler arası çelişkileri işaret eder ve editörü ayrıntılı matrise girmeden önce yönlendirir. Editör, yalnızca bu nottan genel tabloyu çıkarabilmelidir: hangi ana kaygılar karşılandı, hangilerinde kısmi yanıt verildi, gerçek anlamda açık kalan nokta var mı?

Sword (2017), başarılı akademisyenlerin nasıl yazdığını incelediği görgül çalışmasında, mesleki iletişimde netlik ve doğrudanlığı, üretken akademik pratiği diğerlerinden tutarlı biçimde ayıran özellikler olarak saptar. Editöre yazılan not, bu netliğin en yoğun sınavıdır. Not bir savunma değil, bir harita sunar. İyi bir harita uzun olmak zorunda değildir. Editör bu nottan şunu anlar: yazar revizyonu ciddiye almıştır, süreç kontrol altındadır ve arkasından gelen matris dikkatle okunmayı hak etmektedir.

## 8. Etik Sınırlar ve Beyan

Yapay zekâ yardımının beyanı, hakem yanıt sürecinde de zorunludur. Hangi katkının açıklanacağı aşağıdaki tabloda netleşir.

| Durum | Beyan |
|---|---|
| Dilbilgisi ve biçim düzenleme | Beyan edilir |
| Matris formatının oluşturulması | Beyan edilir |
| Analitik yanıtın özü | Yazarın üretimi. Yapay zekâ katkısı olmadığından beyan gerektirmez |
| Bilimsel argümanın geliştirilmesi | Yazarın sorumluluğu |
| Kaynak doğrulama | Yapay zekâ destekli. Beyan edilir |

Bir yanıt mektubunda yapay zekâ kullanımı, bir beyan cümlesiyle belirtilir. Aşağıdaki örnek sentetik bir beyan metnidir.

> Bu yanıt mektubunun yapılandırılmasında bir yapay zekâ destekli araç kullanılmıştır. Araç, izlenebilirlik matrisinin formatını ve düz yazının dilbilgisel düzenlemesini destekledi. Tüm analitik içerik, hakem yorumlarına verilen yanıtların özü ve eklenen bilimsel argümanlar, yazarlar tarafından kaleme alınmıştır. Yapay zekâ kullanımı yazarlık iddiasını oluşturmaz.

Bu beyan, Yayın Etiği Komitesi ve Uluslararası Tıp Dergisi Editörleri Komitesi'nin yapay zekâ konumlarıyla uyumludur. Bir beyan, ancak neyin beyan edildiği somutsa anlam taşır. Okur, yapay zekânın yanıt mektubunda nasıl ve hangi biçimlerde kullanıldığını açıkça görebilmelidir. Beyan mektubu zayıflatmaz. Aksine yazarın bütünlüğünü gösterir. Yapay zekâ kullanımına giderek daha dikkatli bakan bir editöryel ortamda bu sinyal ağırlık taşır.

## 9. Yanıt Süre Yönetimi

Bir revizyon daveti çoğunlukla bir süre sınırıyla gelir: otuz, altmış ya da doksan gün. Başından bir plana bağlanmazsa bu süre hızla tükenir. Doksan günlük bir planın ilk dilimi hakem raporlarını bütünüyle okumaya, izlenebilirlik matrisine tüm yorumları işlemeye ve büyük yapısal değişiklikleri planlamaya ayrılır. Bu aşamada hangi bölümlerin yeniden yazılacağı, yeni bir analiz gerekip gerekmediği ve literatürde açık kalan boşlukların neler olduğu netleşir. Orta dilimde uygulama başlar: değişiklikler makaleye işlenir, her satır için yanıt metni yazılır. Kapanış dilimi matrisi tamamlar, revize edilmiş metnin özgün hakem kaygılarına karşı bir bütünlük okumasından geçirilmesini sağlar ve editör notunu hazırlar.

Daha kısa sürelerde plan orantılı olarak sıkışır. Ne var ki matris mantığı değişmez. Önemli olan, revizyon süresinin her gününün matristeki görünür bir satıra bağlanmasıdır. Sürenin ortasında tamamlanmış satır oranına bakan bir yazar, ilerlemenin kaba bir hissinden daha değerli bir şeye sahiptir: kaç satır kaldığının gerçekçi bir sayımına. Bu sayım, kalan zamana nereden bakılacağına dair iyi kararlar almanın tek gerçek zeminidir.

## 10. Köprü, Sorun Giderme Protokolüne

Hakem yanıt mektubu hazırlanırken Claude Code akarken işler ters gidebilir. Bir komut beklenmedik bir sonuç verebilir. Bir dosya bozulabilir. Bir model yanıtı bağlam sınırına takılabilir. Bir sonraki kitapçık, sorun giderme protokolünü doğrudan ele alır. İşler ters gittiğinde sistematik olarak ne yapılacağını ve bir araştırmacının panik yerine bir yöntemle nasıl ilerleyeceğini gösterir.

## Kaynakça

Atıflar APA 7 biçimindedir. DOI'ler 2026-06-04 tarihinde Crossref üzerinden doğrulanmıştır.

Belcher, W. L. (2019). *Writing your journal article in twelve weeks: A guide to academic publishing success* (2nd ed.). University of Chicago Press. ISBN 978-0-226-49991-8

Bordage, G. (2001). Reasons reviewers reject and accept manuscripts: The strengths and weaknesses in medical education reports. *Academic Medicine*, 76(9), 889–896. https://doi.org/10.1097/00001888-200109000-00010

Else, H. (2023). Abstracts written by ChatGPT fool scientists. *Nature*, 613(7944), 423. https://doi.org/10.1038/d41586-023-00056-7

Hosseini, M., Rasmussen, L. M., & Resnik, D. B. (2023). Using AI to write scholarly publications. *Accountability in Research*, 31(7), 715–723. https://doi.org/10.1080/08989621.2023.2168535

Noble, W. S. (2017). Ten simple rules for writing a response to reviewers. *PLOS Computational Biology*, 13(10), e1005730. https://doi.org/10.1371/journal.pcbi.1005730

Provenzale, J. M., & Stanley, R. J. (2005). A systematic guide to reviewing a manuscript. *American Journal of Roentgenology*, 185(4), 848-854. https://doi.org/10.2214/AJR.05.0782

Sword, H. (2017). *Air & light & time & space: How successful academics write*. Harvard University Press. https://doi.org/10.4159/9780674977617

Williams, J. M., & Bizup, J. (2016). *Style: Lessons in clarity and grace* (12th ed.). Pearson. ISBN 978-0-13-408041-3

---

**Kitapçık kimliği.** `010-01-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-20
**Sözcük sayısı (yaklaşık).** 1881 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 8
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`009-01-0001`](../../009-ethics-irb/009-01-0001/tr.md). Yapay Zekâ Destekli Araştırmada Etik, Prensipten Davranışa
**Sonraki kitapçık.** [`012-01-0001`](../../012-troubleshooting/012-01-0001/tr.md). İşler Ters Gittiğinde, Çalışan Bir Sorun Giderme Protokolü
