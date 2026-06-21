---
title_en: "AI in Teaching, Course Design, Supervision, and Student Feedback"
title_tr: "Öğretimde Yapay Zekâ, Ders Tasarımı, Süpervizyon ve Öğrenci Geri Bildirimi"
booklet_id: "013-01-0001"
category: "013-teaching-supervision"
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
verified_citations_count: 9
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Öğretimde Yapay Zekâ, Ders Tasarımı, Süpervizyon ve Öğrenci Geri Bildirimi

Bu kitapçık, sosyal bilimcinin araştırmacı kimliğinin yanı sıra öğretim üyesi, danışman ve süpervizör olarak taşıdığı rolü ele alır. Araştırmada kurulan kaynak disiplini ve etik zemin, öğretim bağlamında farklı ama eşdeğer derecede kritik biçimler kazanır: öğrenci emeğinin korunması, öğrenme sorumluluğunun yerinde tutulması ve değerlendirme adaletinin sürdürülmesi.

Yapay zekâ bu rollerin her birinde belirli işlevler üstlenebilir. Ders izlencesi taslağı hazırlayabilir, okuma listesi önerilerini hızlandırabilir, rubrik çerçevesi oluşturabilir, geri bildirim dilini düzenleyebilir. Ama öğrencinin düşünme sürecini devralamaz. Bir ödevdeki asıl kazanımı, yani öğrencinin argüman kurmayı, kaynakla karşılaşmayı ve eleştirel çıkarım yapmayı öğrenmesini, yerinden edemez. Klinik süpervizyon materyalini anonimleştirmeden işleyemez. Bir değerlendirme sürecinde öğrenciye karşı adil bir zemin kuramaz.

Bu sınırları baştan belirlemek, yapay zekâyı reddetmek anlamına gelmez. Nerede işe yaradığını, nerede devreye girmemesi gerektiğini ve nerede pedagojik yargının araçtan ayrı tutulması zorunlu olduğunu bilmek demektir.

## 1. Öğretim ve araştırma farkı

Araştırmada amaç bilgi üretmektir. Yeni bir bulgu ortaya koymak, bir kavramı test etmek, bir ilişkiyi belgelemek. Öğretimde amaç farklıdır: öğrencinin düşünme kapasitesini geliştirmek, kavramla kendi başına hesaplaşmasını sağlamak, bilgiyi üretme sürecini içselleştirdiği bir ortam kurmak.

Bu fark, yapay zekânın her iki bağlamdaki rolünü doğrudan etkiler. Araştırmacı kendi çalışması için araç kullandığında, ürünün doğruluğundan ve bütünlüğünden kendisi sorumludur. Öğretmen yapay zekâyı ders sürecine dahil ettiğinde ise hesap verebilirlik katmanlanır: öğretmenin kendi bilimsel yargısından, ama aynı zamanda öğrencinin öğrenme sürecinden de sorumludur.

Zawacki-Richter ve diğerleri (2019), yükseköğretimde yapay zekâ uygulamalarını sistematik biçimde inceleyen çalışmalarında, teknik kapasite ile pedagojik tasarım arasındaki boşluğa dikkat çeker. Bir aracın mevcut olması, onu sınıf ortamına almayı ya da ödev değerlendirmesine dahil etmeyi otomatik olarak meşrulaştırmaz. Hangi pedagojik amaca hizmet ettiği, öğrencinin hangi öğrenme hedefini güvence altına aldığı ve değerlendirme adaletini nasıl etkilediği açıkça tanımlanmalıdır.

Ödev tasarımının amacı yalnızca ürün almak değildir. Öğrencinin o ürünü üretirken geçirdiği süreç, argümanını kurduğu, kaynakla karşılaştığı, hata yapıp düzelttiği deneyim, ödülün kendisidir. Bu süreci devre dışı bırakan bir araç kullanımı, öğrencinin öğrenmesini kolaylaştırmaz. Onu engeller. Zimmerman (2002), öz düzenlemeli öğrenme üzerine temel çalışmasında bu noktayı açıkça kurar: bağımsız düşünme kapasitesi, yalnızca üretilen ürünle değil, üretme sürecindeki aktif katılımla gelişir.

## 2. Ders izlencesi tasarımı

Bir ders izlencesi, en yüzeysel okumayla haftalık konu listesidir. Ama işlevi bundan çok daha derindir. Öğrenciye yapılan bir öğrenme sözleşmesidir: bu derste neler beklendiğini, hangi becerilerin kazanılacağını, nasıl değerlendirileceğini ve öğretmenin pedagojik önceliklerini belgeleyen bir metin.

Yapay zekâ bu süreçte taslak işlevi görebilir. Claude Code'a ders amacını, hedef kitleyi ve hafta sayısını verdiğinizde makul bir iskelet üretir: haftalık akış önerisi, olası okuma kategorileri, değerlendirme bileşenlerinin ağırlıklandırması. Bu taslak, sıfırdan başlamanın önündeki ilk engeli kaldırır ve öğretmenin odağını düzenlemeden içeriğe çevirmesine yardımcı olabilir.

Ama izlencenin pedagojik omurgası öğretmene aittir ve devredilemez. Hangi okuma neden bu haftada yer alıyor, hangi sıralama öğrencinin kavramsal gelişimini en iyi destekliyor, hangi haftada zorlanma bekleniyor ve bu zorlanma nasıl karşılanacak, hangi ödev hangi düşünme becerisini hedefliyor? Bu sorular üretken bir yapay zekâ modelinin cevap veremeyeceği sorular değildir. Ama cevabını bilmesi için dersi, öğrenci kitlesini ve kurumsal bağlamı sizin bildiğiniz kadar bilmesi gerekir, ki bu mümkün değildir.

Kasneci ve diğerleri (2023), büyük dil modellerinin eğitim bağlamındaki fırsatlarını ve sınırlılıklarını inceleyen kapsamlı çalışmalarında, modellerin içerik üretiminde etkin olabildiğini ama pedagojik uygunluk kararlarını öğretmene bırakmak gerektiğini vurgular. İzlence bir kez hazırlandıktan sonra sürekli revize gerektiren canlı bir belgedir. Dönem ortasında sınıfın nereye geldiğini gören öğretmen, bir sonraki haftanın ağırlığını yeniden ayarlar. Bu esneklik ve bağlamsal yargı, herhangi bir araçtan gelecek değildir.

## 3. Okuma listesi ve kaynak doğrulama

Bir okuma listesi hazırlamak, aynı zamanda bir öğretim kararı vermektir. Öğrenciye hangi kaynakla, hangi sırayla ve hangi amaçla karşılaştıracağını belirlemek, metodolojik bir tercihtir. Araştırmada kaynak seçimi nasıl usul ve doğrulama gerektiriyorsa, öğretimde de aynı disiplin geçerlidir.

Yapay zekâ okuma listesi önerebilir. Bir konu alanına giren temel çalışmaları listeleyebilir, kronolojik ya da tematik düzenleme yapabilir, farklı bakış açılarını temsil eden kaynaklar önerebilir. Bu öneriler zaman kazandırabilir, gözden kaçan bir kaynağa dikkat çekebilir. Ama bu listedeki her başlığın bağımsız olarak doğrulanması gerekir.

Kaynak uydurma riski öğretim bağlamında da gerçektir. Bir model plausible görünen bir başlık, yazar adı ve yayın yılı üretebilir. Öğrenciye verilen bir kaynak listesindeki hatalı ya da var olmayan bir başlık, yalnızca akademik bir hata değildir: öğrencinin arama sürecini kesen, zamanını çalan ve güvenini sarsan bir başarısızlıktır.

Bu nedenle her kaynak DOI, yayıncı sayfası ya da güvenilir bir kütüphane kaydıyla bağımsız olarak doğrulanmalıdır. Dijital akademik kimlik bilgisi olmayan kaynaklar için JSTOR, Google Scholar ya da kurumsal kütüphane kataloğu teyit noktası olarak kullanılabilir. Bu doğrulama, araştırmadaki atıf hijyeninin tam karşılığıdır ve aynı titizliği gerektirir. Öğrenciye verilen kaynak, bu süzgeçten geçmemişse öğretim sorumluluğu eksik kalmış demektir.

## 4. Rubrik hazırlama

Rubrik, değerlendirme adaletinin somut ve görünür halidir. Hangi kriterin ne anlama geldiğini, performansın hangi düzeyde ne ölçüde karşılandığını ve puanın nasıl hesaplandığını öğrenciye baştan gösterir. İyi hazırlanmış bir rubrik, öğrencinin belirsizlikle değil beklentiyle çalışmasını sağlar.

Yapay zekâ rubrik taslağı üretme konusunda oldukça işlevseldir. Bir ödevin amacını tarif ettiğinizde boyutları ayırabilir, her boyut için performans düzeylerini yazabilir ve puanlamayı dağıtabilir. Bu taslak, rubrik geliştirmenin en zaman alıcı ilk adımını kolaylaştırır.

Ama her ölçütün ders hedefiyle ilişkisi, öğrencilerin nasıl değerlendirileceğini ve eğer ölçütler arasında önem farkı varsa ağırlıklandırmanın nasıl yapılacağını öğretmen belirlemelidir. Sadler (1989), değerlendirme ölçütleri üzerine temel çalışmasında rubriğin yalnızca bir puanlama aracı olmadığını gösterir: iyi tanımlanmış kriterler, öğrencinin kendi çalışmasını değerlendirme kapasitesini de geliştiren bir öğretim aracıdır. Bu işlevi yerine getirmesi için ölçütlerin, öğrencinin gerçekten kendi argümanını değerlendirebildiği bir dilde yazılması gerekir.

Rubrik, öğrenciyi cezalandırma aracı değildir. Beklentiyi baştan görünür kılmak ve öğrencinin değerlendirme öncesinde kendi çalışmasını bu beklentiye göre gözden geçirebilmesini sağlamak içindir. Yapay zekâ tarafından üretilen bir taslağın bu işlevi yerine getirmesi, öğretmenin hem teknik doğruluğu hem de pedagojik uygunluğu ayrıca denetlemesini gerektirir.

## 5. Öğrenci metnine geri bildirim

Geri bildirim, öğrencinin gelişimindeki en kritik noktalardan birini işaret eder. Ama etkili geri bildirim vermek, zaman ve dikkat gerektiren bir süreçtir. Otuz öğrencinin araştırma taslağını tek oturumda okuyup her birine anlamlı bir yorum yazmak, çoğu öğretim üyesinin karşılaştığı gerçek bir yük.

Yapay zekâ bu yükü belirli ölçüde hafifletebilir. Geri bildirim metinlerini daha açık, daha yapıcı ve daha okunaklı hale getirme konusunda işlevsel bir araç olabilir. Bir yorum taslağını alıp daha sistematik bir dile çevirebilir, belirsiz ifadeleri somutlaştırabilir, tonun tutarlılığını artırabilir.

Carless (2006), geri bildirim algısını öğretmen ve öğrenci perspektifinden inceleyen çalışmasında, yorumun nasıl iletildiğinin içeriği kadar önemli olduğunu gösterir. Öğrenci geri bildirimi sürecin önüne geçemezse, yani ne yapacağını değil ne ürettiğini görürse, geri bildirim öğrenme fırsatına dönüşmez. Winstone ve Carless (2019), etkili geri bildirim süreçlerini inceleyen kapsamlı çalışmalarında, geri bildirimi öğrencinin aktif olarak kullandığı bir öğrenme kaynağı olarak tasarlamanın gerekliliğini vurgular.

Bu tartışmadan çıkan pratik sonuç nettir: yapay zekâ geri bildirim dilini düzenleyebilir, ama geri bildirimin içeriğini, yani öğrencinin argümanının neresinin tutarlı olduğunu, nerede derinlik eksik kaldığını ve bir sonraki taslakta neye odaklanması gerektiğini belirleyen akademik yargı öğretmene aittir. Geri bildirim öğrencinin metnini onun yerine yazmamalıdır. Öğrencinin bir sonraki adımı görebilmesine yardımcı olmalıdır.

Bununla birlikte önemli bir sınır söz konusudur: öğrenci metni, yazılı izin ve kurumsal onay olmadan üçüncü taraf bir yapay zekâ aracına verilemez. Öğrenciye ait özgün metin kişisel verinin kapsamına girebilir. Kurumsal politika ve öğrenci bilgilendirmesi, araç kullanımından önce açıkça ele alınmalıdır.

## 6. Tez danışmanlığı

Tez danışmanlığı, öğretim üyesinin öğrenciyle kurduğu en uzun soluklu ve en derinlikli eğitim ilişkisidir. Bu ilişkinin yapay zekâ ile kesiştiği birkaç alan vardır ve her alan kendi sınırını taşır.

Literatür haritası çıkarmak, tezin ilk aşamalarında en çok zaman alan işlemlerden biridir. Bir model, ilgili alandaki temel çalışmaları hızla listeleyebilir, tematik gruplamalar önerebilir ve boşlukları sezdirebilir. Bölüm iskeleti kurmak, argüman akışını görselleştirmek ve metodoloji bölümünün mantıksal tutarlılığını test etmek için de yardımcı olabilir.

Ama danışmanın akademik yargısı, hiçbir araç tarafından ikame edilemez. Araştırma sorusunun alana özgün katkısını değerlendirmek, metodolojik seçimlerin kabul edilebilirliğini belirlemek, öğrencinin düşünce gelişimini izlemek ve tezin savunulabilirliği konusunda akademik bir görüş oluşturmak, danışmana ait işlevlerdir. Bu işlevler, sürecin ürünüyle değil sürecin kendisiyle birlikte oluşur.

Öğrencinin yapay zekâyla kurduğu ilişki de ayrıca ele alınmalıdır. Model yardımıyla üretilmiş bir bölümü kendi çalışması gibi sunan öğrenci, hem akademik dürüstlük sınırını aşmış hem de kendi tez sürecini kısaltmıştır. Öğrenci, yapay zekânın ürettiği içeriği kendi eleştirel süzgecinden geçirmeyi öğrenmek zorundadır. Boud ve Molloy (2013), öğrenmeye yönelik geri bildirim modellerini tartıştıkları çalışmalarında bu noktaya dolaylı ama güçlü bir biçimde işaret eder: öğrenci, sürecin aktif öznesi olduğunda gelişir. Araçla üretilen içerik bu özneliği ortadan kaldırıyorsa araç, yardımcı değil engelleyici olmuş demektir.

## 7. Klinik süpervizyon sınırları

Klinik süpervizyon, öğretim içindeki en hassas alandır. Süpervizyonda paylaşılan materyal, doğası gereği özel ve gizli niteliktedir: bir danışan vaka notu, bir seans içeriği, bir danışan hakkındaki değerlendirme, eğitim sürecindeki bir stajyerin yaşadığı zorluk. Bu materyalin herhangi bir yapay zekâ aracına aktarılması, anonimleştirme yapılmadan düşünülemez.

Anonimleştirme süreci de dikkatsiz yapılırsa yetersiz kalır. İsim ve kurum adını kaldırmak, çoğu zaman yeterli değildir. Kişiyi tanımlamaya yetecek birleşik bilgilerin, yani yaş, cinsiyet, meslek, kurumun adı geçmeden tanımlanabilecek bağlamın da ayıklanması gerekir.

Bu sınır eğitim amacıyla gevşetilemez. "Öğrenciye ders anlatmak için kullanıyorum" gerekçesi, gizlilik yükümlülüğünü değiştirmez. Klinik süpervizyon materyali özeldir. Bir süpervizyon görüşmesinin içeriğini ya da vaka notunun herhangi bir parçasını yapay zekâ aracına aktarmadan önce anonim hale getirilmiş olması zorunludur. Bu zorunluluk, mesleki etik kodları, ulusal veri koruma mevzuatı ve kurumsal etik politikaların kesişim noktasıdır.

Süpervizyon, gizlilik sorumluluğunun en güçlü hissedildiği alanlardan biridir. Bu sorumluluğu taşımak, araç kullanımındaki kısa yolları kapatmak demektir.

## 8. Yapay zekâ şüphesi ve adil değerlendirme

Yapay zekâ dedektörleri, son yıllarda akademik dürüstlük tartışmasının merkezi haline geldi. Bir öğrencinin sunduğu metin yapay zekâ tarafından üretilmiş mi, değil mi? Bu soruyu cevaplamak için tasarlanmış araçlar hızla yaygınlaştı. Ama bu araçların teknik sınırlamaları, gerçek bir değerlendirme adaleti sorununa dönüşmektedir.

Liang ve diğerleri (2023), GPT dedektörlerinin anadili İngilizce olmayan yazarlar aleyhine sistematik bir önyargı taşıdığını ampirik olarak göstermiştir. Kısa cümle yapısı, açık sözdizimi, sınırlı sözcük dağarcığı gibi özellikler, bazı öğrencilerin doğal yazı stilinin yanlış pozitif bir sınıflandırmayla sonuçlanmasına yol açmaktadır. Türkçe, Arapça ya da Çince anadil arka planından gelen ve İngilizce yazan bir öğrenci, yalnızca yazı stili nedeniyle haksız biçimde işaretlenebilir.

Öğrenciyi yalnızca dedektör çıktısına dayanarak suçlamak adil değildir. Değerlendirme süreci, yapay zekâ şüphesini kaldıracak kadar sağlam olmak için şu destekleri içermelidir: yazım sürecinin kanıtı, taslak geçmişi ya da versiyon kontrolü. Sözlü savunma ya da yüz yüze görüşme, öğrencinin metni gerçekten kavrayıp kavramadığının test edildiği bir zemin. Pedagojik görüşme, yani öğrencinin düşünce sürecini takip etmeye yönelik açık uçlu sorular. Şüphe, cezadan önce konuşmayı gerektirir. Bu kural hem etik açıdan zorunludur hem de kurumsal düzeyde savunulabilir bir değerlendirme pratiğinin temelidir.

## 9. Ders düzeyinde yapay zekâ politikası

Her ders, yapay zekâ kullanımına ilişkin açık bir politika içermelidir. Bu politikanın yokluğu, öğrencinin ne yapması gerektiğini bilmediği belirsiz bir alan yaratır. Belirsizlik, öğrenciyi hem etik hatalara açık kılar hem de öğretmeni tutarsız değerlendirme süreçlerine.

Ders politikası şu soruları yanıtlamalıdır. Yapay zekânın hangi kullanımı serbesttir: taslak için beyin fırtınası, gramer denetimi, kaynak arama. Hangi kullanım kısıtlıdır: uygun beyanla birlikte metin yardımı. Hangi kullanım yasaktır: ödevin büyük bölümünü yapay zekâya yazdırmak. Beyan nasıl yapılacak: her görevde standart bir açıklama şablonu mı, yoksa yöntem bölümünde açık bir not mu.

Bu kararlar dersin niteliğine, ödev türüne ve kurumsal politikaya göre farklılaşır. Bir tamamlama ödevi ile bir analiz ödevi aynı sınırı taşımak zorunda değildir. Önemli olan, sınırın belirsiz kalmamasıdır. UNESCO (2023), üretici yapay zekânın eğitim ve araştırmada kullanımına ilişkin rehberinde açık politikanın kurumsal düzeyde bir zorunluluk olduğunu vurgular. Bu beklenti, ders düzeyindeki uygulamaya kadar iner.

Politika, cezalandırıcı olmaktan çok öğrenme sorumluluğunu açıklamalıdır. Öğrenciye "bunu yaparsan bu olur" yerine "bu derste bu aracı bu şekilde kullanıyoruz ve işte nedeni" diyebilmek, politikayı pedagojik bir araç haline getirir.

## 10. Skill çıktıları

`/teaching-feedback-ai-boundaries` skill'i bu kitapçıkta ele alınan iş akışlarını doğrudan destekler. Ders izlencesi taslağı üretmek, okuma listesi önerileri oluşturmak ve bu önerilerin doğrulama adımlarını planlamak için bir başlangıç iskeleti sunar. Ödev yönergesi ve rubrik taslağı hazırlamak, performans boyutlarını ve değerlendirme ölçütlerini ayrıştırmak için kullanılabilir. Öğrenciye yönelik geri bildirim dilini düzenlemek, daha yapıcı ve daha açık bir ton kurmak için yardımcı olabilir. Ders düzeyinde yapay zekâ kullanım politikası ve öğrenciye aktarılacak sınırlar için şablon bir dil oluşturmak da bu skill'in çıktıları arasındadır.

Skill, bu kitapçığın temel iddiasını işlevselleştirir: yapay zekâ öğretimde bir verimlilik aracıdır, ama pedagojik sorumluluk aracının ötesine geçmesi için kullanıcının araçla her noktada bilinçli bir ilişki kurması gerekir. Araç neyi kolaylaştırdığını, neyi alamayacağını ve öğrencinin öğrenme sürecini nerede koruma altına alması gerektiğini bilen bir öğretim üyesinin elinde anlam kazanır.

## Kaynakça

Atıflar APA 7 biçimindedir. Hakemli kaynakların DOI'leri Crossref üzerinden bağımsız olarak doğrulanmıştır. UNESCO kurumsal belgesi gri literatür olarak atıflanmıştır. URL 2026-06-21 tarihinde erişilebilir durumdaydı.

Boud, D., & Molloy, E. (2013). Rethinking models of feedback for learning: The challenge of design. *Assessment & Evaluation in Higher Education*, 38(6), 698–712. https://doi.org/10.1080/02602938.2012.691462

Carless, D. (2006). Differing perceptions in the feedback process. *Studies in Higher Education*, 31(2), 219–233. https://doi.org/10.1080/03075070600572132

Kasneci, E., Sessler, K., Küchemann, S., Bannert, M., Dementieva, D., Fischer, F., Gasser, U., Groh, G., Günnemann, S., Hüllermeier, E., Krusche, S., Kutyniok, G., Michaeli, T., Nerdel, C., Pfeffer, J., Poquet, O., Sailer, M., Schmidt, A., Seidel, T., Stadler, M., Weller, J., Kuhn, J., & Kasneci, G. (2023). ChatGPT for good? On opportunities and challenges of large language models for education. *Learning and Individual Differences*, 103, Article 102274. https://doi.org/10.1016/j.lindif.2023.102274

Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). GPT detectors are biased against non-native English writers. *Patterns*, 4(7), Article 100779. https://doi.org/10.1016/j.patter.2023.100779

Sadler, D. R. (1989). Formative assessment and the design of instructional systems. *Instructional Science*, 18(2), 119–144. https://doi.org/10.1007/bf00117714

UNESCO. (2023). *Guidance for generative AI in education and research*. https://unesdoc.unesco.org/ark:/48223/pf0000386693

Winstone, N., & Carless, D. (2019). *Designing effective feedback processes in higher education: A learning-focused approach*. Routledge. https://doi.org/10.4324/9781351115940

Zawacki-Richter, O., Marín, V. I., Bond, M., & Gouverneur, F. (2019). Systematic review of research on artificial intelligence applications in higher education. Where are the educators? *International Journal of Educational Technology in Higher Education*, 16, Article 39. https://doi.org/10.1186/s41239-019-0171-0

Zimmerman, B. J. (2002). Becoming a self-regulated learner: An overview. *Theory Into Practice*, 41(2), 64–70. https://doi.org/10.1207/s15430421tip4102_2

---

**Kitapçık kimliği.** `013-01-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 2025 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 9
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`012-01-0001`](../../012-troubleshooting/012-01-0001/tr.md) İşler Ters Gittiğinde
**Sonraki kitapçık.** [`014-01-0001`](../../014-tool-portability/014-01-0001/tr.md) Claude Code'un Ötesinde, Codex ve Taşınabilir Ajan Disiplini
