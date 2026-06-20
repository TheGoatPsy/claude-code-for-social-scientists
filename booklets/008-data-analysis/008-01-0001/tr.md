---
title_en: "Reproducible Quantitative Workflows"
title_tr: "Yeniden Üretilebilir Nicel İş Akışları"
booklet_id: "008-01-0001"
category: "008-data-analysis"
language: "tr"
version: "0.1.0"
date_published: "2026-05-29"
date_last_revised: "2026-06-20"
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
human_review_date: "2026-06-20"
verified_citations_count: 10
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Yeniden Üretilebilir Nicel İş Akışları

Bu rehberin önceki kitapçıkları aracın ne olduğunu, sohbet penceresinden nasıl ayrıldığını, nasıl kurulduğunu ve hangi kalıcı talimatlarla yönetildiğini ele aldı. Bu kitapçık, sosyal bilimcinin coding agent ile en sık yaptığı işe odaklanır: nicel veri analizi. Anthropic'in 2026 yılında ABD ve Kanada'daki 1.260 nicel sosyal bilimciyle yürüttüğü tarama, ankete katılan coding agent kullanıcılarının büyük çoğunluğunun aracı kod üretmek için, en çok da nicel veriyi analiz etmek amacıyla kullandığını ortaya koyar (Lyttelton ve diğerleri, 2026). Bu çalışmayı okurken dikkatli bir araştırmacının kaydetmesi gereken bir sınır vardır: rapor Anthropic tarafından desteklenmiş, hakemli olmayan bir kaynaktır ve yayımcının incelenen konunun kendisi olmasından kaynaklanan yapısal bir çıkar çatışması taşır. Bu kısıtlama göz önünde tutularak, bulgu bağımsız araştırmanın genel çizgisiyle örtüşür: yapay zekâ yardımı, yapılandırılmış, tekrar eden ve yüksek hacimli görevlerde yoğunlaşır (Ziems ve diğerleri, 2024). Oysa analizi bir ajana devretmek, yeniden üretilebilirliği kendiliğinden getirmez. Tersine, yeni bir kırılganlık yaratır. Bu kitapçık, otonom analiz akışını dürüst ve yeniden üretilebilir tutmanın disiplinini ele alır.

## Ajan tabanlı analizin zor problemi

Bir ajan, bir veri setini ve bir araştırma fikrini alıp analizi yazabilir, çalıştırabilir, çıktıyı yorumlayabilir ve kendi başına yineleyebilir. Yukarıda belirtilen çıkar çatışması kısıtlamasını akılda tutarak okunması gereken Lyttelton ve diğerleri (2026) taraması, kullanımın tam da bu yönde yoğunlaştığını ortaya koyar. Bu yoğunlaşma hem gücün hem riskin kaynağıdır.

Hesaplamalı araştırmada yeniden üretilebilirlik, başkasının ya da aylar sonra aynı araştırmacının aynı veriden aynı sonuca ulaşabilmesi demektir (Peng, 2011). Bir ajan analizi saniyeler içinde ürettiğinde, ara kararlar, denenen yollar ve nihai koda götüren muhakeme görünmez kalabilir. Somut bir senaryo düşünün: örtük yanlılığı araştıran bir sosyal psikolog, anket verisi üzerinde bir regresyon çalıştırıyor. Ajan, birkaç geçerli değişken kodlaması ve model belirtimi arasında seçim yaparken bunların hiçbirini günlüğe geçirmiyor ve temiz görünümlü bir sonuç döndürüyor. On iki ay sonra bir ortak yazar bu sonucu yeniden üretemiyor. Sorun ajanın yetkinliği değil: bir kaydın yokluğudur.

Sandve ve diğerleri (2013), yeniden üretilebilir hesaplamalı araştırma için on basit kural sıralar. Bu kuralların özünde sürecin her adımının kaydedilmesi ve mümkün olduğunca otomatikleştirilmesi yatar. Wilson ve diğerleri (2017) bu talebi tüm yetkinlik düzeylerindeki bilimsel hesaplama için pratik bir çerçeveye taşır: sürüm denetimi, ortam yakalama ve veri işleme hattının otomasyonu. Ajan tabanlı analiz bu disiplini kolaylaştırmaz, aksine zorlaştırır. Hızın getirdiği kolaylık, kayıt tutma alışkanlığının önüne geçer. Sonuç bir saniyede gelirse onu nasıl ürettiğinizi yazmak gereksiz görünür. Oysa bir yıl sonra o sonucu yeniden üreten kişi için, tam da o kayıt belirleyicidir.

## İşi ajan yaptığında yeniden üretilebilir ne demek

Bir analiz, ancak çıktısına götüren süreç sabitlendiğinde yeniden üretilebilir olur. Ajan tabanlı bir akışta sürecin temel bileşenlerinin tamamı kayda geçmelidir.

Ajana verilen talimat, analizin asıl metnidir: kapsamını, varsayımlarını, dışlama ölçütlerini tanımlar. Model ve sürümü de kaydedilmelidir, çünkü aynı istem farklı bir modelde ya da farklı bir model sürümünde farklı kod üretebilir. Veri sürümü bir sağlama değeri ya da sürüm etiketiyle sabitlenmeli, hangi anlık görüntünün kullanıldığı belirsiz kalmamalıdır. Bölme, örnekleme ve önyükleme içeren her adım sabit bir rastgelelik tohumu olmadan her çalışmada farklı sonuç verir. Tohumun belirtim günlüğüne açıkça yazılması şarttır. Çalışma ortamı da bu kayıtların ayrılmaz parçasıdır: paket sürümleri, kod değişmemiş olsa bile sonucu sessizce değiştirebilir.

Bu bileşenler, bu rehberin daha önce tanıttığı iki kalıba doğrudan bağlanır. `CLAUDE.md`, modeli, talimatı ve sınırları sabitleyerek analizin yapay zekâ bileşenini belgeler (kitapçık 001-01-0004). İkinci kalıp ise istemleri, ara kararları ve veri pasaportlarını kalıcı bir klasörde toplayarak araştırma sürecini oturumlar arası izlenebilir kılan hafızayı arşive dönüştürme disiplinidir (kitapçık 003-01-0001). Bu kavram, bu rehberin araştırmacı pratiği için geliştirdiği işlevsel bir çerçevedir. Yerleşik bir akademik standart değildir. Birlikte, ajan tabanlı analizi tek seferlik bir sihir olmaktan çıkarıp belgelenmiş bir yordama dönüştürürler.

## Çatallanan yolların bahçesi, artık otomatik

Bir veri setinde sayısız geçerli analiz yolu vardır: hangi değişkenlerin dışlanacağı, hangi dönüşümün uygulanacağı, hangi alt grubun inceleneceği. Her seçim savunulabilir, her seçim farklı bir sonucu mümkün kılar. Gelman ve Loken (2014), bunu çatallanan yolların bahçesi olarak adlandırır. Araştırmacı tek bir hipotezi sınadığını sanırken, veriye bağlı kararlar görünmez bir çoklu karşılaştırmalar ağacı yaratır. Simmons ve diğerleri (2011), bu araştırmacı serbestlik derecelerinin, açıkça raporlanmadığında, neredeyse her sonucu istatistiksel olarak anlamlı gösterebileceğini deneysel olarak ortaya koyar.

Bir ajan bu sorunu kat kat büyütür. Ajan şikâyet etmez. Saatlik işi saniyeye sıkıştırır. Bir araştırmacının saatler harcayacağı onlarca belirtimi saniyeler içinde dener ve en temiz görüneni sunabilir. Niyet kötü olmasa bile, sonuç seçici raporlamadır. Yukarıda belirtilen çıkar çatışması kısıtlamasını göz önünde tutarak okunması gereken Lyttelton ve diğerleri (2026) taraması, ankete katılan araştırmacıların tam da bu riskten, yapay zekânın seçici raporlamayı ve riskten kaçınan artımsal araştırmayı kötüleştirmesinden çekindiğini kaydeder. Bu korku abartılı değildir. Ajan tabanlı hız, zaten var olan bir yöntemsel kırılganlığı elle tutulur, gerçek bir tehlikeye dönüştürür.

## Ön kayıt zihniyeti ve belirtim günlüğü

Bu tehlikenin panzehiri eskidir ve ajan tabanlı çağda öncekinden çok daha değerlidir. Ön kayıt, analiz planını veriye bakmadan, ajan tabanlı bağlamda ise en azından ajanı çalıştırmadan önce yazıya dökmektir. Nosek ve diğerleri (2018), ön kaydın doğrulayıcı ile keşfedici analizi verinin analistin seçimlerini etkileyemeyeceği bir noktada ayırarak serbestlik derecelerini kontrol altına aldığını savunur. Munafò ve diğerleri (2017), yeniden üretilebilir bilim için hazırladıkları yaygın atıf gören manifestoda, ön kaydı ve şeffaf raporlamayı alanın sağlamlığının yapısal temeli sayar. Bunlar, araştırmacının tercihine bırakılmış iyileştirmeler değildir. Alanın mimarisini kuran zorunluluklardır.

Ajan tabanlı akışta bunun somut hâli bir belirtim günlüğüdür: ajanı çalıştırmadan önce yazılan, planlanan analizi, asıl hipotezi ve önceden sabitlenmiş kararları kaydeden düz metin ya da Markdown bir dosya. Ajan keşif sırasında alternatif belirtimler denerse, bunların keşfedici nitelikte olduğu belirtilir. Doğrulayıcı sonucun yerine geçemezler. Plandan her sapma günlüğe gerekçesiyle birlikte işlenir. Böylece ajanın ürettiği zenginlik gizli bir balık avına değil, bir makaleyi zayıflatmak yerine güçlendiren açık bir duyarlılık analizine dönüşür.

## Bulan notlayan olamaz, istatistiğe uygulanmış

Bu rehberin tekrar eden ilkesi şudur: bir bulguyu üreten araç, aynı zamanda onu onaylayan merci olamaz. İstatistikte bu ilke iki kat önemlidir. Bir ajan, bir testin çıktısını yorumlarken çıktının kendisiyle çelişen bir özet sunabilir. Katsayının işaretini, anlamlılık eşiğini ya da etki büyüklüğünü yanlış aktarabilir. Bu nedenle ajanın yorumu her zaman ham çıktıya, yani tablodaki sayıya karşı bağımsız olarak doğrulanmalıdır. Asıl kriter tablodaki sayıdır.

Bu uyarının gerekçesi modelin yapısından gelir. Model, anlamadan istatistiksel örüntü üreten bir sistemdir ve en titiz talimatla bile bu risk ortadan kalkmaz (Bender ve diğerleri, 2021). Üretilen metin, bilgi üretimi açısından, doğru görünmek ile doğru olmak arasındaki farkı kendiliğinden gözetmeyen bir karaktere sahip olabilir (Hicks ve diğerleri, 2024). Bir regresyon tablosunun akıcı bir özeti, tablonun söylediği şeyi söylediği anlamına gelmez. Sonuç basittir: sayının kendisini oku. Yapısal disiplin olmadan ajan tabanlı analiz güvenilir olmaz. Onunla birlikte ise yeniden üretilebilir bir araç hâline gelir.

## Prosedürü devret, yargıyı devretme

Ajan tabanlı analizde devredilebilen ile devredilemeyen arasındaki çizgi, yeniden üretilebilirlik kadar önemlidir. Devredilebilenler tekrar eden yordamlardır: veriyi yükleme, önceden belirlenmiş plana göre dönüştürme, bir grafiği üretme, bir tabloyu biçimlendirme. Devredilemeyen ise istatistiksel yargıdır. Hangi testin veri yapısına uyduğu, hangi varsayımın alanın kuramsal kısıtları çerçevesinde savunulabilir olduğu, hangi gözlemin meşru biçimde dışlanabileceği ve bir etki büyüklüğünün kuramsal olarak ne anlam taşıdığı araştırmacıda kalır.

Bir ajan belirli bir test önerebilir ve gerekçesini açıklayabilir. Ama o gerekçenin geçerliliğine karar vermek, hem alanın kuramını hem de verinin bağlamını bilen araştırmacının işidir. Talimat dosyası yordamı araca devreder, yargıyı değil (kitapçık 001-01-0004). Ajan analizi hızlandırır, sorumluluğu ise araştırmacı üstlenir.

## Pratikte yeniden üretilebilir ajan tabanlı iş akışı

Bu disiplin, araştırmacının bizzat sahiplendiği somut bir dizi adıma iner.

Her rastgele adımda, her bölme, örnekleme ve önyükleme işleminde tohumu sabitleyin ve bu tohumu belirtim günlüğüne açıkça yazın. Çalışma ortamını yakalayın: paket sürümlerini bir kilit dosyasında dondurun ki analiz bir yıl sonra bugünküyle aynı ortamda çalışsın. Sonucu kesin saymadan önce analizi temiz bir oturumda baştan yeniden çalıştırın. Birikmiş duruma dayanan bir sonuç yeniden üretilebilir değildir. Ajanın izlediği yolu günlüğe yazın: hangi belirtimlerin denendiği ve seçilenin neden seçildiği kaydedilmelidir. Böylece makalenin yöntem bölümü gerçek analitik süreci yansıtır. Son olarak asıl istemi ve model sürümünü çıktının yanında arşivleyin, ayrı tutmayın. Böylece analizin yapay zekâ bileşeni, ne yapıldığını anlamak isteyen bir okuyucu için geri kazanılabilir olur.

Bu adımlar, Sandve ve diğerleri (2013) ile Wilson ve diğerleri (2017) tarafından ortaya konan ilkenin ajan tabanlı akışa taşınmış hâlidir: sürecin her adımını kaydedin ve otomatikleştirin. Talimat dosyası bir makalenin yöntem bölümünün makineye bakan yüzüyse, bu günlük de analizin sağlama defteridir. Bu disiplin olmadan ajanın hızı yeniden üretilebilirliği zayıflatır. Disiplinle birlikte ise ajan araştırmanın güvenilir bir parçasına dönüşür.

## Yapay zekânın analitik rolünün dürüst beyanı

Analizde kullanılan yapay zekâ, makalenin yöntem bölümünde ya da yapay zekâ katkı beyanında açıkça belirtilmelidir. Bir beyan tek başına yeterli değildir. Asıl önemli olan, yapay zekânın analizde nasıl ve hangi biçimlerde kullanıldığının okura açıkça anlatılmasıdır. Bu rehberin etik kitapçığı, beyanın prensipten davranışa nasıl indiğini gösterir (kitapçık 009-01-0001). Bu kitapçığın kendisi de bir örnektir: frontmatter bloğu, yapay zekâ araçlarının da okuyabildiği, onlara işin doğru yapılmasına yön veren yapılandırılmış bir bloktur. Blok, metnin büyük ölçüde yapay zekâ tarafından, insan onaylı bir taslak üzerinden yazıldığını ve yazar tarafından gözden geçirildiğini açıkça ortaya koyar. Aynı dürüstlük, bir ajanın yürüttüğü analiz için de geçerlidir.

Bu rehberdeki `AI-AUTHORSHIP.md` dosyası, kademelere ayrılmış bir katkı sınıflandırması sunar. Bu sınıflandırmanın ince bir ayrımını belirtmek gerekir: bu, rehber içinde araştırmacı pratiği için geliştirilmiş işlevsel bir tanımdır ve yerleşik bir akademik standart değildir. Ajan yalnızca kodu biçimlendirdiyse bu bir düzeydir. Analizi baştan sona tasarlayıp yürüttüyse bambaşka bir düzeydir. Araştırmacı, hangi kararın kendisine, hangisinin araca ait olduğunu kaydeder. Bu kayıt, hem yeniden üretilebilirliğin hem de bilimsel dürüstlüğün koşuludur. Lyttelton ve diğerleri (2026) taramasının verileri, taşıdığı çıkar çatışması kısıtlamasına karşın, ankete katılan araştırmacıların şeffaf beyanı ajan tabanlı analizin yarattığı nitelik kaybına karşı doğrudan bir yanıt saydığını ortaya koyar. Araştırmacı kaygısı ile beyan pratiği arasındaki bu örtüşme kayıt altına almaya ve üzerine harekete geçmeye değerdir.

## Bir sonraki kitapçık

Bu kitapçık, nicel ajan tabanlı iş akışlarının yeniden üretilebilirlik omurgasını kurdu. Veri analizi kategorisinin sonraki kitapçıkları bu temeli genişletecek: istatistiksel test seçiminde yapay zekâ danışma disiplini ve nitel kodlamada insan gözetimi. Bu arada, analizde yapay zekânın rolünün dürüst beyanı daha geniş bir etik çerçeveye oturur. Kitapçık 009-01-0001 buradan devam eder.

---

## Kaynakça

Atıflar APA 7 biçimindedir. Her DOI 2026-06-04 tarihinde Crossref üzerinden bağımsız olarak doğrulanmıştır. Lyttelton ve diğerleri (2026) Anthropic tarafından desteklenmiş gri literatürdür. DOI yayıncı sayfasına çözümlenir. Wilson ve diğerleri (2017) 2026-06-04 tarihinde eklendi.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610-623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Gelman, A., & Loken, E. (2014). The statistical crisis in science. *American Scientist*, 102(6), 460. https://doi.org/10.1511/2014.111.460

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, 26(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Lyttelton, T., Massenkoff, M., & Wilmers, N. (2026). *Coding agents in the social sciences* [Anthropic tarafından desteklenmiş rapor, gri literatür, çıkar çatışması: yayıncı çalışmanın incelediği konunun kendisidir]. Anthropic. https://www.anthropic.com/research/coding-agents-social-sciences

Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J., & Ioannidis, J. P. A. (2017). A manifesto for reproducible science. *Nature Human Behaviour*, 1(1), Article 0021. https://doi.org/10.1038/s41562-016-0021

Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, 115(11), 2600-2606. https://doi.org/10.1073/pnas.1708274114

Peng, R. D. (2011). Reproducible research in computational science. *Science*, 334(6060), 1226-1227. https://doi.org/10.1126/science.1213847

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, 9(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychological Science*, 22(11), 1359-1366. https://doi.org/10.1177/0956797611417632

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLoS Computational Biology*, 13(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510

Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2024). Can large language models transform computational social science? *Computational Linguistics*, 50(1), 237-291. https://doi.org/10.1162/coli_a_00502

---

**Kitapçık kimliği.** `008-01-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-20
**Sözcük sayısı (yaklaşık).** 1561 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 10
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`007-02-0001`](../../007-academic-writing/007-02-0001/tr.md). DOI Disiplini ile APA 7
**Sonraki kitapçık.** [`009-01-0001`](../../009-ethics-irb/009-01-0001/tr.md). Yapay Zekâ Destekli Araştırmada Etik, Prensipten Davranışa
