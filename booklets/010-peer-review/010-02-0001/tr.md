---
title_en: "Anti-AI-Trace Writing for Revisions"
title_tr: "Revizyonlarda Yapay Zekâ İzini Silmek"
booklet_id: "010-02-0001"
category: "010-peer-review"
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
    model_dated: null  # no dated identifier published by Anthropic for Fable 5 as of 2026-06-10
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

# Revizyonlarda Yapay Zekâ İzini Silmek

Önceki kitapçık hakem yanıt mektubunu izlenebilirlik matrisiyle kurdu ve dördüncü bölümünde bir soruyu bilerek açık bıraktı. Yanıt mektubu bittiğinde masada bir de revize edilmiş metin durur ve o metin çoğu zaman yolun bir yerinde yapay zekâ desteğiyle şekillenmiştir. Desteğin kendisi meşrudur. Geriye kalan, üslup tortusudur. Model destekli düzyazı tanınabilir retorik alışkanlıklar taşır ve bu alışkanlıklar yazarın sesinin üzerine oturur. Bu kitapçık o tortuyu revizyon sırasında söken iki katmanlı bir yöntemi anlatır ve daha yöntem başlamadan tek bir ilkeyi sabitler. Üslubu yönetmek yazarın hakkıdır. Katkıyı beyan etmek yazarın borcudur. İkisi ayrı raylarda ilerler ve biri ötekiyle takas edilemez.

## 1. İz Nedir, Ne Değildir

Yapay zekâ izi, model destekli metinlerde tekrarlayan biçem desenlerinin toplamıdır. Kaç maddenin geleceğini önceden duyuran başlık bunlardan biridir. Aynı uzunlukta kurulan paragraflar, kavramların hep üçlü kümeler hâlinde sıralanması, bir şeyin önce ne olmadığını kurup sonra ne olduğunu ilan eden cümleler ve her bölümü aynı ritimle kapatan özetler de öyle. Tek başına hiçbiri kusur sayılmaz. Üst üste bindiklerinde ise insan elinden çıkmış düzyazının taşımadığı bir simetri doğar ve okur, adını koyamasa bile bunu fark eder.

İki dilde çalışan yazar için ize bir katman daha eklenir. Taslak Türkçeden İngilizceye ya da tersine geçerken model, çeviri kalıplarını da birlikte taşır. Ödünç metaforlar, kaynak dilden ithal sözdizimi ve hedef dilde kimsenin kurmayacağı cümleler metne sızar.

İz bir içerik hatası değildir. Yanlış bulgu, uydurma kaynak ya da şişirilmiş iddia birer dürüstlük sorunudur ve bu rehberin başka kitapçıklarında doğrudan ele alınır. İz, üslup düzeyinde bir imzadır. Silinmesi metnin söylediğini değil, seslenişini değiştirir. Okuru yanıltma sorusu üslup katında çözülmez. O sorunun adresi beyan satırıdır ve bu kitapçık o adrese tekrar tekrar dönecektir.

## 2. Tespit Araçları Neyi Görür, Neyi Göremez

Bir metnin modelden çıkıp çıkmadığını dışarıdan saptama girişimleri iki koldan ilerledi ve ikisi de ölçüldü. İlk kol insan yargısıdır. Else (2023), ChatGPT ile üretilmiş özetlerin deneyimli bilim insanlarını yanıltabildiğini Nature sayfalarında aktardı. Gao ve diğerleri (2023) aynı soruyu denetimli bir kurguya taşıdı. Kör hakemler üretilmiş özetlerin yüzde altmış sekizini yakalayabildi ve aynı oturumda gerçek özetlerin yüzde on dördünü yanlışlıkla üretilmiş diye işaretledi. İkinci kol otomatik dedektörlerdir. Weber-Wulff ve diğerleri (2023), on ikisi herkese açık ikisi ticari olmak üzere on dört tespit aracını sistematik biçimde sınadı. En yüksek doğruluk değerleri bile yüzde seksenin altında kaldı. Üretilmiş metin bir yapay zekâ aracıyla yeniden ifade edildiğinde toplam doğruluk yüzde yirmi altıya indi. Yazarların vardığı yargı serttir. Eldeki araçlar ne isabetli ne güvenilirdir.

Bu iki bulgu kümesi aynı noktada birleşir. Makine metninin görünür bir bölümünü kaçıran ve dürüst yazarların ölçülebilir bir bölümünü suçlayan bir mekanizma, bilimsel bütünlüğün yükünü taşıyamaz. Tespit kenarda bir işe yarayabilir. Temel olarak iki yönde birden çöker.

## 3. Yanlış Pozitifin Bedeli

Yanlış pozitif soyut bir istatistik değildir. Bir yazarın dürüstlüğüne yöneltilmiş asılsız bir suçlamadır ve bu suçlama herkese eşit dağılmaz. Liang ve diğerleri (2023), yaygın GPT dedektörlerini iki derlem üzerinde sınadı. Ana dili İngilizce olmayan yazarların TOEFL denemelerinde ortalama yanlış pozitif oranı yüzde altmış biri geçti. Denemelerin yaklaşık beşte biri, sınanan dedektörlerin tamamı tarafından aynı anda makine çıktısı sayıldı. Aynı araçlar Amerikalı öğrencilerin denemelerini doğru sınıflandırdı.

Mekanizma ikinci dilden yazanın aleyhine kuruludur. Dedektörler metnin şaşırtıcılığını ölçer. Bir dil modeli bir sonraki sözcüğü kolayca tahmin edebiliyorsa şaşırtıcılık düşüktür ve metin makine çıktısına benzetilir. İkinci dilde yazan bir insan ise doğal olarak daha dar bir sözcük dağarcığıyla, daha kurallı cümlelerle ilerler. Temkinli ve düzgün yazmak, bu rejimde başlı başına şüphe nedenine dönüşür. Weber-Wulff ve diğerlerinin (2023) makine çevirisinden geçen metinlerde yanlış pozitif riskinin keskin biçimde arttığı bulgusu, aynı tabloyu başka bir kapıdan gösterir.

Türkçeden İngilizceye yazan bir sosyal bilimci bu tablonun tam ortasında durur. Tespite dayalı bir bütünlük rejimi iki dilli yazarı baştan kuşku altına alır. Beyana dayalı bir rejim ise yazarın ne kullandığını kendisinin söylemesine güvenir. Bu kitapçığın yöntemi ikinci rejimi varsayar ve bir sonraki bölüm bu varsayımın etik zeminini kurar.

## 4. Bütünlük Görünmezlikte Değil Beyandadır

Bu rehberin önceki kitapçıkları beyan ilkesini farklı bağlamlarda işledi. Burada ilke en keskin sınavına girer ve sınav, bu araçları dürüstçe kullanan herkesin eninde sonunda sorduğu bir soruyla açılır. Metnimdeki yapay zekâ izini silersem yapay zekâ kullanımımı gizlemiş olur muyum?

Yanıt iki katmanın ayrı tutulmasında yatar. Hosseini ve diğerleri (2023), bilimsel yayında yapay zekâ kullanımını incelerken aracın metnin biçimini düzenlemesi ile içeriğini üretmesi arasındaki ayrımın bulanıklaşmadan korunmasını ister ve beyan yükümlülüğünü kullanımın görünürlüğüne değil kullanımın kendisine bağlar. Üslup yazarın egemenlik alanıdır. Araştırmacı her cümleyi yeniden kurabilir, metni istediği kadar düzeltme turundan geçirebilir, istediği kalıbı sökebilir. Bu edimlerin hiçbiri beyan yükümlülüğü doğurmaz ya da düşürmez. Yükümlülük metnin nasıl okunduğundan değil, üretiminde neyin kullanıldığından doğar. İz silinmiş ve beyan yerindeyse ortada aldatma yoktur. Metin pürüzsüzdür ve künyesi dürüsttür. İz beyanla birlikte silinmişse yapılan iş üslup bakımı olmaktan çıkar. Adı okuru yanıltma girişimidir.

Bu çizgi, rehberin zaten izlediği editoryal standartlarla örtüşür. Yayın etiği kuruluşları ve editör birlikleri yapay zekâ katkısının açıklanmasını ister. Hiçbiri metnin belirli bir üslupta bırakılmasını şart koşmaz. İstenen tek şey katkının açık yazılmasıdır.

## 5. Birinci Katman, Retorik Mimariyi Sökmek

İlk katman dilden bağımsız desen sınıflarına bakar ve sayımla başlar. Metin her desen sınıfı için taranır, geçiş sayıları hiçbir şey değiştirilmeden önce kaydedilir. Düzeltmeyi ölçülebilir kılan bu sayımdır.

Taranacak sınıflar birinci bölümden tanıdıktır. Kaç maddenin geleceğini önceden duyuran başlık ve cümleler. Üç öğeli sıralamaların mekanik tekrarı. Gerçek bir karşıtlık kalmadığı hâlde sürdürülen karşıtlık kalıbı. Birbirinin yerine geçebilecek uzunlukta paragraflar. Aynı kapanış ritmiyle biten bölümler. Aynı küçük bağlaç ailesinden dönen geçişler.

Sökme işi sınıf sınıf ilerler. Sayı duyuran başlık, içeriği taşıyan bir başlıkla değiştirilir. Üçlülerin bir kısmı ikiye iner, bir kısmı dörde çıkar, bir kısmı cümlenin içine dağılır. Karşıtlık kalıbı yalnızca karşıtlığın gerçek olduğu yerde kalır. Paragraf uzunluğu içeriğe teslim edilir. Kısa bir nokta kısa bir paragrafı hak eder. Bu katmanda taramayı ve sayımı Claude Code üstlenir, neyin kalacağına yazar karar verir. Geçiş bittiğinde sayım tekrarlanır ve aradaki fark kaydedilir. O fark, dokuzuncu bölümde kurulacak savunu dosyasının ilk belgesidir.

## 6. İkinci Katman, Doğallık ve Kalk Avı

İkinci katman iki dilli yazarındır ve hedefi, metnin hedef dilde doğal seslenmesidir. Çeviri kalkı, bir dildeki yapının başka bir dile sözcüğü sözcüğüne taşınmasıdır. Model destekli çeviri ve yeniden yazım kalkı bol üretir, çünkü model iki dil arasındaki en kısa köprüyü kurar. İngilizcede doğal duran bir metafor Türkçede iğreti kalabilir. Türkçeye özgü bir deyiş, İngilizceye olduğu gibi taşındığında anlamını yolda bırakır.

Bu katmanın testi tektir ve teknik değildir. Cümle sesli okunur ve tek bir soru sorulur. Bu dilde yazan biri bu cümleyi hiç kurar mıydı? Gözün alıştığı pürüzü kulak anında yakalar. Ödünç akademik klişe, kaynak dilden taşınan sözdizimi ve aktarılmış imge, görünmeden önce duyulur.

Rehberin iş akışında yön iki taraflıdır. Türkçe taslaktan İngilizce yeniden yazıma geçerken İngilizcenin doğallığı denetlenir. İngilizce literatür notlarından Türkçe bölüme dönerken aynı denetim Türkçeye uygulanır. Yeniden yazım çeviri değildir. Ana hattı koruyup her cümleyi hedef dilin içinde yeniden kurmak, kalka karşı en güvenilir panzehirdir.

## 7. Homojenleşme ve Yazarın Sesi

Bu zahmete neden girilir? Yanıt verimlilikte değil, bir literatürün muhtaç olduğu ses çeşitliliğindedir. Noy ve Zhang (2023), üretken yapay zekâ desteğinin profesyonel yazma işlerinde hem hızı hem kaliteyi yükselttiğini deneysel olarak gösterdi ve aynı deneyde yazarlar arasındaki eşitsizliğin azaldığını kaydetti. Dağılım ortaya doğru sıkışır. Doshi ve Hauser (2024) benzer sıkışmayı içerik düzeyinde ölçtü. Destek alan yazarların öyküleri tek tek daha yaratıcı bulunurken öykülerin toplamı çeşitliliğini yitirdi.

Bilimsel literatür için bu bulgular bir uyarıdır. Binlerce yazar aynı modelden destek alır ve desenleri yerinde bırakırsa literatür tek bir sese doğru çekilir. Yazarın kendi üslubunu geri kazanması bu yüzden süs değildir. Alanın düşünmeye devam etmek için muhtaç olduğu çokseslilik adına bir katkıdır. Kendi cümlesini yeniden kuran yazar, kendisiyle birlikte okurunu da modelin ortalamasından kurtarır.

## 8. Yapılmayacaklar

İki katmanlı yöntemin sınırını, olmayı reddettiği şeyler çizer.

| Durum | Değerlendirme |
|---|---|
| İz silinir, beyan korunur | Meşru üslup bakımı |
| İz silinir, beyan da kaldırılır | Aldatma. Yöntemin amacının dışında |
| Metin, dedektör atlatmak için insanlaştırıcı araçlardan geçirilir ve kullanım beyan edilmez | Aldatma. Üstelik kırılgan, çünkü dedektörler değişir |
| Hakemin doğrudan sorusuna yanıtta kullanım inkâr edilir | Doğrudan dürüstlük ihlali |
| İz silme, atıf doğrulamanın yerine sayılır | Kategori hatası. Atıf bütünlüğü ayrı bir süreçtir |

Son satır kendi paragrafını hak eder. Walters ve Wilder (2023), model üretimi kaynakçalarda uydurma ve hatalı atıfların ne kadar yaygın olduğunu belgeledi. Uydurma atıf bir üslup pürüzü değil içerik sahteciliğidir ve hiçbir üslup çalışması onu temizlemez. İzi silinmiş ama atıfları doğrulanmamış bir metin, cilalanmış bir risk taşıyıcısıdır. Atıf doğrulamanın kendisi bu rehberin APA 7 ve DOI disiplini kitapçığında anlatılır.

## 9. Savunulabilir Bir Revizyon İş Akışı

Gerçek hakem baskısı altında yöntem belirli bir sırayla işler. Revizyona girerken beyan cümlesi dondurulur. Metnin hangi bölümünün hangi destekle üretildiğini söyleyen bu cümle yazılır ve revizyon boyunca dokunulmadan bırakılır. Ardından desen sayımı alınır, birinci katman işletilir, ikinci katman sesli okumayla kapanır ve sayım tekrarlanır. Atıf çekirdeği yeniden doğrulanır. Revizyonda metne giren kaynaklar da çıkan kaynaklar da bu doğrulamanın kapsamındadır. Son adım, beyan cümlesinin hâlâ yerinde durduğunun gözle kontrolüdür.

Bu sıranın ürettiği şey, süreci savunan bir dosyadır. Editör ya da hakem sorduğunda yazarın elinde tarihli bir kayıt vardır. Hangi desen sınıfından kaç adet bulundu ve kaçı söküldü. Hangi kaynak hangi tarihte hangi veri tabanından doğrulandı. Beyan cümlesi hangi sürümler boyunca aynı kaldı. Bu kaydın tutulmasını Claude Code otomatikleştirir. Savunulabilirlik, sorulduğunda gösterilebilen şeydir.

## 10. Köprü, Sürecin Kırıldığı Ana

Revizyon, bu rehberin anlattığı iş akışlarının en yoğun kesişimidir. Arşiv, atıf doğrulama, iki dilli yeniden yazım ve beyan disiplini aynı hafta aynı metnin üzerinde çalışır. Hareketli parça arttıkça bir şeylerin durma ihtimali de artar. Bir oturum yarıda kesilebilir. Bir dosya kimsenin bırakmadığı bir hâlde bulunabilir. Kapanış kitapçığı tam o ana ayrılmıştır ve işler ters gittiğinde panik yerine yöntemle ilerleyen bir sorun giderme protokolünü anlatır.

## Kaynakça

Atıflar APA 7 biçimindedir. DOI'ler 2026-06-10 tarihinde Crossref üzerinden doğrulanmıştır.

Doshi, A. R., & Hauser, O. P. (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. *Science Advances*, 10(28), eadn5290. https://doi.org/10.1126/sciadv.adn5290

Else, H. (2023). Abstracts written by ChatGPT fool scientists. *Nature*, 613(7944), 423. https://doi.org/10.1038/d41586-023-00056-7

Gao, C. A., Howard, F. M., Markov, N. S., Dyer, E. C., Ramesh, S., Luo, Y., & Pearson, A. T. (2023). Comparing scientific abstracts generated by ChatGPT to real abstracts with detectors and blinded human reviewers. *npj Digital Medicine*, 6(1), Article 75. https://doi.org/10.1038/s41746-023-00819-6

Hosseini, M., Rasmussen, L. M., & Resnik, D. B. (2023). Using AI to write scholarly publications. *Accountability in Research*, 31(7), 715–723. https://doi.org/10.1080/08989621.2023.2168535

Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). GPT detectors are biased against non-native English writers. *Patterns*, 4(7), 100779. https://doi.org/10.1016/j.patter.2023.100779

Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. *Science*, 381(6654), 187-192. https://doi.org/10.1126/science.adh2586

Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, 13, Article 14045. https://doi.org/10.1038/s41598-023-41032-5

Weber-Wulff, D., Anohina-Naumeca, A., Bjelobaba, S., Foltýnek, T., Guerrero-Dib, J., Popoola, O., Šigut, P., & Waddington, L. (2023). Testing of detection tools for AI-generated text. *International Journal for Educational Integrity*, 19(1), Article 26. https://doi.org/10.1007/s40979-023-00146-z

---

**Kitapçık kimliği.** `010-02-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-20
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1592 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 8
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`010-01-0001`](../010-01-0001/tr.md). İzlenebilirlik Matrisleri ile Hakem Yanıt Mektupları
**Sonraki kitapçık.** [`012-01-0001`](../../012-troubleshooting/012-01-0001/tr.md). İşler Ters Gittiğinde, Çalışan Bir Sorun Giderme Protokolü
