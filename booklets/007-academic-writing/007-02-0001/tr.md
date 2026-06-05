---
title_en: "APA 7 with DOI Discipline"
title_tr: "DOI Disiplini ile APA 7"
booklet_id: "007-02-0001"
category: "007-academic-writing"
language: "tr"
version: "0.1.0"
date_published: "2026-05-24"
date_last_revised: "2026-06-05"
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
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-05"
verified_citations_count: 10
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Türkçe kaynak üzerinden şampiyonluk düzeyinde sıfırdan yeniden yazım. Greenhalgh ve diğerleri (2016) yanlış uygulama gerekçesiyle çıkarıldı, yerine doğrudan veritabanı kapsam iddiasını destekleyen Bramer ve diğerleri (2017) alındı. EN aşamasında yapılan tüm akademik düzeltmeler Türkçe yüzeye aktarıldı."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# DOI Disiplini ile APA 7

Önceki kategori kasanın klasör mimarisini kurmuştu. Bu kitapçık, o kasaya giren her referansın bibliyografik temizliğini ele alır. Dijital Nesne Tanımlayıcı, yani DOI, ilk bakışta bir stil kılavuzunu tatmin etmek için künyenin sonuna eklenen bir karakter dizisi gibi görünebilir. Değil. Üretici dil modellerinin bibliyografik açıdan inandırıcı ama hiç var olmamış atıflar üretebildiği bir dönemde DOI, araştırmacının elindeki en hızlı ampirik testtir: atıf gerçekse DOI'si çözülür, DOI çözülmüyorsa atıf yoktur. Bu kitapçık o testi, Claude Code iş akışında bir kez kurulan ve her makalede yeniden kullanılan bir doğrulama protokolüne dönüştürür.

## 1. APA 7 Ana Hatları ve DOI'nin Konumu

APA 7, sosyal bilimlerde en yaygın atıf standardıdır (American Psychological Association, 2020). Bir dergi makalesi künyesi yazar, yıl, başlık, dergi adı, cilt, sayı, sayfa ve DOI bileşenlerinden oluşur. Bu bileşenlerin büyük çoğunluğu bir makaleyi tanımlamaya yeter. DOI ise farklı bir işlev üstlenir: bir makaleyi tanımlamaz, onu doğrular. DOI, yayımlanmış bir çalışmanın değişmeyen, kalıcı ve makinece çözülebilir adresidir. Dergi web siteleri taşınsa da birleşse de bu adres doğru kalmaya devam eder.

APA 7, DOI'yi olabildiğince zorunlu kılar. Gerekçe teknik değil, epistemolojiktir. Uluslararası Tıp Dergisi Editörleri Komitesi de (2024) bilimsel çalışmanın yürütülmesi ve raporlanmasına ilişkin önerilerinde atıf doğruluğunu yazarın temel sorumluluklarından biri olarak tanımlar. DOI bu sorumluluğu pratiğe taşır. Crossref'te çözülen bir DOI, söz konusu atıfın var olduğunun kanıtıdır. Çözülmeyen bir DOI, referans listesine girmemesi gereken bir kaydın işaretidir.

## 2. Yapay Zekâ ve Hayali Atıf, Ampirik Kanıtlar

DOI disiplininin neden bu denli kritik olduğunu görmek için üretici yapay zekâ modellerinin atıf davranışına bakmak gerekir. Bu modeller, gerçek görünen ama var olmayan atıflar üretebilir. Bir görüş değil, ölçülmüş bir olgudur bu.

Walters ve Wilder (2023), ChatGPT tarafından üretilen bibliyografik atıflarda yüksek oranda uydurma ve hata olduğunu sistematik biçimde belgelemiştir: üretilen atıfların önemli bir kısmı ya hiç var olmayan makalelere işaret ediyor ya da gerçek makalelerin künyelerini yanlış birleştiriyordu. Bhattacharyya ve diğerleri (2023), tıbbi içerik özelinde aynı bulguyu doğrulayarak ChatGPT tarafından üretilen tıbbi metinlerdeki uydurma ve hatalı referans oranının yüksekliğini göstermiştir. Farklı disiplinleri kapsayan bu iki çalışma aynı yapısal sonuca ulaşır: üretici modeller gerçeği değil, en olası metni üretir. Bir atıf, modelin eğitim verisindeki kalıplara uyduğu sürece üretilir. O atıfın gerçekten var olup olmadığına bakılmaz.

Else (2023), ChatGPT tarafından yazılan özetlerin deneyimli bilim insanlarını bile yanıltabildiğini ortaya koyduğunda, sorunun yüzeysel bir hata olmadığı, modelin temel çalışma biçiminden beslendiği netleşti. Hicks ve diğerleri (2024) bu davranışı kavramsal düzeyde çerçeveleyerek modelin çıktısının doğruluk kaygısı taşımadığını, yalnızca akla yatkınlık ürettiğini göstermiştir. Sallam (2023) ise sağlık eğitimi ve araştırmasındaki uygulamaları sistematik bir derlemeyle ele alarak bu modellerin sunduğu gerçek olanakların yanında atıf doğruluğuna ilişkin geçerli kaygıların da belgelendiğini ortaya koymuştur. Klinik bir araştırmacı için hayali bir atıf yalnızca biçimsel bir hata değildir. Bilimsel kayıtta bir bütünlük ihlaline, ve dolayısıyla etik bir riske, dönüşür.

## 3. Üçlü İndeks Üçgenlemesi

Hiçbir veri tabanı herhangi bir araştırma alanının tüm genişliğini kapsamaz. Bu nedenle tek bir indeks, bir atıfı doğrulamak için yeterli değildir. Çözüm üçgenlemedir: bir atıfın üç bağımsız indekste çapraz kontrol edilmesi. Crossref, PubMed ve Semantic Scholar, bu üçlü birlikte, sosyal bilim ile sağlık bilimlerinin büyük çoğunluğunu kapsar.

Crossref, DOI'lerin merkezi kayıt altyapısıdır (Crossref, 2026): DOI taşıyan her makale bu altyapı üzerinden sorgulanabilir. PubMed, biyomedikal ve sağlık literatürünün ulusal kütüphane altyapısıdır (National Library of Medicine, 2026). Klinik psikoloji ve halk sağlığı araştırmacıları için PubMed, Crossref'in kapsamadığı birçok kaynağı barındırır. Semantic Scholar ise anlamsal arama ve atıf grafiği sunarak bir makalenin hangi sonraki çalışmalar tarafından atıflandığını gösterir. Her üç indeks farklı güçlere sahiptir: Crossref DOI çözümünde, PubMed klinik kapsamda, Semantic Scholar atıf ilişkilerinde öne çıkar.

Tek bir indekse güvenmenin yaratacağı kör noktalar soyut bir iddia değildir. Bramer ve diğerleri (2017), sistematik derleme arama stratejilerini karşılaştırdıkları prospektif çalışmada farklı veri tabanı kombinasyonlarının anlamlı ölçüde farklı geri çağırma sonuçları ürettiğini göstermiştir: hiçbir tek veri tabanı ilgili literatürün tamamını kapsamadı ve veri tabanları arasındaki örtüşme önemli ölçüde eksikti. Tek bir indekse güvenmek araştırmacıyı tam da göremeyeceği kör noktalara mahkûm eder.

Üçgenlemenin pratik maliyeti düşüktür. Her atıf için üç indeksi tek seferde taramak gerekmez. Çoğu atıf Crossref'te ilk denemede doğrulanır. Yalnızca çözülmeyen ya da tutarsız üst veri döndüren kayıtlar ikinci ve üçüncü indekse taşınır. Semantic Scholar'ın atıf grafiği ayrıca bir keşif değeri taşır: anahtar bir makaleden yola çıkan araştırmacı, onu atıflayan güncel çalışmalara ulaşarak literatür haritasını ileriye doğru da genişletir. Bu, anahtar kelime aramasının sistematik biçimde başaramadığı bir yöndür. Üçgenleme bu yüzden ne bir yük ne de salt bir güvenlik önlemidir: hayali atıfları yakalar ve literatür haritasını aynı anda genişletir.

## 4. Crossref API ile DOI Doğrulaması

Crossref, doğrulamayı betiklenebilir kılan bir uygulama programlama arayüzü, yani API sunar. Bir DOI'nin gerçekliği tek bir komutla kontrol edilebilir.

```bash
# Bir DOI'nin künyesini Crossref API ile doğrula
curl -fsSL "https://api.crossref.org/works/10.1038/d41586-023-00056-7" \
  | jq '.message.title, .message.author, .message["container-title"]'
```

Bu komut, DOI'nin Crossref kayıtlarında var olup olmadığını ve dönen künye bilgilerinin elde tutulandan farklı olup olmadığını gösterir. DOI yoksa API hata döndürür. Bu, atıfın uydurma olduğunun ilk kesin işaretidir. Claude Code bu kontrolü bibliyografya iş akışının standart bir adımı haline getirebilir ve her makale tamamlanmadan önce tüm referans listesi üzerinde otomatik olarak çalıştırabilir.

Sürdürülebilir kullanım için Crossref bir nezaket havuzu politikası uygular: bir istek, iletişim adresi içeren bir `mailto` parametresiyle gönderildiğinde daha yüksek hız sınırı ve daha güvenilir yanıt elde eder. Burada kişisel bir adres değil, kurumsal ya da takma bir adres kullanılmalıdır.

```bash
# Nezaket havuzu, kurumsal bir iletişim adresiyle
curl -fsSL "https://api.crossref.org/works/10.1038/d41586-023-00056-7?mailto=arastirmaci@kurum.edu.tr" \
  | jq '.message.title'
```

Nezaket havuzu, bu doğrulamayı ölçekte sürdürülebilir kılan şeydir. Beş kaynak için değil, yüz kaynaklı bir referans listesi için.

## 5. PubMed Üzerinden PMID ile Doğrulama

Klinik ve biyomedikal literatür için ikinci bir doğrulama katmanı PubMed Kimliği, yani PMID üzerinden gelir (National Library of Medicine, 2026). Her PubMed kaydı benzersiz bir PMID taşır. DOI altyapısından bağımsızdır. Hem DOI hem PMID taşıyan bir makale, iki bağımsız sistemden çift doğrulama imkânı sunar: Claude Code bir DOI'yi PubMed'de arayarak karşılık gelen PMID'yi bulabilir ve iki sistemin döndürdüğü künye bilgilerini karşılaştırabilir. İki bağımsız altyapının aynı kaydı vermesi, atıfın gerçekliğine dair güçlü bir kanıttır.

Klinik psikoloji araştırmacısı için bu katman özellikle değerlidir. Psikoloji ve sağlık bilimlerinin önemli bir kısmı PubMed'de dizinlenmiştir. PMID çapraz kontrolü, Crossref'in tek başına yakalayamadığı bir başarısızlık biçimini de yakalar: doğru çözülen ama üst verisi değişmiş ya da dergi sahipliği el değiştirmiş bir DOI.

## 6. DergiPark ve TR Dizin Üzerinden Türkçe Makale DOI'leri

Türkçe makaleler için doğrulama önceki bir kategoride kurulan altyapıya dayanır. DergiPark, Crossref ile entegre olduğundan platformdaki makaleler DOI taşır ve aynı Crossref API doğrulamasından geçebilir. Bir Türkçe makalenin APA 7 künyesi, İngilizce bir makaleninkiyle aynı disiplini gerektirir. Ek olarak birkaç dilsel kural devreye girer.

APA 7, Türkçe yazar isimleri için soyadı ve baş harf biçimini korur: "Yılmaz, A. A." biçiminde. İki yazar arasında Türkçe "ve" yerine "&" işareti kullanılır, çünkü künye kaynak dilinden bağımsız olarak İngilizce APA 7 konvansiyonuna uyar. Türkçe dergi adı italik tutulur ve başlığın İngilizce çevirisi köşeli parantez içinde hemen ardından verilir. Bir TR Dizin makalesinin tam APA 7 künyesi şu yapıyı izler:

```text
Yazar, A. A., & Yazar, B. B. (Yıl). Makalenin Türkçe başlığı
[Makalenin İngilizce çevirisi]. Derginin Türkçe Adı, Cilt(Sayı),
Sayfa-Sayfa. https://doi.org/{dogrulanmis-doi}
```

Bu künye, DergiPark üzerinden alınan DOI ile doğrulanır. Türkçe başlığın İngilizce çevirisi alan terminolojisine duyarlı olduğundan yazarın sorumluluğundadır. Model bir taslak çeviri önerse de son karar araştırmacınındır.

## 7. Bibliyografya Hijyeni Pipeline'ı, Sekiz Adım

Doğrulama disiplini gerçek değerini, bir kez kurulan ve her makalede yeniden kullanılan bir protokole dönüştüğünde kazanır. Aşağıdaki sekiz adım o protokolün iskeletidir.

1. **Toplama.** Tüm atıflar birincil kaynaklardan künye olarak toplanır.
2. **DOI çıkarma.** Her künyenin DOI'si belirlenir. Yokluğu açıkça not edilir.
3. **Crossref doğrulama.** Her DOI Crossref API ile kontrol edilir.
4. **Çapraz kontrol.** Klinik kaynaklar PubMed PMID ile çapraz doğrulanır. Üst veri tutarsızlıkları ortaya çıktığında Semantic Scholar üçüncü kaynak olarak devreye girer.
5. **Künye eşleştirme.** API'den dönen üst veri eldeki künyeyle karşılaştırılır. Tutarsızlıklar elle çözüm için işaretlenir.
6. **DOI'siz kaynaklar.** DOI taşımayan kaynaklar ayrı ele alınır, 9. bölümdeki köşe durum kuralları uygulanır.
7. **Biçimleme.** Doğrulanmış künyeler APA 7 biçimine getirilir.
8. **İnsan denetimi.** Tüm liste yazar tarafından son bir okumayla onaylanır. Doğrulama otomatiktir ama sorumluluk insanidir.

Claude Code birinci ile yedinci adımları destekler: toplama, DOI çıkarma, API doğrulama, çapraz kontrol, künye karşılaştırma ve biçimleme. Son denetim her zaman araştırmacıda kalır. Otomasyon hata yüzeyini daraltır. Sorumluluğu devretmez.

## 8. Yaygın Dil Modeli Atıf Başarısızlık Modları

Uydurma tek tip bir hata olarak karşımıza çıkmaz. Belirli başarısızlık biçimlerini tanıyan bir araştırmacı onları daha hızlı yakalar. Aşağıdaki tablo en yaygın olanları ve her birinin pipeline'ın hangi adımında yakalandığını göstermektedir.

| Başarısızlık modu | Açıklama | Doğrulama nasıl yakalar |
|---|---|---|
| Sahte DOI | Var olmayan bir DOI üretilir | Crossref API hata döndürür |
| Yanlış yıl | Gerçek makale, yanlış yayın yılı | Crossref künyesi yılı düzeltir |
| Hibrit yazar listesi | İki ayrı makalenin yazarları birleştirilir | Künye eşleştirme tutarsızlığı gösterir |
| Gerçek dergide hayali makale | Var olan dergi, var olmayan makale | DOI çözülmez, başlık bulunamaz |
| Yanlış sayfa aralığı | Gerçek makale, hatalı sayfa numaraları | Crossref sayfa alanı düzeltir |

Her başarısızlık modu pipeline'ın belirli bir adımında yakalanır. Bu, protokolün atıfları tek tek gözle taramaktan neden daha güçlü olduğunu tam olarak açıklar. Tek geçişli göz taraması akla yatkınlığı yakalar. Protokol gerçekliği yakalar.

## 9. Köşe Durumlar, DOI Olmayan Kaynaklar

Her kaynak DOI taşımaz. Bu durumlar da kendi disiplinini gerektirir. Kitaplar çoğunlukla DOI yerine ISBN taşır. Doğrulama ISBN üzerinden yayıncı kataloğuna ya da kütüphane kayıtlarına dayanır. Dijital kayıt standart hale gelmeden önce yayımlanan eski makalelerde DOI bulunmayabilir. Bu durumda dergi arşivi ya da kütüphane kaydı doğrulama kaynağı olur. Raporlar, tezler ve resmi belgelerden oluşan gri literatür de çoğunlukla DOI taşımaz. Doğrulama kurumsal kaynak üzerinden yapılır. YÖK Ulusal Tez Merkezi'nden alınan bir tez bu kategoriye girer.

DOI olmayan kaynaklar için temel kural şudur: doğrulama başka bir kalıcı tanımlayıcıya dayanmalıdır. ISBN, kurumsal arşiv URL'si ya da kütüphane kaydı. Önemli olan, atıfın gerçekliğinin orijinal iddiadan bağımsız bir kaynakla teyit edilmesidir. APA 7 (American Psychological Association, 2020) bu kaynak türleri için ayrı künye biçimleri tanımlar. DOI disiplini ise bu biçimlerden bağımsızdır. Disiplin stilde değil, doğrulama eyleminin kendisindedir.

## 10. Köprü, Etik Katmana

DOI hijyeni teknik görünür. Özü doğrudan etiktir. Hayali bir atıf yalnızca biçimsel bir hata değildir: bilimsel kaydı kirleten ve bu makaleyi ileride okuyan her araştırmacıyı yanıltan bir bütünlük ihlalidir. Bir sonraki kategori bu etik katmanı genişletir. Yapay zekâ destekli araştırmada etiğin sonradan eklenen bir bölüm değil baştan kurulan bir iş akışı belgesi olduğunu gösterir. Atıf doğrulama disiplini o etik iş akışının ilk ve en somut bileşenidir.

Araştırmacının hangi aracı kullandığı, ilk taslağı hangi modelin ürettiği, bibliyografyayı hangi pipeline'ın işlediği fark etmeksizin, bilimsel kaydın güvenilirliğini koruyan insanın kurduğu disiplindir. Bu değişmedi. Yalnızca riskin hacmi değişti.

## Kaynakça

Atıflar APA 7 biçimindedir. Tüm DOI'ler 2026-06-04 tarihinde Crossref üzerinden bağımsız olarak doğrulanmıştır.

American Psychological Association. (2020). *Publication manual of the American Psychological Association* (7th ed.). https://doi.org/10.1037/0000165-000

Bhattacharyya, M., Miller, V. M., Bhattacharyya, D., & Miller, L. E. (2023). High rates of fabricated and inaccurate references in ChatGPT-generated medical content. *Cureus*, 15(5), e39238. https://doi.org/10.7759/cureus.39238

Bramer, W. M., Rethlefsen, M. L., Kleijnen, J., & Franco, O. H. (2017). Optimal database combinations for literature searches in systematic reviews: A prospective exploratory study. *Systematic Reviews*, 6, 245. https://doi.org/10.1186/s13643-017-0644-y

Crossref. (2026). *Crossref REST API documentation*. https://api.crossref.org/swagger-ui

Else, H. (2023). Abstracts written by ChatGPT fool scientists. *Nature*, 613(7944), 423. https://doi.org/10.1038/d41586-023-00056-7

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, 26(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

International Committee of Medical Journal Editors. (2024). *Recommendations for the conduct, reporting, editing, and publication of scholarly work in medical journals*. https://www.icmje.org/recommendations/

National Library of Medicine. (2026). *PubMed user guide*. https://pubmed.ncbi.nlm.nih.gov/help/

Sallam, M. (2023). ChatGPT utility in healthcare education, research, and practice: Systematic review on the promising perspectives and valid concerns. *Healthcare*, 11(6), 887. https://doi.org/10.3390/healthcare11060887

Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, 13, Article 14045. https://doi.org/10.1038/s41598-023-41032-5

---

**Kitapçık kimliği.** `007-02-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-04
**Sözcük sayısı (yaklaşık).** 1936 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 10
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`004-01-0001`](../../004-vault-architecture/004-01-0001/tr.md). Klasör Disiplini ve Maps of Content (MOC) Kalıbı
**Sonraki kitapçık.** [`009-01-0001`](../../009-ethics-irb/009-01-0001/tr.md). Yapay Zekâ Destekli Araştırmada Etik, Prensipten Davranışa
