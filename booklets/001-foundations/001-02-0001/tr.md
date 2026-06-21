---
title_en: "Research Lifecycle Map, From Idea to Publication, From Publication to Archive"
title_tr: "Araştırma Yaşam Döngüsü, Fikirden Yayına, Yayından Arşive"
booklet_id: "001-02-0001"
category: "001-foundations"
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

# Araştırma Yaşam Döngüsü, Fikirden Yayına, Yayından Arşive

Bu kitapçık, rehberin tamamını tek bir çerçevede konumlandırır. Önceki temeller kitapçıkları Claude Code'un sosyal bilimci açısından ne anlam taşıdığını, ajanlı çalışmanın sohbet penceresinden nasıl ayrıldığını, ilk kurulumun hangi yöntemsel filtrelerle sınanacağını ve CLAUDE.md aracılığıyla kalıcı talimat disiplininin nasıl kurulacağını ele almıştı. Bu kitapçık ise araştırmacının daha gündelik ama yanıtlanması çok daha zor olan sorusuna odaklanır: Akademik çalışmanın şu an hangi aşamasındayım ve bu aşamada hangi protokole ihtiyacım var?

Sosyal bilimcinin çalışma hayatı tek bir doğrusal çizgi izlemez. Bir yandan makale taslağı yazılır, bir yandan etik kurul dosyası bekler, bir yandan hakem yorumu gelir, bir yandan geçen yıl arşivlenen kaynak yeniden aranır. Bu paralel akışların içinde yapay zekâ desteği anlamlı bir rol üstlenebilir. Ama yalnızca doğru aşamaya doğru araç bağlandığında. Yanlış aşamada kullanılan güçlü bir araç üretkenliği artırmak yerine yöntemi bulanıklaştırır ve karar izini koparır.

Bu kitapçığın merkezi iddiası şudur: Claude Code, sosyal bilimcinin akademik yaşam döngüsüne ancak aşama teşhisiyle güvenli biçimde yerleşebilir. Araçtan önce aşama, aşamadan önce sorumluluk, sorumluluktan sonra otomasyon gelir. Bu sıra tersine çevrildiğinde araştırmacı aracı kullanmaz. Araç araştırmacıyı kullanır.

## 1. Yaşam döngüsünü neden haritalamak gerekir

Araştırmacının en sık yaptığı hata, elindeki işi yanlış adlandırmasıdır. Literatür taraması yaptığını sanırken aslında araştırma sorusunu daha net hale getirmeye çalışıyor olabilir. Analize geçtiğini düşünürken hâlâ veri temizleme kararlarını kayda geçirmemiş olabilir. Hakem yanıtı yazarken fark edebilir ki makalenin kuramsal çerçevesi yeniden kurulmayı beklemektedir.

Yaşam döngüsü haritası bu karışıklığı azaltır. Harita, araştırmacıya hangi soruyu sorması gerektiğini gösterir. Fikir aşamasında doğru soru literatür listesi değildir. Önce araştırma sorusunun taşıdığı kavramsal gerilimin görünür kılınmasıdır. Analiz aşamasında doğru soru yalnızca hangi istatistiksel testin çalıştırılacağı değildir. Önce hangi kararların veriye bakılmadan önce yazıya dökülmüş olduğudur. Yazım aşamasında doğru soru ne kadar metin üretildiği değildir. Üretilen metnin araştırma boyunca alınan kararlarla ne ölçüde tutarlı olduğudur.

Yaşam döngüsü bu nedenle bir üretim takvimi değildir. Bir muhakeme aracıdır. Hangi aşamada hangi riskin belirdiğini, hangi belgenin üretilmesi gerektiğini ve hangi yapay zekâ desteğinin meşru sınırlar içinde kaldığını gösterir. Munafò ve diğerleri (2017), yeniden üretilebilir bilim için yayın öncesi tasarım şeffaflığını, veri yönetimini ve analiz planlamasını çerçevelendirici ilkeler olarak öne çıkarmıştır. Bu ilkelerin her biri yaşam döngüsünde farklı bir düğüme oturur. Döngü haritalanmadan hangi ilkenin nerede devreye gireceğini belirlemek mümkün değildir.

Yapay zekâ destekli çalışmada bu gereklilik daha da ağır basar. Bir ajan, araştırmacının henüz sormadığı bir soruya yanıt üretebilir. Araştırma sorusunu netleştirmeye çalışırken alternatif analiz yolları önerebilir. Açık uçlu bir talimat karşısında araştırmacının düşündüğünden farklı bir çıktı aşamasına atlayabilir. Bu kayma sessizdir ve hızlıdır. Harita olduğunda fark edilir, harita olmadığında ancak yayın sürecinde görünür hale gelir.

## 2. Fikirden araştırma sorusuna

Bir fikir, henüz araştırma sorusu değildir. Fikir çoğu zaman geniş, sezgisel ve kişisel bir gözlemden doğar. Araştırma sorusu ise sınırları çizilmiş, literatürde yeri olan ve bir yöntemle cevaplanabilir bir yapıya kavuşmuş ifadedir. Bu dönüşüm önemsiz görünebilir, oysa araştırmanın tamamı bu dönüşümün kalitesine bağlıdır.

Ajan bu aşamada işe yarar. Benzer kavramları gösterebilir, alan tartışmalarını sınıflandırabilir, sorunun çok geniş ya da çok dar kaldığı yerleri işaretleyebilir. Bir fikrin hangi teorik gelenekle kesiştiğini sormak, hangi yöntem ailesinin bu soruyla daha önce ilgilendiğini araştırmak, kavramsal yakınlıklar ve mesafeler üzerine beyin fırtınası yapmak. Bunların tamamında ajan katkı sunabilir.

Ancak araştırma sorusunun entelektüel sorumluluğu araştırmacıda kalır. Klinik psikolojide bir sorunun etik ağırlığını, eğitim bilimlerinde bir sorunun pedagojik sonucunu, sosyolojide bir sorunun bağlamsal yükünü yalnızca olasılıksal metin üretimi belirleyemez. Model, soruyu parlaklaştırabilir. Ama hangi sorunun araştırılmaya değer olduğunu araştırmacının alan bilgisi ve etik sorumluluğu karara bağlar. Bu sınır aşıldığında araştırma sorusu görünürde araştırmacının değil modelin sorusuna dönüşür.

Bu aşamada üretilmesi gereken belge kısa bir araştırma fikri notudur. Notun içermesi gereken başlıklar nettir: problem ifadesi, olası kavramsal çerçeveler, hedef alan ve okuyucu kitlesi, ilk kaynak alanları, beklenen veri türü ve olası etik riskler. Bu not ilerleyen aşamalarda etik kurul başvurusuna, yöntem bölümüne ve yapay zekâ katkı beyanına zemin hazırlar. Yazılmadan açık bırakılırsa ilerleyen aşamalarda yapay zekânın ne zaman devreye girdiğini kanıtlamak güçleşir.

## 3. Literatür taramasından sistematik iş akışına

Literatür taraması başlangıçta keşif niteliğindedir. Araştırmacı alanı tanır, kavramların sınırlarını görür, temel tartışmaları ayırır, hangi soruların yanıtsız kaldığını fark eder. Bu keşifsel aşamada araç serbestçe kullanılabilir. Kavram ağları kurulabilir, terminoloji tartışılabilir, alan haritalanabilir.

Ancak bir noktadan sonra tarama sistematikleşmek zorundadır. Hangi veri tabanları kullanıldı, hangi arama sorguları denendi, hangi dil ve tarih sınırları uygulandı, hangi kayıtlar dahil edildi ve hangileri dışarıda bırakıldı. Bu sorular yanıtlanmadan literatür taraması yalnızca iyi niyetli bir dolaşma olarak kalır. Yeniden üretilebilir araştırmada tarama protokolünün belgelenmesi, bulguların belgelenmesi kadar önemlidir (Wilson ve diğerleri, 2017).

Claude Code bu aşamada kaynak künye çıkarma, DOI doğrulama, kaynak pasaportu açma ve veri tabanı katmanlarını ayırma işlerinde güçlüdür. Tarama sırasında üretilen arama günlükleri, kullanılan sorgu dizeleri ve dahil etme ile dışlama kararları ayrı dosyalara kaydedilmelidir. Bu kayıtlar ilerleyen aşamalarda yöntem bölümünün temelini oluşturur ve sistematik bir tarama gerektiren dergilerde hakemler bu belgeleri doğrudan talep edebilir.

Önemli bir sınır burada da geçerlidir: dahil etme ve dışlama kararlarının son sahibi insan araştırmacıdır. Bir kaynağın kapsama alınıp alınmayacağı kararı alan bilgisine, araştırma sorusuna ve yöntemsel denkleme göre verilir. Ajan bu kararı araştırmacı adına veremez. Verilmiş kararı kayda geçirebilir, tutarsızlıkları işaretleyebilir, eksik bilgileri tamamlamaya yardımcı olabilir.

## 4. Etik kuruldan önce yapay zekâ sınırları

Etik kurul başvurusu araştırma başladıktan sonra tamamlanan bir evrak değildir, özellikle yapay zekâ destekli araştırmada. Çünkü verinin hangi araçlarla işleneceği, hangi dizinlerde tutulacağı, anonimleştirme işleminin ne zaman yapılacağı ve ajanın hangi materyale erişemeyeceği araştırma tasarımının parçasıdır.

Klinik veri, mülakat dökümü, öğrenci metni ya da küçük topluluklara ait saha notları söz konusu olduğunda yaşam döngüsü hemen hassas veri protokolüne geçer. Ham veri ile çalışma verisi ayrılır. Kimliksizleştirme tamamlanmadan ajan oturumuna veri aktarılmaz. Bu kural kolaylık uğruna esnetilmez. Araştırmacı etik kurula yalnızca katılımcı bilgi formunu değil, yapay zekâ araçlarının hangi aşamada nasıl kullanıldığını ve veri güvenliğinin nasıl sağlandığını da açıklar.

Bu aşamada üretilecek belge etik ve veri güvenliği notudur. Bu not ilerleyen aşamalarda etik kurul dosyasına, yöntem bölümüne ve yapay zekâ katkı beyanına dönüşür. Araştırma türüne bağlı olarak hangi verilerin anonimleştirilmeden ajan oturumuna girmeyeceği, yerel depolama ile bulut işlem arasındaki tercih ve çalışma sırasında ortaya çıkan yeni veri türleri için ek protokoller bu belgede yer alır. Özellikle ön kayıt süreçlerinde çalışan araştırmacılar için bu protokolün, analiz başlamadan önce yazılmış olması hem bilimsel hem etik bir gerekliliktir (Nosek ve diğerleri, 2018).

## 5. Veri toplama ve veri hazırlama

Veri toplama aşamasında yapay zekânın rolü dikkatli biçimde sınırlandırılmalıdır. Anket maddesi taslağı hazırlamak, görüşme formu düzenlemek, veri sözlüğü oluşturmak ve proje dosya yapısını kurmak gibi hazırlık görevlerinde destek alınabilir. Katılımcı yanıtlarının veya ham saha verilerinin doğrudan ajan oturumuna aktarılması ise yalnızca onam alındıktan, kimliksizleştirme yapıldıktan ve güvenli işlem koşulları sağlandıktan sonra değerlendirilebilir.

Veri hazırlama aşaması çoğu zaman görünmezdir. Oysa analiz sonuçlarının güvenilirliği büyük ölçüde burada belirlenir. Eksik veri kararları, dışlama ölçütleri, değişken dönüştürme tercihleri, kod kitabı ve veri sözlüğü. Bunlar çalışma bittikten sonra en zor geri dönülen kararlardır. Bu yüzden veri hazırlama kararları ayrı bir eşik olarak ele alınmalı ve her karar gerekçesiyle birlikte kaydedilmelidir. Sandve ve diğerleri (2013), yeniden üretilebilir hesaplamalı araştırmada her veri dönüştürme adımının açıkça belgelenmesini on temel kuraldan biri olarak formüle etmiştir.

Açık bilim ilkeleri bu aşamada erken devreye girer. Veri paylaşım planı, depolama dizini ve formatlama tercihleri yayın sonrası değil veri toplanırken kararlaştırılır. Wilkinson ve diğerlerinin (2016) formüle ettiği FAIR ilkeleri (bulunabilir, erişilebilir, birlikte çalışabilir, yeniden kullanılabilir) bu tercihleri yönlendiren referans çerçevesidir. Ajan bu ilkelere uyumlu dosya yapısı, üst veri şablonu ve belgeleme altyapısı kurmakta yardımcı olabilir. Ama hangi verilerin paylaşılacağı, hangi verinin gizli kalacağı ve hangi koşullarda erişim açılacağı kararlarını araştırmacı ve kurumun etik protokolü belirler.

## 6. Analiz, ön kayıt ve karar günlüğü

Analize geçmek yalnızca kod çalıştırmak değildir. Analize geçmek, hangi iddianın hangi yöntemle sınanacağını yazılı biçimde taahhüt etmektir. Bu taahhüt olmadan doğrulayıcı analiz ile keşfedici analiz birbirine karışır ve veriye bakarak hipotez üretme ile hipotezi sınama aynı analize sıkışır.

Ajan tabanlı analizde bu sorun daha belirgindir. Ajan hızla alternatif testler önerebilir, görselleştirmeler üretebilir, yorumlar yazabilir. Hız, kararın tam olarak ne zaman ve neden alındığını belirsizleştirebilir. Bu nedenle analize geçmeden önce ya bir ön kayıt belgesi hazırlanır ya da en azından yerel bir analiz planı yazılır. Birincil sonuç değişkeni, dışlama ölçütleri, planlanan testler, kabul edilen istatistiksel eşik ve keşfedici analizlerin sınırı bu belgede yer alır. Nosek ve diğerleri (2015), açık araştırma kültürünün kurumsal biçimde yerleşmesinin önkoşullarından birini tam da bu ön taahhüt pratiği olarak tanımlamıştır.

Analiz sırasında ortaya çıkan her plansız karar bir sapma günlüğüne işlenir. Modelin önerdiği bir test eklendiyse, bir değişken çıkarıldıysa, örneklem değiştirildiyse bu değişiklik gerekçesiyle birlikte kaydedilir ve keşfedici analiz olarak işaretlenir. Kaydedilmeden yapılan her değişiklik makalenin yeniden üretilebilirliğini sessizce aşındırır. Ajan bu günlüğü oluşturmakta, tutmakta ve analiz tamamlandığında tartışma bölümüne işlenecek sapmaların özetini çıkarmakta yardımcı olabilir. Ama değişiklik kararını meşrulaştıran bağlamsal gerekçeyi araştırmacı yazar.

## 7. Yazım, gönderim ve hakemlik

Yazım aşamasında yapay zekâ desteği en görünür biçimine kavuşur. IMRAD iskeletini kurmak, iki dilli yeniden yazım yapmak, DOI doğrulamak, dergi uyumu değerlendirmek, kapak mektubu hazırlamak ve yapay zekâ katkı beyanı taslağı üretmek bu aşamanın temel görevleridir. Ancak yazım aşaması yalnızca metin üretimi değildir. Araştırma boyunca alınmış kararların, tercih edilen çerçevelerin ve keşfedilen bulguların okunabilir ve savunulabilir bir forma kavuşturulmasıdır.

Bu fark önemlidir. Model akıcı metin üretebilir, ama araştırmacının hangi bulguyu öne çıkardığını, hangi sınırlamayı dürüstçe adlandırdığını ve hangi çıkarımın veriden değil yorumdan geldiğini belirleyemez. Bu kararlar araştırmacının entelektüel kimliğine aittir ve yapay zekâ beyanında eksiksiz biçimde ifade edilmelidir. Yayın süreci giderek daha fazla şeffaflık talep etmekte, üretici yapay zekânın hangi bileşende nasıl kullanıldığı sorusunu standart hale getirmektedir (Nosek ve diğerleri, 2015).

Hakemlik aşaması yaşam döngüsünün sonu değildir. Yeni bir üretim turudur. Hakem yorumu geldiğinde izlenebilirlik matrisi açılır. Her yorum bir satıra bağlanır, yapılan ya da reddedilen değişiklik konumu ve gerekçesiyle kaydedilir, revize edilmiş bölüm orijinal bölümle karşılaştırılabilir biçimde arşivlenir. Yapay zekâ revizyon metninin herhangi bir bileşeninde kullanıldıysa beyan derginin güncel politikasına göre güncellenir. Belcher'ın (2019) gösterdiği gibi, başarılı akademik yayın süreci ustalık değil sistemdir. Hakemlik turu bu sistemin en kritik noktasıdır ve izlenebilirlik olmadan geçilemez.

Gönderim öncesi kontrol listesi şu öğeleri kapsar: dergi uyumu ve kapsam değerlendirmesi, biçimlendirme ve kelime sayısı sınırı, etik onay numarasının tutarlılığı, yapay zekâ katkı beyanının varlığı, kaynakların DOI ile doğrulanmış olması ve açık bilim bileşenlerinin (veri, kod, ön kayıt) bağlantılarının çalışıyor olması. Bu kontrol listesi ajan aracılığıyla yönetilebilir. Ama son imzayı araştırmacı atar.

## 8. Sunum, kamu iletişimi ve öğretim

Bir çalışma makale yayımlandığında bitmez. Konferansta sunulur, derste anlatılır, kamuya aktarılır, öğrencinin metnine örnek olur. Bu aşamada metin türü değiştiği için etik sorumluluk da biçim değiştirir. Slayt, poster, ders izlencesi, blog yazısı ve sosyal medya metni aynı akademik çekirdekten çıkar. Ama her biri farklı bir okuyucuya ve farklı bir yorum çerçevesine hitap eder.

Yapay zekâ burada biçim dönüştürme konusunda güçlüdür. Uzun bir makaleyi ders materyaline uyarlamak, poster için kilit bulguları düzenlemek, konferans sunumu için bölüm sıralamasını yeniden kurmak. Bunlar ajanın işe yarar biçimde katkı sunduğu görevlerdir. Ancak sadeleştirme bilginin sorumluluğunu azaltmaz. Ruh sağlığı konularında tanı koymadan anlatmak, kriz durumlarında yönlendirme eklemek, bireysel deneyimi evrensel gerçekmiş gibi sunmamak ve kaynak sadakatini korumak yükümlülükleri sunum biçimine bakılmaksızın geçerlidir.

Öğretim bağlamında ek bir sorumluluk katmanı vardır. Öğrencilerin yapay zekâ kullanımına ilişkin kurumsal politikalar birbirinden farklılık gösterir ve bu politikalar gelişmeye devam etmektedir. Bir araştırmacının öğrencilere modelleyeceği pratik, bu politikalarla tutarlı olmalı ve öğrencilerin kendi bağlamlarında neye izin verildiğini, neyin gerekçelendirme gerektirdiğini anlayabilmelerini sağlamalıdır.

## 9. Arşiv, açık bilim ve kapanış

Yaşam döngüsünün son aşaması arşivdir. Arşiv, çalışmanın bittiği yer değildir. Gelecekteki çalışmanın başlayacağı yerdir. Kaynak pasaportları, analiz kodu, veri sözlüğü, ek materyal, karar günlükleri, sapma kayıtları, yapay zekâ katkı beyanları ve açık bilim paketi burada birleşir. Kitzes ve diğerleri (2018), veri yoğun araştırmada arşivin yeniden üretim değerinin yalnızca depolanan dosyalara değil, bu dosyaların ne zaman ve nasıl üretildiğini gösteren belgelere bağlı olduğunu somut vaka çalışmalarıyla göstermiştir.

Bu aşamada araştırmacı kendisine tek bir soru sorar: bu çalışma beş yıl sonra açıldığında, araştırmacının kendisi dahil, herhangi biri neyin neden yapıldığını anlayabilecek mi? Eğer yanıt olumsuzsa, yayımlanmış makale bile arşiv açısından eksik kalmıştır. İyi bir arşiv yalnızca dosya depolamaz. Kararın izini, kaynağın kökenini ve insan denetiminin hangi aşamada nasıl gerçekleştiğini korur.

FAIR ilkeleri arşiv aşamasında en somut biçimini alır: veriler bulunabilir bir depo adresinde mi, meta veri standartlarına uygun mu, farklı yazılımlarla açılabilecek formatlarda mı ve yeniden kullanım koşulları açıkça belirtilmiş mi? Wilson ve diğerleri (2014) bu gereklilikleri bilimsel hesaplama için temel pratik standartlar olarak tanımlamıştır. Bu standartlar yalnızca veri bilimcileri için değil, nicel ya da nitel herhangi bir araştırma yürüten sosyal bilimci için de geçerlidir.

Arşiv kapanışı aynı zamanda bir sonraki projenin açılışıdır. Önceki projenin arşiv kararları bir sonraki projenin tasarım kararlarını besler. Kavramsal çerçeve yeniden kullanılır, ölçekler güncellenir, veri sözlüğü genişletilir, yöntem açıklaması rafine edilir. Bu süreklilik, birbirinden kopuk projeler yerine gelişen bir araştırma hattı inşa eder.

## 10. Skill yönlendirmesi ve çıktı standardı

Bu kitapçığın pratik karşılığı `/research-lifecycle-pipeline` skill'idir. Bu skill araştırmacının mevcut aşamasını belirler, bu aşamaya özgü risk düzeyini çıkarır, kullanılacak skill listesini önerir ve oturum sonunda hangi artefaktların arşive yazılması gerektiğini bildirir.

Her aşamanın bir çıktısı olmalıdır. Fikir notu, arama günlüğü, etik veri notu, analiz planı, kaynak pasaportu, açık bilim paketi, hakem yanıt matrisi, sunum beyanı ya da arşiv kapanış kaydı. Bunlardan hangisinin üretildiği aşamaya ve araştırma türüne göre değişir. Ama çıktısı olmayan bir aşama, ileride yeniden üretilemeyen ve kanıtlanamayan bir aşamadır.

Her aşamada ajan desteğinin boyutu da değişir. Fikir aşamasında ajan bir düşünce ortağıdır. Literatür aşamasında bir kaynak yöneticisidir. Etik aşamasında bir uyarı ve belgeleme aracıdır. Analiz aşamasında bir hesaplama ortağıdır. Ama karar sahibi değildir. Yazım aşamasında bir dil ve biçim destekçisidir. Ama entelektüel sorumluluğu devralamaz. Arşiv aşamasında bir düzenleme ve doğrulama aracıdır.

Bu dağılım tesadüf değildir. Her aşamada insan araştırmacının taşıması gereken sorumluluk, ajanın alabileceği görev kadar belirgindir. Yaşam döngüsü disiplini, araştırmacıyı bu sınırları her aşamada yeniden hatırlatarak çalışmaya davet eder. Araştırmayı kahramanca hafıza ve kişisel özen yükünden çıkarır. Görünür, denetlenebilir ve aktarılabilir bir çalışma düzenine yerleştirir.

---

## Kaynakça

Atıflar APA 7 biçimindedir. Tüm DOI bağlantıları 2026-06-21 tarihinde Crossref üzerinden doğrulanmıştır. Belcher (2019) ve Kitzes ve diğerleri (2018) kitap künyelerine ait ISBN'ler yayıncı katalog kayıtlarıyla teyit edilmiştir.

Belcher, W. L. (2019). *Writing your journal article in twelve weeks: A guide to academic publishing success* (2. baskı). University of Chicago Press. ISBN 978-0-226-49991-8

Kitzes, J., Turek, D., & Deniz, F. (Ed.). (2018). *The practice of reproducible research: Case studies and lessons from the data-intensive sciences*. University of California Press. ISBN 978-0-520-29673-3

Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J., & Ioannidis, J. P. A. (2017). A manifesto for reproducible science. *Nature Human Behaviour*, *1*(1), Article 0021. https://doi.org/10.1038/s41562-016-0021

Nosek, B. A., Alter, G., Banks, G. C., Borsboom, D., Bowman, S. D., Breckler, S. J., Buck, S., Chambers, C. D., Chin, G., Christensen, G., Contestabile, M., Dafoe, A., Eich, E., Freese, J., Glennerster, R., Goroff, D., Green, D. P., Hesse, B., Humphreys, M., … Yarkoni, T. (2015). Promoting an open research culture. *Science*, *348*(6242), 1422–1425. https://doi.org/10.1126/science.aab2374

Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, *115*(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, *9*(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.-W., Bonino da Silva Santos, L., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., … Mons, B. (2016). The FAIR guiding principles for scientific data management and stewardship. *Scientific Data*, *3*, Article 160018. https://doi.org/10.1038/sdata.2016.18

Wilson, G., Aruliah, D. A., Brown, C. T., Chue Hong, N. P., Davis, M., Guy, R. T., Haddock, S. H. D., Huff, K. D., Mitchell, I. M., Plumbley, M. D., Waugh, B., White, E. P., & Wilson, P. (2014). Best practices for scientific computing. *PLoS Biology*, *12*(1), e1001745. https://doi.org/10.1371/journal.pbio.1001745

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLoS Computational Biology*, *13*(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510

---

**Kitapçık kimliği.** `001-02-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 2272 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 9
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`001-01-0004`](../001-01-0004/tr.md). CLAUDE.md ve Kalıcı Talimat Disiplini
**Sonraki kitapçık.** [`002-04-0001`](../../002-academic-access/002-04-0001/tr.md). DergiPark, ULAKBİM TR Dizin, HEAL Link ve Bölgesel İndeksleme
