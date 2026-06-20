---
title_en: "MCP for the Researcher: What, Why, When"
title_tr: "Araştırmacı İçin MCP: Ne, Neden, Ne Zaman"
booklet_id: "006-01-0001"
category: "006-mcp-plugins"
language: "tr"
version: "0.1.0"
date_published: "2026-06-12"
date_last_revised: "2026-06-20"
authors:
  - name: "Onour Impram"
    orcid: "0000-0003-1076-3928"
    role: "author, principal reviewer"
ai_assisted: true
ai_tools:
  - name: "Claude Code"
    vendor: "Anthropic"
    model_alias: "claude-fable-5"
    model_dated: null  # no dated identifier published by Anthropic for Fable 5 as of 2026-06-12
    role: "drafting, verification, citation lookup"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-20"
verified_citations_count: 6
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Araştırmacı İçin MCP: Ne, Neden, Ne Zaman

Önceki kitapçık oturumun içini ritüellerle düzenledi. Açılış, kapanış ve aradaki koruyucu denetimler artık altyapıya bağlı. Bu kitapçık oturumun dışarıyla kurduğu ilişkiye geçer. Claude Code kendi hâlinde bir adadır. Sizin arşivinizi okur, sizin dosyalarınıza yazar ve eğitiminden taşıdığı bilgiyle konuşur. Oysa araştırma yaşamı adada geçmez. Kaynak kataloğu dışarıdadır, veri tabanı dışarıdadır, referans yöneticisi dışarıdadır. Aradaki köprünün adı Model Context Protocol, kısaca MCP'dir ve bu kitapçık köprüyü araştırmacının gözünden anlatır. Ne olduğu, neden değerli olduğu ve en az bunlar kadar önemlisi, ne zaman gerekmediği.

## 1. Oturumun Sınırı

Her aracın bir erişim sınırı vardır ve bu sınır bilinçli bir güvenlik kararıdır. Claude Code, varsayılan kurulumunda çalışma dizininizdeki dosyalarla ve sizin onayladığınız komutlarla yetinir. Dışarıdaki bir hizmete kendiliğinden bağlanmaz. Bu sınır araştırmacıyı korur, ancak bir bedeli vardır. Literatür taraması yapan bir oturum, kaynak kataloğuna bakamıyorsa modelin hatırladığıyla yetinmek zorundadır.

MCP bu sınırı denetimli biçimde açan standarttır (Anthropic, 2024). Protokol, aracın dışarıdaki bir hizmetle nasıl konuşacağını tek tip kurallara bağlar. Hizmet tarafında küçük bir sunucu durur, araç tarafında o sunucunun sunduğu yetenekler görünür ve aradaki her çağrı tanımlı bir sözleşmeden geçer. Araştırmacının kurduğu şey bir köprüdür ve köprünün iki ucu da görünürdür.

## 2. Ne, Protokolün Sade Tarifi

Teknik sözlüğü iki kavrama indirgemek mümkündür. Sunucu, belirli bir hizmete açılan kapıdır. Bir PubMed sunucusu kaynak kataloğuna, bir Zotero sunucusu referans kitaplığınıza, bir dosya sunucusu belirli bir klasöre açılır. Araç ise o kapıdan hangi işlemlerin geçebileceğini bildirir. Ara, getir, listele. Claude Code bir MCP sunucusuna bağlandığında, o sunucunun araçları oturumun kullanabileceği yetenekler listesine eklenir (Anthropic, 2026).

Somut fark bir örnekle görünür. MCP'siz bir oturumda sosyal kaygı ölçekleri üzerine kaynak istediğinizde model, eğitiminde gördüklerinden bir liste kurar. PubMed sunucusuna bağlı bir oturumda ise aynı istek bir arama çağrısına dönüşür ve dönen liste, kataloğun o anki gerçek kayıtlarıdır. İlkinde model hatırlar. İkincisinde model bakar.

## 3. Neden, Hatırlamak Yerine Bakmak

Hatırlamak ile bakmak arasındaki fark, bu rehberin en çok döndüğü bütünlük sorununun ta kendisidir. Walters ve Wilder (2023), modelin hatırlayarak ürettiği kaynakçalarda uydurma ve hatalı künyelerin yaygınlığını belgeledi. Üretim, gerçeğe benzeyen ama var olmayan kayıtlar çıkarabilir. Gerçek bir katalogdan dönen kayıt ise en azından varlık sorununu çözmüş olarak gelir. Künye oradadır, çünkü kayıt oradadır.

Bu yüzden MCP, araştırma bağlamında bir konfor aracı olmaktan fazlasıdır. Hata türünü değiştirir. Uydurma riskinin yerini, bulunmuş kaydın doğru okunması ve doğru aktarılması gibi denetlenebilir işler alır. Doğrulama yükü ortadan kalkmaz, başka kitapçıklarda anlatılan atıf disiplini aynen sürer. Ancak yükün en tehlikeli bileşeni, yoktan var etme, devreden büyük ölçüde çıkar.

## 4. Ne Zaman Gerekmez

Dürüst bir rehber bu bölümü atlamaz. Her dışa bağlantı bir bakım yükü, bir güven sorusu ve bir kırılma noktasıdır. Wilson ve diğerleri (2017), bilimsel hesaplama pratiğinde aracın en gösterişlisini değil, işi gören en sadesini önerir. İlke MCP kararına doğrudan uygulanır. Haftada bir kez yaptığınız ve bir dakika süren bir işlem için sunucu kurulmaz. Tarayıcıda açtığınız tek bir sayfa yeterliyse köprüye gerek yoktur.

Karar sorusu şudur. Bu bağlantı, oturum içinde sık tekrarlanan ve elle yapıldığında hata biriktiren bir işi mi taşıyor? Yanıt evetse köprü adaydır. Yanıt hayırsa eklenen her sunucu, kullanılmayan bir kapı ve unutulan bir yetki olarak kalır. Az kapılı bir ev, hem daha güvenli hem daha kolay denetlenir.

## 5. Güven Triyajı

Köprü kurulacaksa ilk soru teknik değil, sosyaldir. Bu sunucuyu kim yazdı? Resmî bir sağlayıcının yayımladığı sunucu ile kimliği belirsiz bir depodan indirilen sunucu aynı güven sınıfında değildir. İkinci soru erişim kapsamıdır. Sunucu neye dokunabiliyor? Yalnızca arama yapan bir katalog sunucusu ile dosya sistemine yazabilen bir sunucu farklı risk düzeylerindedir. Üçüncü soru veri akışıdır. Sorgularınız hangi makineye gidiyor ve orada ne kadar tutuluyor?

Bu temkinli tutumun akademik kültürde kökü vardır. Tenopir ve diğerleri (2011), bilim insanlarının veri paylaşımına ilkesel olarak açık ama pratikte temkinli olduğunu, kötüye kullanım ve hak teslimi kaygılarının paylaşım davranışını belirgin biçimde sınırladığını geniş bir anketle gösterdi. Aynı koruyucu içgüdü, araç katmanında da işletilmelidir. Verinizin nereye aktığını bilmeden köprü açmamak, paranoya değil meslek ahlakıdır.

## 6. Veri Akışı ve Kişisel Verilerin Korunması

Triyajın en sert kuralı katılımcı verisine dairdir. Ham görüşme dökümleri, kimlik içeren tablolar ve onam formları, hiçbir üçüncü taraf MCP sunucusundan geçirilmez. Onam formunda öngörülmemiş her aktarım, KVKK ve GDPR yükümlülüklerinden önce katılımcıya verilmiş sözün ihlalidir. Nitel kodlama kitapçığındaki sıralama burada da geçerlidir. Önce anonimleştirme, sonra araç. Anonimleştirilmiş veride bile sunucunun nerede çalıştığı sorulur, çünkü yerel çalışan bir sunucu ile sorguları uzak bir hizmete taşıyan sunucu aynı şey değildir.

Aynı dikkat günlük sorgulara da iner. Bir katalog sunucusuna gönderilen arama dizgesi bile bir veri izidir. Araştırma konunuzun hassas olduğu durumlarda bu izin nerede biriktiğini bilmek istersiniz. Kural yalındır. Köprüden geçen her şeyin bir alıcısı vardır ve alıcıyı tanımadan paket gönderilmez.

## 7. Asgari İzin Kurulumu

Kurulumda ilke, en az yetkidir. Salt okunur mod yeterliyse yazma izni verilmez. Sunucu belirli bir klasöre bakacaksa bütün diske değil o klasöre açılır. Kimlik bilgisi gerekiyorsa yapılandırma dosyasına gömülmez, ortam değişkeninde tutulur ve arşiv deposuna asla girmez. Önceki kitapçığın koruyucu hook'u burada ikinci kez iş görür. Depoya giden her kayıt gizli bilgi taramasından geçtiği için, yanlışlıkla dosyaya yazılmış bir anahtar kapıda yakalanır.

Bu kuralların her biri tek başına küçüktür. Birlikte, bir köprünün en kötü gününde verebileceği zararın tavanını çizerler. Güvenlik mühendisliğinin yaşlı ilkesi araştırma arşivinde de geçerlidir. Bir bileşene, işini yapmaya yetecek kadar yetki ver, fazlasını verme.

## 8. Doğrulama Probları

Kurulan köprü, kullanılmadan önce sınanır ve sınama bilinen bir kayıtla yapılır. Kataloğa bağlandıysanız, künyesini ezbere bildiğiniz bir makaleyi aratın. Dönen kayıt başlığıyla, yazarlarıyla ve DOI'siyle elinizdekiyle eşleşiyorsa köprü doğru kurulmuştur. Eşleşmiyorsa sorun erken ve ucuz yakalanmıştır. Referans yöneticisine bağlandıysanız, kitaplığınızda olduğunu bildiğiniz bir kaydı listeletin.

Bu bilinen kayıt probu, kitapçığın doğrulama ilkesinin en küçük örneğidir. Bir altyapının çalıştığı, ilk gerçek ihtiyaçta değil, sonucu önceden bilinen bir denemede gösterilir. Prob başarılıysa kayıt altına alınır ve köprü artık iş akışının güvenilir bir parçasıdır.

## 9. Beyan ve Yöntem Kaydı

MCP kullanımı, araştırmanın altyapısına dahil olduğu anda yöntemin de parçasıdır. Hosseini ve diğerleri (2023) beyan yükümlülüğünü kullanımın kendisine bağlar ve bu ilke arama altyapısını kapsar. Sistematik bir tarama hangi katalogda, hangi araçla ve hangi tarihte yapıldıysa yöntem bölümü bunu söyler. Yapay zekâ destekli bir tarama akışında MCP sunucusunun adı ve sürümü bu kaydın doğal parçasıdır.

Kayıt yükünü hafifleten araç yine arşivin kendisidir. Hangi kaynağın hangi köprüden, hangi sorguyla ve ne zaman geldiğini oturum sırasında not eden bir defter, beyan cümlesini yazma anında hazır eder. Bir sonraki kitapçığın konusu olan kaynak pasaportu, tam bu defterin sistematik hâlidir.

## 10. Köprü, Kaynakların Kimliğine

Arşiv kuruldu, ritüeller bağlandı ve oturum artık dışarıdaki kataloglara denetimli köprülerle bakıyor. Köprüden geçen her kaynak bir soruyu beraberinde getirir. Bu kayıt nereden geldi, hangi sorguyla bulundu ve hangi taslakta kullanıldı? Bir sonraki kitapçık bu sorunun sistemini kurar. Kaynak pasaportu, her kaynağın oturumlar arası kimlik kartıdır ve atıf bütünlüğünün arşiv katmanındaki güvencesidir.

## Kaynakça

Atıflar APA 7 biçimindedir. DOI'ler 2026-06-12 tarihinde Crossref üzerinden doğrulanmıştır.

Anthropic. (2024). *Model Context Protocol*. https://modelcontextprotocol.io

Anthropic. (2026). *Claude Code documentation*. https://docs.claude.com/en/docs/claude-code

Hosseini, M., Rasmussen, L. M., & Resnik, D. B. (2023). Using AI to write scholarly publications. *Accountability in Research*, 31(7), 715–723. https://doi.org/10.1080/08989621.2023.2168535

Tenopir, C., Allard, S., Douglass, K., Aydinoglu, A. U., Wu, L., Read, E., Manoff, M., & Frame, M. (2011). Data sharing by scientists: Practices and perceptions. *PLoS ONE*, 6(6), e21101. https://doi.org/10.1371/journal.pone.0021101

Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, 13, Article 14045. https://doi.org/10.1038/s41598-023-41032-5

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLoS Computational Biology*, 13(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510

---

**Kitapçık kimliği.** `006-01-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-20
**Sözcük sayısı (yaklaşık).** 1240 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 6
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`005-02-0001`](../../005-hooks-automation/005-02-0001/tr.md). Ritüel Hook'lar: Günlük Kayıt, Oturum Kalıcılığı, Boş Zaman
**Sonraki kitapçık.** [`007-01-0001`](../../007-academic-writing/007-01-0001/tr.md). IMRAD İskeleti: İki Dilli Bir Yaklaşım
