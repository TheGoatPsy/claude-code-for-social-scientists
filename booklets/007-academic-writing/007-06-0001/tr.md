---
title_en: "Grant Proposals and Project Texts, From Idea to Work Package"
title_tr: "Proje Başvurusu ve Hibe Metni, Fikirden İş Paketine"
booklet_id: "007-06-0001"
category: "007-academic-writing"
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

# Proje Başvurusu ve Hibe Metni, Fikirden İş Paketine

Bir araştırma fikri ile bir proje başvurusu arasındaki mesafe çoğu zaman küçümsenir. Makale yazmak biten bir çalışmayı anlatmaktır. Başvuru metni ise henüz olmayan bir şeyi, ama olabilirliği kanıtlanmış biçimde, karşı tarafa göstermektir. Bu fark dilin niteliğini, argümanın yapısını ve sorumluluğun dağılımını kökten değiştirir. Sosyal bilimcinin bu türde karşılaştığı güçlük yalnızca teknik değildir. Gelecek zamanı güvenilir kılmak, kısıtlar içinde düşünce özgürlüğünü korumak ve hakem kurulunun farklı beklentilerini tek metinde karşılamak da bu güçlüğün parçasıdır. Yapay zekâ bu süreçte ciddi bir yardımcıya dönüşebilir. Ama aynı süreç yapay zekânın en sık yanlış yönlendirdiği alandır: aşırı vaat, şişirilmiş etki ve takvim iyimserliği modelin varsayılan eğilimleridir. Bir başvuru metninin hakem kurulunu ikna etmesi için yalnızca fikrin sağlamlığı değil, projenin nasıl yapılacağına dair somut bir planın varlığı gerekir. Bu kitapçık, fikri iş paketine dönüştürme sürecinin her aşamasını ele alır ve yapay zekânın nerede gerçekten işe yaradığını, nerede araştırmacının derinlemesine düşünmesinin zorunlu olduğunu gösterir.

## 1. Araştırma Fikri ile Proje Fikri Arasındaki Fark

Araştırma fikri meraktan doğar. Bir örüntüyü açıklamak, bir çelişkiyi çözmek ya da mevcut alanyazının görmezden geldiği bir soruyu sormak, bir araştırmacıyı yıllarca sürdürebilir. Bu merak özüyle özgürdür: sınır koymaz, kaynak hesaplamaz, başarısızlık takvimi tutmaz. Proje fikri ise bu özgürlüğün sistematik olarak kısıtlandığı formdur. Sınırlı bir süre, sınırlı bir bütçe, belirlenmiş bir fon çağrısı ve somut teslim edilebilirler. Her iyi araştırma fikri iyi bir proje değildir. Proje, uygulanabilirliği kanıtlanmış fikirdir.

Bu dönüşümün ilk adımı uygulanabilirlik sorusunu dürüstçe sormaktır. Soru üç yılda yanıtlanabilir mi? Ekip bu yöntemi gerçekten uygulayabilir mi? Etik kurul süreci öngörülen takvime sığar mı? Saha erişimi güvenceli mi? Locke, Spirduso ve Silverman (2014), tez ve hibe başvuruları üzerine yazdıkları kapsamlı rehberde bu kısıtların proje planlamasının başında masaya yatırılması gerektiğini vurgular. Kısıtlar sona bırakıldığında başvuru metni şişirilmiş bir fikir üzerine kurulur ve hakem kurulları bunu dokümanda hisseder.

Claude Code bu dönüşümde iki somut işe yarar. Birincisi, araştırma sorusunu fon çağrısının öncelik alanlarıyla karşılaştıran bir eşleştirme taslağı çıkarabilir. İkincisi, bir fikri somut çıktılara ve sorumluluklara bölmek için ilk soru listesini hazırlayabilir. Ama uygulanabilirliğin gerçek değerlendirmesi araştırmacıya aittir: saha, ekip kapasitesi, kurumsal destek ve yerel kısıtlar model tarafından bilinemez.

Fon çağrısı ile araştırma fikri arasındaki stratejik uyum da bu aşamada kurulur. TÜBİTAK 1001 programı Türkiye'de yürütülen temel araştırmaları, Horizon Europe ise uluslararası ortaklık gerektiren uygulamalı projeleri öncelikli olarak destekler. Bu iki programın beklenti dili, değerlendirme ağırlıkları ve bütçe tavan normları birbirinden belirgin biçimde ayrılır. Araştırmacının aynı fikri farklı çağrılara uyarlarken her çağrının mantığını içselleştirmesi gerekir. Model bu uyarlama sürecinde taslak üretebilir, ancak çağrı panelinin gerçek beklentisini araştırmacının geçmiş hakem deneyiminden ya da çağrı yorumlarından öğrenmesi gerekir.

## 2. Problem, Amaç, Hedef ve Çıktı

Başvuru metinlerinde en sık birbirine karışan dört kavram vardır: problem, amaç, hedef ve çıktı. Bunların birbirinden ayrılmaması, teknik açıdan birbiriyle tutarsız başvurulara neden olur. Hakem değerlendirmelerinde en yaygın reddedilme gerekçelerinden biri de bu tutarsızlıktır.

Problem, neden çalışmaya ihtiyaç olduğunu gösterir. Alanyazındaki boşluk, toplumsal ya da politika düzeyindeki eksiklik, mevcut ölçüm araçlarının yetersizliği, çelişkili bulgular: bunların hepsi birer problem çerçevesidir. Amaç, projenin genel yönünü ifade eder. Somut değil, yönelimseldir. Hedefler ise amacı ölçülebilir ve zaman-sınırlı adımlara kırar. İyi hedef SMART ölçütlerine uyar: özgün, ölçülebilir, ulaşılabilir, ilgili ve zamanlı. Çıktılar ise projenin sonunda fiilen teslim edilecek ürünlerdir: veri seti, rapor, yayın, politika özeti, eğitim materyali. Her çıktı en az bir hedefe bağlıdır. Hiçbir hedef çıktısız kalmaz.

Bu dört katmanı net biçimde ayıran bir tablo, hem başvurucunun kendi kafasını toplamasını hem de hakem kurulunun değerlendirme sürecini kolaylaştırır. Sık yapılan bir hata, amacı hedefle, hedefi ise çıktıyla özdeşleştirmektir. "Psikolojik dayanıklılık mekanizmalarını anlamak" bir amaçtır. "Birinci ay sonunda ölçek uyarlama tamamlanmış olacak" bir hedeftir. "Hakemli bir dergide yayımlanmış ölçek uyarlama makalesi" ise bir çıktıdır. Bu ayrım sayfalarca genel ifadeden daha fazlasını anlatır. Claude Code bu tabloyu operatörün verdiği ham notlardan oluşturabilir. Ancak her hedefin gerçekten ölçülebilir olup olmadığını ve her çıktının proje süresi içinde teslim edilebilir olduğunu kontrol etmek araştırmacıya aittir. Przeworski ve Salomon (1995), araştırma önerilerinde netlik ve özlülüğün hakem ikna sürecinin merkezinde yer aldığını belirtir. Gösteriş, derinliğin yerini tutmaz. Gerçekçilik ise en güvenilir ikna biçimidir.

## 3. İş Paketi Mantığı

İş paketi, projenin yürütülebilir birimidir. Fon çağrısına bağlı olarak WP (Work Package) ya da Task adıyla anılır. Her iş paketi altı temel bileşeni barındırır: sorumlu kişi veya kurum, süre ve takvim, görev listesi, ara çıktılar (deliverables), riskler ve bağımlılıklar. İyi iş paketi, hakemlere şunu gösterir: bu projenin iyi düşünülmüş olması yetmez, nasıl yürütüleceği de bilinmektedir.

İş paketinin yazımında sık rastlanan iki hata birbirinin tersidir. İlki iş paketini genel hedefin tekrarına indirgemektir. Bu yaklaşım icraatı gizler ve hakemin güvenini sarsar. İkincisi ise iş paketini aşırı ayrıntıyla doldurmak ve ana argümanı görünmez kılmaktır. İyi iş paketi, proje dışındaki bir okuyucunun hangi kişinin hangi ayda ne yapacağını ve bu çalışmanın hangi çıktıya hizmet ettiğini anlayabileceği bir netlikte yazılır.

Yapay zekâ iş paketi taslağı üretebilir. Bu taslak, hangi görevlerin hangi iş paketine girdiğine dair başlangıç noktası olarak işe yarar. Ancak gerçek kapasite hesaplaması, araştırma asistanı başına haftalık saat, etik kurul süreci, saha erişim izin zamanlaması ve kurumsal idari süreçler araştırmacının yerel bilgisini gerektirir. Bu veriler doğru girilmezse model her zaman iyimser bir tablo üretir. Horizon Europe gibi büyük çerçeve programlarda iş paketi bütçesiyle, göstergesiyle (KPI) ve risk kaydıyla birlikte gelir. Claude Code bu çok bileşenli yapının taslağını hızla kurar, ama her sayıyı araştırmacı teyit etmek zorundadır (European Commission, 2025).

## 4. Zaman Çizelgesi ve Gantt Mantığı

Zaman çizelgesi bir iyimserlik belgesi değildir. Projenin gerçek iş yükünü ve bileşenler arasındaki bağımlılıkları gösterir. Etik kurul onayı, pilot çalışma, veri toplama, transkripsiyon, analiz, yazım, iç gözden geçirme, düzeltme ve son raporlama: bunların her biri gerçek sürelerle düşünülmelidir.

Gantt şeması bu bileşenleri görsel olarak sıralar ve paralel çalışan görevleri ayrı satırlarda, bağımlı olanları ardışık hücrelerle gösterir. Sosyal bilimlerde en sık hafife alınan süreler üçtür: veri toplama (katılımcı bulmak ve onaylarını almak zamana yayılır), transkripsiyon (bir saat kayıt için ortalama dört saatin üzerinde zaman ayrılır) ve etik kurul (Türkiye'de kurumdan kuruma iki hafta ile dört ay arasında değişebilir). Bu üç süreçten herhangi biri gecikmesi öngörülen kritik yoldaki her şeyi ileriye iter.

Claude Code Gantt taslağı üretebilir. Ama gerçek süreleri araştırmacı girer: kendi üniversitesindeki etik kurul pratiğini, ekibinin gerçek kapasitesini, saha bölgesinin mevsimsel kısıtlarını ve kendi kurumsal tatil takvimini. Model bu bilgileri çıktısına yansıtamaz. Sonuç olarak modelin ürettiği takvim her zaman denetimle girilmesi gereken bir taslaktır, bitmiş bir plan değil.

Zaman çizelgesini proje içinde tutarlı kılan ikinci araç kilometre taşı (milestone) mantığıdır. Kilometre taşı bir sürecin değil bir sonucun tamamlandığını işaretler: "etik kurul onayı alındı", "pilot veri toplama tamamlandı", "ilk iş paketi raporu teslim edildi". Bu ayrım önemlidir çünkü fon kuruluşunun izleme sürecinde kilometre taşı kaçırılması mali yaptırım gerekçesi olabilir. Claude Code kilometre taşı listesi üretebilir. Ancak her taşın gerçekçi bir tarihe bağlanması ve taşlar arasındaki bağımlılıkların doğru sıralanması araştırmacının iş yükü tahminini gerektirir.

## 5. Risk Yönetimi

Her projenin riski vardır. İyi başvuru riski inkâr etmez, tanır ve azaltma planı sunar. Risk yokmuş gibi yazılmış başvurular çoğu zaman Lamont'un (2009) gözlemlediği şeyi doğrular: deneyimli hakem kurulu üyeleri metodolojik zayıflıkları ve gerçekçi olmayan iddiaları sözsüz önkabul olarak kullanan başvurulardan daha kolay tanır. Gerçekçi bir risk analizi ise araştırmacının alana hakimiyetini gösterir.

Sosyal bilimde tipik riskler birkaç kategoride toplanır. Katılımcı riski: öngörülen sayıya ulaşılamaması, geri çekilme oranının yüksek çıkması. Veri riski: ölçüm aracının beklenen psikometrik kaliteyi karşılamaması, saha koşullarının değişmesi. Ekip riski: araştırma asistanının dönem ortasında ayrılması. Bütçe riski: kur dalgalanması, beklenmeyen açık erişim ücreti, ek transkripsiyon maliyeti. Düzenleyici risk: etik kurul gecikmesi, kurumsal izin süreci. Her risk için azaltma planı sorulur: nasıl önceden önlenebilir, yaşandığında nasıl yönetilir.

Claude Code risk listesi çıkarabilir, hatta yöntem bölümüne dayanarak olası zayıf noktaları tespit edebilir. Ancak yerel riskler, kendi kurumunuzdaki etik kurul pratiği, saha bölgesindeki ulaşım ve dil engelleri, kurumun bütçe esnekliği araştırmacının bilgisidir. Bu bilgi metne girilmedikçe risk tablosu jenerik kalır ve hakem bunu anında fark eder. Porter'ın (2007) çerçevesiyle düşünülürse akademisyenler çoğu zaman araştırma sorusunun güçlüğünü açıklamakta usta ama projenin yürütülmesiyle ilgili kısıt ve riskleri somutlaştırmakta zorlanırlar. İyi bir risk bölümü tam da bu boşluğu kapatır.

## 6. Etki Bölümü

Etki bölümü başvuru metninin en kolay şişirilen alanıdır. "Bu çalışma alana katkı sağlayacaktır" ya da "politika yapıcılara yön verecektir" gibi cümleler her başvuruda bulunur ve bu yüzden hakemlerin gözünde hiçbir bilgi taşımaz. Güçlü etki metni somuttur: kimin neyi farklı yapacağını, hangi kanaldan, ne zaman gösterir.

Sosyal bilimde etki birkaç farklı kanaldan akar. Bilimsel etki: alanyazındaki boşluğu kapatmak, yeni bir ölçüm aracı geliştirmek, teorik bir çerçeveyi test etmek. Politika etkisi: bulguların hangi kurum ya da kuruluş kararlarını etkileyebileceğini somutlaştırmak. Klinik ya da uygulama etkisi: klinisyenlerin, sosyal hizmet uzmanlarının ya da eğitimcilerin pratiğini değiştirmek. Toplumsal etki: kamuoyunun bir konuda daha bilinçli olmasına katkı sunmak. Her etki türü farklı kanıt gerektirir ve farklı paydaş gruplarını muhatap alır.

İkincil yayın planı, konferans bildirisi, politika özeti, kamuoyuna açık veri seti: bunlar etki iddiasını destekleyen somut yaygınlaştırma araçlarıdır. Bir çalışmanın etkisi gerçek olabilir ama belgelenmemişse hakem kurulu için var olmaz. Etki beyanını Claude Code yapılandırabilir. Ama "kimin neyi farklı yapacağı" sorusunun cevabı araştırmacının alana özgü bilgisinden gelir. Model bu cevabı üretemez, yalnızca çerçeveleyebilir.

Horizon Europe başvurularında etki bölümü ayrı bir değerlendirme kriteri olarak puanlanır ve toplam puanın önemli bir bölümünü oluşturur. Bu çerçevede "bilimsel etki", "teknolojik etki" ve "toplumsal etki" ayrı başlıklar altında gerekçelendirilir. Sosyal bilimciler için en güç kısım teknolojik etki başlığıdır. Bu başlık boş bırakılabilir ya da araştırmanın kullandığı dijital yöntemlerin (ölçek uyarlama yazılımı, açık veri altyapısı, yapay zekâ destekli kodlama araçları) geliştirme ya da test sürecine katkısı şeklinde doldurulabilir. Claude Code bu üç eksenin taslak metnini üretebilir. Hangi eksene ne kadar alan ayrılacağı ve iddialar için hangi kanıtların sunulabileceği araştırmacının proje deneyimine ve önerilen çalışmanın gerçek kapsamına bağlıdır.

## 7. Bütçe Gerekçesi

Bütçe gerekçesi bir finansal liste değil, yöntemsel bir savunmadır. Her harcama kalemi bir iş paketine ve bir çıktıya bağlanmalıdır. "Seyahat giderleri: 3.000 €" değil, "iş paketi 2 kapsamında üç saha ziyareti, İstanbul ve Komotini bölgelerinde toplam altı gün, veri toplama görevi için tek kişilik konaklama ve ulaşım" biçiminde gerekçelendirilmelidir. Bu gerekçe hem hakemlerin değerlendirme sürecini kolaylaştırır hem de ilerleyen aşamalarda fon kuruluşunun denetim sorularına zemin hazırlar.

Bütçede gerekçesi en zor yazılan kalemler birkaç başlık altında toplanır: araştırma asistanlığı ücretleri (çalışılan ülkenin asgari ücret ve akademik tarife normlarına göre hesaplanmalıdır), transkripsiyon ve çeviri giderleri, açık erişim yayın ücretleri (APC olarak anılan bu kalem Scopus ve SSCI dergilerinde genellikle 1.000-3.500 € arasında değişir), yazılım lisansı ve veri depolama, etik kurul ücretleri ve katılımcı teşvik ödeneği.

Türk akademisyenler için özellikle kritik bir kalem kur farkı tamponudur. TÜBİTAK ya da Avrupa fonlarında bütçeyi oluştururken döviz kuru oynaklığını göz önünde bulundurmak zorunludur. Claude Code bütçe dilini düzenleyebilir ve kalemi gerekçeyle birleştiren önerme cümlelerini hazırlayabilir. Ancak gerçek maliyet rakamları ülke, kurum ve yıla göre değişir. Modelin ürettiği sayı başlangıç tahminidir, kesinleşmiş değildir. NIH (2025) uygulama kılavuzu bütçe gerekçesini başvurunun ayrılmaz bir parçası olarak tanımlar ve her kalemin doğrudan araştırma hedeflerine hizmet ettiğinin açıkça gösterilmesini zorunlu kılar.

## 8. Etik ve Veri Yönetimi Planı

Yapay zekâ destekli bir projede veri yönetimi planı standart etik bölümünün ötesine geçer. Hangi verilerin toplanacağı, nerede saklanacağı, nasıl anonimleştirileceği, hangi araçlara ve hangi modellere gösterileceği, kimin erişebileceği ve proje sonunda ne paylaşılıp ne arşivleneceği: bunların her biri açıkça tanımlanmalıdır.

Veri yönetimi planının üç katmanı vardır. Birincisi, toplanan ham verinin güvencesidir: ses kayıtları, anket yanıtları, gözlem notları. Bunlar GDPR ve Türk KVKK mevzuatına uygun biçimde güvenli sunucularda saklanmalı ve proje dışı erişime kapalı tutulmalıdır. İkincisi, işlenmiş verinin yapay zekâ araçlarıyla ilişkisidir: ham transkriptlerin Claude Code ya da benzeri bir araca gönderilmesi veri işleme kapsamına girer ve etik protokolde açıklanmalıdır. Üçüncüsü ise açık veri ve yeniden üretilebilirlik boyutudur: hangi veri türleri anonimleştirilerek açık depozitoya (örneğin Zenodo veya OSF) yüklenecek, hangisi hassasiyet gerekçesiyle kısıtlı kalacak.

Etik onay süreci, kurumsal etik kurulun incelemesinden bağımsız olarak fon kuruluşunun ek etik değerlendirme gerektirip gerektirmediğini de kapsar. Türkiye'de yapay zekâ araçlarına veri aktarımı KVKK kapsamında açık rıza ve aydınlatma yükümlülüğü doğurabilir. Bu yükümlülüğün etik başvuru formunda açıkça yer alması hem etik kurulun hem de fon kuruluşunun beklentisini karşılar. Horizon Europe H2020 ve HE dönemlerinde bu değerlendirme ayrı bir form ve zaman çizelgesiyle işler. Claude Code veri yönetimi planının taslağını FAIR ilkelerine (Bulunabilir, Erişilebilir, Birlikte çalışılabilir, Yeniden kullanılabilir) uygun biçimde üretebilir. Ancak hangi verilerin açılacağına, hangi araçların kullanılacağına ve hangi kısıtların uygulanacağına araştırmacı karar verir.

## 9. Başvuru Öncesi Bütünlük Kontrolü

Başvuru metni tamamlanmadan önce iç tutarlılık denetimi yapılmalıdır. Bu denetim beş soruyu yanıtlar. Her araştırma sorusu için karşılık gelen en az bir iş paketi var mı? Her iş paketinin bütçede satırı var mı? Her çıktı için bütçede ve takvimde yer var mı? Her etki iddiasını destekleyen en az bir somut yaygınlaştırma etkinliği var mı? Etik bölüm, toplanacak tüm veri türlerini kapsıyor mu?

Bu beş sorunun hepsine olumlu yanıt verildiğinde başvuru metni yapısal olarak bütündür. Eksik bir halka bulunduğunda modelin parlattığı cümlelerin arkasında yapısal bir çöküş gizlenir. Hakem kurulları bu tür parçalanmaları sistematik biçimde yakalar. Friedland ve Folt (2009), bilimsel başvurularda yönteme verilen ayrıntının yeterliliğini değerlendirirken her metodolojik adım için "kim, ne, nerede, ne zaman, nasıl" sorularının yanıtlanmasının zorunlu olduğunu belirtir. Bu ölçüt, sosyal bilim başvuruları için de aynı geçerlilikle uygulanır.

Bütünlük kontrolünü yapay zekâya devredebilirsiniz. Claude Code başvuru metnini okur ve boş halkaları listeler. Ama listede yer alan her maddeyi araştırmacı teyit eder. Model bazen başvuru metnindeki yüzeysel bir cümleyi gerçek bir bağlantı olarak okuyabilir. Araştırmacının son okuma sorumluluğu kalkamaz.

## 10. Skill Çıktıları

`/grant-proposal-workpackage-builder` skill'i bu kitapçıkta ele alınan bileşenlerin tamamını kapsar. Amaç ve hedef ayrımı tablosu, iş paketi şablonu (sorumlu, süre, görevler, çıktılar, riskler ve azaltma stratejisi), Gantt taslağı, risk ve azaltma planı, etki beyanı, bütçe gerekçesi şablonu ve veri yönetimi planı özeti üretir.

Bu skill'in birincil değeri, araştırmacının her bileşeni ayrı ayrı düşünmesini zorunlu kılacak bir çerçeve kurmaktır. Boş taslak, ne eksik olduğunu görmeyi kolaylaştırır. Doldurulmuş taslak ise iç tutarsızlıkları yüzeye çıkarır. Skill çıktısı bir taslaktır, başvurunun kendisi değil. Gerçek başvuru her zaman araştırmacının yerel bilgisi, kurumsal gerçeklik ve hakemin beklentisi süzgecinden geçerek yeniden yazılır. Belcher'ın (2019) yayın sürecine ilişkin haftalık takvim programında olduğu gibi, yazım sürecini erken başlatmak ve her bileşeni ayrı bir oturum olarak ele almak, son dakika panikini ve yapısal eksikliği önleyen temel pratiktir.

## Kaynakça

Atıflar APA 7 biçimindedir. DOI'ler ve URL'ler 2026-06-21 tarihinde doğrulanmıştır.

Belcher, W. L. (2019). *Writing your journal article in twelve weeks: A guide to academic publishing success* (2nd ed.). University of Chicago Press. ISBN 978-0-226-49991-8

European Commission. (2025). *Horizon Europe*. Directorate-General for Research and Innovation. https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe_en

Friedland, A. J., & Folt, C. L. (2009). *Writing successful science proposals* (2nd ed.). Yale University Press. ISBN 978-0-300-11939-8

Hosseini, M., Rasmussen, L. M., & Resnik, D. B. (2023). Using AI to write scholarly publications. *Accountability in Research*, *31*(7), 715–723. https://doi.org/10.1080/08989621.2023.2168535

Lamont, M. (2009). *How professors think: Inside the curious world of academic judgment*. Harvard University Press. ISBN 978-0-674-03266-8

Locke, L. F., Spirduso, W. W., & Silverman, S. J. (2014). *Proposals that work: A guide for planning dissertations and grant proposals* (6th ed.). SAGE. ISBN 978-1-452-21685-0

National Institutes of Health. (2025). *Write your application*. U.S. Department of Health and Human Services. https://grants.nih.gov/grants/how-to-apply-application-guide.html

Porter, R. (2007). Why academics have a hard time writing good grant proposals. *Journal of Research Administration*, *38*(2), 37–43.

Przeworski, A., & Salomon, F. (1995). *On the art of writing proposals: Some candid suggestions for applicants to Social Science Research Council competitions*. Social Science Research Council. https://www.ssrc.org/publications/the-art-of-writing-proposals/

---

**Kitapçık kimliği.** `007-06-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 2321 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 9
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`007-05-0001`](../007-05-0001/tr.md). Çok Dilli Kavram Geçerliği, Türkçe, İngilizce ve Yunanca Arasında Akademik Düşünmek
**Sonraki kitapçık.** [`008-01-0001`](../../008-data-analysis/008-01-0001/tr.md). Yeniden Üretilebilir Nicel İş Akışları
