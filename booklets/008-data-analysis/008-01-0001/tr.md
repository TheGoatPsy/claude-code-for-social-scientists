---
title_en: "Reproducible Quantitative Workflows"
title_tr: "Yeniden Üretilebilir Nicel İş Akışları"
booklet_id: "008-01-0001"
category: "008-data-analysis"
language: "tr"
version: "0.2.0"
date_published: "2026-05-29"
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
    model_dated: null  # Anthropic, Opus 4.8 için tarihli tanımlayıcı yayımlamadı (2026-05-29)
    role: "drafting, verification, citation lookup, bilingual authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 11
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Yeniden Üretilebilir Nicel İş Akışları

Bu kitapçık, sosyal bilimcinin kodlama ajanlarıyla en sık yaptığı işlerden birine odaklanır: nicel veri analizi. Önceki kitapçıklar aracın ne olduğunu, nasıl kurulduğunu, hangi kalıcı talimatlarla yönetileceğini ve akademik yazı sürecinde nasıl kullanılacağını ele almıştı. Burada mesele artık doğrudan analitik iş akışıdır. Bir veri seti, bir araştırma sorusu ve bir ajan aynı çalışma dizininde buluştuğunda, araştırmacının ilk sorumluluğu hız değil, yeniden üretilebilirliktir.

Anthropic'in 2026 yılında ABD ve Kanada'daki 1.260 nicel sosyal bilimciyle yürüttüğü tarama, ankete katılan kodlama ajanı kullanıcılarının aracı en çok kod üretmek ve nicel veriyi analiz etmek için kullandığını göstermektedir (Lyttelton ve diğerleri, 2026). Bu rapor hakemli bir yayın değildir ve Anthropic tarafından desteklenmiştir. Dolayısıyla çalışmanın yayıncısı, aynı zamanda incelenen teknolojinin üreticisidir. Bu çıkar çatışması açıkça not edilmelidir. Bununla birlikte bulgu, yapay zekâ yardımının yapılandırılmış, tekrarlı ve yüksek hacimli görevlerde yoğunlaştığını gösteren bağımsız literatürle de uyumludur (Ziems ve diğerleri, 2024).

Bu kitapçığın temel iddiası şudur. Ajan tabanlı analiz, nicel sosyal bilim araştırmalarında ciddi bir verimlilik sağlayabilir. Ancak bu verimlilik yalnızca belirtim günlüğü, sabit tohum, veri sürümü, çalışma ortamı kaydı, insan denetimi ve açık beyanla birlikte akademik değer taşır. Aksi durumda hız, yeniden üretilebilirliği güçlendirmek yerine zayıflatır.

## 1. Ajan Tabanlı Analizin Zor Problemi

Bir ajan, bir veri setini ve bir araştırma fikrini alıp analiz kodu yazabilir, çalıştırabilir, çıktıyı yorumlayabilir ve kendi önerilerini yineleyebilir. Bu kapasite, araştırmacının zamanını azaltabilir. Ancak aynı kapasite, analizin hangi ara kararlarla şekillendiğini görünmez hâle getirebilir. Nicel analizde sorun çoğu zaman yalnızca yanlış kod yazılması değildir. Asıl sorun, doğru görünen bir sonuca hangi karar yoluyla ulaşıldığının kayıt dışı kalmasıdır.

Hesaplamalı araştırmada yeniden üretilebilirlik, aynı veriden aynı sonuca yeniden ulaşılabilmesi anlamına gelir (Peng, 2011). Bu tanım, ajan tabanlı analizde daha da önem kazanır. Çünkü ajan saniyeler içinde çok sayıda dönüşüm, model belirtimi, dışlama ölçütü ve tablo üretim adımı deneyebilir. Araştırmacı bu adımların hangilerinin denendiğini, hangisinin seçildiğini ve neden seçildiğini kaydetmezse, sonucun bilimsel statüsü zayıflar.

Somut bir örnek düşünelim. Örtük yanlılığı çalışan bir sosyal psikolog, anket verisi üzerinde regresyon modeli kuruyor. Ajan birkaç değişken kodlaması, birkaç dışlama ölçütü ve iki model belirtimi arasında seçim yapıyor. Sonuç temiz görünüyor. Tablo düzenli, p-değerleri makul, metin akıcı. Ancak on iki ay sonra ortak yazarlardan biri analizi yeniden üretmek istediğinde aynı sonuca ulaşamıyor. Burada sorun ajanın yetersizliği değildir. Sorun, karar yolunun kaydedilmemiş olmasıdır.

Sandve ve diğerleri (2013), yeniden üretilebilir hesaplamalı araştırma için sürecin her adımının kaydedilmesi ve mümkün olduğunca otomatikleştirilmesi gerektiğini vurgular. Wilson ve diğerleri (2017) bu ilkeyi bilimsel hesaplama pratiğine taşır. Sürüm denetimi, ortam yakalama ve veri işleme hattının otomasyonu yalnızca yazılım mühendisliği ayrıntısı değildir. Nicel sosyal bilimci için de bilimsel güvenilirliğin altyapısıdır. Ajan tabanlı analiz bu gerekliliği azaltmaz. Tam tersine, daha görünür hâle getirir.

## 2. İşi Ajan Yaptığında Yeniden Üretilebilirlik Ne Demek?

Bir analizin yeniden üretilebilir sayılabilmesi için yalnızca çıktısının saklanması yetmez. O çıktıya götüren yolun da sabitlenmesi gerekir. Ajan tabanlı bir akışta bu yol birkaç bileşenden oluşur. Ajana verilen istem, kullanılan model ve sürüm, veri setinin sürümü, rastgelelik tohumu, paket sürümleri, çalıştırılan kod ve ara kararlar kaydedilmelidir.

Ajana verilen talimat analizin yöntemsel metnidir. Hangi değişkenlerin kullanılacağını, hangi dışlama ölçütlerinin uygulanacağını, hangi modelin öncelikli olduğunu ve hangi çıktının beklendiğini belirler. Model ve sürüm kaydı da önemlidir. Aynı istem farklı bir modelde ya da farklı bir model sürümünde farklı kod üretebilir. Veri sürümü sabitlenmezse aynı dosyanın hangi anlık görüntüsünün kullanıldığı belirsiz kalır. Rastgelelik tohumu yazılmazsa örnekleme, bölme ve önyükleme adımları her çalıştırmada farklı sonuç verebilir.

Bu bileşenler rehberin önceki kitapçıklarında kurulan iki kalıba bağlanır. CLAUDE.md, modelin talimat ve sınırlarını belgeleyen kalıcı talimat dosyasıdır. Hafızayı arşive dönüştürme kalıbı ise istemleri, veri pasaportlarını, ara kararları ve çıktı kayıtlarını kalıcı bir klasör düzeninde tutar. Bu iki kalıp yerleşik akademik standartlar olarak değil, bu rehberin araştırmacı pratiği için geliştirdiği uygulayıcı çerçeveler olarak sunulmaktadır. Birlikte, ajan tabanlı analizi tek oturumluk bir işlem olmaktan çıkarıp izlenebilir bir iş akışına dönüştürürler.

## 3. Çatallanan Yolların Bahçesi Artık Otomatik

Bir veri setinde çoğu zaman birden fazla savunulabilir analiz yolu vardır. Hangi değişkenlerin dışlanacağı, hangi dönüşümün uygulanacağı, hangi alt grubun analiz edileceği ve hangi model belirtiminin kullanılacağı sonuçları değiştirebilir. Gelman ve Loken (2014), bu durumu çatallanan yolların bahçesi olarak adlandırır. Araştırmacı tek bir hipotezi sınadığını düşünebilir, ancak veriye bağlı kararlar görünmez bir çoklu karşılaştırmalar ağacı üretir.

Simmons ve diğerleri (2011), açıkça raporlanmayan araştırmacı serbestlik derecelerinin neredeyse her sonucu anlamlı gösterebileceğini deneysel olarak ortaya koymuştur. Ajan tabanlı analiz bu riski büyütür. Çünkü ajan yorulmaz, beklemez, itiraz etmez. Araştırmacının saatlerce sürecek biçimde deneyebileceği alternatifleri saniyeler içinde çalıştırabilir. En temiz görünen sonucu sunabilir. Niyet kötü olmasa bile, kayıt tutulmadığında bu süreç seçici raporlamaya dönüşebilir.

Lyttelton ve diğerleri (2026) raporunda, ankete katılan sosyal bilimcilerin yapay zekânın seçici raporlamayı ve riskten kaçınan artımsal araştırmayı kötüleştirebileceğinden kaygı duyduğu belirtilmektedir. Raporun gri literatür ve satıcı kaynaklı olduğu unutulmamalıdır. Yine de kaygının kendisi yöntemsel olarak ciddidir. Ajan tabanlı hız, zaten var olan kırılganlığı görünmez biçimde büyütebilir.

## 4. Ön Kayıt Zihniyeti ve Belirtim Günlüğü

Bu riskin en güçlü panzehirlerinden biri ön kayıt zihniyetidir. Ön kayıt, analitik kararların veriye bakmadan önce yazıya dökülmesidir. Ajan tabanlı analizde bu, en azından ajanı çalıştırmadan önce planlanan analizin ve birincil hipotezin kaydedilmesi anlamına gelir. Nosek ve diğerleri (2018), ön kaydın doğrulayıcı analiz ile keşfedici analizi birbirinden ayırarak araştırmacı serbestlik derecelerini daha görünür kıldığını savunur. Munafò ve diğerleri (2017), ön kayıt ve şeffaf raporlamayı yeniden üretilebilir bilimin yapısal temelleri arasında konumlandırır.

Bu kitapçığın pratik önerisi belirtim günlüğüdür. Belirtim günlüğü, ajanı çalıştırmadan önce yazılan ve planlanan analizi, asıl hipotezi, kullanılacak değişkenleri, dışlama ölçütlerini, model belirtimini ve rastgelelik tohumunu kaydeden düz metin ya da Markdown dosyasıdır. Ajan keşif sırasında alternatif belirtimler denerse, bunlar keşfedici olarak işaretlenir. Doğrulayıcı sonucun yerine geçmezler.

Plandan her sapma gerekçesiyle birlikte günlüğe yazılır. Böylece ajanın ürettiği analitik zenginlik gizli bir balık avına değil, açık bir duyarlılık analizine dönüşür. Bu kayıt, makaleyi zayıflatmaz. Tam tersine, hakem karşısında savunulabilir hâle getirir.

## 5. Bulan Notlayan Olamaz, İstatistiğe Uygulanmış

Bu rehberin tekrar eden ilkesi şudur. Bir bulguyu üreten araç, aynı zamanda o bulguyu onaylayan merci olamaz. İstatistikte bu ilke iki kat önemlidir. Bir ajan, bir testin çıktısını yorumlarken katsayının işaretini, anlamlılık eşiğini, güven aralığını ya da etki büyüklüğünü yanlış aktarabilir. Bu nedenle ajanın yorumu her zaman ham çıktıya karşı bağımsız olarak doğrulanmalıdır. Asıl ölçüt tablodaki sayıdır.

Bu uyarının gerekçesi modelin yapısında yatar. Büyük dil modelleri gerçek bir anlayışa sahip olmaksızın istatistiksel örüntüler üretebilir (Bender ve diğerleri, 2021). Ürettikleri metin, doğru görünmek ile doğru olmak arasındaki farkı kendiliğinden gözetmeyebilir (Hicks ve diğerleri, 2024). Bir regresyon tablosunun akıcı bir özeti, tablonun gerçekten söylediği şeyi söylediği anlamına gelmez.

Araştırmacı bu nedenle sayıyı kendisi okumalıdır. Ajanın yorumunu ham çıktıya karşı doğrulanması gereken bir taslak olarak ele almalıdır. Yapısal disiplin olmadan ajan tabanlı analiz güvenilir olmaz. Disiplinle birlikte ise yeniden üretilebilir bir çalışma aracına dönüşebilir.

## 6. Prosedürü Devret, Yargıyı Devretme

Ajan tabanlı analizde devredilebilen ile devredilemeyen arasındaki çizgi net tutulmalıdır. Devredilebilenler tekrar eden yordamlardır. Veriyi yüklemek, önceden belirlenmiş plana göre dönüştürmek, bir grafiği üretmek, bir tabloyu biçimlendirmek ve kodu çalıştırmak bu gruba girer.

Devredilemeyen ise istatistiksel yargıdır. Hangi testin veri yapısına uygun olduğu, hangi varsayımın alanın kuramsal kısıtları içinde savunulabilir olduğu, hangi gözlemin dışlanabileceği ve bir etki büyüklüğünün kuramsal anlamı araştırmacıda kalır. Ajan belirli bir test önerebilir. Ancak o gerekçenin geçerli olup olmadığına karar vermek, alanın kuramını ve verinin bağlamını bilen araştırmacının işidir.

Talimat dosyası yordamı araca devredebilir. Yargıyı devredemez. Ajan analizi hızlandırır. Bilimsel sorumluluğu araştırmacı üstlenir.

## 7. Pratikte Yeniden Üretilebilir Ajan Tabanlı İş Akışı

Bu disiplin, araştırmacının bizzat sahiplenmesi gereken somut adımlara iner. Her rastgele adımda, her bölme, örnekleme ve önyükleme işleminde tohum sabitlenmeli ve belirtim günlüğüne yazılmalıdır. Çalışma ortamı yakalanmalıdır. Paket sürümleri kilit dosyasında tutulmalı, analiz bir yıl sonra aynı ortamda yeniden çalıştırılabilmelidir.

Sonuç kesin kabul edilmeden önce analiz temiz bir oturumda baştan çalıştırılmalıdır. Birikmiş oturum durumuna dayanan sonuç yeniden üretilebilir değildir. Ajanın izlediği yol kaydedilmelidir. Hangi belirtimlerin denendiği, hangisinin seçildiği ve neden seçildiği açık olmalıdır. Asıl istem ve model sürümü çıktının yanında arşivlenmelidir.

Bu adımlar, Sandve ve diğerleri (2013) ile Wilson ve diğerleri (2017) tarafından ortaya konan ilkelerin ajan tabanlı akışa taşınmış biçimidir. Sürecin her adımı kaydedilir. Tekrar eden kısımlar otomatikleştirilir. Son karar araştırmacıda kalır.

## 8. Yapay Zekânın Analitik Rolünün Dürüst Beyanı

Analizde yapay zekâ kullanıldıysa, bu kullanım yöntem bölümünde ya da yapay zekâ katkı beyanında açıkça belirtilmelidir. Bir beyan tek başına yeterli değildir. Okur, yapay zekânın analizde nasıl ve hangi aşamalarda kullanıldığını anlayabilmelidir.

Bu rehberdeki AI-AUTHORSHIP.md dosyası, yapay zekâ katkısını farklı düzeylerde sınıflandıran işlevsel bir çerçeve sunar. Bu sınıflandırma yerleşik bir akademik standart değildir. Rehber içinde araştırmacı pratiğini düzenlemek için geliştirilmiş bir uygulayıcı tanımdır. Ajan yalnızca kodu biçimlendirdiyse bu bir düzeydir. Analizi baştan sona tasarlayıp yürüttüyse bambaşka bir düzeydir.

Araştırmacı, hangi kararın kendisine, hangisinin araca ait olduğunu kaydetmelidir. Bu kayıt, hem yeniden üretilebilirliğin hem de bilimsel dürüstlüğün koşuludur. Lyttelton ve diğerleri (2026) raporu, çıkar çatışması sınırlılığına karşın, araştırmacıların şeffaf beyanı ajan tabanlı analizin yaratabileceği nitelik kaybına karşı önemli bir yanıt olarak gördüğünü göstermektedir.

## 9. Bir Sonraki Kitapçık

Bu kitapçık, nicel ajan tabanlı iş akışlarının yeniden üretilebilirlik omurgasını kurdu. Veri analizi kategorisinin sonraki kitapçıkları bu temeli genişletecektir. İstatistiksel test seçiminde yapay zekâ danışma disiplini ve nitel kodlamada insan gözetimi bu çerçevenin iki devam hattıdır.

Analizde yapay zekânın rolünün dürüst beyanı ise daha geniş bir etik çerçeveye bağlanır. 009-01-0001, Yapay Zekâ Destekli Araştırmada Etik, Prensipten Davranışa, bu noktadan devam eder.

---

## Kaynakça

Atıflar APA 7 biçimindedir. Her DOI 2026-06-21 tarihinde Crossref üzerinden bağımsız olarak doğrulanmıştır. Lyttelton ve diğerleri (2026) Anthropic tarafından desteklenmiş gri literatürdür. DOI yayıncı sayfasına çözümlenir. Wilson ve diğerleri (2017) 2026-06-04 tarihinde eklendi.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610–623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Gelman, A., & Loken, E. (2014). The statistical crisis in science. *American Scientist*, *102*(6), 460. https://doi.org/10.1511/2014.111.460

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, *26*(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Lyttelton, T., Massenkoff, M., & Wilmers, N. (2026). *Coding agents in the social sciences* [Anthropic tarafından desteklenmiş rapor, gri literatür, çıkar çatışması: yayıncı çalışmanın incelediği konunun kendisidir]. Anthropic. https://www.anthropic.com/research/coding-agents-social-sciences

Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J., & Ioannidis, J. P. A. (2017). A manifesto for reproducible science. *Nature Human Behaviour*, *1*(1), Article 0021. https://doi.org/10.1038/s41562-016-0021

Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, *115*(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114

Peng, R. D. (2011). Reproducible research in computational science. *Science*, *334*(6060), 1226–1227. https://doi.org/10.1126/science.1213847

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, *9*(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychological Science*, *22*(11), 1359–1366. https://doi.org/10.1177/0956797611417632

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLoS Computational Biology*, *13*(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510

Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2024). Can large language models transform computational social science? *Computational Linguistics*, *50*(1), 237–291. https://doi.org/10.1162/coli_a_00502

---

**Kitapçık kimliği.** `008-01-0001`
**Sürüm.** `0.2.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1524 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 11
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`007-02-0001`](../../007-academic-writing/007-02-0001/tr.md). DOI Disiplini ile APA 7
**Sonraki kitapçık.** [`009-01-0001`](../../009-ethics-irb/009-01-0001/tr.md). Yapay Zekâ Destekli Araştırmada Etik, İlkeden Davranışa
