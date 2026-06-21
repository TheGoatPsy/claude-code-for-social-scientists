---
title_en: "Memory as Vault. A First Principles Introduction"
title_tr: "Hafızayı Arşive Dönüştürmek. İlkesel Bir Giriş"
booklet_id: "003-01-0001"
category: "003-memory-system"
language: "tr"
version: "0.2.0"
date_published: "2026-05-24"
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
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.8 as of 2026-06-21
    role: "drafting, verification, citation lookup"
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
original_concept: true
---

# Hafızayı Arşive Dönüştürmek. İlkesel Bir Giriş

İlkesel Bir Giriş

## Giriş

Önceki kategori, akademik erişim altyapısını ele almıştı. Bu kitapçık ise erişilen her belgenin nereye gideceği sorusuyla başlar. Bir makale künyesi, bir mülakat dökümü, bir klinik gözlem notu ya da bir alan günlüğü yalnızca bulunmakla yetinmez. Araştırmacının çalışma düzeni içinde yerini bulmalıdır.

Bu kitapçık, bu soruya hafızayı arşive dönüştürme kalıbı üzerinden yanıt verir. Bu kalıp, yazarın özgün bir uygulayıcı kavramıdır. Bilişsel bilim ya da bilgi bilimi literatüründe yerleşik bir kuram olarak sunulmamaktadır. Burada, sosyal bilimcinin yıllar içinde biriken akademik bağlamını kalıcı, gezilebilir ve yeniden kullanılabilir bir yapıda tutmasına yardımcı olan bir çalışma çerçevesi olarak önerilmektedir.

Temel iddia şudur. Akademik hafıza kendiliğinden korunmaz. Not almak, kaynak biriktirmek ya da PDF saklamak tek başına yeterli değildir. Araştırmacının ihtiyacı, biriken bilgiyi yalnızca depolayan değil, bağlayan, geri çağıran ve yeni çalışmalarda yeniden kullanılabilir hâle getiren bir arşiv mimarisidir.

## 1. Niçin Kalıcı Bir Arşiv?

Sorunu iki sosyal bilim örneği üzerinden somutlaştırmak mümkündür. On yıldır klinik pratik yürüten bir psikoloğu düşünelim. Elinde seans notları, vaka formülasyonları, süpervizyon kayıtları ve okuduğu yüzlerce makalenin özetleri vardır. Bu birikim klinik sezginin, mesleki hafızanın ve akademik üretimin önemli bir parçasıdır. Ancak farklı klasörlere, not uygulamalarına, PDF kenar notlarına ve eski disk yedeklerine dağılmışsa, fiilen erişilebilir değildir.

Benzer biçimde Komotini ve çevresindeki köylerde uzun süreli bir saha çalışması yürüten bir araştırmacıyı düşünelim. Elinde alan defterleri, gözlem günlükleri, fotoğraflar, görüşme notları ve mülakat dökümleri vardır. Bu birikim yalnızca veri değildir. Yıllar içinde oluşan saha bilgisinin, ilişkilerin, bağlamın ve kavramsal sezginin kaydıdır. Fakat yapısız kaldığında her yeni çalışma, önceki emeğin önemli bir kısmını yeniden kurmak zorunda bırakır.

Her iki örnekte de sorun aynıdır. Bağlam birikir, ancak birikmek erişmek anlamına gelmez. Kronolojik bir not defterinde bir şeyi bulmak için onu ne zaman yazdığınızı hatırlamanız gerekir. Yapısal bir arşivde ise bilginin hangi konuya, hangi projeye, hangi kaynak ailesine ve hangi araştırma kararına ait olduğunu bilmeniz yeterlidir.

Bu ayrım uzun vadede belirleyicidir. Hafızayı arşive dönüştürme kalıbı, yapay zekâ destekli bir çalışma aracını geçici bir not yardımcısından çıkarıp, araştırmacının akademik bağlamıyla çalışabilen kalıcı bir bilgi düzenine bağlamayı amaçlar. Bu kalıbın verimlilik sağlayacağı iddiası, bilgi erişimi literatüründen ve uygulayıcı deneyiminden türeyen bir çıkarımdır. Kontrollü bir araştırmada doğrudan sınanmış bir etki iddiası olarak okunmamalıdır.

## 2. Tarihsel Zincir. Memex'ten Zettelkasten'a

Hafızayı arşive dönüştürme fikri, yalnızca çağdaş yapay zekâ araçlarıyla ortaya çıkmış değildir. Kişisel bilgi mimarisinin daha uzun bir tarihsel çizgisi vardır. Bu çizgiyi görmek, önerilen kalıbın neden yalnızca pratik bir klasör tavsiyesi olmadığını anlamaya yardımcı olur.

Bu hattın erken ve etkili başlangıç noktalarından biri Vannevar Bush'un Memex tasarımıdır. Bush (1945), bireyin kitaplarını, kayıtlarını ve yazışmalarını saklayabilecek, bunlar arasında çağrışımsal izler kurabilecek kişisel bir hafıza aygıtı tasavvur etmişti. Bush'un temel sezgisi güçlüydü. İnsan zihni yalnızca hiyerarşik klasörlerle değil, çağrışımlarla da çalışır. Bu nedenle bilgi sistemi de yalnızca tek bir ağaç yapısına değil, bağlantılara ve izlere dayanmalıdır.

Ted Nelson (1965), hipertekst fikrini geliştirerek metinlerin doğrusal değil ağsal biçimde birbirine bağlanabileceğini gösterdi. Niklas Luhmann ise Zettelkasten sistemiyle bu düşüncenin akademik üretimde ne kadar güçlü olabileceğini pratik olarak ortaya koydu. Luhmann'ın fiş kutusu, her biri atomik bir düşünce taşıyan, birbirine referanslarla bağlanan notlardan oluşuyordu. Bu sistem, onun üretkenliğinin arkasındaki önemli çalışma düzenlerinden biri olarak tartışılır.

Sönke Ahrens (2017), Zettelkasten yaklaşımını çağdaş bilgi çalışanları için yeniden yorumladı. Atomik notlar, bağlantılar ve not alma sistemini yalnızca depolama değil düşünme aracı olarak görme fikri, bugün dijital arşivlerin temel mantığıyla güçlü biçimde örtüşür.

Bush, Nelson, Luhmann ve Ahrens çizgisinin ortak noktası şudur. Bilgi yalnızca saklandığında değil, bağlantılandığında değer kazanır. Bu kitapçığın önerdiği arşiv kalıbı, bu geleneği yapay zekâ destekli araştırma çalışma düzenine taşır. Yeni olan, geri çağırma ve sentez adımlarının artık arşiv içinde çalışan bir dil modeliyle desteklenebilmesidir.

## 3. Kalıbın İşlevsel İlkeleri

Hafızayı arşive dönüştürme kalıbı, birkaç işlevsel ilkeye dayanır. Bu ilkeler belirli bir yazılıma bağlı değildir. Amaç, araştırmacının yıllar boyunca taşıyabileceği bir bilgi düzeni kurmaktır.

İlk ilke düz metindir. Arşivdeki belgeler mümkün olduğunca açık, taşınabilir ve uzun ömürlü biçimlerde tutulmalıdır. Markdown bu nedenle güçlü bir seçenektir. Herhangi bir editörle açılabilir, özel bir yazılıma bağımlı değildir ve uzun vadeli taşınabilirlik sağlar.

İkinci ilke üst veridir. Frontmatter, bir dosyanın başına eklenen yapılandırılmış bilgi alanıdır. Tarih, tür, etiket, proje, ilişkili dosyalar ve kaynak durumu gibi bilgiler burada tutulabilir. Bu alanlar dosyayı yalnızca insan için değil, araçlar için de sorgulanabilir hâle getirir.

Üçüncü ilke dosya ağacıdır. Bilgi, rastgele bir klasörde değil, araştırmacının çalışma mantığını yansıtan bir dizin içinde yaşamalıdır. Dosya ağacı yalnızca düzen değil, gelecekteki erişilebilirliğin mühendislik temelidir.

Dördüncü ilke bağlantıdır. Belgeler arasındaki bağlantılar, Nelson'un hipertekst fikrinin arşiv içindeki karşılığıdır. Bir mülakat notu, bir kavram notuna, bir kaynak pasaportuna ve bir makale taslağına bağlanabilir. Böylece bilgi tekil dosyalarda donmaz, ilişkili bir ağ içinde hareket eder.

Beşinci ilke içerik haritasıdır. Maps of Content, yani MOC, belirli bir konuya giriş kapısı işlevi görür. Araştırmacı bir temaya girmek istediğinde tek tek arama yapmak yerine o temanın ana haritasından ilerleyebilir.

Bu ilkelerin somut uygulaması değişebilir. Markdown yerine başka bir düz metin biçimi, farklı bir üst veri şeması ya da farklı bir klasör mantığı kullanılabilir. Değişmemesi gereken şey alttaki mantıktır. Bilgiyi yakala, sakla, geri çağır ve yeni bağlamda kullan.

## 4. Hafızayı Arşive Dönüştürme Kalıbı

Bu kitapçığın çalışma çerçevesinde hafızayı arşive dönüştürme kalıbı dört adımlı bir döngü olarak düşünülebilir. Input, Store, Retrieve ve Present. Bu İngilizce terimler yazılım ve bilgi mimarisi bağlamında yerleşik oldukları için korunmuştur. Türkçe karşılıklarıyla ifade edersek, bilgi arşive girer, uygun yere yerleştirilir, gerektiğinde geri çağrılır ve yeni bir akademik bağlamda kullanılır.

Input. Bilginin arşive girdiği adımdır.

Store. Bilginin doğru yere, doğru üst veriyle ve doğru bağlantılarla yerleştirildiği adımdır.

Retrieve. Bilginin arama, bağlantı ya da üst veri sorgusu ile geri çağrıldığı adımdır.

Present. Geri çağrılan bilginin yeni bir metinde, analizde, sentezde ya da karar sürecinde kullanıldığı adımdır.

Bu döngüyü sıradan bir veri tabanı işleminden ayıran şey, Present adımından sonra döngünün yeniden Input'a dönmesidir. Araştırmacı bir literatür sentezi yazdığında, o sentez yeni bir atomik not olarak arşive girebilir. Bir kavram haritası oluşturduğunda, bu harita daha önceki notlarla yeni bağlantılar kurabilir. Bir vaka formülasyonu ya da saha analizi geliştirildiğinde, bu çıktı arşivin gelecekteki düşünme düzenini yeniden şekillendirebilir.

Bu nedenle arşiv yalnızca büyümez. Zaman içinde olgunlaşır. İyi tutulan bir arşiv, araştırmacının değişen düşünme biçiminin kaydına dönüşür. Bu, özellikle uzun soluklu doktora projelerinde, klinik araştırmalarda, saha çalışmalarında ve çok dilli literatür izleme süreçlerinde belirleyicidir.

## 5. Claude Code ile Bütünleşme

Hafızayı arşive dönüştürme kalıbının yapay zekâ destekli iş akışındaki gücü, Claude Code'un dosya sistemiyle çalışabilmesinden gelir. Araç, arşiv dizinindeki dosyaları okuyabildiğinde, yanıtlarını yalnızca genel eğitim verisine değil, araştırmacının kendi biriktirdiği belgelere dayandırabilir. Bu, aracı daha değerli kılan ana farklardan biridir.

Bu mekanizma geri çağırma destekli üretim yaklaşımıyla ilişkilidir. Lewis ve diğerleri (2020), retrieval augmented generation çerçevesinde modelin yanıt üretmeden önce harici bir bilgi tabanından ilgili parçaları çekebileceğini göstermiştir. Bu kitapçığın önerisi, iyi yapılandırılmış bir Markdown arşivinin Claude Code için böyle bir bilgi tabanı işlevi görebileceğidir. Bu, rehberin uygulayıcı çıkarımıdır ve kontrollü bir çalışmada doğrudan sınanmış bir öneri olarak sunulmamaktadır.

Burada sınır açık tutulmalıdır. Arşiv, geri çağırma için güçlü bir temel sağlar. Ancak planlama ve araştırma yargısı araştırmacıda kalır. Valmeekam ve diğerleri (2023), büyük dil modellerinin karmaşık planlama görevlerinde önemli sınırlara sahip olduğunu göstermiştir. Bu nedenle Claude Code, arşivden bilgi çekebilir, bağlantıları görünür kılabilir ve sentez önerileri sunabilir. Fakat araştırma planının uygunluğu, bulgunun anlamı ve nihai akademik karar araştırmacının sorumluluğundadır.

Khattab ve diğerlerinin DSPy çalışması, geri çağırma ve üretim bileşenlerinin daha biçimsel işlem hatları içinde nasıl düzenlenebileceğini gösterir. Bu tür yaklaşımlar, arşiv tabanlı iş akışlarının ileride daha denetlenebilir hâle getirilebileceğini düşündürür. Ancak bu kitapçığın amacı belirli bir teknik çerçeveyi zorunlu kılmak değil, sosyal bilimcinin kendi arşivini güvenilir bir geri çağırma katmanı olarak düşünmesini sağlamaktır.

## 6. Geri Çağırma Kalıpları

Bir arşivden bilgi geri çağırmanın birden fazla yolu vardır. Her yol farklı bir araştırma ihtiyacına karşılık gelir.

En temel yol metin aramasıdır. Araştırmacı bir terimi, kavramı ya da ifadeyi arşiv genelinde arar. Bu yöntem hızlı ve kesindir. Ancak yalnızca kullanılan kelimeyi bulur. Aynı anlamı taşıyan farklı ifadeleri kaçırabilir.

İkinci yol dosya örüntüsü eşlemesidir. Belirli bir yıl, proje, klasör ya da dosya adlandırma düzenine göre dosyalar çağrılır. Örneğin 2025 saha notları, belirli bir proje klasöründeki mülakatlar ya da yalnızca kaynak pasaportları bu yolla bulunabilir.

Üçüncü yol frontmatter sorgusudur. Belgelerin üst verileri doğrudan sorgulanır. Belirli bir etikete sahip, belirli tarihten sonra oluşturulmuş ya da belirli bir projeye bağlı tüm dosyalar seçilebilir. Arşivin yapısal gücü en çok burada görünür. Araştırmacı artık yalnızca hatırlamaya değil, üst veriye dayalı seçim yapar.

Dördüncü yol anlam aramasıdır. MCP üzerinden bağlanan bir araç ya da anlam arama sistemi, tam kelime eşleşmesi olmasa bile yakın anlamlı dosyaları yüzeye çıkarabilir. Örneğin kaygı araması, endişe, korku, tedirginlik ya da kaçınma içeren dosyaları da bulabilir.

Bu kalıplar birbirinin yerine geçmez. İyi bir arşiv iş akışı çoğu zaman önce üst veriyle aday dosya kümesini daraltır, sonra bu küme içinde metin araması yapar, en sonunda gerektiğinde anlam aramasıyla daha geniş bağlantıları keşfeder.

## 7. Riskler

Hafızayı arşive dönüştürme kalıbı güçlüdür. Ancak taşıdığı riskler açıkça görülmelidir.

İlk risk kavramsal ve teknik yorgunluktur. Arşivi sürekli düzenlemek, etiketlemek ve bağlantılamak emek ister. Bu emek arşivin sağladığı değeri aşarsa sistem bir yardımdan çok yüke dönüşür. Bu nedenle amaç mükemmel düzen değil, işlevsel gezinmedir. Yeterince iyi yapı, aşırı ayrıntılı ama sürdürülemeyen yapıdan daha değerlidir.

İkinci risk araç bağımlılığıdır. Araştırmacı tüm arşivini tek bir uygulamaya ya da tek bir satıcının ekosistemine bağlarsa, o uygulama değiştiğinde ya da ortadan kalktığında yılların birikimi risk altına girer. Düz metin ilkesi bu riski azaltır. Markdown ya da benzeri açık biçimler, arşivin farklı araçlara taşınabilmesini sağlar.

Üçüncü ve en ağır risk klinik ve hassas veridir. Anonimleştirilmemiş hasta verisi, kimlik bilgisi içeren mülakat dökümü ya da etik kurul kapsamındaki hassas materyal arşive gelişigüzel girmemelidir. Klinik veri ancak kimliksizleştirilmiş, etik kurul onayıyla uyumlu ve veri koruma ilkelerine uygun biçimde arşivlenebilir.

## 8. Türkiye ve Yunanistan Bağlamı

Klinik veri ve insan katılımcı verisi söz konusu olduğunda, Türkiye ve Yunanistan benzer ilkeleri paylaşan iki farklı hukuki çerçeve sunar. Türkiye'de 6698 sayılı Kişisel Verilerin Korunması Kanunu, sağlık verisini özel nitelikli kişisel veri olarak ele alır. Kişisel Verileri Koruma Kurumu (2024), kişisel sağlık verilerinin korunmasına ilişkin rehberinde açık rıza, amaç sınırlılığı ve veri minimizasyonu ilkelerini vurgular.

Bu çerçevenin pratik sonucu açıktır. Türkiye'de klinik psikolog, hastane araştırmacısı ya da insan katılımcıyla çalışan sosyal bilimci, arşivinde anonimleştirilmemiş klinik veri tutmamalıdır. Arşiv, araştırmaya hizmet ederken kişisel veri güvenliğini zayıflatmamalıdır.

Yunanistan ise Avrupa Birliği üyesi olduğu için Genel Veri Koruma Tüzüğü çerçevesine tabidir. Avrupa Veri Koruma Kurulu (2024), araştırmada kişisel verilerin işlenmesine ilişkin sınırları veri minimizasyonu ve amaç sınırlılığı ilkeleriyle ilişkilendirir. Komotini'deki Demokritus Üniversitesi gibi kurumlarda yürütülen saha çalışmalarında mülakat dökümlerinin kodlanması, katılımcı kimliklerinin ayrıştırılması ve erişimin sınırlandırılması bu ilkelerin pratik karşılığıdır.

KVKK ve GDPR aynı değildir. Ancak araştırmacının çalışma arşivi açısından ortak mesaj nettir. Arşiv kullanılabilir olmalı, fakat katılımcının mahremiyetini ve hukuki korumasını zayıflatmamalıdır.

## 9. Köprü. Arşiv Mimarisine

Hafızayı arşive dönüştürme döngüsünün en kritik adımlarından biri Store, yani bilginin doğru yere yerleştirilmesidir. Bu soru ilk bakışta basit görünür. Değildir. Yanlış klasör mimarisi yıllar içinde sessiz bir verimlilik vergisine dönüşür. Dosya aramaları uzar, sonuçlar gürültülenir, yeni projeler eski birikimi yeniden kurmak zorunda kalır.

Doğru arşiv mimarisi ise dosya bulmayı hatırlama yükünden çıkarır, gezinilebilir bir bilgi yapısına dönüştürür. Bir sonraki kitapçık, klasör disiplini ve Maps of Content kalıbını bu nedenle uzun vadeli sonuçları olan mühendislik kararları olarak ele alır.

## Kaynakça

Atıflar APA 7 biçimindedir. DOI'ler ve arXiv kimlikleri 2026-06-21 tarihinde Crossref üzerinden bağımsız olarak doğrulanmıştır. Bush (1945) ve Luhmann (1992), DOI kaydı döneminden öncedir. Ahrens (2017) bir popüler yayındır. Kişisel Verileri Koruma Kurumu (2025) ve Avrupa Veri Koruma Kurulu (2024) düzenleyici otorite gri literatür kaynaklarıdır; bu kaynaklarda DOI bulunmamaktadır.

Ahrens, S. (2017). *How to take smart notes: One simple technique to boost writing, learning and thinking*. ISBN 978-1542866507

Avrupa Veri Koruma Kurulu. (2024). *Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models*. https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en

Bush, V. (1945, Temmuz). As we may think. *The Atlantic Monthly*, 176(1), 101–108.

Khattab, O., Singhvi, A., Maheshwari, P., Zhang, Z., Santhanam, K., Vardhamanan, S., Haq, S., Sharma, A., Joshi, T. T., Moazam, H., Miller, H., Zaharia, M., & Potts, C. (2023). DSPy: Compiling declarative language model calls into self-improving pipelines. *arXiv*. https://arxiv.org/abs/2310.03714

Kişisel Verileri Koruma Kurumu. (2025, 26 Şubat). *Özel nitelikli kişisel verilerin işlenmesine ilişkin rehber*. https://www.kvkk.gov.tr/Icerik/8184/Ozel-Nitelikli-Kisisel-Verilerin-Islenmesine-Iliskin-Rehber

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems*, 33, 9459–9474. https://arxiv.org/abs/2005.11401

Luhmann, N. (1992). Kommunikation mit Zettelkästen. In *Universität als Milieu: Kleine Schriften* (s. 53–61). Haux.

Nelson, T. H. (1965). Complex information processing: A file structure for the complex, the changing and the indeterminate. *Proceedings of the 1965 20th National Conference*, 84–100. https://doi.org/10.1145/800197.806036

Valmeekam, K., Marquez, M., Sreedharan, S., & Kambhampati, S. (2023). On the planning abilities of large language models: A critical investigation. *Advances in Neural Information Processing Systems*, 36, 75993–76005. https://doi.org/10.52202/075280-3320

---

**Kitapçık kimliği.** `003-01-0001`
**Sürüm.** `0.2.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1849 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 9
**Uydurma atıf sayısı.** 0
**Özgün kavram.** Hafızayı arşive dönüştürme kalıbı, yazarın özgün uygulayıcı kavramıdır ve burada rehberin çalışma çerçevesi olarak sunulmaktadır.
**Önceki kitapçık.** [`002-04-0001`](../../002-academic-access/002-04-0001/tr.md). DergiPark, ULAKBİM TR Dizin, HEAL Link ve Bölgesel İndeksleme
**Sonraki kitapçık.** [`004-01-0001`](../../004-vault-architecture/004-01-0001/tr.md). Klasör Disiplini ve Maps of Content (MOC) Kalıbı
