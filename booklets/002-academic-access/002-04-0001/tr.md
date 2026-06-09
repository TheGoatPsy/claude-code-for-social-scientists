---
title_en: "DergiPark, ULAKBIM TR Dizin, HEAL-Link, and Regional Indexing"
title_tr: "DergiPark, ULAKBIM TR Dizin, HEAL-Link ve Bölgesel İndeksleme"
booklet_id: "002-04-0001"
category: "002-academic-access"
language: "tr"
version: "0.1.0"
date_published: "2026-05-24"
date_last_revised: "2026-06-05"
authors:
  - name: "Onour Impram"
    orcid: "0000-0003-1076-3928"
    role: "author, principal reviewer"
ai_assisted: true
ai_tools:
  - name: "Claude Code"
    vendor: "Anthropic"
    model_alias: "claude-opus-4-7"
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.7 as of 2026-05-24
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "co-drafting"
human_review: "complete"
human_review_date: "2026-06-05"
verified_citations_count: 10
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
signature_booklet: true
---

# DergiPark, ULAKBIM TR Dizin, HEAL-Link ve Bölgesel İndeksleme

Bu rehberin önceki kategorisi Claude Code'un kurulumunu ve ilk oturumunu ele almıştı. Kurulumdan sonra ortaya çıkan ilk gerçek soruya geliyoruz: Türkçe ya da Yunanca yayın yapan bir akademisyen, kaynaklarına nasıl güvenilir biçimde erişir? Bu kitapçık, rehberin imza katkısıdır. Uluslararası yapay zekâ rehberlerinin yapısal olarak boş bıraktığı bir kategoriyi açıkça doldurmak için yazıldı. Hedef, bölgesel akademik altyapının haritasını çizmek ve bu altyapıyı Claude Code iş akışına bağlamaktır.

## 1. Uluslararası Rehberlerin Yapısal Sessizliği

Yapay zekâ destekli akademik iş akışı üzerine yazılmış uluslararası rehberlerin neredeyse tamamı, İngilizce literatürü ve İngilizce dünyanın indeksleme altyapısını varsayar. Web of Science, Scopus, Google Scholar, Semantic Scholar. Bu altyapı, dünyanın büyük bir bilim üretimini kapsıyor. Ama tamamını değil. Ortada yapısal bir asimetri var: hem ölçülmüş hem belgelenmiş bir olgu. van Leeuwen ve diğerleri (2001), Science Citation Index'in dil yanlılığını ve bunun ulusal araştırma performansının uluslararası karşılaştırmalarında yarattığı bozulmayı belgeleyen çalışmalarında, bu asimetrinin somut ve ölçülebilir olduğunu göstermiştir. Mongeon ve Paul-Hus (2016) ise Web of Science ile Scopus'un dergi kapsamını karşılaştıran ampirik analizlerinde, her iki veri tabanının da belirli dilleri ve disiplinleri ötekine kıyasla daha zayıf kapsadığını ortaya koymuştur.

Bu asimetrinin pratik sonucu açıktır. Türkiye ve Yunanistan'daki bir sosyal bilimci, yalnızca uluslararası veri tabanlarına dayanan bir Claude Code iş akışı kurarsa, kendi dilindeki literatürün önemli bir kesimini göremez. Bir sistematik derleme, bir kuramsal çerçeve, bir doktora tez taraması: hepsi bu kör nokta yüzünden eksik kalır. Bölgesel indeksleme altyapısı, dolayısıyla, gelişmiş bir özellik değil tutarlı bir iş akışının zorunlu bir parçasıdır. Bu kitapçık o parçanın haritasını ve doldurma protokolünü sunar: Türk ve Yunan altyapıları, erişimin teknik gerçekleri ve somut bir iş akışı.

## 2. DergiPark ve Crossref Köprüsü

DergiPark, TÜBİTAK ULAKBİM ev sahipliğinde yürüyen, yüzlerce Türk akademik dergisinin tek bir çatı altında yayımlandığı platformdur (TÜBİTAK ULAKBİM, 2024). Sosyal bilimci için DergiPark'ın en kritik özelliği Crossref entegrasyonudur. Bu entegrasyon, platformdaki makalelerin Dijital Nesne Tanımlayıcı, yani DOI aldığı anlamına gelir. DOI, Claude Code üzerinden bir makaleye erişmenin en sağlam tutamağıdır. Çünkü DOI, uluslararası bibliyografik altyapıdaki kalıcı ve değişmez bir kayıt adresidir.

Pratikte şöyle çalışır. Bir DergiPark makalesinin DOI'sine sahipseniz, Claude Code bu DOI üzerinden bibliyografik üst veriyi çekebilir. DOI içerik müzakeresi adı verilen mekanizma, bir DOI adresine belirli bir biçim talebiyle gidildiğinde, makalenin künyesini yapılandırılmış olarak döndürür.

```bash
# Bir DOI'nin künyesini BibTeX olarak çek (DergiPark DOI'lerinin de kullandığı Crossref içerik müzakeresi)
curl -LH "Accept: application/x-bibtex" https://doi.org/10.3390/publications7010018
```

Bu komut doi.org üzerinden Crossref'e gider ve makalenin künyesini BibTeX olarak getirir. Örnekteki DOI, Crossref'e kayıtlı herhangi bir makaleye ait olup DergiPark DOI'leri de aynı mekanizmayı kullanır. Künye geldikten sonra Claude Code bu kaydı APA 7 biçimine çevirebilir, arşivinizdeki bir referans dosyasına ekleyebilir ya da kaynakçanızla tutarlılığını denetleyebilir. DergiPark'ın Crossref entegrasyonu, Türkçe literatürü uluslararası bibliyografik altyapıya bağlayan köprüdür. Bu köprü olmasa, Türkçe kaynaklar her seferinde elle girilmek zorunda kalırdı.

## 3. ULAKBİM TR Dizin ve Ulusal Kalite Filtresi

ULAKBİM TR Dizin, Türkiye'nin ulusal atıf dizinidir ve DergiPark'tan farklı bir işlev görür (TÜBİTAK ULAKBİM, 2026). DergiPark bir yayın platformuyken, TR Dizin bir kalite filtresidir. Bir derginin TR Dizin'de yer alması, yayın etiği, hakemlik süreci ve biçimsel standartları kapsayan değerlendirme ölçütlerini karşıladığı anlamına gelir. Bu ayrım sosyal bilimci için belirleyicidir. TÜBİTAK ULAKBİM'in yayımladığı rehber belgelere göre, TR Dizin'de dizinlenen dergiler doktora yeterlik, akademik teşvik, atama ve yükseltme süreçlerinde ağırlık taşır.

Mongeon ve Paul-Hus'un (2016) ortaya koyduğu yapısal kapsam farkının burada doğrudan pratik bir sonucu vardır. Sosyal bilimlerde TR Dizin'deki dergilerin önemli bir kısmı Web of Science ya da Scopus'ta yer almaz. Bu durum, uluslararası ticari veri tabanlarının kapsama politikasının bir yansımasıdır. Dergilerin özsel niteliğiyle ilgisi yoktur. Dolayısıyla bir Türk sosyal bilimci TR Dizin'i çoğunlukla elle takip etmek zorunda kalır. Claude Code burada bir filtre rolü üstlenebilir. Literatür taraması yaparken modele TR Dizin kapsamındaki dergileri ayrı bir başlık altında toplamasını talimat olarak verebilirsiniz. Bu, taramanın çıktısını ulusal değerlendirme süreçlerinin gereksinimlerine göre düzenler ve her taramada uluslararası ile ulusal görünürlük arasındaki ayrımı açıkça ortaya koyar.

## 4. YÖK Tez Merkezi ve Kurumsal Denetimli Bilgi

Yükseköğretim Kurulu Tez Merkezi, 1987'den bu yana Türk üniversitelerinde tamamlanan tezlerin merkezi arşividir (YÖK, 2026). Sosyal bilim araştırmacısı için bu arşiv kendine özgü bir kaynak türüdür. Bir doktora tezi, yayımlanmamış olmakla birlikte kurumsal denetime tabi tutulmuş bir metindir. Aynı konudaki dergi makalesinden çoğu zaman daha ayrıntılı bir yöntem bölümü ve daha kapsamlı bir literatür taraması içerir. Tezlerin kronolojik olarak erişilebilir olması ise Türkiye'deki bir alanın tarihsel gelişimini izlemeyi mümkün kılar.

Claude Code ile çalışırken Tez Merkezi kayıtları için tutarlı bir künye biçimi kurmak önemlidir. Tezler DOI taşımadığından künye bilgisi elle girilir. Arşivinizde standart bir tez künye şablonu tutmak, sonraki taramalarda tutarlılığı korur. Modele bir tez künyesi verdiğinizde, APA 7 yayımlanmamış doktora tezi biçimine çevirmesini ve referans dosyanıza eklemesini isteyebilirsiniz. Tez Merkezi, uluslararası veri tabanlarının neredeyse hiç kapsamadığı bir kaynak türüdür. Bu yönüyle bölgesel iş akışının ayırt edici bir parçasıdır.

## 5. HEAL-Link ve Yunanistan'ın Konsorsiyum Altyapısı

Yunanistan tarafında temel altyapı HEAL-Link'tir, yani Yunan Akademik Kütüphaneler Birliği konsorsiyumudur (HEAL-Link, 2026). HEAL-Link, Yunanistan'daki akademik kurumları ortak bir abonelik çatısı altında toplayarak üye kurumlara Springer Nature, Wiley ve Elsevier gibi büyük yayıncıların paketlerine erişim sağlar. Yunanistan Avrupa Birliği üyesi olduğundan konsorsiyum yapısı Birlik düzeyindeki açık erişim politikalarından en azından kısmen etkilenir. Ancak herhangi bir yayıncı anlaşmasının bu politikalarla tam örtüşmesi, ilgili sözleşmeye bağlıdır ve otomatik değildir.

Komotini'deki Demokritus Üniversitesi somut bir örnek sunar. Demokritus'ta bir psikoloji araştırmacısı HEAL-Link üzerinden bir makaleye erişmek istediğinde, erişim kurumsal kimlik doğrulaması üzerinden gerçekleşir. Bu süreç genellikle EZproxy adı verilen bir aracı sistem üzerinden yürür. EZproxy, kullanıcının kurumsal hesabını yayıncının erişim kontrolüne bağlar. Böylece abonelikli içeriğe kampüs dışından da ulaşılabilir.

```text
# EZproxy üzerinden erişimin temel mantığı
Kullanıcı -> Kurumsal giriş (EZproxy) -> Yayıncı erişim kontrolü -> Tam metin
```

Claude Code bu zincirde tam metni doğrudan indirmez. Tam metin erişimi kullanıcının kurumsal kimliğine bağlıdır ve kullanıcı sözleşmesinin sınırları içinde kalmalıdır. Bunun yerine Claude Code makalenin künyesini, DOI'sini ve erişim adresini düzenler. Kullanıcının kendi tarayıcısı üzerinden tam metne ulaşmasını kolaylaştırır.

## 6. EZproxy ve Kurumsal VPN Gerçekleri

Kampüs dışı erişim, hem Türkiye hem Yunanistan'da pratik bir engel olabilir. EZproxy ve kurumsal sanal özel ağlar, kullanıcının kurumsal kimliğini taşıyarak abonelikli kaynaklara erişimi mümkün kılar. Bu erişimin sınırları katıdır. Erişim kişiseldir ve devredilemez. Bir araştırmacı kurumdan ayrıldığında sona erer. Otomatik toplu indirme ise çoğu yayıncı sözleşmesinde açıkça yasaktır. Bir Claude Code iş akışı tek bir oturumda yüzlerce makaleyi otomatik indirmeye kalkarsa, kurumun erişimi yayıncı tarafından askıya alınabilir.

Bu kısıtlamalardan bölgesel iş akışının temel kuralı doğar. Claude Code künye, DOI ve erişim adresi düzeyinde çalışır. Tam metin indirme, kullanıcının kendi tarayıcısı ve kurumsal kimliği üzerinden sözleşme sınırları içinde yapılır. Bu kural pratik olduğu kadar etiktir. Erişimi sürdürülebilir kılar ve kurumsal aboneliği korur.

## 7. Akademik Teşvik Sisteminde İndekslemenin Yeri

Türkiye'de akademik teşvik düzenlemesi, bir akademisyenin yıllık üretimini puanlayan ve karşılığında ek ödeme sağlayan bir sistemdir. Bu sistemde bir yayının puanı, dergisinin indekslendiği veri tabanına göre değişir. Web of Science'ın belirli dizinlerindeki bir dergi, yalnızca TR Dizin'deki bir dergiden farklı puanlanır. Bu puanlama, dergi seçimini doğrudan şekillendirir.

Bu kitapçık teşvik kurallarının belirli rakamlarını vermez. Düzenleme sık değişir ve belirli bir yıla bağlanmış bir rakam metni hızla eskitir. Önemli olan ilkedir. İndeksleme seçimi, bir akademisyen için görünürlüğün çok ötesinde somut bir kurumsal değerlendirme sonucu doğurur. Claude Code ile literatür taraması ya da dergi seçimi yaparken, modele indeksleme bilgisini ayrı bir alan olarak takip ettirmek bu kurumsal gerçeği iş akışına dahil eder. Bir derginin hangi veri tabanında yer aldığı, taramanın çıktısında her zaman görünür tutulmalıdır. Bu bilgi, kurumsal konumlanmanın somut bir izidir.

## 8. Dil Sınırlarını Aşan Bir Tarama İş Akışı

Bir sosyal anksiyete araştırmacısı Türkçe, Yunanca ve İngilizce literatürü tek bir tarama içinde toplamak istiyor. Geleneksel yol birbirinden kopuk üç ayrı aramanın yürütülmesi, farklı arayüzlerde elde edilen sonuçların elle birleştirilmesi ve tekrarlı kayıtların giderilmesidir. Claude Code ile yapılandırılmış yaklaşım, bu üç katmanı tek bir iş akışında düzenler.

Önce kaynak katmanları tanımlanır. İngilizce katman için uluslararası veri tabanları, Türkçe katman için DergiPark ve TR Dizin, Yunanca katman için HEAL-Link aracılığıyla erişilen yayıncı paketleri. Claude Code'un dış araçlara bağlanması Model Bağlam Protokolü, yani MCP üzerinden yapılır. Bibliyografik bir MCP sunucusu yapılandırıldığında, model arama ve künye çekme işlemlerini bu sunucu üzerinden yürütür.

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

Bu yapılandırma bir iskelettir. Gerçek sunucu adı, kullanıcının tercih ettiği bibliyografik MCP'ye göre değişir. Önemli olan mimaridir. Model künye düzeyindeki işlemleri yapılandırılmış bir araç üzerinden yapar. Tam metin erişimi kullanıcının kurumsal kimliğinde kalır. Tarama tamamlandığında model üç katmanı tek bir kaynakçada birleştirir. Her kaydın hangi katmandan ve hangi indeksten geldiğini ayrı alanlarda tutar. Sonuç, sosyal anksiyete literatürünün dil sınırlarını aşan bütüncül bir haritasıdır. Tenopir ve diğerleri (2019), araştırmacıların makaleleri nasıl keşfettiklerini, okuduklarını ve kullandıklarını inceleyen uluslararası çalışmalarında, araştırmacıların erişim engellerine karşı aktif olarak strateji değiştirdiğini bulmuştur. Bu rehber, bu bulgudan erişim sürtünmesini azaltmanın pratik değerinin kanıtı olarak yararlanır. Ancak bu bulguyu çok dilli Claude Code iş akışlarına genişletmek, doğrudan o çalışmanın kurduğunun değil, rehberin kendi çıkarımıdır.

## 9. Diller Arası Atıf Değerlendirmeleri

Türkçe ya da Yunanca bir kaynağı İngilizce bir makalede atıflarken hem biçimsel hem etik boyutlar devreye girer. Biçimsel olarak APA 7, özgün dildeki başlığı korur ve köşeli parantez içinde İngilizce çevirisini ekler. Bu kural, kaynağın özgün kimliğini korurken İngilizce okura erişilebilirlik sağlar. Claude Code bir Türkçe kaynağın künyesini bu biçime çevirebilir. Ama çevirinin doğruluğu yazarın sorumluluğundadır. Başlık çevirisi alan terminolojisine duyarlıdır ve modele doğrulama yapılmadan devredilemez.

Etik düzeyde, dil asimetrisi bir görünürlük sorununu da beraberinde getirir. Larivière ve diğerleri (2015), akademik yayıncılığın dijital çağdaki tekelci yapısını ortaya koyan çalışmalarında, hangi üretimin görünür olduğunun büyük ölçüde ticari altyapı tarafından belirlendiğini göstermiştir. Bu rehberin bu bulgudan çıkardığı çıkarım, doğrudan o makalenin kurduğu değil, rehberin kendisininkidir. Türkçe ya da Yunanca bir kaynağı İngilizce bir makalede atıflamak, aynı zamanda ticari altyapının sistematik olarak görünmez kıldığı üretime bir ölçüde görünürlük kazandıran bir tercihtir. Bölgesel literatürü uluslararası tartışmaya taşımak, bu kitapçığın altyapısal amacıyla aynı doğrultudadır.

## 10. Kullanıcı Sözleşmelerinin Çerçevelediği Etik Katman

Türk ve Yunan kütüphanelerinin ve yayıncı paketlerinin kullanıcı sözleşmeleri, neyin yapılıp neyin yapılamayacağını belirler. Bir Claude Code iş akışında bu sınırlar her zaman gözetilmelidir. Otomatik toplu indirme yasaktır. Erişim kişiseldir, devredilemez ve abonelikli içerik konsorsiyum dışına aktarılamaz. Bu kurallar, erişimin var olmasının koşuludur.

Bir başka etik katman kaynak kalitesidir. Demir (2018), yağmacı dergilerin nerede kurulduğunu ve araştırmacıların neden onlarda yayımladığını inceleyen karma yöntemli çalışmasında, bu tür dergilerin büyük çoğunluğunun gelişmekte olan ülkelerde konumlandığını ve kurumsal baskıların araştırmacıları düşük kaliteli dergilere yönelten etkenler arasında olduğunu bulmuştur. Bu çalışmanın kapsamı Türkiye'ye özgü değil, geneldir. Bununla birlikte teşvik sistemlerinin yayım tercihlerini şekillendirdiği her bölgesel bağlamda, araştırmacıları düşük kaliteli yayınlara iten yapısal baskılara ilişkin bulguları doğrudan geçerlidir. Bu kitapçık belirli dergi adları vermez, çünkü listeler hızla değişir ve yanlış bir suçlamanın ağır sonuçları olur. Bunun yerine ilke düzeyinde bir güvence önerir. TR Dizin kapsamı, konsorsiyum üyeliği ve kurumsal kütüphane onayı, bir kaynağın güvenilirliği için çok katmanlı bir filtre oluşturur. Açık bilim çerçevesi bu filtreyi tamamlar. UNESCO'nun (2021) açık bilim tavsiyesi, erişim, kalite ve hakkaniyeti bir arada ele alan uluslararası bir politika zemini sunar. Tavsiye metni bu boyutları birbirini destekleyen ilkeler olarak çerçeveler.

## 11. Hafıza Sistemine Köprü

Bu kitapçıkta kurulan altyapı, DOI çekme, TR Dizin filtreleme, HEAL-Link kimlik doğrulaması, tez kayıtları, üç dilde tarama, hep belge ve kayıt üretir. İkinci kritik soru, bu kayıtlara oturum kapandıktan sonra ne olduğudur. Üç dilde toplanmış künyeler, bir doktora tez taraması, bir sistematik derlemenin ham maddesi. Bunların hepsinin bir sonraki oturumda yeniden bulunabilir olması gerekir. Söz konusu olan teknik bir mühendislik kalıbı sorusudur. Bir sonraki kategori, hafızayı arşive dönüştürme kalıbını ilkesel temelinden kurar ve gelen her belgenin nasıl kalıcı ve geri çağrılabilir bir yapıda tutulacağını gösterir. Burada kurulan altyapı, oturum kapandığında kaybolmaz.

## Kaynakça

Atıflar APA 7 biçimindedir. Her DOI Crossref üzerinden bağımsız olarak doğrulanmıştır. Kurumsal URL'ler 2026-06-04 tarihi itibarıyla erişilebilir olduğu doğrulanmıştır.

Demir, S. B. (2018). Predatory journals: Who publishes in them and why? *Journal of Informetrics*, 12(4), 1296-1311. https://doi.org/10.1016/j.joi.2018.10.008

HEAL-Link. (2026). *Hellenic Academic Libraries Link consortium*. https://www.heal-link.gr

Larivière, V., Haustein, S., & Mongeon, P. (2015). The oligopoly of academic publishers in the digital era. *PLOS ONE*, 10(6), e0127502. https://doi.org/10.1371/journal.pone.0127502

Mongeon, P., & Paul-Hus, A. (2016). The journal coverage of Web of Science and Scopus: A comparative analysis. *Scientometrics*, 106(1), 213-228. https://doi.org/10.1007/s11192-015-1765-5

Tenopir, C., Christian, L., & Kaufman, J. (2019). Seeking, reading, and use of scholarly articles: An international study of perceptions and behavior of researchers. *Publications*, 7(1), 18. https://doi.org/10.3390/publications7010018

TÜBİTAK ULAKBİM. (2024). *DergiPark Akademik platform*. https://dergipark.org.tr

TÜBİTAK ULAKBİM. (2026). *TR Dizin dergi değerlendirme kriterleri*. https://trdizin.gov.tr

UNESCO. (2021). *UNESCO recommendation on open science* (SC-PCB-SPP/2021/OS/UROS). https://unesdoc.unesco.org/ark:/48223/pf0000379949

van Leeuwen, T. N., Moed, H. F., Tijssen, R. J. W., Visser, M. S., & van Raan, A. F. J. (2001). Language biases in the coverage of the Science Citation Index and its consequences for international comparisons of national research performance. *Scientometrics*, 51(1), 335-346. https://doi.org/10.1023/A:1010549719484

YÖK. (2026). *Yükseköğretim Kurulu Ulusal Tez Merkezi*. https://tez.yok.gov.tr

---

**Kitapçık kimliği.** `002-04-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-04
**Sözcük sayısı (yaklaşık).** 2087 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 10
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`001-01-0003`](../../001-foundations/001-01-0003/tr.md). Kurulum, İlk Oturum, Sağlık Testleri
**Sonraki kitapçık.** [`003-01-0001`](../../003-memory-system/003-01-0001/tr.md). Hafızayı Arşive Dönüştürmek, İlkesel Bir Giriş
