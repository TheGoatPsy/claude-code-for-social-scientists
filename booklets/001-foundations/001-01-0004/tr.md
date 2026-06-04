---
title_en: "CLAUDE.md and the Discipline of Standing Instructions"
title_tr: "CLAUDE.md ve Kalıcı Talimat Disiplini"
booklet_id: "001-01-0004"
category: "001-foundations"
language: "tr"
version: "0.1.0"
date_published: "2026-05-29"
date_last_revised: "2026-06-04"
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
human_review_date: "2026-06-04"
verified_citations_count: 9
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# CLAUDE.md ve Kalıcı Talimat Disiplini

Bu rehberin ilk üç broşürü sırasıyla üç soruyu yanıtladı: Claude Code nedir, sohbet penceresinden neden farklıdır, güvenli biçimde nasıl kurulur. Kurulum tamamlandığında araştırmacının önünde duran ilk kalıcı karar ne bir komuttur ne de bir yapılandırmadır. O karar yöntemseldir. Araca her oturumun başında neyi bilmesi gerektiğini nasıl yazarsınız? Bu kararın somut yeri `CLAUDE.md` dosyasıdır. Bu broşür `CLAUDE.md`'yi bir kolaylık ayarı olarak değil, akademik üretimi biçimlendiren, belgeleyen ve disipline eden bir yöntem aracı olarak ele alır.

## 1. Talimat neden bir yöntem aracıdır

Her sohbet oturumu sıfırdan başlar. Araç, önceki oturumda hangi atıf stilini istediğinizi, klinik veri için hangi etik sınırı koyduğunuzu ya da Türkçe çıktı için hangi standardı uyguladığınızı taşımaz. Her oturumda bunlar ya yeniden kurulur ya da sessizce unutulur.

Kalıcı bir bağlam dosyası bu boşluğu kapatır. Claude Code `CLAUDE.md`'yi oturumun başında okur, içeriğini kalıcı bir talimat olarak yükler. Teknik olarak bu, sistem komutuna değil konuşmaya proje bağlamı olarak enjekte edilir (Anthropic, 2025). Araç bundan sonra o dosyanın kurduğu çerçeve içinde hareket eder: araştırmacının kim olduğunu, hangi standartlara bağlı olunduğunu, hangi sınırların geçilemeyeceğini bilir.

Sosyal bilimci için bu farkın anlamı somuttur. Talimat dosyası üslubun, atıf disiplininin, etik sınırların ve yöntemsel tercihlerin tek ve denetlenebilir kaynağı hâline gelir. Her oturumda "APA 7, hayali atıf yok" diye yeniden yazmak yerine araştırmacı bu standardı bir kez yazar ve yerine sabitler. Küçük ama belirleyici bir adım: kişisel bir alışkanlığı kuruma dönüştürmek.

## 2. CLAUDE.md nedir, aracın kalıcı bağlamı

`CLAUDE.md`, ajanın her oturumun başında otomatik olarak okuduğu sade bir markdown dosyasıdır. İçeriği özgürdür: araştırmacının kim olduğu, projenin amacı, beklenen üslup, atıf kuralları, dosya düzeni alışkanlıkları ve geçilemez etik sınırlar bu dosyada düz cümlelerle ifade edilir. Dosya kod değildir. Araştırmacının da aracın da okuyabileceği, çalışma standartlarının yazılı ifadesidir.

Dosya aynı anda birden fazla katmanda çalışabilir. `~/.claude/CLAUDE.md` konumundaki bir dosya, makinedeki tüm projeler için geçerli olan kullanıcı düzeyinde talimatları taşır. Proje kökündeki `./CLAUDE.md` ya da `./.claude/CLAUDE.md` ekiple paylaşılır ve yalnızca o projeye özgüdür. `CLAUDE.local.md` ise depoya eklenmeden kalan kişisel tercihler katmanıdır. Paylaşılan ekip bağlamı içinde bireysel araştırmacının kendi ayarlamalarını yapabildiği ayrı bir katman. Üst ve alt dizinlerdeki dosyalar Claude o alt ağaçlardaki dosyaları okurken kümülatif olarak yüklenir (Anthropic, 2025). Daha yerel dosyalar yükleme sırasında en son okunur, dolayısıyla talimatları bağlamda en sona düşer.

Akademik tekrarlanabilirlik açısından önemli bir teknik ayrıntı vardır. `/compact` komutu (uzun oturum geçmişini sıkıştıran bir işlem) çalıştırıldıktan sonra proje kökündeki `CLAUDE.md` diskten yeniden okunur ve yeniden enjekte edilir. Alt dizinlerdeki dosyalar ise otomatik olarak yeniden enjekte edilmez. Claude o özel alt ağaçtaki bir dosyayı okuyacağı bir sonraki sefere kadar beklerler (Anthropic, 2025). Bunu bilmek, oturum ortasındaki sessiz bağlam yitimini önler.

Sohbet penceresine yazılan bir talimattan bu dosyayı ayıran üç temel özellik vardır. Birincisi kalıcılıktır: sohbet talimatı pencere kapanınca silinir, `CLAUDE.md` ise diskte yaşar. İkincisi sürüm kontrolüdür: dosya bir depo içinde tutulduğunda araştırmacının yöntemsel standartlarının zaman içindeki evrimi izlenebilir hâle gelir. Üçüncüsü paylaşılabilirliktir: aynı dosya bir araştırma ekibinde, bir laboratuvarda ya da bir tez danışmanlığı ilişkisinde ortak çalışma standardına dönüşür. Bu üç özellik talimatı geçici bir istekten kalıcı bir yöntemsel altyapıya taşır.

## 3. Komut duyarlılığı ve disiplinin gerekçesi

Talimatı dikkatle yazmak için kesin, ampirik temelli bir gerekçe vardır. Dil modelleri, komutun küçük biçim değişikliklerine sezgisel olmayan biçimlerde duyarlıdır. Sclar ve diğerleri (2023), yalnızca biçimlendirme farkının, araya eklenen bir boşluğun ya da değiştirilen bir ayracın, test ettikleri açık kaynak modellerde az sayıda örnekli (few-shot) ayarda doğrulukta büyük farklara yol açabildiğini gösterdi. Aynı içerik farklı biçimde sunulduğunda anlamlı ölçüde farklı çıktı verebilir.

Sosyal bilimci için bu bulgunun sonucu doğrudandır: tekrarlanabilirlik komutun kararlılığına bağlıdır. Oturum talimatı her seferinde gelişigüzel ve sözlü olarak verilirse sonuçların oturumlar arasında tutarlı kalacağının güvencesi yoktur. Oysa yazılı, sürümlenmiş ve sınanmış bir talimat bu duyarlılığı kontrol altına alır.

Bu durum komutu akademik yöntemin alanına taşır. Dağınık ve sözlü talimat kalibre edilmemiş bir ölçüm aletine benzer. Sabit ve yazılı talimat ise kalibre edilmişine. Komutun biçimi yöntemin biçimi hâline gelir. Tıpkı yöntemin kendisi gibi belgelenmelidir.

## 4. Komut kalıplarından kalıcı yapılandırmaya

Prompt mühendisliği dağınık bir kişisel hünerden taranmış bir alana dönüştü. White ve diğerleri (2023), defalarca işe yarayan komut kalıplarını katalog biçiminde derleyip bu kalıpların görevler ve bağlamlar arasında aktarılabilir olduğunu ortaya koydu. Schulhoff ve diğerleri (2024) ise alanın tekniklerini sistematik bir derlemede bir araya getirdi. Bu iki çalışma birlikte şunu kurar: iyi komut rastlantı değil, belgelenebilir bir uygulamadır. Yazılabilir, sınanabilir ve zaman içinde geliştirilebilir.

Tek tek kalıpların ötesinde ise daha sağlam bir fikir yatar. Knuth'un (1984) literate programming kavramı şunu savunuyordu: kod öncelikle bir insanın okuması için yazılmalı, bir makineye devredilen komutlar yığını değil bir insana anlatılan metin biçiminde düzenlenmelidir. `CLAUDE.md` aynı ruhu taşır. Aracın davranışını, sonraki araştırmacının ve gelecekteki kendi benliğinizin okuyup anlayabileceği düz bir dille belgeler. İyi bir `CLAUDE.md`, makineye teslim edilen komut yığını değil, bir çalışma standardının insan tarafından okunabilen ifadesidir. Herhangi bir meslektaşın inceleyebileceği, sorgulayabileceği ve geliştirebileceği bir ifade.

## 5. Tekrarlanabilirlik altyapısı olarak CLAUDE.md

Sandve ve diğerleri (2013), tekrarlanabilir hesaplamalı araştırma için on kural sıraladı. Bu kuralların tamamında ortak bir buyruk akar: sürecin her adımı kaydedilmeli ve mümkün olduğunca otomatikleştirilmelidir. Böylece başka biri ya da aylar sonra aynı araştırmacı aynı sonucu aynı başlangıç noktasından yeniden üretebilsin.

`CLAUDE.md`, bu ilkeyi yapay zekâ destekli iş akışına taşıyan somut bir araçtır. Kullanılan model, aracın izlediği talimat ve çalıştığı sınırlar tek bir sürümlü dosyada sabitlendiğinde çalışmanın yapay zekâ bileşeni belgelenmiş olur. Bir yıl sonra aynı `CLAUDE.md`, aynı başlangıç noktasıdır. Böylece yapay zekâ destekli araştırmanın en kırılgan yönü, yani sürecin tekrar edilememesi sorunu, doğrudan karşılanmış olur. Talimat dosyası, yöntem bölümünün makineye bakan yüzüdür. Yöntem bölümü insan okuruna ne yaptığınızı anlatır. `CLAUDE.md` araca aynı şeyi söyler. Tıpkı yöntem bölümü gibi dürüst, eksiksiz ve çalışma paylaşılmadan önce teslim edilmiş olmalıdır.

Burada önemli bir uyarı vardır. Anthropic'in kendi belgeleri, `CLAUDE.md` içeriğinin sistem komutuna değil konuşmaya proje bağlamı olarak enjekte edildiğini belirtir. Claude bu talimatlara uymaya çalışır, ama kesin uyum, özellikle belirsiz ya da çelişkili talimatlarda, garanti edilmez (Anthropic, 2025). Talimat dosyası davranışı disipline eder, onu mekanik olarak zorlamaz. Doğrulama yine araştırmacının sorumluluğundadır.

## 6. Sosyal bilimci için CLAUDE.md'de ne bulunmalı

İyi bir talimat dosyası soyut değil somuttur. Sosyal bilimci için altı başlık zorunlu asgariyi oluşturur.

Birincisi kimlik ve uzmanlıktır. Araç kiminle çalıştığını, hangi düzeyde bir akademik muhatap beklediğini ve hangi alanda olduğunu bilmelidir. İkincisi üsluptur. Cümle yapısı tercihleri, emoji yasağı, akademik yazında beklenen ton ve herhangi bir dergi hedefine ya da kurumsal başvuruya özgü alışılagelen kurallar buraya girer.

Üçüncüsü atıf disiplinidir. APA 7 standardı, hayali atıf yasağı ve her DOI'nin referans listesine girmeden önce bağımsız olarak doğrulanması zorunluluğu açıkça belirtilmelidir. Dördüncüsü etik sınırlardır. Anonimleştirilmemiş klinik veri paylaşılmaması, KVKK ve GDPR yükümlülüklerine uyulması ve paylaşılan belgelere tanımlayıcı bilgi yazılmaması gibi kurallar dosyada yer almalıdır.

Beşincisi dil katmanıdır. İki dilli çalışan bir araştırmacı hangi bağlamda Türkçe hangi bağlamda İngilizce beklendiğini tam olarak tanımlayabilir. Türkçe diakritik harflerin ASCII'ye düşürülmemesi gibi açık bir kuralı da ekleyebilir. Altıncısı doğrulama beklentisidir. Aracın bir görevi tamamlandı saymadan önce neyi kanıtlaması gerektiği yazılmalıdır. Bu altı başlığın her biri önceki broşürlerin soyut ilkesini araç düzeyinde somut bir davranışa çevirir.

## 7. Sınırlar, talimat davranışı biçimlendirir ama doğruluğu garanti etmez

İyi yazılmış bir `CLAUDE.md` güçlü bir araçtır. Ama iki sınır açıkça adlandırılmadan kullanılırsa, ona eleştirisiz güvenen araştırmacıyı yanıltır.

Birinci sınır modelin olasılıksal doğasıdır. Talimat ne kadar özenli olursa olsun model hâlâ istatistiksel bir sistemdir. Talimat hata oranını düşürür, sıfırlamaz. En titiz talimat altında bile gerçek bir anlayış olmaksızın istatistiksel örüntü üretme riski sürer (Bender ve diğerleri, 2021). Üretilen metin, epistemik düzeyde, doğru görünmek ile doğru olmak arasındaki farkı kendiliğinden gözetmeyen bir karakter taşıyabilir (Hicks ve diğerleri, 2024). Bu nedenle talimat, doğrulama disiplininin yerini almaz. Onu tamamlar.

İkinci sınır daha incedir. Talimat bilişsel yükü dışarı verir. Risko ve Gilbert (2016), bilişsel boşaltmanın hem fayda hem maliyet taşıdığını gösterdi. Dışarı verilen şey hatırlama yükü olduğunda kazanç açıktır, ama dışarı verilen şey muhakemenin kendisi olduğunda kayıp gizlidir. `CLAUDE.md`'nin dışarıya vermesi gereken tekrar eden yordamdır. Hangi üslubun beklendiği, hangi biçimin istendiği, hangi sınırın geçilemeyeceği. Dışarıya verilmemesi gereken ise bilimsel yargıdır. Bir bulgunun anlamı, bir yorumun geçerliliği, bir etik kararın ağırlığı araştırmacıda kalır. Talimat yordamı devreder, yargıyı değil.

## 8. Türkçe ve Batı Trakya Özgülü

Kalıcı talimat disiplini, yalnızca kolaylık olarak değil, iki dilli ve bölgesel bağlamda ayrı bir değer kazanır.

Tek bir `CLAUDE.md`, hem Türkçe hem İngilizce çalışan bir araştırmacı için ortak yöntemsel bağlam olabilir. Dosya hangi durumda hangi dilin beklendiğini bir kez tanımlar. Türkçe diakritik harflerin ASCII'ye düşürülmemesi kuralını da oraya ekler. Böylece iki dil arasında gidip gelen bir akademisyen için her oturumda yeniden açıklama yükü ortadan kalkar.

Bölgesel terimler ve altyapılar da talimatın doğal konusudur. DergiPark, ULAKBIM TR Dizin, HEAL-Link. Bunların adları, rolleri ve atıf ile erişim için doğru prosedürler dosyada sabitlenebilir. Böylece araç yeniden düzeltme gerektirmeksizin bu kaynakları doğru biçimde kullanır. Komotini gibi yer adlarının tercih edilen imlası ve bölge üniversitelerinin doğru kurumsal adları da aynı şekilde yerleştirilebilir.

Batı Trakya azınlık bağlamında çalışan bir araştırmacı için terimlerin doğru ve tutarlı kullanımı yalnızca biçimsel bir mesele değildir. Kimliğe ve akademik bütünlüğe ilişkindir. `CLAUDE.md` bu tutarlılığı kişisel bir tercih olmaktan çıkarıp belgelenmiş, paylaşılabilir bir standarda dönüştürür. Personel değişikliklerini, proje devirlerini ve zamanın geçişini atlatır.

## 9. Bir sonraki broşür

`CLAUDE.md`, araca her oturumun başında ne yapacağını söyler. Ama çalışmanın kendisi, ara sonuçları, birikmiş kararlar, alan notları ve manuskript taslakları nerede yaşayacak? Talimat davranışı biçimlendirir. Belleği kurmaz.

Bir sonraki broşür kalıcı belleğin mimarisini ilkeden başlayarak ele alır. Kasa Olarak Hafıza, yılları aşan akademik bağlamın nasıl korunacağını, düzenleneceğini ve sorgulanabileceğini kayıpsız biçimde gösterir. Broşür 003-01-0001 buradan devam eder.

---

## Kaynakça

Atıflar APA 7 biçimindedir. Her DOI ve tanımlayıcı, 2026-06-04 tarihinde Crossref, arXiv veya Anthropic'in resmi belgeleri üzerinden bağımsız olarak doğrulanmıştır.

Anthropic. (2025). *Memory: Claude Code documentation*. https://platform.claude.com/docs/en/claude-code

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610-623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, 26(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Knuth, D. E. (1984). Literate programming. *The Computer Journal*, 27(2), 97-111. https://doi.org/10.1093/comjnl/27.2.97

Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. *Trends in Cognitive Sciences*, 20(9), 676-688. https://doi.org/10.1016/j.tics.2016.07.002

Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS Computational Biology*, 9(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285

Schulhoff, S., Ilie, M., Balepur, N., Kahadze, K., Liu, A., Si, C., et al. (2024). The prompt report: A systematic survey of prompt engineering techniques. *arXiv*. https://arxiv.org/abs/2406.06608

Sclar, M., Choi, Y., Tsvetkov, Y., & Suhr, A. (2023). Quantifying language models' sensitivity to spurious features in prompt design, or: How I learned to start worrying about prompt formatting. *arXiv*. https://arxiv.org/abs/2310.11324

White, J., Fu, Q., Hays, S., Sandborn, M., Olea, C., Gilbert, H., Elnashar, A., Spencer-Smith, J., & Schmidt, D. C. (2023). A prompt pattern catalog to enhance prompt engineering with ChatGPT. *arXiv*. https://arxiv.org/abs/2302.11382

---

**Broşür kimliği.** `001-01-0004`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-04
**Sözcük sayısı (yaklaşık).** 1782 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 9
**Halüsinasyon atıf sayısı.** 0
**Önceki broşür.** [`001-01-0003`](../001-01-0003/tr.md). Kurulum, İlk Oturum, Sağlık Testleri
**Sonraki broşür.** [`003-01-0001`](../../003-memory-system/003-01-0001/tr.md). Kasa Olarak Hafıza, İlkesel Bir Giriş
