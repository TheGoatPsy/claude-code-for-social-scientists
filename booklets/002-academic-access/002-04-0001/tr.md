---
title_en: "DergiPark, ULAKBIM TR Dizin, HEAL-Link, and Regional Indexing"
title_tr: "DergiPark, ULAKBİM TR Dizin, HEAL Link ve Bölgesel İndeksleme"
booklet_id: "002-04-0001"
category: "002-academic-access"
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
signature_booklet: true
---

# DergiPark, ULAKBİM TR Dizin, HEAL Link ve Bölgesel İndeksleme

Bu kitapçık, Claude Code for Social Scientists rehberinin akademik erişim kategorisini açar. İlk kategori, Claude Code'un ne olduğunu, ajanlı çalışma mantığını, kurulumunu ve kalıcı talimat disiplinini ele almıştı. Bu kitapçık ise kurulumdan sonra ortaya çıkan ilk ciddi soruya odaklanır. Türkçe, Yunanca ve İngilizce kaynaklarla çalışan bir sosyal bilimci, akademik literatüre nasıl güvenilir biçimde erişir ve bu erişimi Claude Code iş akışına nasıl sorumlu biçimde bağlar?

Bu soru teknik görünür, ancak yalnızca teknik değildir. Literatür taraması, araştırmacının hangi kaynakları gördüğü, hangi kaynakları dışarıda bıraktığı ve hangi kaynakları güvenilir saydığı üzerinden şekillenir. Bir arama yalnızca Web of Science, Scopus ya da Google Scholar üzerinden yürütüldüğünde, Türkçe ve Yunanca literatürün önemli bir bölümü görünmez kalabilir. Bu görünmezlik, yalnızca kaynak sayısını azaltmaz. Araştırma sorusunun bağlamını, kavramsal haritasını ve bölgesel duyarlılığını da zayıflatır.

Bu kitapçığın amacı, bölgesel akademik altyapıyı Claude Code ile çalışırken göz ardı edilmemesi gereken yöntemsel bir katman olarak ele almaktır. DergiPark, ULAKBİM TR Dizin, YÖK Tez Merkezi, HEAL Link, EZproxy, kurumsal VPN ve çok dilli atıf düzeni, burada yalnızca erişim araçları olarak değil, akademik üretimin kapsamını ve güvenilirliğini belirleyen altyapılar olarak tartışılır.

Bu kitapçığın temel iddiası şudur. Bölgesel indeksleme, sosyal bilimci için ikincil bir ayrıntı değildir. Türkçe ve Yunanca kaynaklarla çalışan araştırmacı açısından literatürün adil, eksiksiz ve denetlenebilir biçimde kurulmasının zorunlu koşullarından biridir. Claude Code bu süreci kolaylaştırabilir, ancak erişim haklarını, kaynak kalitesini ve kurumsal sınırları araştırmacının yerine değerlendiremez.

## 1. Uluslararası Rehberlerin Görmediği Alan

Yapay zekâ destekli akademik çalışma üzerine yazılmış birçok uluslararası rehber, İngilizce literatürü ve İngilizce dünyanın indeksleme altyapısını varsayar. Web of Science, Scopus, Google Scholar ve Semantic Scholar bu rehberlerde çoğu zaman doğal başlangıç noktası olarak kabul edilir. Bu veri tabanları önemlidir. Ancak sosyal bilimlerde akademik üretimin tamamını temsil etmez.

Bu temsil sorunu yeni değildir. van Leeuwen ve diğerleri (2001), Science Citation Index kapsamındaki dil yanlılığının ulusal araştırma performansının karşılaştırılmasını nasıl etkilediğini göstermiştir. Mongeon ve Paul-Hus (2016) ise Web of Science ile Scopus'un dergi kapsamını karşılaştırarak, veri tabanlarının dil, disiplin ve yayın türü bakımından eşit temsil sunmadığını ortaya koymuştur.

Bu bulguların Türkiye ve Yunanistan bağlamında doğrudan karşılığı vardır. Türkçe ya da Yunanca çalışan bir sosyal bilimci, yalnızca uluslararası veri tabanlarına dayanan bir tarama yürüttüğünde, kendi alanındaki bölgesel literatürün önemli bir kısmını kaçırabilir. Bu durum sistematik derlemelerde, doktora tezlerinde, yerel bağlamı olan kuramsal çalışmalarda ve azınlık toplulukları üzerine yürütülen araştırmalarda daha da kritik hâle gelir.

Bu nedenle bölgesel indeksleme altyapısı gelişmiş bir ek özellik olarak değil, tutarlı bir akademik iş akışının zorunlu parçası olarak görülmelidir. Claude Code bu altyapıyı kendiliğinden bilmez. Araştırmacı, hangi indeksin ne işe yaradığını, hangi kaynağın hangi yolla doğrulanacağını ve hangi erişim kanalının hangi etik sınırlar içinde kullanılacağını açık biçimde tanımlamalıdır.

## 2. DergiPark ve Crossref Köprüsü

DergiPark, TÜBİTAK ULAKBİM tarafından yürütülen ve Türkiye'de çok sayıda akademik dergiyi tek çatı altında toplayan açık erişimli bir yayın platformudur. Sosyal bilimci için DergiPark'ın en önemli özelliklerinden biri, birçok makalenin DOI üzerinden uluslararası bibliyografik altyapıya bağlanabilmesidir. DOI, bir makalenin kalıcı ve doğrulanabilir kaydına ulaşmayı sağlayan güçlü bir tanımlayıcıdır.

Claude Code ile çalışırken DOI, Türkçe literatürü düzenlemek için önemli bir tutamak sağlar. Bir DergiPark makalesinin DOI bilgisi varsa, Claude Code bu DOI üzerinden bibliyografik üst verinin çekilmesine, APA 7 biçimine dönüştürülmesine, kaynak dosyasına eklenmesine ya da kaynakça tutarlılığının denetlenmesine yardım edebilir. Ancak burada dikkat edilmesi gereken nokta şudur. Claude Code atfı kendisi icat etmemelidir. DOI üzerinden doğrulanmış üst veriyle çalışmalıdır.

Crossref içerik müzakeresi bu noktada pratik bir köprü kurar. DOI adresine belirli bir biçim talebiyle gidildiğinde, makalenin künyesi yapılandırılmış olarak alınabilir. Örneğin BibTeX biçimi aşağıdaki gibi istenebilir.

```bash
curl -LH "Accept: application/x-bibtex" https://doi.org/10.3390/publications7010018
```

Bu örnekteki DOI, Crossref'e kayıtlı herhangi bir makaleye ait olabilir. DergiPark DOI'leri de aynı bibliyografik mantıkla çalışır. Bu sayede Türkçe literatür, yalnızca elle girilen yerel bir kaynak listesi olmaktan çıkar, uluslararası referans altyapısıyla ilişkili hâle gelir.

Bu köprü özellikle iki açıdan değerlidir. Birincisi, kaynakça hatalarını azaltır. İkincisi, Türkçe kaynakların uluslararası metinlerde daha düzenli ve doğrulanabilir biçimde kullanılmasını sağlar. Ancak DOI bulunması, makalenin yöntemsel niteliğini garanti etmez. DOI erişim ve tanımlama aracıdır. Bilimsel değerlendirme yine araştırmacının sorumluluğundadır.

## 3. ULAKBİM TR Dizin ve Ulusal Kalite Filtresi

ULAKBİM TR Dizin, DergiPark'tan farklı bir işleve sahiptir. DergiPark bir yayın platformudur. TR Dizin ise Türkiye'de belirli ölçütleri karşılayan akademik dergileri tarayan ulusal bir dizindir. Bu ayrım önemlidir. Bir derginin DergiPark'ta yayımlanması ile TR Dizin kapsamında yer alması aynı şey değildir.

TR Dizin, yayın etiği, hakemlik süreci, editoryal yapı, düzenlilik ve biçimsel standartlar gibi ölçütler üzerinden dergileri değerlendirir. Bu nedenle Türkiye'deki akademik teşvik, atama, yükseltme, doktora ve kurum içi değerlendirme süreçlerinde ayrıca önem taşır. Sosyal bilimci açısından TR Dizin yalnızca bibliyografik bir kayıt değildir. Ulusal akademik görünürlük ve kurumsal değerlendirme açısından da sonuç doğuran bir göstergedir.

Mongeon ve Paul-Hus'un (2016) ortaya koyduğu kapsam farkı burada pratik karşılık bulur. Sosyal bilimlerde TR Dizin'de yer alan birçok dergi Web of Science ya da Scopus'ta yer almayabilir. Bu durum derginin kendiliğinden niteliksiz olduğu anlamına gelmez. Çoğu zaman uluslararası veri tabanlarının kapsam politikası, dil tercihi ve disiplin öncelikleriyle ilişkilidir.

Claude Code ile literatür taraması yapılırken TR Dizin bilgisi ayrı bir alan olarak izlenmelidir. Örneğin bir kaynak tablosunda dergi adı, DOI, yayın yılı ve örneklem türünün yanında, TR Dizin kapsamında olup olmadığı da kaydedilebilir. Böylece araştırmacı uluslararası görünürlük ile ulusal akademik değerlendirme arasındaki farkı açık biçimde görebilir.

## 4. YÖK Tez Merkezi ve Kurumsal Denetimli Bilgi

YÖK Ulusal Tez Merkezi, Türkiye'de tamamlanan yüksek lisans ve doktora tezlerinin merkezi arşividir. Sosyal bilim araştırmacısı için bu arşiv özel bir kaynak türü sunar. Tezler çoğu zaman dergi makalelerine göre daha ayrıntılı yöntem bölümleri, daha geniş literatür tartışmaları ve daha kapsamlı bağlamsal açıklamalar içerir.

Tezlerin akademik değeri, yayımlanmış makale ile aynı kategoriye konulmalarından değil, kurumsal denetimden geçmiş olmalarından gelir. Bir doktora tezi, hakemli dergi makalesi değildir. Ancak danışmanlık, jüri değerlendirmesi ve üniversite onayı gibi süreçlerden geçtiği için, araştırmacıya alanın gelişimini izlemek açısından önemli bir zemin sunabilir.

Claude Code ile çalışırken YÖK Tez Merkezi kayıtları için tutarlı bir künye şablonu oluşturmak gerekir. Tezlerin çoğu DOI taşımaz. Bu nedenle yazar adı, tez başlığı, yıl, üniversite, enstitü, tez türü ve erişim adresi gibi alanlar standart biçimde kaydedilmelidir. Claude Code bu bilgileri APA 7'ye uygun biçime dönüştürmeye yardım edebilir. Ancak künye verisinin doğruluğu YÖK Tez Merkezi kaydı üzerinden araştırmacı tarafından kontrol edilmelidir.

Bu arşiv, özellikle Türkiye bağlamlı çalışmalar için uluslararası veri tabanlarının görmediği bir kaynak katmanı sağlar. Bu nedenle bölgesel literatür haritası kurarken tezler yalnızca destekleyici materyal olarak değil, alanın tarihsel gelişimini gösteren kurumsal izler olarak da değerlendirilmelidir.

## 5. HEAL Link ve Yunanistan'ın Konsorsiyum Altyapısı

Yunanistan tarafında temel akademik erişim altyapılarından biri HEAL Link'tir. HEAL Link, Yunan akademik kütüphanelerinin ortak abonelik konsorsiyumu olarak çalışır ve üye kurumlara büyük yayıncı paketlerine erişim sağlar. Bu yapı, Yunanistan'daki üniversite araştırmacıları için uluslararası literatüre erişimde önemli bir rol oynar.

Komotini'deki Demokritos Üniversitesi bağlamı bu açıdan somut bir örnek sunar. Bir araştırmacı HEAL Link üzerinden bir makaleye erişmek istediğinde, süreç çoğu zaman kurumsal kimlik doğrulama üzerinden yürür. Kampüs dışında ise EZproxy ya da benzeri sistemler devreye girebilir. Bu sistemler, kullanıcının kurumsal üyeliğini yayıncı erişim kontrolüyle ilişkilendirir.

Burada Claude Code'un rolü dikkatle sınırlandırılmalıdır. Claude Code, araştırmacının kurumsal kimliğiyle abonelikli içeriği otomatik biçimde toplu indiren bir araç olarak kullanılmamalıdır. Bunun yerine makale künyelerini, DOI bilgilerini, erişim adreslerini ve kaynak tablolarını düzenleyen bir çalışma yardımcısı olarak kullanılmalıdır. Tam metin erişimi, araştırmacının kendi kurumsal hesabı ve kütüphane sözleşmesi sınırları içinde kalmalıdır.

```text
Kullanıcı -> Kurumsal giriş, EZproxy veya VPN -> Yayıncı erişim kontrolü -> Tam metin
```

Bu ayrım hem pratik hem etik açıdan önemlidir. Claude Code erişimi kolaylaştırabilir, ancak erişim hakkının sahibi değildir. Kurumsal abonelikler kişiseldir, devredilemez ve yayıncı sözleşmeleriyle sınırlıdır.

## 6. EZproxy ve Kurumsal VPN Gerçekleri

Kampüs dışı erişim, hem Türkiye hem Yunanistan'da akademik çalışmanın pratik eşiklerinden biridir. EZproxy ve kurumsal VPN sistemleri, araştırmacının kurum kimliğini yayıncı sistemlerine taşır. Böylece kampüs dışından abonelikli içeriklere erişim mümkün hâle gelir. Ancak bu erişim sınırsız değildir.

Birincisi, erişim kişiseldir. Araştırmacının kurumsal hesabına bağlıdır ve başkalarıyla paylaşılamaz. İkincisi, kurumdan ayrılma ya da yetkinin sona ermesi durumunda erişim hakkı da sona erer. Üçüncüsü, birçok yayıncı sözleşmesi otomatik toplu indirmeyi açıkça yasaklar. Bu nedenle Claude Code'un tek oturumda yüzlerce tam metni indirmesi gibi bir iş akışı hem etik hem kurumsal açıdan risklidir.

Bu noktadan bölgesel iş akışının temel kuralı çıkar. Claude Code künye, DOI, erişim adresi, özet, kaynak tablosu ve dizin bilgisi düzeyinde çalışmalıdır. Tam metin erişimi araştırmacının kendi tarayıcısı, kendi kurumsal kimliği ve ilgili lisans koşulları içinde yürütülmelidir.

Bu kural, araştırmacının hızını bir ölçüde sınırlıyor gibi görünebilir. Ancak uzun vadede erişimi sürdürülebilir kılar. Kurumsal aboneliklerin askıya alınmasını, yayıncı sözleşmelerinin ihlal edilmesini ve araştırma ekibinin erişim hakkının riske girmesini önler.

## 7. Akademik Teşvik Sisteminde İndekslemenin Yeri

Türkiye'de akademik teşvik ve benzeri kurumsal değerlendirme süreçlerinde derginin hangi dizinlerde tarandığı somut sonuçlar doğurur. Bu nedenle indeksleme bilgisi yalnızca bibliyografik bir ayrıntı değildir. Araştırmacının dergi seçimini, yayın stratejisini ve kurumsal görünürlüğünü etkileyen bir ölçüttür.

Bu kitapçık belirli teşvik puanları vermez. Çünkü teşvik düzenlemeleri ve kurum içi uygulamalar zaman içinde değişebilir. Kalıcı olan ilke şudur. Bir yayının hangi dizinde yer aldığı, akademisyenin kurumsal değerlendirme bağlamında nasıl konumlanacağını etkiler. Bu nedenle Claude Code ile dergi seçimi, literatür taraması ya da yayın stratejisi çalışılırken indeksleme bilgisi ayrı bir alan olarak tutulmalıdır.

Örneğin bir dergi listesi hazırlanırken derginin Web of Science, Scopus, TR Dizin, DergiPark, DOAJ ya da diğer indekslerdeki durumu ayrı sütunlarda gösterilebilir. Böylece araştırmacı yalnızca konu uyumuna değil, görünürlük ve değerlendirme koşullarına da bakabilir. Bu, yayın stratejisini daha açık ve denetlenebilir hâle getirir.

## 8. Dil Sınırlarını Aşan Bir Tarama İş Akışı

Bir sosyal anksiyete araştırmacısının Türkçe, Yunanca ve İngilizce literatürü aynı çalışma içinde değerlendirmek istediğini düşünelim. Geleneksel yol, üç ayrı dil ve üç ayrı erişim katmanı üzerinden arama yapmak, sonuçları elle birleştirmek ve tekrar eden kayıtları temizlemektir. Bu süreç yapılabilir, ancak hata üretmeye ve zaman kaybettirmeye açıktır.

Claude Code ile daha yapılandırılmış bir yaklaşım kurulabilir. Önce kaynak katmanları tanımlanır. İngilizce literatür için uluslararası veri tabanları, Türkçe literatür için DergiPark, ULAKBİM TR Dizin ve YÖK Tez Merkezi, Yunanca ve uluslararası abonelikli literatür için HEAL Link ve kurumsal erişim yolları ayrı katmanlar olarak belirlenir.

Daha sonra her kaydın hangi dilde, hangi indeks üzerinden ve hangi erişim yoluyla bulunduğu ayrı alanlarda tutulur. Bu, yalnızca kaynak toplamak için değil, taramanın kapsamını denetlemek için de önemlidir. Araştırmacı hangi dilde ne kadar kaynak gördüğünü, hangi kaynak türlerinin eksik kaldığını ve hangi erişim engelleriyle karşılaştığını açık biçimde izleyebilir.

Model Context Protocol, yani MCP, bu tür iş akışlarında bibliyografik araçlara yapılandırılmış erişim sağlayabilir. Ancak MCP bağlantıları kullanıcı tarafından kurulmalı ve sınırlandırılmalıdır. Claude Code'un hangi kaynağa hangi yetkiyle eriştiği açık olmalıdır. Aşağıdaki yapı, yalnızca mimariyi göstermek için verilmiş bir iskelettir. Gerçek sunucu adı ve argümanlar araştırmacının kullandığı bibliyografik MCP'ye göre değişir.

```json
{
  "mcpServers": {
    "bibliyografik-arama": {
      "command": "<bibliyografik MCP sunucusu>",
      "args": ["--source", "crossref"],
      "env": {}
    }
  }
}
```

Bu yapının amacı tam metinleri otomatik indirmek değildir. Amaç künye düzeyindeki işlemleri yapılandırılmış ve denetlenebilir bir araç üzerinden yürütmektir. Tam metin erişimi yine araştırmacının kurumsal kimliği ve lisans koşulları içinde kalır.

Tenopir ve diğerleri (2019), araştırmacıların makaleleri keşfetme, okuma ve kullanma pratiklerini inceledikleri çalışmada, erişim engellerinin araştırmacıları farklı stratejiler geliştirmeye ittiğini göstermiştir. Bu kitapçık bu bulgudan şu sonucu çıkarır. Erişim sürtünmesini azaltan, ancak lisans ve etik sınırları koruyan iş akışları sosyal bilimci için yüksek pratik değer taşır. Bu sonuç, Tenopir ve diğerlerinin doğrudan kurduğu bulgunun ötesinde, bu rehberin çok dilli Claude Code iş akışlarına uyguladığı yöntemsel bir yorumdur.

## 9. Diller Arası Atıf Değerlendirmeleri

Türkçe ya da Yunanca bir kaynağı İngilizce bir makalede kullanmak yalnızca biçimsel bir atıf meselesi değildir. Aynı zamanda görünürlük, çeviri ve kavramsal temsil meselesidir. APA 7, İngilizce dışındaki başlıkların özgün dilde korunmasına ve gerekirse köşeli parantez içinde İngilizce çevirisinin verilmesine imkân tanır. Bu uygulama, hem kaynağın özgün kimliğini korur hem de İngilizce okur için erişilebilirlik sağlar.

Claude Code bu tür bir künyeyi biçimlendirmeye yardım edebilir. Ancak başlık çevirisi araştırmacının sorumluluğundadır. Çünkü kavramların alan içindeki karşılığı, doğrudan makine çevirisine bırakılamayacak kadar hassastır. Özellikle psikoloji, eğitim bilimleri, siyaset bilimi ve azınlık çalışmaları gibi alanlarda bir terimin yanlış çevrilmesi, yalnızca dil hatası değil, kavramsal kayma üretir.

Larivière ve diğerleri (2015), akademik yayıncılığın dijital çağdaki tekelci yapısını tartışırken, hangi üretimin görünür olduğunun büyük ölçüde ticari altyapılar tarafından belirlendiğini göstermiştir. Bu kitapçığın bu bulgudan çıkardığı sonuç şudur. Türkçe ya da Yunanca bir kaynağı İngilizce bir makalede doğru biçimde atıflamak, bölgesel akademik üretimi uluslararası tartışmaya taşımanın küçük ama anlamlı bir yoludur.

## 10. Kullanıcı Sözleşmeleri ve Etik Katman

Akademik erişim yalnızca teknik erişim değildir. Her kütüphane, konsorsiyum ve yayıncı paketi belirli kullanıcı sözleşmeleriyle çalışır. Bu sözleşmeler hangi materyalin indirilebileceğini, nasıl saklanabileceğini, kimlerle paylaşılamayacağını ve hangi otomasyonların yasak olduğunu belirler.

Claude Code iş akışında bu sınırlar açık biçimde korunmalıdır. Otomatik toplu indirme yapılmamalıdır. Abonelikli tam metinler konsorsiyum dışına aktarılmamalıdır. Kurumsal erişim kişisel olmayan bir veri havuzu gibi kullanılmamalıdır. Bu kurallar yalnızca hukuki değil, akademik etik açısından da önemlidir. Çünkü kurumsal erişim hakkı, bütün araştırmacı topluluğunu etkileyen ortak bir imkândır.

Kaynak kalitesi de bu etik katmanın parçasıdır. Demir (2018), yağmacı dergilerde yayın yapma örüntülerini incelerken, kurumsal baskıların ve akademik teşvik mekanizmalarının araştırmacıları düşük kaliteli dergilere yöneltebileceğini göstermiştir. Bu bulgu, belirli bir ülkeye indirgenmemelidir. Ancak yayın baskısının güçlü olduğu bölgesel akademik bağlamlarda dikkatle ele alınmalıdır.

Bu kitapçık belirli dergi adları vermez. Çünkü dergi listeleri değişir ve yanlış sınıflandırma ciddi sonuçlar doğurabilir. Bunun yerine çok katmanlı bir güvence önerir. TR Dizin kapsamı, kurumsal kütüphane onayı, yayıncı şeffaflığı, hakemlik bilgisi, açık bilim ilkeleri ve kaynak doğrulama birlikte değerlendirilmelidir. UNESCO'nun açık bilim tavsiyesi, erişim, kalite ve hakkaniyeti birlikte düşünen uluslararası bir politika zemini sunar.

## 11. Hafıza Sistemine Köprü

Bu kitapçıkta ele alınan bütün erişim katmanları kayıt üretir. DOI kayıtları, TR Dizin bilgisi, DergiPark bağlantıları, YÖK Tez Merkezi künyeleri, HEAL Link üzerinden erişilen yayıncı sayfaları, tarama tabloları, üç dilli kaynak listeleri ve erişim notları. Bunların değeri yalnızca o oturumda kullanılmalarında değil, daha sonra yeniden bulunabilir olmalarında yatar.

Bu nedenle akademik erişim konusu doğrudan hafıza ve arşiv mimarisiyle ilişkilidir. Bir kaynak bir kez bulunduğunda, bir sonraki oturumda yeniden kaybolmamalıdır. Hangi kaynağın hangi dilde, hangi dizinde, hangi erişim yoluyla ve hangi kullanım sınırları içinde bulunduğu kaydedilmelidir.

Bir sonraki kategori bu soruya geçer. Akademik hafıza nasıl arşive dönüştürülür? Kaynak kayıtları, kararlar, notlar ve tarama çıktıları yıllar içinde nasıl korunur? Claude Code ile çalışan bir sosyal bilimci, geçici oturum çıktılarından kalıcı ve geri çağrılabilir bir araştırma arşivine nasıl geçer?

003-01-0001, Hafızayı Arşive Dönüştürmek. İlkesel Bir Giriş, bu noktadan devam eder.

## Kaynakça

Atıflar APA 7 biçimindedir. Her DOI Crossref üzerinden bağımsız olarak doğrulanmıştır. Kurumsal URL'ler 2026-06-21 tarihi itibarıyla erişilebilir olduğu doğrulanmıştır.

Demir, S. B. (2018). Predatory journals: Who publishes in them and why? *Journal of Informetrics*, 12(4), 1296–1311. https://doi.org/10.1016/j.joi.2018.10.008

HEAL-Link. (2026). *Hellenic Academic Libraries Link consortium*. https://www.heal-link.gr

Larivière, V., Haustein, S., & Mongeon, P. (2015). The oligopoly of academic publishers in the digital era. *PLOS ONE*, 10(6), e0127502. https://doi.org/10.1371/journal.pone.0127502

Mongeon, P., & Paul-Hus, A. (2016). The journal coverage of Web of Science and Scopus: A comparative analysis. *Scientometrics*, 106(1), 213–228. https://doi.org/10.1007/s11192-015-1765-5

Tenopir, C., Christian, L., & Kaufman, J. (2019). Seeking, reading, and use of scholarly articles: An international study of perceptions and behavior of researchers. *Publications*, 7(1), 18. https://doi.org/10.3390/publications7010018

TÜBİTAK ULAKBİM. (2024). *DergiPark Akademik platform*. https://dergipark.org.tr

TÜBİTAK ULAKBİM. (2026). *TR Dizin dergi değerlendirme kriterleri*. https://trdizin.gov.tr

UNESCO. (2021). *UNESCO recommendation on open science* (SC-PCB-SPP/2021/OS/UROS). https://unesdoc.unesco.org/ark:/48223/pf0000379949

van Leeuwen, T. N., Moed, H. F., Tijssen, R. J. W., Visser, M. S., & van Raan, A. F. J. (2001). Language biases in the coverage of the Science Citation Index and its consequences for international comparisons of national research performance. *Scientometrics*, 51(1), 335–346. https://doi.org/10.1023/A:1010549719484

YÖK. (2026). *Yükseköğretim Kurulu Ulusal Tez Merkezi*. https://tez.yok.gov.tr

---

**Kitapçık kimliği.** `002-04-0001`
**Sürüm.** `0.2.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 2361 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 10
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`001-01-0003`](../../001-foundations/001-01-0003/tr.md). Kurulum, İlk Oturum ve Sağlamlık Denetimleri
**Sonraki kitapçık.** [`003-01-0001`](../../003-memory-system/003-01-0001/tr.md). Hafızayı Arşive Dönüştürmek. İlkesel Bir Giriş
