---
title_en: "MCP for the Researcher. What, Why, When"
title_tr: "Araştırmacı İçin MCP. Ne, Neden, Ne Zaman"
booklet_id: "006-01-0001"
category: "006-mcp-plugins"
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
    model_dated: null
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

# Araştırmacı İçin MCP. Ne, Neden, Ne Zaman

## Giriş

Önceki kitapçık oturumun içini ritüellerle düzenlemişti. Açılış, kapanış ve aradaki koruyucu denetimler artık araştırmacının hatırlamasına değil, altyapıya bağlanmıştı. Bu kitapçık oturumun dışarıyla kurduğu ilişkiye geçer. Çünkü araştırma yaşamı yalnızca yerel dosyalardan ibaret değildir. Kaynak katalogları, veri tabanları, referans yöneticileri ve kurumsal sistemler çoğu zaman oturumun dışındadır.

Claude Code varsayılan hâliyle sınırlı bir çalışma alanında hareket eder. Araştırmacının arşivini okuyabilir, izin verilen dosyalara yazabilir ve eğitiminden taşıdığı bilgiyle yanıt üretebilir. Ancak araştırmacının gerçek ihtiyacı çoğu zaman bunun ötesindedir. Bazen modele hatırlatmak değil, dışarıdaki güvenilir bir kaynağa baktırmak gerekir. Model Context Protocol, kısaca MCP, bu ihtiyaca verilen standartlaşmış yanıtlardan biridir.

Bu kitapçığın temel iddiası şudur. MCP, araştırmacı için bir konfor eklentisi olmaktan çok, dış kaynaklara denetimli biçimde bağlanmanın yöntemsel aracıdır. Ancak her bağlantı aynı zamanda yeni bir güven, bakım ve veri akışı sorusu doğurur. Bu nedenle MCP yalnızca ne olduğu üzerinden değil, neden gerekli olduğu ve ne zaman gereksiz olduğu üzerinden de değerlendirilmelidir.

## 1. Oturumun Sınırı

Her aracın bir erişim sınırı vardır ve bu sınır yalnızca teknik bir kısıtlama değildir. Aynı zamanda güvenlik kararıdır. Claude Code varsayılan kurulumunda çalışma dizinindeki dosyalarla ve araştırmacının onayladığı komutlarla sınırlıdır. Dışarıdaki bir hizmete kendiliğinden bağlanmaz. Bu sınır araştırmacıyı korur. Ancak belirli akademik görevlerde bir bedeli vardır.

Literatür taraması yapan bir oturum, kaynak kataloğuna bakamıyorsa modelin hatırladığıyla yetinmek zorunda kalır. Bu durum, özellikle atıf bütünlüğü açısından risklidir. Modelin hatırlaması ile kaynağa bakması aynı şey değildir. Araştırma bağlamında güvenilirlik çoğu zaman bu ayrımda belirir.

MCP, bu sınırı denetimli biçimde açan standarttır (Anthropic, 2024). Protokol, Claude Code'un dışarıdaki bir hizmetle nasıl konuşacağını belirli kurallara bağlar. Hizmet tarafında küçük bir sunucu bulunur. Araç tarafında ise bu sunucunun sunduğu işlemler görünür olur. Araştırmacının kurduğu şey bir köprüdür. Bu köprünün iki ucu da tanımlı ve denetlenebilir olmalıdır.

## 2. Ne. Protokolün Sade Tarifi

MCP'yi teknik ayrıntıya boğmadan iki kavramla anlatmak mümkündür. Sunucu ve araç. Sunucu, belirli bir hizmete açılan kapıdır. Bir PubMed sunucusu akademik kataloglara, bir Zotero sunucusu referans kitaplığına, bir dosya sunucusu belirli bir klasöre açılabilir. Araç ise bu kapıdan hangi işlemlerin geçebileceğini bildirir. Ara, getir, listele, oku ya da sınırlı biçimde yaz.

Claude Code bir MCP sunucusuna bağlandığında, o sunucunun sunduğu araçlar oturumun kullanabileceği yetenekler listesine eklenir (Anthropic, 2026). Böylece model yalnızca kendi eğitim verisine dayanmak zorunda kalmaz. Tanımlı bir arayüz üzerinden dış kaynağa bakabilir.

Somut fark basittir. MCP'siz bir oturumda sosyal kaygı ölçekleri üzerine kaynak istediğinizde model eğitiminde gördüklerinden bir liste kurar. PubMed sunucusuna bağlı bir oturumda ise aynı istek bir arama çağrısına dönüşür. Dönen liste, katalogdaki gerçek kayıtlara dayanır. İlkinde model hatırlar. İkincisinde model bakar. Araştırma açısından bu fark kritiktir.

## 3. Neden. Hatırlamak Yerine Bakmak

Hatırlamak ile bakmak arasındaki fark, bu rehberin merkezindeki bütünlük sorunuyla doğrudan ilişkilidir. Walters ve Wilder (2023), ChatGPT tarafından üretilen kaynakçalarda uydurma ve hatalı künyelerin yaygınlığını göstermiştir. Model, gerçeğe benzeyen ama var olmayan kayıtlar üretebilir. Bu risk yalnızca teknik bir hata değildir. Akademik güvenilirliği doğrudan ilgilendirir.

Gerçek bir katalogdan dönen kayıt ise en azından varlık sorununu çözmüş olarak gelir. Kayıt katalogdadır. DOI, başlık, yazar ve yayın bilgisi doğrulanabilir bir altyapıdan alınır. Elbette bu, bütün denetim yükünün ortadan kalktığı anlamına gelmez. Kayıt yine doğru okunmalı, uygun biçimde aktarılmalı ve bağlama göre değerlendirilmelidir.

Bu nedenle MCP araştırma bağlamında bir kolaylık aracından fazlasıdır. Hata türünü değiştirir. Yoktan kaynak uydurma riskini azaltır ve araştırmacının denetleyebileceği daha somut bir iş yüküne dönüştürür. Atıf disiplini devam eder. Ancak en riskli aşama olan hayali künye üretimi önemli ölçüde sınırlanır.

## 4. Ne Zaman Gerekmez?

Dürüst bir rehber, MCP'nin her durumda gerekli olmadığını açıkça söylemelidir. Her dış bağlantı bir bakım yükü, bir güven sorusu ve bir kırılma noktasıdır. Wilson ve diğerleri (2017), bilimsel hesaplama pratiğinde en gösterişli aracı değil, işi gören en sade çözümü önermektedir. Bu ilke MCP kararına doğrudan uygulanabilir.

Haftada bir kez yapılan ve tarayıcıda bir dakika süren bir işlem için sunucu kurmak çoğu zaman gereksizdir. Tek bir sayfaya bakmak yeterliyse köprüye ihtiyaç yoktur. MCP, sık tekrarlanan, elle yapıldığında hata biriktiren ve oturum içinde yapılandırılmış biçimde yürütülmesi gereken işler için anlam kazanır.

Karar sorusu şudur. Bu bağlantı araştırmacının düzenli olarak yaptığı, hata riski taşıyan ve araçla birlikte daha denetlenebilir hâle gelecek bir işi mi taşıyor? Yanıt evetse MCP adaydır. Yanıt hayırsa eklenen her sunucu kullanılmayan bir kapı ve unutulan bir yetki olarak kalır. Az kapılı bir sistem çoğu zaman daha güvenli ve daha denetlenebilirdir.

## 5. Güven Triyajı

Bir köprü kurulacaksa ilk soru teknik değil, sosyaldir. Bu sunucuyu kim yazdı? Resmî bir sağlayıcı tarafından yayımlanan sunucu ile kimliği belirsiz bir depodan indirilen sunucu aynı güven sınıfında değildir. İkinci soru erişim kapsamıdır. Sunucu neye dokunabilir? Yalnızca arama yapan bir katalog sunucusu ile dosya sistemine yazabilen bir sunucu aynı risk düzeyinde değildir.

Üçüncü soru veri akışıdır. Sorgular nereye gider? Hangi makinede işlenir? Kayıt tutulur mu? Ne kadar süre saklanır? Araştırmacı bu soruların yanıtını bilmeden köprü açmamalıdır.

Tenopir ve diğerleri (2011), bilim insanlarının veri paylaşımına ilkesel olarak açık olmalarına rağmen pratikte kötüye kullanım, hak teslimi ve denetim kaybı gibi kaygılar nedeniyle temkinli davrandıklarını göstermiştir. Aynı temkin araç katmanında da gereklidir. Verinin nereye aktığını bilmeden bağlantı açmamak paranoya değildir. Araştırma etiğinin araç düzeyindeki karşılığıdır.

## 6. Veri Akışı ve Kişisel Verilerin Korunması

Güven triyajının en sert kuralı katılımcı verisiyle ilgilidir. Ham görüşme dökümleri, kimlik içeren tablolar, onam formları, klinik materyaller ve kişisel tanımlayıcı içeren dosyalar hiçbir üçüncü taraf MCP sunucusundan geçirilmemelidir. Onam formunda öngörülmemiş her aktarım, yalnızca teknik bir ihmal değil, katılımcıya verilmiş sözün ihlalidir.

Nitel kodlama ve etik kitapçıklarında kurulacak temel sıralama burada da geçerlidir. Önce anonimleştirme, sonra araç. Anonimleştirilmiş veride bile sunucunun nerede çalıştığı sorulmalıdır. Yerel çalışan bir sunucu ile sorguları uzak bir hizmete taşıyan sunucu aynı şey değildir.

Aynı dikkat günlük sorgular için de geçerlidir. Bir katalog sunucusuna gönderilen arama dizgesi bile araştırma konusuna ilişkin bir veri izi bırakabilir. Araştırma konusu hassassa, bu izin nerede biriktiğini bilmek gerekir. Kural yalındır. Köprüden geçen her bilginin bir alıcısı vardır. Alıcı tanınmadan veri gönderilmez.

## 7. Asgari İzin Kurulumu

MCP kurulumunda temel ilke en az yetkidir. Salt okunur erişim yeterliyse yazma izni verilmemelidir. Sunucu belirli bir klasöre bakacaksa bütün diske değil yalnızca o klasöre erişmelidir. Kimlik bilgisi gerekiyorsa yapılandırma dosyasına gömülmemeli, ortam değişkeni gibi daha güvenli bir yöntemde tutulmalı ve arşiv deposuna asla girmemelidir.

Önceki kitapçıkta ele alınan koruyucu hook'lar burada ikinci kez önem kazanır. Depoya giden her kayıt gizli bilgi taramasından geçerse, yanlışlıkla dosyaya yazılmış bir anahtar kapıda yakalanabilir. Böylece MCP bağlantılarının açtığı risk, başka bir altyapı bileşeniyle sınırlandırılır.

Bu kuralların her biri tek başına küçük görünür. Birlikte, bir köprünün kötü gününde verebileceği zararın üst sınırını çizerler. Araştırma arşivinde güvenlik mühendisliğinin temel ilkesi geçerlidir. Bir bileşene işini yapmaya yetecek kadar yetki verilir. Fazlası verilmez.

## 8. Doğrulama Probları

Kurulan köprü kullanılmadan önce sınanmalıdır. Bu sınama sonucu önceden bilinen bir kayıtla yapılır. Kataloğa bağlandıysanız, künyesini iyi bildiğiniz bir makaleyi aratın. Dönen kayıt başlık, yazarlar, yıl ve DOI bakımından elinizdeki bilgiyle eşleşiyorsa köprü temel düzeyde doğru çalışıyor demektir. Eşleşmiyorsa sorun ilk gerçek ihtiyaç anında değil, erken ve ucuz bir aşamada yakalanmış olur.

Referans yöneticisine bağlandıysanız, kitaplığınızda olduğunu bildiğiniz bir kaydı listeletin. Dosya sistemine bağlandıysanız, hassas veri içermeyen ve içeriğini bildiğiniz bir test dosyasını okutun. Amaç araçtan etkileyici bir yanıt almak değildir. Amaç, altyapının gerçekten beklenen kaynağa baktığını doğrulamaktır.

Bu bilinen kayıt probu, rehberin doğrulama ilkesinin küçük ölçekli uygulamasıdır. Bir altyapının çalıştığı, ilk önemli görevde değil, sonucu önceden bilinen bir denemede gösterilmelidir.

## 9. Beyan ve Yöntem Kaydı

MCP kullanımı araştırmanın altyapısına dahil olduğunda, yöntemsel kaydın da parçası hâline gelir. Hosseini ve diğerleri (2023), yapay zekâ kullanımına ilişkin beyan yükümlülüğünün kullanımın niteliğine bağlı olduğunu vurgular. Bu ilke arama altyapısını da kapsar. Sistematik bir tarama hangi katalogda, hangi araçla, hangi tarihte ve hangi sorguyla yapıldıysa yöntem bölümünde bunun belirtilmesi gerekir.

Yapay zekâ destekli bir tarama akışında MCP sunucusunun adı, sürümü ve görevi bu kaydın doğal parçasıdır. Kullanılan bağlantının ne yaptığı, hangi veriye eriştiği ve araştırmacının bu çıktıyı nasıl denetlediği açık olmalıdır.

Kayıt yükünü hafifleten yapı yine arşivin kendisidir. Hangi kaynağın hangi köprüden, hangi sorguyla ve ne zaman geldiğini oturum sırasında not eden bir defter, beyan cümlesini yazma anında hazır eder. Kaynak pasaportu kitapçığı bu defterin sistematik hâlini kuracaktır.

## 10. Köprü. Kaynakların Kimliğine

Arşiv kurulduğunda, ritüeller bağlandığında ve oturum dış kataloglara denetimli köprülerle bakmaya başladığında yeni bir soru doğar. Köprüden geçen her kaynak nereden geldi? Hangi sorguyla bulundu? Hangi tarihte doğrulandı? Hangi taslakta kullanıldı?

Bir sonraki kitapçık bu sorunun sistemini kurar. Kaynak pasaportu, her kaynağın oturumlar arası kimlik kartıdır. Atıf bütünlüğünün arşiv katmanındaki güvencesi de tam burada başlar.

## Kaynakça

Atıflar APA 7 biçimindedir. DOI'ler 2026-06-21 tarihinde Crossref üzerinden doğrulanmıştır.

Anthropic. (2024). *Model Context Protocol*. https://modelcontextprotocol.io

Anthropic. (2026). *Claude Code documentation*. https://code.claude.com/docs

Hosseini, M., Rasmussen, L. M., & Resnik, D. B. (2023). Using AI to write scholarly publications. *Accountability in Research*, *31*(7), 715–723. https://doi.org/10.1080/08989621.2023.2168535

Tenopir, C., Allard, S., Douglass, K., Aydinoglu, A. U., Wu, L., Read, E., Manoff, M., & Frame, M. (2011). Data sharing by scientists: Practices and perceptions. *PLoS ONE*, *6*(6), e21101. https://doi.org/10.1371/journal.pone.0021101

Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, *13*, Article 14045. https://doi.org/10.1038/s41598-023-41032-5

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLoS Computational Biology*, *13*(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510

---

**Kitapçık kimliği.** `006-01-0001`
**Sürüm.** `0.2.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1393 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 6
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`005-02-0001`](../../005-hooks-automation/005-02-0001/tr.md). Ritüel Hook'lar. Günlük Kayıt, Oturum Kalıcılığı ve Boş Zaman Bakımı
**Sonraki kitapçık.** [`007-01-0001`](../../007-academic-writing/007-01-0001/tr.md). IMRAD İskeleti. İki Dilli Bir Yaklaşım
