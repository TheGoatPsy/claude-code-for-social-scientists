---
title_en: "Systematic Reviews and Scoping Reviews, From Search to PRISMA Flow"
title_tr: "Sistematik Derleme ve Kapsam Derlemesi, Aramadan PRISMA Akışına"
booklet_id: "002-05-0001"
category: "002-academic-access"
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
    model_dated: null
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "co-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 10
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Sistematik Derleme ve Kapsam Derlemesi, Aramadan PRISMA Akışına

Önceki kitapçık, Türkçe, Yunanca ve İngilizce akademik literatüre güvenilir biçimde erişmenin altyapısını kurdu. DergiPark, ULAKBİM TR Dizin, HEAL Link ve YÖK Tez Merkezi ayrı ayrı bilindiğinde değerlidir. Ama derleme çalışmasında asıl sorun bunları tek bir denetlenebilir akışta birleştirmektir. Bu kitapçık tam da o noktadan başlar: erişim sağlandıktan sonra ne yapılacağından.

Sistematik derleme ve kapsam derlemesi, sosyal bilimci için yalnızca çok kaynak okumak değildir. Hangi sorunun sorulduğunu, hangi kaynakların nerede arandığını, hangi kayıtların neden elendiğini ve hangi kararların kim tarafından verildiğini gösterebilmektir. Bu ikisi arasındaki fark, metodolojik bir ayrıntı olarak geçiştirilemez. Çalışmanın başında yanlış türü seçmek, hem araştırma sorusunu hem de sonuçları şekillendirir.

Bu kitapçığın temel iddiası şudur: yapay zekâ başlık ve özet ön elemesini hızlandırabilir, arama günlüklerini düzenleyebilir, dışlama gerekçelerini sınıflayabilir. Ama dahil etme ve dışlama kararının son sahibi araştırmacıdır. PRISMA akışı, modelin değil araştırmacının hesap verebilirlik belgesidir. Bu kitapçık, o hesap verebilirlik zincirini başından sonuna inşa etmenin pratik yolunu gösterir.

## 1. Sistematik derleme ve kapsam derlemesi arasındaki fark

Sistematik derleme, genellikle belirli ve dar bir soruya belirli dahil etme ölçütleriyle yanıt arar. Çoğu zaman bulguları sentezlemeyi, bazen meta-analizle nicelleştirmeyi hedefler. Kapsam derlemesi ise daha farklı bir işlev üstlenir: bir alanın genişliğini, kavramlarını, yöntemsel çeşitliliğini ve araştırma boşluklarını haritalandırır. İkisi de sistematik arama ve raporlama disiplini gerektirir. Ama aynı amaçla yapılmaz.

Bu ayrım, çalışmanın ilk sayfasında net biçimde konulmazsa sonradan pahalıya mal olur. Alan henüz kavramsal olarak dağınıksa, temel tanımlar yerleşmemişse ya da hangi yöntemlerin konuyla ilgili olduğu belirsizse, kapsam derlemesi daha uygun başlangıç noktasıdır. Buna karşılık soru dardır, dahil etme ölçütleri önceden belirlenebilir durumdadır ve çalışmalar birbirleriyle karşılaştırılabilir nitelikteyse sistematik derleme daha güçlü bir zemin sunar. Higgins ve diğerleri (2019), sistematik derlemenin en ayırt edici özelliğinin önceden tanımlanmış yöntemler çerçevesinde yürütülmesi olduğunu vurgular.

Bu ayrımın açık yazılması, çalışmanın yöntem bölümünü doğrudan güçlendirir. Okur yalnızca ne yapıldığını değil, neden bu derleme türünün tercih edildiğini de görür. Yapay zekâ bu ayrımı açıklayabilir, iki tür arasındaki farkları karşılaştırmalı biçimde çıkarabilir. Ama hangi türün o araştırmaya daha uygun olduğuna araştırmacı karar verir. Model bu kararı veremez. Çünkü uygunluk, alandaki yerleşik pratiği, veri tabanı kapsamını ve araştırmacının zaman kaynaklarını birlikte dikkate almayı gerektirir.

## 2. Araştırma sorusunu yapılandırmak

Derleme sorusu gündelik meraktan farklıdır. Derleme sorusu, arama dizgesine ve dahil etme ölçütüne doğrudan dönüşebilen bir yapıya sahip olmalıdır. Bu yapıyı kazandırmak için soru çerçeveleme araçlarına başvurmak hem yöntembilimsel sağlamlık hem de araştırmacının zamanını korumak açısından değerlidir.

Klinik ve sağlıkla kesişen sorularda PICO çerçevesi yaygın olarak kullanılır: Popülasyon, Müdahale, Karşılaştırma, Sonuç. Nitel ve karma yöntemli çalışmalarda SPIDER çerçevesi daha esnektir: Örneklem, Olgu, Tasarım, Değerlendirme, Araştırma türü. Kapsam derleme sorularında ise PCC çerçevesi öne çıkar: Popülasyon, Kavram, Bağlam. Peters ve diğerleri (2020), JBI kılavuzlarında kapsam derlemeleri için PCC çerçevesinin nasıl uygulanacağını ayrıntılı biçimde gösterir.

Claude Code bu aşamada somut iş üstlenebilir: soru taslakları önerir, kavram eşdeğerlerini çıkarır, aynı soruyu farklı çerçevelere göre yeniden yazar. Ama modelin önerdiği her soru araştırılabilir değildir. Soru, kaynak alanının gerçekliği, veri tabanlarının kapsam sınırları ve araştırmacının zaman kaynakları içinde değerlendirilmelidir.

Bu aşamanın somut çıktısı bir soru çerçevesi dosyasıdır. O dosyada ana soru, alt sorular, kavramların dil karşılıkları, popülasyon ya da bağlam sınırı ve çalışma kapsamının dışında bırakılan alanlar açıkça yazılır. Bu dosya hem kayıt aracıdır hem de derleme boyunca ölçütlerin sürünmesini, yani başta belirlenen sınırların farkında varılmadan genişlemesini, önleyen bir ankaj noktasıdır.

## 3. Veri tabanı katmanları ve bölgesel arama

Sosyal bilimcinin derleme iş akışı yalnızca Web of Science ve Scopus ile kapanmaz. Bu veri tabanları geniş ve değerlidir. Ama Türkiye ve Yunanistan bağlamını taşıyan çalışmalar için zorunlu ama yeterli olmayan bir başlangıç noktasıdır. Bramer ve diğerleri (2017), sistematik derleme için hangi veri tabanı kombinasyonlarının en kapsamlı sonucu verdiğini deneysel olarak incelemiş ve tek bir veri tabanına bağlı kalmanın geri çağırma oranını belirgin biçimde düşürdüğünü göstermiştir.

Bu bulgunun Türkiye ve Yunanistan bağlamındaki yansıması doğrudandır. Türkçe literatür için DergiPark, ULAKBİM TR Dizin ve YÖK Tez Merkezi ayrı katmanlar olarak işlenmelidir. Yunanca ve uluslararası abonelikli literatür için HEAL Link ve kurumsal erişim yolları ayrıca planlanmalıdır. İki dilli ya da bölgesel konularda bu katmanlı yaklaşım özellikle belirleyicidir: bir çalışma uluslararası indekslerde görünmeyebilir, ama yerel alanda kuramsal ya da tarihsel olarak temel bir başvuru niteliği taşıyabilir.

Arama günlüğü her veri tabanı için ayrı tutulmalıdır. Hangi sorgu, hangi tarihte, hangi filtrelerle çalıştırıldığı, kaç kayıt döndüğü, kaç yinelenen kayıt olduğu. Bu sayılar sonradan hesap veremezsiniz, ancak baştan kaydedebilirsiniz. Ve bu sayılar daha sonra PRISMA akışının sayısal temelini oluşturur.

## 4. Arama dizgesi günlüğü

Arama dizgesi derlemenin iskeletidir. İyi bir arama dizgesi yalnızca anahtar kelime listesi değildir. Eş anlamlıları, varyant yazımları, dil karşılıklarını, Boolean bağlaçlarını ve veri tabanından veri tabanına değişen sözdizimi kurallarını içerir.

Somut bir örnek bu noktada açıklayıcıdır. Türkçe ve İngilizce sosyal kaygı literatürünü taramak isteyen bir araştırmacı için arama dizgesi şu katmanları taşımalıdır:

```
("sosyal kaygı" OR "sosyal fobi" OR "sosyal anksiyete")
AND
("social anxiety" OR "social phobia" OR "social anxiety disorder")
AND
("ergen*" OR "adolescent*" OR "genç*" OR "youth")
```

Aynı sorgu PsycINFO'da Thesaurus terimleriyle, PubMed'de MeSH terimleriyle, DergiPark'ta Türkçe başlık ve özet alanlarıyla yeniden uyarlanmalıdır. Claude Code bu uyarlamada somut katkı sağlayabilir: farklı veri tabanlarının sözdizimi kurallarını karşılaştırabilir, Türkçe ve İngilizce kavram eşdeğerlerini önerebilir, nihai dizgeyi denetlemek için kontrol soruları üretebilir.

Arama günlüğünde başarısız denemeler de saklanır. McGowan ve diğerleri (2016), PRESS kılavuzunda elektronik arama stratejilerinin akran değerlendirmesine tabi tutulması gerektiğini vurgular. Hangi sorgunun fazla gürültü ürettiği, hangisinin alanı yapay biçimde daralttığı, hangisinin yerel literatürü dışarıda bıraktığı, ileride hem yöntemsel bir güvence hem gerekirse hesap verebilirlik belgesi olur.

## 5. Dahil etme ve dışlama ölçütleri

Dahil etme ve dışlama ölçütleri veriye bakmadan önce yazılmalıdır. Bu kural yalnızca yöntembilimsel titizlik adına değil, aynı zamanda seçim yanlılığını önlemek için geçerlidir. Ölçütler veriye bakıldıktan sonra belirlenirse, farkında olmaksızın sonuçları destekler görünen çalışmaları dahil etme, desteklemeyenleri dışlama eğilimi güçlenir.

Ölçütler açık kategoriler içermelidir: yayın yılı aralığı, dahil edilen dil ya da diller, çalışma türü (örneğin yalnızca deneysel mi, nitel de dahil mi), örneklem tanımı, yöntemsel asgari standartlar, bağlam sınırı ve tam metne erişilebilirlik koşulu. Ölçütler fazla gevşekse çalışma büyür ve yönetilemez hale gelir. Fazla dar kurulursa alan yapay biçimde küçülür ve bulgular yetersiz temsil içerir.

Yapay zekâ ölçüt taslakları önerebilir, benzer derlemelerde kullanılan ölçütleri çıkarabilir ve ölçüt listesinin tutarlılığını denetleyebilir. Ancak ölçütlerin o alana özgü uygunluğunu araştırmacı belirler. Modelin "makul" dediği ölçüt, yerel literatürü ya da bölgesel yöntemsel gelenekleri dışarıda bırakıyorsa yöntembilimsel açıdan zayıftır.

Dışlama gerekçeleri standartlaştırılmalıdır. En yaygın gerekçe sınıfları şunlardır: tam metin erişilemiyor, yanlış popülasyon, yanlış sonuç değişkeni ya da kavram, uygun olmayan çalışma türü, yinelenen kayıt, kapsama alınan dil dışı. Bu gerekçe sınıflarının baştan tanımlanması, hem çift değerlendirici sürecinde hem PRISMA akışında hem de ek dosyalarda tutarlılık sağlar. Shamseer ve diğerleri (2015), PRISMA-P protokol raporlama rehberinde ölçütlerin protokol aşamasında yazılmış olmasının sonradan derleme sürecindeki kaymaları nasıl önlediğini gösterir.

## 6. Yapay zekâ destekli ön eleme

Başlık ve özet ön elemesinde yapay zekâ ciddi zaman tasarrufu sağlayabilir. Bin kaydı elle okumak ile yapay zekâ destekli ön sınıflama sonucunda şüpheli kayıtlara odaklanmak arasındaki fark, özellikle büyük derlemelerde belirleyicidir. Model, aday kayıtları dahil etme ölçütlerine göre sınıflayabilir, belirsiz kayıtları işaretleyebilir ve dışlama gerekçesi taslakları oluşturabilir.

Ama bu sınıflama bir karar değildir. Bir ön elemedir. Fark önemlidir.

En güvenli düzen çift katmanlıdır. Model önce aday sınıflama yapar ve belirsiz kayıtları işaretler. İnsan araştırmacı bu sınıflamayı denetler ve belirsiz kayıtları otomatik olarak dışlamaz: tam metin aşamasına taşır ya da ikinci değerlendiriciye gönderir. Modelin önerdiği dışlama kararı, araştırmacının onayı olmadan uygulanmaz.

Özellikle bölgesel ve çok dilli kaynaklarda model hatası daha olasıdır. Türkçe başlıkta kullanılan bir kavram, İngilizce literatürdeki karşılığıyla birebir örtüşmeyebilir. Yunanca bir terimin kuramsal ağırlığı, İngilizce özete tam olarak taşınmamış olabilir. Bu nedenle modelin dışlama önerileri, yerel dil ve bağlam bilgisiyle denetlenmelidir. Ouzzani ve diğerleri (2016), Rayyan uygulamasının çift kör değerlendirme düzenini nasıl desteklediğini gösterir. Yapay zekâ destekli ön eleme araçları da aynı ilkeyi taşımalıdır: modelin sınıflaması insan denetiminin yerini almaz.

## 7. Çift değerlendirici ve uyuşmazlık protokolü

Sistematik derleme geleneğinde çift değerlendirici düzeni güvenilirliğin temel güvencesidir. İki araştırmacı aynı kayıtları birbirinden bağımsız değerlendirir. Uyuşmazlıklar tartışılır. Gerekirse üçüncü kişi devreye girer. Yapay zekâ bu düzende üçüncü hakem değildir. En fazla yardımcı sınıflayıcı ya da ön eleme asistanı işlevi üstlenebilir.

Uyuşmazlık protokolü çalışmanın başında yazılmalıdır. Hangi durumlarda tam metne geçileceği, hangi durumlarda dışlama kararının netleşeceği, hangi durumlarda üçüncü değerlendiriciye gidileceği önceden belirlenmeli ve belgelenmelidir. Belirsizlik durumunda dışlamak yerine ilerletmek, yani şüpheli kaydı tam metin aşamasına taşımak, daha güvenli bir işlem ilkesidir. Potansiyel olarak dahil edilebilir bir çalışmayı erken elemek, potansiyel olarak dışlanması gereken birini tutmaktan daha pahalı bir hata üretir.

Bu protokol, derleme yayınında raporlanmalıdır. Okur yalnızca kaç kaydın dışlandığını değil, bu kararların nasıl verildiğini de görmelidir. Levac ve diğerleri (2010), kapsam derlemelerinde değerlendirici güvenilirliğinin nasıl artırılacağını tartışır ve sürecin şeffaflığının hem metodolojik değerlendirme hem de bulguların yorumlanması açısından merkezi olduğunu vurgular.

## 8. PRISMA akışına hazırlık

PRISMA akışı yalnızca bir şekil değildir. Derlemenin karar ekonomisini gösteren bir belgedir. Kaç kayıt bulundu, kaç yinelenen kayıt çıkarıldı, kaç başlık ve özet elendi ve hangi gerekçeyle, kaç tam metin incelendi, kaç çalışma sonunda dahil edildi. Bu sayıların her biri, arama günlüğünden ve eleme kayıtlarından gelmelidir. Page ve diğerleri (2021), PRISMA 2020 bildirgesinde akış diyagramının derleme boyunca nasıl besleneceğini ve hangi sayıların neye karşılık geldiğini ayrıntılı biçimde gösterir.

Claude Code bu sayıları tarama tablolarından çıkarabilir, yinelenen kayıtları işaretleyebilir ve PRISMA akışı için özet üretebilir. Ama sayısal tutarlılık insan tarafından denetlenmelidir. Bir kaydın iki kez sayılması, dışlama gerekçesinin yanlış sınıfa girmesi ya da farklı veri tabanlarından gelen yinelenenlerin gözden kaçması, derlemenin güvenilirliğini zedeler ve okurda soru işareti bırakır.

Akış diyagramı çalışmanın sonunda hatırlanarak çizilmez. Süreç boyunca beslenir. En sağlam PRISMA diyagramı, her arama ve eleme adımı tamamlandığında güncellenen, anlık kayıtlardan oluşur. Bunu sağlamanın pratik yolu, arama günlüğünü ve eleme tablolarını her oturumun ardından güncellemektir. Çalışmanın sonunda geriye dönük bir yeniden yapılandırma değil, birikimli bir kayıt hedeflenir.

Tricco ve diğerleri (2018), PRISMA-ScR genişlemesinde kapsam derleme raporlamasına özgü akış öğelerini tanımlar. Sistematik derleme ile kapsam derlemesinin akış diyagramları birbirinden farklı sütunlar ve adımlar içerebilir. Kullanılan derleme türüne karşılık gelen rapor şablonunun baştan belirlenmiş olması bu açıdan önemlidir.

## 9. Kaynak pasaportu ve atıf doğrulama

Derleme çalışmasında kaynak pasaportu yöntembilimsel bir zorunluluk haline gelir. Her kayıt şu bilgileri taşımalıdır: hangi veri tabanında, hangi sorguyla, hangi tarihte bulunduğu. DOI ya da alternatif kalıcı tanımlayıcısının doğrulanıp doğrulanmadığı. Başlık ve özet aşamasında mı, yoksa tam metin aşamasında mı elendiği ya da dahil edildiği. Dışlama gerekçesi.

DOI doğrulama, özellikle yapay zekâ destekli künye üretiminde merkezi bir güvenlik katmanıdır. Model doğru görünen ama var olmayan ya da yanlış makaleye işaret eden bir DOI üretebilir. Bu nedenle modelin önerdiği hiçbir kaynak, Crossref üzerinden bağımsız doğrulama yapılmadan kaynakçaya girmez. DOI yoksa ISBN, kurumsal URL, tez merkezi kaydı ya da yayıncı sayfası ikincil doğrulama noktası olarak kullanılır.

```bash
curl -LH "Accept: application/x-bibtex" https://doi.org/10.1136/bmj.n71
```

Bu komut, PRISMA 2020 makalesinin BibTeX künyesini Crossref üzerinden çeker. Aynı mantık derlemeye dahil edilen her kayıt için uygulanabilir. Kayıt künye bilgisiyle birlikte kaynak pasaportunun ilgili satırına eklenir. Derleme yalnızca dahil edilen çalışmaların değil, dışlanan kayıtların da izini tutar. Bu iz, hem yayın sonrası sorgulara yanıt vermenin hem de bulguların yeniden üretilebilirliğini güvence altına almanın zeminini oluşturur.

## 10. Skill protokolü ve çıktı paketi

Bu kitapçığın çalışan karşılığı `/prisma-scoping-review-pipeline` skill'idir. Skill, soru çerçevesini, arama dizgesi günlüğünü, veri tabanı katmanlarını, tarama tablosunu, dışlama gerekçelerini, PRISMA sayı özetini ve yapay zekâ katkı beyanını birlikte üretir. Her bileşen ayrı bir dosyaya kaydedilir ve birlikte araştırma arşivinin bir parçası haline gelir.

Çıktı paketi şu dosyalardan oluşmalıdır: `review-question.md` soru çerçevesini, alt soruları ve kavram karşılıklarını tutar. `search-log.md` her veri tabanı için arama sorgularını, tarihleri, filtreleri ve kayıt sayılarını içerir. `database-layer-map.md` hangi kaynağın hangi katmana girdiğini ve hangi erişim yoluyla bulunduğunu gösterir. `screening-table.csv` başlık ve özet aşamasındaki her kaydı ölçütlere göre sınıflar. `exclusion-reasons.csv` dışlama gerekçelerini standart kodlarla tutar. `prisma-counts.md` PRISMA akış diyagramı için sayısal özeti içerir. `source-passport-ledger.md` her kaydın DOI durumunu ve doğrulama sonucunu gösterir. `ai-disclosure-note.md` yapay zekânın hangi aşamada, ne ölçüde katkı sağladığını kaydeder.

Bu dosyalar bir arada olduğunda derleme yalnızca yazılmış bir metin olmaktan çıkar. Denetlenebilir, yeniden üretilebilir ve arşivlenebilir bir araştırma nesnesine dönüşür. Üçüncü bir araştırmacının aynı soruyu, aynı ölçütlerle, aynı kayıt izini takip ederek bağımsız biçimde değerlendirebilmesi, derlemenin bilimsel güvenilirliğinin en sağlam göstergesidir.

## Kaynakça

Atıflar APA 7 biçimindedir. Her DOI Crossref üzerinden bağımsız olarak doğrulanmıştır. Kurumsal URL'ler 2026-06-21 tarihi itibarıyla erişilebilir olduğu doğrulanmıştır.

Arksey, H., & O'Malley, L. (2005). Scoping studies: Towards a methodological framework. *International Journal of Social Research Methodology*, *8*(1), 19–32. https://doi.org/10.1080/1364557032000119616

Bramer, W. M., Rethlefsen, M. L., Kleijnen, J., & Franco, O. H. (2017). Optimal database combinations for literature searches in systematic reviews: A prospective exploratory study. *Systematic Reviews*, *6*(1), Article 245. https://doi.org/10.1186/s13643-017-0644-y

Higgins, J. P. T., Thomas, J., Chandler, J., Cumpston, M., Li, T., Page, M. J., & Welch, V. A. (Eds.). (2019). *Cochrane handbook for systematic reviews of interventions* (2nd ed.). Wiley. https://doi.org/10.1002/9781119536604

Levac, D., Colquhoun, H., & O'Brien, K. K. (2010). Scoping studies: Advancing the methodology. *Implementation Science*, *5*, Article 69. https://doi.org/10.1186/1748-5908-5-69

McGowan, J., Sampson, M., Salzwedel, D. M., Cogo, E., Foerster, V., & Lefebvre, C. (2016). PRESS peer review of electronic search strategies: 2015 guideline statement. *Journal of Clinical Epidemiology*, *75*, 40–46. https://doi.org/10.1016/j.jclinepi.2016.01.021

Ouzzani, M., Hammady, H., Fedorowicz, Z., & Elmagarmid, A. (2016). Rayyan: A web and mobile app for systematic reviews. *Systematic Reviews*, *5*, Article 210. https://doi.org/10.1186/s13643-016-0384-4

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., … Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ*, *372*, n71. https://doi.org/10.1136/bmj.n71

Peters, M. D. J., Marnie, C., Tricco, A. C., Pollock, D., Munn, Z., Alexander, L., McInerney, P., Godfrey, C. M., & Khalil, H. (2020). Updated methodological guidance for the conduct of scoping reviews. *JBI Evidence Synthesis*, *18*(10), 2119–2126. https://doi.org/10.11124/JBIES-20-00167

Shamseer, L., Moher, D., Clarke, M., Ghersi, D., Liberati, A., Petticrew, M., Shekelle, P., & Stewart, L. A. (2015). Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015: Elaboration and explanation. *BMJ*, *349*, g7647. https://doi.org/10.1136/bmj.g7647

Tricco, A. C., Lillie, E., Zarin, W., O'Brien, K. K., Colquhoun, H., Levac, D., Moher, D., Peters, M. D. J., Horsley, T., Weeks, L., Hempel, S., Akl, E. A., Chang, C., McGowan, J., Stewart, L., Hartling, L., Aldcroft, A., Wilson, M. G., Garritty, C., … Straus, S. E. (2018). PRISMA extension for scoping reviews (PRISMA-ScR): Checklist and explanation. *Annals of Internal Medicine*, *169*(7), 467–473. https://doi.org/10.7326/M18-0850

---

**Kitapçık kimliği.** `002-05-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1999 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 10
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`002-04-0001`](../002-04-0001/tr.md). DergiPark, ULAKBİM TR Dizin, HEAL Link ve Bölgesel İndeksleme
**Sonraki kitapçık.** [`003-01-0001`](../../003-memory-system/003-01-0001/tr.md). Hafızayı Arşive Dönüştürmek, İlkesel Bir Giriş
