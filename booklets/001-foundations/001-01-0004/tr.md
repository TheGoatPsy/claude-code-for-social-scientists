---
title_en: "CLAUDE.md and the Discipline of Standing Instructions"
title_tr: "CLAUDE.md ve Kalıcı Talimat Disiplini"
booklet_id: "001-01-0004"
category: "001-foundations"
language: "tr"
version: "0.2.0"
date_published: "2026-05-29"
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
    model_dated: null  # Anthropic, Opus 4.8 için tarihli tanımlayıcı yayımlamadı (2026-05-29)
    role: "drafting, verification, citation lookup, bilingual authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "full-draft"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 9
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# CLAUDE.md ve Kalıcı Talimat Disiplini

Bu kitapçık, Claude Code ile çalışırken kalıcı talimatların neden yalnızca teknik bir kolaylık değil, yapay zekâ destekli akademik üretimin yöntemsel altyapılarından biri olduğunu ele alır. Önceki kitapçıklar Claude Code'un ne olduğunu, sohbet penceresinden nasıl ayrıldığını ve ilk kurulumun nasıl denetlenmesi gerektiğini tartışmıştı. Bu kitapçık ise kurulumdan sonra araştırmacının karşılaştığı ilk kalıcı soruya odaklanır.

Araca her oturumun başında neyi bilmesi gerektiği nasıl söylenecektir?

Bu sorunun pratik karşılığı CLAUDE.md dosyasıdır. Ancak CLAUDE.md yalnızca bir ayar dosyası olarak görülmemelidir. Sosyal bilimci açısından bu dosya, üslup tercihlerinin, atıf disiplininin, etik sınırların, veri güvenliği ilkelerinin, dil kullanım kurallarının ve proje düzeyindeki yöntemsel beklentilerin yazılı hâle getirildiği bir çalışma standardıdır.

Bu kitapçığın temel iddiası şudur. CLAUDE.md, yapay zekâ destekli araştırmada davranış sürekliliği sağlayan, araştırmacının yöntemsel tercihlerini belgeleyen ve oturumlar arasındaki dağılmayı azaltan bir talimat altyapısıdır. Bununla birlikte CLAUDE.md, doğruluğu garanti eden bir mekanizma değildir. Davranışı biçimlendirir, ancak bilimsel yargının ve insan denetiminin yerine geçmez.

## 1. Talimat Neden Yöntemsel Bir Araçtır?

Yapay zekâ ile çalışan araştırmacının karşılaştığı temel sorunlardan biri süreksizliktir. Her oturum, özellikle sıradan sohbet arayüzlerinde, büyük ölçüde yeni bir başlangıç gibi çalışır. Araç önceki oturumda hangi atıf standardının istendiğini, hangi veri türlerinin kesinlikle paylaşılmaması gerektiğini, Türkçe metinlerde hangi dilsel hassasiyetlerin korunacağını ya da araştırmacının hangi kavramsal çerçeveyi benimsediğini kendiliğinden güvenilir biçimde taşımaz.

Bu durum akademik üretim açısından ciddi bir sorundur. Çünkü araştırma tekil yanıtların toplamı değildir. Aynı yöntemsel ilkelerin, aynı kaynak denetimi alışkanlıklarının, aynı etik sınırların ve aynı dil standartlarının zaman içinde korunması gerekir. Eğer bu standartlar her oturumda yeniden sözlü biçimde kuruluyorsa, süreç kırılgan hâle gelir. Araştırmacı her seferinde aynı çerçeveyi yeniden anlatmak zorunda kalır. Bu da hem bilişsel yükü artırır hem de çıktıların tutarlılığını zayıflatır.

CLAUDE.md bu soruna kalıcı bir yanıt sunar. Araç, oturum başında bu dosyayı okuyarak proje bağlamını ve araştırmacının temel talimatlarını yükler. Anthropic'in belgelerine göre bu içerik sistem komutu olarak değil, konuşmaya proje bağlamı olarak eklenir (Anthropic, 2025). Bu ayrım önemlidir. Dosya, modelin davranışını yönlendirir, ancak onu mekanik biçimde zorlamaz.

Sosyal bilimci için bu dosyanın değeri tam burada ortaya çıkar. Talimatlar geçici bir istek olmaktan çıkar, yazılı ve denetlenebilir bir yöntemsel standarda dönüşür. APA 7 beklentisi, uydurma atıf yasağı, klinik veri paylaşmama kuralı, Türkçe diakritik harflerin korunması, çift dilli yazım ilkeleri ve kaynak doğrulama gerekliliği her oturumda yeniden söylenmek yerine dosyada sabitlenebilir.

Bu anlamda CLAUDE.md, kişisel bir çalışma alışkanlığını yöntemsel bir belgeye dönüştürür.

## 2. CLAUDE.md Nedir?

CLAUDE.md, Claude Code'un proje bağlamını ve kalıcı talimatları okumak için kullandığı sade bir Markdown dosyasıdır. Kod dosyası değildir. Araştırmacı, ekip ve araç tarafından okunabilen açık bir metindir. İçeriği araştırmacının çalışma bağlamına göre değişebilir. Kimlik, proje amacı, beklenen yazım tonu, kaynak doğrulama kuralları, dosya düzeni, etik sınırlar ve görev tamamlama ölçütleri bu dosyada yer alabilir.

Bu dosya farklı düzeylerde konumlandırılabilir. Kullanıcı düzeyinde bir CLAUDE.md, makinedeki tüm projeler için geçerli genel talimatları taşıyabilir. Proje kökündeki CLAUDE.md ise belirli bir araştırma projesine, laboratuvara, kitapçık serisine ya da makale dosyasına özgü çalışma standartlarını belirleyebilir. Yerel ve depoya eklenmeyen kişisel ayarlar için ayrı dosyalar da kullanılabilir. Böylece paylaşılan proje standardı ile bireysel çalışma tercihleri birbirinden ayrılabilir.

Akademik açıdan bu katmanlı yapı değerlidir. Çünkü araştırma çoğu zaman tek kişinin bireysel bilgisayarında ilerleyen bir süreç değildir. Ekip çalışması, danışmanlık ilişkisi, laboratuvar standardı, ortak yazarlık ve açık kaynaklı dokümantasyon bu sürece dahil olabilir. CLAUDE.md, bu farklı aktörler arasında yazılı bir yöntemsel zemin sağlar.

Burada teknik bir ayrıntı da önemlidir. Uzun oturumlarda geçmişin sıkıştırılması ya da bağlamın yeniden düzenlenmesi sırasında bazı talimatların yeniden okunması gerekebilir. Anthropic belgeleri, belirli bağlam sıkıştırma işlemlerinden sonra proje kökündeki CLAUDE.md dosyasının yeniden okunabileceğini, alt dizinlerdeki dosyaların ise ancak ilgili alt ağaçtaki dosyalarla çalışıldığında yeniden bağlama dahil edilebileceğini belirtir (Anthropic, 2025). Bu ayrıntı, oturum ortasında sessiz bağlam yitimi yaşanmaması için bilinmelidir.

Sohbet penceresine yazılan bir talimat ile CLAUDE.md arasındaki fark bu noktada belirginleşir. Sohbet talimatı geçicidir. CLAUDE.md ise dosya sisteminde yaşar. Sürümlenebilir, paylaşılabilir, gözden geçirilebilir ve zaman içindeki değişimi izlenebilir. Bu özellik, talimatı kişisel hafızadan çıkarıp araştırma altyapısının parçası hâline getirir.

## 3. Komut Duyarlılığı ve Talimat Disiplini

Dil modelleri, yalnızca içerik düzeyinde değil, biçim düzeyinde de duyarlıdır. Talimatın nasıl yazıldığı, hangi sırayla verildiği, hangi ayracın kullanıldığı ve hangi örneklerin eklendiği çıktı üzerinde beklenmedik etkiler yaratabilir. Sclar ve diğerleri (2023), komut biçimindeki küçük farklılıkların model performansında anlamlı değişikliklere yol açabildiğini göstermiştir. Bu bulgu, sosyal bilimci için doğrudan yöntemsel sonuç taşır.

Araştırmacı her oturumda talimatlarını farklı biçimde, dağınık ve sözlü olarak veriyorsa, çıktılar arasındaki tutarlılığın bozulması şaşırtıcı değildir. Oysa yazılı, sürümlenmiş ve denetlenmiş bir talimat dosyası, bu değişkenliği azaltabilir. Bu durum CLAUDE.md'yi basit bir kolaylık olmaktan çıkarır. Talimatın kendisi, yapay zekâ destekli araştırma yönteminin parçası hâline gelir.

Bu noktada ölçüm aracı benzetmesi yararlıdır. Kalibre edilmemiş bir ölçüm aracı nasıl her kullanımda farklı sonuçlar üretebilirse, dağınık ve değişken talimatlar da farklı oturumlarda farklı davranışlara yol açabilir. CLAUDE.md, talimatları sabitleyerek bu değişkenliği azaltır. Elbette tamamen ortadan kaldırmaz. Ancak araştırmacıya hangi standartların araca ne zaman ve nasıl verildiğini belgeleyebilme imkânı sağlar.

Bu nedenle iyi bir CLAUDE.md dosyası yalnızca pratik bir not değildir. Tekrarlanabilirliğe katkı sunan yöntemsel bir kayıttır. Araştırmacının gelecekte kendisine, ekibine, danışmanına ya da okuyucusuna şu soruya yanıt vermesini sağlar. Bu araç hangi talimatlar altında çalıştı?

## 4. Komut Kalıplarından Kalıcı Yapılandırmaya

Komut mühendisliği başlangıçta çoğu zaman bireysel deneme yanılma becerisi gibi görülüyordu. Ancak son yıllarda bu alan daha sistematik biçimde ele alınmaya başladı. White ve diğerleri (2023), tekrar eden ve farklı görevlerde kullanılabilen komut kalıplarını kataloglaştırdı. Schulhoff ve diğerleri (2024) ise komut mühendisliği tekniklerini sistematik bir tarama içinde değerlendirdi. Bu çalışmalar, etkili komut vermenin yalnızca kişisel sezgiye dayalı olmadığını gösterir. Komutlar belgelenebilir, sınıflandırılabilir ve zaman içinde geliştirilebilir.

CLAUDE.md bu gelişmeyi proje düzeyinde somutlaştırır. Tek tek komutlar geçici kalabilir. Ancak kalıcı talimat dosyası, araştırmacının çalışma biçimini araca sürekli biçimde aktaran yapılandırılmış bir metne dönüşür. Böylece komut mühendisliği anlık bir beceri olmaktan çıkar, araştırma altyapısının bir parçası hâline gelir.

Knuth'un okuryazar programlama yaklaşımı burada anlamlı bir tarihsel benzetme sunar. Knuth'a göre kod yalnızca makinenin çalıştıracağı bir komutlar dizisi olarak değil, insanın okuyabileceği ve anlayabileceği bir metin olarak düzenlenmelidir. CLAUDE.md de benzer bir ilkeyi yapay zekâ destekli araştırma ortamına taşır. Aracın davranışını yalnızca makineye kapalı bir yapılandırma olarak değil, araştırmacının, ekibin ve gelecekteki okuyucunun anlayabileceği düz metin olarak belgeler.

İyi bir CLAUDE.md, yalnızca araca ne yapacağını söylemez. Aynı zamanda insanlara da bu aracı hangi yöntemsel ilkelerle kullandığınızı gösterir. Bu yönüyle talimat dosyası hem çalışma protokolü hem de hesap verebilirlik belgesidir.

## 5. Tekrarlanabilirlik Altyapısı Olarak CLAUDE.md

Tekrarlanabilirlik, hesaplamalı araştırmanın temel ilkelerinden biridir. Sandve ve diğerleri (2013), tekrarlanabilir hesaplamalı araştırma için sürecin her adımının kaydedilmesi, mümkün olduğunca otomatikleştirilmesi ve gelecekte yeniden üretilebilir biçimde düzenlenmesi gerektiğini vurgular. Yapay zekâ destekli araştırmada bu ilke daha da önem kazanır. Çünkü model davranışı oturumdan oturuma, komuttan komuta ve bağlamdan bağlama değişebilir.

CLAUDE.md bu değişkenliği tamamen ortadan kaldırmaz. Ancak araştırmacının yapay zekâ bileşenini belgeleyebilmesi için önemli bir başlangıç noktası sağlar. Hangi modelin kullanıldığı, hangi talimatların verildiği, hangi etik sınırların belirtildiği, hangi kaynak doğrulama kurallarının zorunlu kılındığı ve hangi dil standartlarının beklendiği dosyada açıkça yer alabilir.

Bu nedenle CLAUDE.md, yöntem bölümünün makineye bakan yüzü olarak düşünülebilir. Bir makalenin yöntem bölümü insan okura araştırmanın nasıl yürütüldüğünü açıklar. CLAUDE.md ise araca hangi sınırlar ve standartlar altında çalışması gerektiğini bildirir. Her ikisi de eksiksiz, dürüst ve denetlenebilir olmalıdır.

Ancak burada önemli bir sınırlama vardır. Anthropic'in belgeleri, CLAUDE.md içeriğinin sistem komutu olarak değil, proje bağlamı olarak işlendiğini belirtir. Bu nedenle model bu talimatlara uymaya çalışır, fakat özellikle belirsiz, çelişkili ya da fazla geniş talimatlarda kesin uyum garanti edilemez (Anthropic, 2025). Talimat dosyası davranışı disipline eder. Doğruluğu, etik uygunluğu ya da kaynak güvenilirliğini kendiliğinden garanti etmez.

Bu nedenle tekrarlanabilirlik yalnızca talimat dosyasına bırakılamaz. Talimat, dosya arşivi, kaynak doğrulama, çıktı denetimi ve insan değerlendirmesi birlikte yürütülmelidir.

## 6. Sosyal Bilimci İçin CLAUDE.md'de Ne Bulunmalı?

İyi bir CLAUDE.md dosyası soyut ve genel ifadelerden oluşmamalıdır. Sosyal bilimci için kullanışlı bir talimat dosyası, araştırma bağlamını, çalışma standartlarını ve geçilemez sınırları somut biçimde tanımlamalıdır.

İlk olarak, araç kiminle çalıştığını bilmelidir. Araştırmacının alanı, akademik düzeyi, çalışma bağlamı ve projenin amacı kısa biçimde belirtilmelidir. Klinik psikoloji, eğitim bilimleri, sosyoloji, siyaset bilimi ya da yapay zekâ etiği gibi farklı alanlar, farklı kavramsal hassasiyetler ve kaynak standartları gerektirir.

İkinci olarak, üslup ve yazım standardı tanımlanmalıdır. Akademik Türkçe mi, uluslararası dergi İngilizcesi mi, iki dilli kitapçık dili mi, etik kurul başvuru dili mi, yoksa hakem yanıtı dili mi beklendiği açık olmalıdır. Gerekiyorsa cümle yapısı, ton, aşırı iddialı ifadelerden kaçınma, emoji kullanmama, kaynak göstermeden kesin iddia kurmama gibi kurallar yazılmalıdır.

Üçüncü olarak, atıf disiplini açık biçimde belirtilmelidir. APA 7 standardı, DOI doğrulama zorunluluğu, uydurma atıf yasağı, yalnızca doğrulanmış kaynakların referans listesine alınması ve kaynak belirsizliğinde açık uyarı verme kuralı dosyada yer almalıdır. Bu bölüm, sosyal bilimlerde yapay zekâ kullanımının en kritik güvenlik katmanlarından biridir.

Dördüncü olarak, etik ve veri güvenliği sınırları yazılmalıdır. Anonimleştirilmemiş klinik veri, ham mülakat dökümü, kişisel tanımlayıcı içeren saha notu ve etik kurul kapsamındaki hassas materyal araca verilmemelidir. KVKK ve GDPR kapsamındaki yükümlülükler açıkça hatırlatılmalıdır. Aracın hassas veriyle çalışması gerekiyorsa, bunun yalnızca anonimleştirilmiş ve etik kurul onayıyla uyumlu biçimde yapılabileceği belirtilmelidir.

Beşinci olarak, dil katmanı tanımlanmalıdır. İki dilli çalışan araştırmacılar için Türkçe ve İngilizce metinlerin hangi durumlarda kullanılacağı, Türkçe diakritik harflerin korunacağı, makine çevirisi yerine yeniden yazım tercih edileceği ve kavram eşleştirmelerinde tutarlılık aranacağı yazılmalıdır.

Altıncı olarak, görev tamamlama ölçütleri belirtilmelidir. Araç bir işi bitirdiğini söylemeden önce hangi kanıtı sunmalıdır? Kaynakları doğruladı mı? Dosya değişikliklerini gösterdi mi? Diff sundu mu? Çıktının hangi dosyaya yazıldığını belirtti mi? Belirsiz kaldığı noktaları açıkça işaretledi mi?

Bu kategoriler CLAUDE.md'yi kişisel bir not olmaktan çıkarır. Araştırmacının çalışma etiğini, kaynak disiplinini ve yöntemsel tercihlerini araca ileten bir protokole dönüştürür.

## 7. Sınırlar. Talimat Davranışı Biçimlendirir, Doğruluğu Garanti Etmez

İyi hazırlanmış bir CLAUDE.md güçlü bir başlangıç noktasıdır. Ancak iki temel sınır açıkça belirtilmelidir.

İlk sınır, modelin olasılıksal doğasıdır. Talimat ne kadar ayrıntılı olursa olsun, büyük dil modeli hâlâ istatistiksel örüntüler üzerinden çıktı üretir. Bender ve diğerlerinin stochastic parrot tartışması, modelin akıcı ve ikna edici metin üretebilmesinin gerçek anlama ya da doğruluk garantisi anlamına gelmediğini gösterir. Hicks ve diğerleri de üretici dil modellerinin epistemik açıdan doğru ile ilgisi zayıf çıktılar üretebileceğini tartışır. Bu nedenle CLAUDE.md, hata riskini azaltabilir. Ancak sıfırlayamaz.

İkinci sınır, bilişsel yükün dışarıya verilmesidir. Risko ve Gilbert'in bilişsel boşaltma üzerine tartışması burada önemlidir. İnsanlar bazı görevleri dış araçlara devrettiklerinde zihinsel yükleri azalabilir. Bu yararlı olabilir. Ancak dışarıya verilen şey yalnızca hatırlama ya da yordam değil, muhakemenin kendisi olduğunda risk ortaya çıkar.

CLAUDE.md'nin dışarıya vermesi gereken şey tekrar eden yordamdır. Hangi atıf biçimi kullanılacak? Hangi veri paylaşılmayacak? Hangi dil standardı korunacak? Hangi dosya düzeni izlenecek?

Dışarıya verilmemesi gereken şey ise bilimsel yargıdır. Bir bulgunun anlamı, bir etik kararın ağırlığı, bir yöntemin uygunluğu, bir kavramın bağlamsal karşılığı ve bir argümanın geçerliliği araştırmacıda kalmalıdır.

Bu nedenle CLAUDE.md, araştırmacının yerine düşünen bir mekanizma olarak değil, araştırmacının çalışma standardını görünür kılan bir yöntem aracı olarak kullanılmalıdır.

## 8. Türkçe, İki Dillilik ve Batı Trakya Bağlamı

Kalıcı talimat disiplini, Türkçe ve İngilizce arasında çalışan araştırmacılar için özel bir önem taşır. Çok dilli akademik üretimde sorun yalnızca çeviri değildir. Kavramların hangi dilde nasıl kurulduğu, hangi bağlamda hangi terimin tercih edildiği ve kültürel özgüllüklerin nasıl korunacağı da yöntemsel bir meseledir.

CLAUDE.md, iki dilli araştırmacı için ortak bir bağlam dosyası işlevi görebilir. Hangi durumda Türkçe yazılacağı, hangi durumda İngilizce yeniden yazım yapılacağı, Türkçe karakterlerin korunacağı, kavram eşleştirmelerinin rastgele yapılmayacağı ve makine çevirisi hissi veren metinlerin kabul edilmeyeceği dosyada sabitlenebilir.

Bölgesel akademik altyapılar da bu dosyada tanımlanabilir. DergiPark, ULAKBİM TR Dizin, HEAL Link, yerel üniversite adları, kurumsal kütüphane erişimleri ve bölgesel indeksleme ölçütleri araca açık biçimde anlatılabilir. Böylece her oturumda aynı düzeltmelerin yapılması gerekmez.

Batı Trakya bağlamında çalışan bir araştırmacı için bu mesele yalnızca biçimsel değildir. Yer adları, azınlık bağlamı, iki dillilik, kurum adları, tarihsel ve kültürel duyarlılıklar akademik doğruluğun parçasıdır. CLAUDE.md, bu hassasiyetleri kişisel hafızaya bırakmak yerine yazılı bir çalışma standardına dönüştürebilir.

Bu yönüyle CLAUDE.md, yalnızca teknik süreklilik sağlamaz. Dilsel, kültürel ve bölgesel tutarlılığın korunmasına da katkı sunar.

## 9. Sonraki Kitapçık

Bu kitapçık, CLAUDE.md dosyasını Claude Code kullanımında kalıcı talimat disiplini açısından ele aldı. Temel argüman şudur. Yapay zekâ destekli akademik üretimde talimatlar geçici, sözlü ve oturumdan oturuma değişen istekler olarak kalmamalıdır. Araştırmacının üslup, atıf, etik, veri güvenliği, dil ve doğrulama standartları yazılı, sürümlenebilir ve denetlenebilir bir dosyada tutulmalıdır.

Bununla birlikte CLAUDE.md belleğin kendisi değildir. Araca her oturumda nasıl davranması gerektiğini söyler. Ancak araştırmanın ara sonuçları, alan notları, kaynak haritaları, hakem yanıtları, veri sözlükleri ve uzun vadeli akademik kararları başka bir arşiv mimarisi içinde yaşamalıdır.

Bir sonraki kitapçık bu soruya geçer. Akademik hafıza nerede tutulur? Araştırma bağlamı yıllar içinde nasıl korunur? Notlar, kaynaklar, kararlar ve yazı taslakları nasıl arşive dönüştürülür?

003-01-0001, Hafızayı Arşive Dönüştürmek, İlkesel Bir Giriş, bu noktadan devam eder.

---

## Kaynakça

Atıflar APA 7 biçimindedir. Her DOI ve tanımlayıcı, 2026-06-21 tarihinde Crossref, arXiv veya Anthropic'in resmi belgeleri üzerinden bağımsız olarak doğrulanmıştır.

Anthropic. (2025). *Memory: Claude Code documentation*. https://code.claude.com/docs/en/memory

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610–623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, *26*(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Knuth, D. E. (1984). Literate programming. *The Computer Journal*, *27*(2), 97–111. https://doi.org/10.1093/comjnl/27.2.97

Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. *Trends in Cognitive Sciences*, *20*(9), 676–688. https://doi.org/10.1016/j.tics.2016.07.002

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, *9*(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Schulhoff, S., Ilie, M., Balepur, N., Kahadze, K., Liu, A., Si, C., Li, Y., Gupta, A., Han, H., Schulhoff, S., Dulepet, P. S., Vidyadhara, S., Ki, D., Agrawal, S., Pham, C., Kroiz, G., Li, F., Tao, H., Srivastava, A., … Resnik, P. (2024). The prompt report: A systematic survey of prompt engineering techniques. *arXiv*. https://arxiv.org/abs/2406.06608

Sclar, M., Choi, Y., Tsvetkov, Y., & Suhr, A. (2023). Quantifying language models' sensitivity to spurious features in prompt design, or: How I learned to start worrying about prompt formatting. *arXiv*. https://arxiv.org/abs/2310.11324

White, J., Fu, Q., Hays, S., Sandborn, M., Olea, C., Gilbert, H., Elnashar, A., Spencer-Smith, J., & Schmidt, D. C. (2023). A prompt pattern catalog to enhance prompt engineering with ChatGPT. *arXiv*. https://arxiv.org/abs/2302.11382

---

**Kitapçık kimliği.** `001-01-0004`
**Sürüm.** `0.2.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 2072 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 9
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`001-01-0003`](../001-01-0003/tr.md). Kurulum, İlk Oturum ve Sağlamlık Denetimleri
**Sonraki kitapçık.** [`001-02-0001`](../001-02-0001/tr.md). Araştırma Yaşam Döngüsü, Fikirden Yayına, Yayından Arşive
