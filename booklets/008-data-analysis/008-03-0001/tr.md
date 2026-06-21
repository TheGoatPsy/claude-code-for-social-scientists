---
title_en: "Qualitative Coding with AI Assistance and Human Oversight"
title_tr: "Yapay Zekâ Yardımı ve İnsan Gözetimiyle Nitel Kodlama"
booklet_id: "008-03-0001"
category: "008-data-analysis"
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
    model_dated: null  # no dated identifier published by Anthropic for Fable 5 as of 2026-06-10
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

# Yapay Zekâ Yardımı ve İnsan Gözetimiyle Nitel Kodlama

Önceki kitapçık nicel kolda danışma disiplinini kurdu. İstatistiksel test seçiminde modelin danışman, kararın yazara ait olduğu bir protokol. Bu kitapçık aynı disiplini nitel kola taşır ve daha en başta zemini netleştirir. Nitel kodlama bir veri işleme adımı değil, yorumlama ediminin kendisidir. Görüşme dökümündeki bir cümleye kod vermek, o cümlenin ne anlattığına dair bir karar vermektir ve bu karar araştırmacının kuramsal duruşundan bağımsız verilemez. Yapay zekâ bu süreçte güçlü bir asistan olabilir. Asistanlığın hangi protokolle güvenli hâle geldiği, alıntı bütünlüğünün nasıl korunduğu ve katkının nasıl beyan edildiği bu kitapçığın konusudur.

## 1. Otomatikleştirilemeyecek Olan

Nitel araştırma geleneklerinin önemli bir bölümünde araştırmacının öznelliği giderilecek bir hata kaynağı değil, analizin kaynağıdır. Braun ve Clarke (2019), refleksif tematik analizi tarif ederken bu noktayı açıkça koyar. Temalar veride hazır bulunup toplanmaz, araştırmacının veriyle ve kuramla kurduğu ilişki içinde üretilir. Bu çerçevede kodlamayı bütünüyle bir makineye devretmek, yöntemin hatasını değil yöntemin kendisini ortadan kaldırır.

Bu tespit yapay zekâ desteğini dışlamaz. Dışladığı şey, desteğin yorum yetkisine dönüşmesidir. Aradaki fark bu kitapçığın her bölümünde yeniden çizilecek ve her seferinde aynı yere oturacaktır. Model işlem yapar, araştırmacı anlam verir.

## 2. Tematik Analizin Omurgası

Protokol kurulmadan önce omurganın kendisi gerekir. Braun ve Clarke (2006), tematik analizi psikoloji alanında sistematikleştiren çalışmalarında süreci altı aşamada tarif eder. Veriyle tanışma, ilk kodların üretilmesi, temaların aranması, temaların gözden geçirilmesi, temaların tanımlanıp adlandırılması ve raporun yazılması. Aşamalar doğrusal değil döngüseldir. Tema gözden geçirilirken kodlara, kod üretilirken veriye dönülür.

Bu altı aşama, yapay zekâ desteğinin haritası olarak da okunabilir. Veriyle tanışma aşamasında destek meşrudur ve sınırlıdır, çünkü dökümleri araştırmacının yerine model okursa tanışma gerçekleşmemiş olur. Kod üretiminde destek en verimli hâlindedir. Tema adlandırma ve rapor aşamasında ise yorum yükü en ağır noktadadır ve yetki devri en risklidir.

## 3. Kod Defteri Tasarımı

Kod defteri, kodlamanın anayasasıdır. Her kod için dört alan tutulur. Kodun etiketi, kavramsal tanımı, dahil etme ve dışlama ölçütleri, bir de doğrudan dökümden alınmış örnek alıntı. Dışlama ölçütü en çok ihmal edilen alandır ve en değerlisidir, çünkü iki kodun sınırı tam orada çizilir. Kaygı ifadesi ile kaçınma davranışı ayrı kodlarsa, ikisinin kesiştiği cümlenin hangi tarafa düşeceğini dışlama ölçütü söyler.

Defter yaşayan bir belgedir. Kodlama ilerledikçe tanımlar keskinleşir, kodlar birleşir ya da bölünür ve her değişiklik tarihli bir notla kaydedilir. Arşiv yapısı bu rehberin hafıza kitapçıklarında kurulduğu gibidir. Kod defteri tek bir dosyada yaşar, sürüm geçmişi onun değişim güncesidir ve bu günce dokuzuncu bölümdeki beyanın da hammaddesini oluşturur.

## 4. Modelin Yeri, Protokollü İkinci Kodlayıcı

Claude Code bu iş akışında iki ayrı rol üstlenebilir ve ikisinin de sınırı bellidir. İlk rol kodlama asistanlığıdır. Model, kod defterindeki tanımlarla bir dökümü tarar ve aday kod atamaları önerir. İkinci rol, protokollü ikinci kodlayıcılıktır. Model, araştırmacının kodladığı bir bölümü aynı defterle ve araştırmacının atamalarını görmeden kodlar. İki kodlama yan yana konur ve uyuşmazlıklar bir listeye düşer.

Bu rolün gerçekçi bir sınırı vardır. Morgan (2023), ChatGPT'nin nitel analiz kapasitesini yayımlanmış bir insan analiziyle karşılaştırdığı vaka çalışmasında, modelin betimsel temaları büyük ölçüde yeniden üretebildiğini, örtük ve yorumlayıcı temalarda ise zayıf kaldığını raporladı. Bulgu, protokolün neden böyle kurulduğunu açıklar. Model yüzeydeki deseni güvenilir biçimde yakalar ve tam bu yüzden betimsel katmanda iyi bir ikinci gözdür. Derin yapıya inen yorum, uyuşmazlık listesinin insan tarafında kalır.

## 5. Güvenilirlik Kontrol Noktaları

Uyuşmazlık listesi, kodlamanın en verimli malzemesidir. O'Connor ve Joffe (2020), kodlayıcılar arası güvenilirlik tartışmasını gözden geçirdikleri çalışmada iki şeyi birden yapar. Güvenilirlik kontrolünün şeffaflığı ve sistematikliği artırabileceğini gösterirler ve kontrolün veri setinin tamamına değil anlamlı bir alt kümesine uygulanmasını, sürecin de açıkça raporlanmasını öneren pratik bir çerçeve sunarlar. Aynı çalışma dürüst bir gerilimi de kaydeder. Refleksif gelenekte yüksek uyuşma oranı başlı başına bir erdem değildir, çünkü yorumun zenginliği tam da farklı okumalarda yatabilir.

Bu iş akışındaki kontrol noktası buna göre kurulur. İnsan ile modelin uyuşmazlık listesi bir oran üretmek için değil, bir konuşma başlatmak için kullanılır. Her uyuşmazlık üç sonuçtan birine bağlanır. Kod defterindeki tanım belirsizdir ve keskinleştirilir. Modelin atadığı kod yüzeysel bir benzerliğe kapılmıştır ve reddedilir. Araştırmacının gözünden kaçan bir desen vardır ve kabul edilir. Üç sonucun üçü de defterin değişim güncesine işlenir.

## 6. Alıntı Bütünlüğü

Nitel raporun kanıtı alıntıdır ve alıntının tek meşru kaynağı dökümün kendisidir. Üretken modellerin belgelenmiş bir uydurma eğilimi vardır. Walters ve Wilder (2023) bu eğilimi kaynakça düzeyinde ölçtüğünde, var olmayan ama tamamen gerçekçi görünen künyelerin ne kadar kolay üretildiğini gösterdi. Aynı eğilimin görüşme verisindeki karşılığı daha sinsidir. Bir dökümü özetleyen model, hiçbir katılımcının kurmadığı ama kurabileceği kadar akla yatkın bir cümleyi alıntı görünümünde sunabilir.

Bu yüzden kural taviz tanımaz. Rapora giren her alıntı, dökümde sözcüğü sözcüğüne aranır ve bulunur. Claude Code bu doğrulamayı otomatikleştirir, çünkü birebir metin araması tam olarak makine işidir. Bulunamayan alıntı ne düzeltilir ne yumuşatılır. Silinir ve yerine dökümden gerçek bir alıntı seçilir. Anonimleştirme amacıyla yapılan değişiklikler ise köşeli ayraçla işaretlenir ve yöntem bölümünde açıklanır.

## 7. Refleksivite Günlüğü

Refleksif gelenekte araştırmacı, analizin aracı olduğu için kendi konumunu da kayıt altına alır. Yapay zekâ destekli kodlamada bu günlüğe yeni bir katman eklenir. Modelle yapılan analiz konuşmalarının kendisi de refleksivite malzemesidir. Hangi istem verildi, model hangi çerçeveyi önerdi, araştırmacı neden kabul ya da reddetti?

Günlük, arşivde kod defterinin yanında yaşar ve her analiz oturumundan sonra birkaç satırla beslenir. Bu satırlar iki işe birden yarar. Analizin denetim izini kurarlar ve araştırmacının modelin çerçevelerine ne ölçüde yaslandığını kendisine gösterirler. Modelin önerdiği her temayı kabul eden bir günlük sayfası, yorum yetkisinin sessizce el değiştirmekte olduğunun erken uyarısıdır.

## 8. Gizlilik ve Veri Koruması

Görüşme verisi, sosyal bilimcinin işlediği en hassas malzemedir ve nitel kodlama iş akışı bu hassasiyete göre kurulur. Temel kural sıralamadadır. Önce anonimleştirme, sonra model. Katılımcı adları, kurum adları ve dolaylı kimlik bilgileri dökümden çıkarılmadan hiçbir parça modele gösterilmez. Kişisel verilerin korunmasına dair yükümlülükler, Türkiye'de KVKK ve Avrupa bağlamında GDPR, onam formunda verilmiş sözlerle birlikte bu sıralamayı hukuken de zorunlu kılar.

Claude Code tarafında bu, çalışma dizini disiplini demektir. Ham dökümler arşivin model erişimine kapalı bölgesinde durur, kodlama oturumları yalnızca anonimleştirilmiş kopyalarla çalışır ve hangi dosyanın hangi bölgede yaşadığı klasör yapısının kendisinden okunur. Onamın kapsamı da burada hatırlanmayı hak eder. Katılımcı verisinin yapay zekâ araçlarıyla işlenebileceği onam formunda öngörülmemişse, bu sınır araştırmacının konforuna göre esnetilemez.

## 9. Beyan

Yapay zekâ destekli kodlamanın beyanı, yöntem bölümünde sürecin tarifiyle yapılır. Hosseini ve diğerleri (2023), beyan yükümlülüğünü kullanımın kendisine bağlarken somutluğu da ister. Okur, aracın nerede durduğunu görebilmelidir. İyi bir beyan cümlesi rolü, protokolü ve yetkinin adresini birlikte verir. Aşağıdaki örnek sentetiktir.

> Kodlama sürecinde Claude Code, kod defteri tanımlarıyla bağımsız ikinci kodlama üreten bir asistan olarak kullanılmıştır. Uyuşmazlıklar birinci yazar tarafından karara bağlanmış, tüm tema tanımları ve yorumlar yazarlar tarafından üretilmiştir. Rapordaki tüm alıntılar dökümlerle sözcüğü sözcüğüne doğrulanmıştır.

Bu üç cümle, bu kitapçığın tamamının özetidir. Protokol şeffaf, yetki insanda, kanıt doğrulanmış.

## 10. Köprü, Etik Çerçeveye

Gizlilik bölümü onam formuna, beyan bölümü dürüstlük ilkesine yaslandı. İkisinin de kökü, araştırma daha tasarlanırken kurulan etik çerçevededir. Bir sonraki kitapçık bu çerçeveyi bütün olarak ele alır. Yapay zekâ destekli araştırmada etik ilkenin gündelik davranışa nasıl çevrildiğini, onamdan veri saklamaya ve beyana uzanan hattı tek bir iş akışı belgesinde toplar.

## Kaynakça

Atıflar APA 7 biçimindedir. DOI'ler 2026-06-21 tarihinde Crossref üzerinden doğrulanmıştır.

Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77–101. https://doi.org/10.1191/1478088706qp063oa

Braun, V., & Clarke, V. (2019). Reflecting on reflexive thematic analysis. *Qualitative Research in Sport, Exercise and Health*, 11(4), 589–597. https://doi.org/10.1080/2159676X.2019.1628806

Hosseini, M., Rasmussen, L. M., & Resnik, D. B. (2023). Using AI to write scholarly publications. *Accountability in Research*, 31(7), 715–723. https://doi.org/10.1080/08989621.2023.2168535

Morgan, D. L. (2023). Exploring the use of artificial intelligence for qualitative data analysis: The case of ChatGPT. *International Journal of Qualitative Methods*, 22, Article 16094069231211248. https://doi.org/10.1177/16094069231211248

O'Connor, C., & Joffe, H. (2020). Intercoder reliability in qualitative research: Debates and practical guidelines. *International Journal of Qualitative Methods*, 19, Article 1609406919899220. https://doi.org/10.1177/1609406919899220

Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, 13, Article 14045. https://doi.org/10.1038/s41598-023-41032-5

---

**Kitapçık kimliği.** `008-03-0001`
**Sürüm.** `0.2.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1159 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 6
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`008-02-0001`](../008-02-0001/tr.md). Yapay Zekâ Danışma Disipliniyle İstatistiksel Test Seçimi
**Sonraki kitapçık.** [`009-01-0001`](../../009-ethics-irb/009-01-0001/tr.md). Yapay Zekâ Destekli Araştırmada Etik, İlkeden Davranışa
