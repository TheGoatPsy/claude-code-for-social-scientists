---
title_en: "Beyond Claude Code, Codex and Portable Agentic Discipline"
title_tr: "Claude Code'un Ötesinde, Codex ve Taşınabilir Ajan Disiplini"
booklet_id: "014-01-0001"
category: "014-tool-portability"
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
verified_citations_count: 10
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Türkçe kaynak metin, operatör taslağından çıkarılıp agresif genişletme yapılmıştır. Tüm bölümler kavramsal derinlikle yeniden yazılmıştır. Birebir çeviri değil."
closing_booklet: true
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Claude Code'un Ötesinde, Codex ve Taşınabilir Ajan Disiplini

Bu rehber Claude Code ile başladı. Birinci kitapçık, aracın sosyal bilimcinin akademik üretim sürecine nasıl yerleştiği sorusunu sordu. Sonraki kitapçıklar, dosya disiplinini, kaynak doğrulamayı, etik çerçeveleri, veri güvenliğini, arşiv mantığını ve sorun giderme protokolünü ele aldı. Bu son kitapçık farklı bir soruyla başlar: peki ya araç değişirse?

Bu soru bugün soyut değildir. Yapay zekâ destekli kodlama ve araştırma araçları hızla çoğalıyor. Codex, GitHub Copilot, Gemini Code Assist ve benzerleri aynı iş akışının içine giriyor. Araştırmacı birini denedi, diğerine geçti ya da kurumu farklı bir platform tercih etti. Araç değişti. Sorun da buradan başlıyor. Çünkü çoğu araştırmacı, araçla birlikte çalışma disiplinini de değiştiriyor. Yeni araçla yeniden başlıyor. Kaynak sorumluluğu, karar günlüğü, beyan disiplini, insan denetimi. Bunlar bir önceki araçta kalmış gibi görünüyor.

Bu kitapçığın savı şudur: iyi bir disiplin belirli bir araca değil, araştırmacının kendisine aittir. Araç değişir. Disiplin taşınır. Bu ayrımı anlamak, rehber boyunca öğrenilen her şeyin gerçek sınavıdır.

## 1. Claude Code'dan Öğrenilen Asıl Şey

Claude Code bu rehberde bir laboratuvar işlevi gördü. Ama asıl öğrenilen, Claude Code'a özgü komutlar ya da kısayollar değildi. Öğrenilen şey, ajan tabanlı bir araçla çalışmanın hangi soruları zorunlu kıldığıydı.

Bu sorular şunlardı: Araç hangi dosyalara erişiyor? Hangi kararı kendi başına alıyor, hangisini araştırmacıya soruyor? Bir kaynak doğrulanmadan kaynakçaya girebilir mi? Klinik veri hangi koşullar altında araca aktarılabilir? Ajan çıktısı ne zaman doğrudan kullanılabilir, ne zaman incelenmesi gerekir? Bunlar teknik sorular değildir, yöntemsel sorulardır. Ve yanıtları Claude Code'a bağlı değildir.

Wooldridge (2009), çok etkenli sistemlerde özerklik ve hesap verebilirlik arasındaki gerilimi temel bir tasarım problemi olarak tanımlar. Bu gerilim, akademik araştırma bağlamında daha da keskinleşir. Çünkü akademik üretim, sonuçlar kadar sürecin de savunulabilir olmasını zorunlu kılar. Bir araç ne kadar güçlü olursa olsun, o savunulabilirlik araştırmacının üzerinde kalır. Bu nedenle Claude Code'dan öğrenilen asıl şey şudur: araç bir yöntemsel ortak olarak ancak araştırmacının onu denetleyebildiği ölçüde değer taşır.

Bu denetim kapasitesi, belirli bir arayüze bağlı değildir. İyi kurulduğunda araçtan araca taşınan bir çalışma alışkanlığına dönüşür.

## 2. Codex Nedir

Codex, OpenAI tarafından geliştirilen ve resmi belgelerde coding agent olarak konumlandırılan bir araç ailesidir (OpenAI, 2026a). Resmi geliştirici belgelerine göre Codex. Kod yazabilir, mevcut bir kod tabanını anlayabilir, kod inceleme ve hata ayıklama görevlerinde kullanılabilir, geliştirme iş akışlarını otomatikleştirebilir. Codex CLI ise terminalden çalışır. Seçili dizindeki kodu okuyabilir, değiştirebilir ve çalıştırabilir (OpenAI, 2026b).

Sosyal bilimci için bu tanım doğrudan önem taşır. Neden doğrudan? Çünkü çağdaş sosyal bilim üretiminde veri analizi, açık bilim paketi, repo bütünlüğü, kaynak doğrulama betikleri ve araştırma otomasyonları giderek daha fazla kod tabanlı hale geliyor. Kod yazmayı bilmeyen bir araştırmacı için bu araçlar ilk etapta uzak görünebilir. Ama aslında tam tersidir. Kod tabanlı iş akışlarına en çok ihtiyaç duyan, bu iş akışlarında destek almaktan en fazla fayda sağlayacak olan, deneyimli bir programcı değil sosyal bilimcidir. Bu yüzden Codex'i anlamak, yalnızca yazılım geliştiricilere yönelik bir egzersiz değildir.

Bu kitapçıkta Codex, Claude Code ile karşılaştırmalı bir düşünce nesnesi olarak ele alınır. Yeni merkez değildir. İkinci örnek alandır. Amaç, iki araç arasında bir tercih önermek değil, araçlar arası geçişte hangi soruların sabit kalması gerektiğini göstermektir.

## 3. Benzerlikler

Claude Code ve Codex, sosyal bilimci açısından aynı temel soruları doğurur. Bu sorular aracın adından önce gelir, çünkü ajan tabanlı araçların ortak yapısından doğarlar.

Birinci soru erişimdir: araç hangi dizine, hangi dosyaya erişiyor? İkinci soru onay eşiğidir: komut çalıştırmadan, dosya değiştirmeden ya da dış servise bağlanmadan önce araç araştırmacıdan açık onay istiyor mu? Üçüncü soru şeffaflıktır: araç, yaptığı değişikliği diff biçiminde gösteriyor mu, yoksa sessizce uygulayıp geçiyor mu? Dördüncü soru kayıttır: çıktı bir yerde arşivleniyor mu, kullanılan model versiyonu ve çalıştırma tarihi kayda geçiyor mu? Beşinci soru ise veri sınırıdır: araç gizli katılımcı verisine, klinik kayıtlara ya da lisanssız materyal içeren dosyalara erişebilir mi?

Mialon ve diğerleri (2023), dil modellerinin harici araç ve veritabanlarıyla entegrasyonunu sistematik biçimde inceler. Bu entegrasyonun araştırmacıya sunduğu fırsatlar kadar, araştırmacının farkında olması gereken gizlilik ve hata yönetimi riskleri de vardır. Araçtan bağımsız denetim matrisi, tam olarak bu riskleri görünür kılmak için tasarlanmıştır.

Bu ortak sorular, araçlar değişse de yanıtlanması gereken sabit bir çerçeve oluşturur. Araç farklı olabilir. Matris değişmez.

## 4. Farklar

Her aracın izin modeli, çalışma ortamı, bulut ile yerel işlem dengesi, beceri yapısı ve veri akışı farklıdır. Bu farklılıklar teknik ayrıntı gibi görünebilir. Ama akademik araştırma bağlamında yöntemsel sonuçları vardır.

İzin modeli, araştırmacının denetim alanını doğrudan belirler. Bir araç varsayılan olarak her komut için onay istiyorsa araştırmacı her adımı görebilir. Varsayılan olarak otonom çalışıyorsa araştırmacının denetim sorumluluğu artmış demektir. Bulut ile yerel işlem dengesi, veri güvenliği açısından kritiktir. Araştırma verisinin sunucuya gidip gitmediğini, hangi veri gizlilik politikasının geçerli olduğunu bilmek, araştırmacının kurumsal etik onay koşullarına uymak için zorunludur.

Araçlar arası geçişte en tehlikeli varsayım şudur: "önceki araçta güvenliydi, burada da güvenlidir." Bu varsayım, iki ayrı aracın farklı erişim modellerini, farklı kayıt pratiklerini ve farklı veri işleme koşullarını görmezden gelir. Claude Code'da güvenli olan bir iş akışı, Codex'e taşınırken bu koşulların her biri ayrı ayrı sınanmalıdır.

Yao ve diğerleri (2023), ReAct çerçevesinde ajan kararlarının nasıl izlenebilir hale getirileceğini gösterir. Bu izlenebilirlik, araçlar arasında transfere izin vermeyen bir özellik değildir. Tam tersine, bu izlenebilirliği talep eden sorular aracın adından bağımsızdır. Hangi araçta çalışıyor olursa olsun, araştırmacının sorması gereken soru aynıdır: bu karar nasıl oluştu ve nerede kayıt altına alındı?

## 5. Taşınması Gereken Beş Unsur

Araçlar değiştiğinde beş şey araştırmacıyla birlikte kalmalıdır. Bunlar kurumsal özelliklere ya da belirli bir araç arayüzüne bağlı değildir. Araştırmacının kendi çalışma alışkanlıklarına aittirler.

Birinci unsur kaynak sorumluluğudur. Hangi araçla çalışılırsa çalışılsın, her atıf doğrulanmalıdır. Model güvenilir bir kaynak sunduğunda bile araştırmacı o kaynağın var olduğunu, içeriğinin iddia edilen şeyi desteklediğini ve künye bilgilerinin doğru olduğunu bağımsız olarak kontrol etmelidir. Bender ve diğerleri (2021), büyük dil modellerinin doğrulama yapılmayan bağlamlarda nasıl hata ürettiğini gösterir. Bu gözlem, modelin adı değiştiğinde geçersiz olmaz.

İkinci unsur veri sınırıdır. Hangi araç kullanılırsa kullanılsın, klinik veri, katılımcı kimlikleri, anonim olmayan niteliksel materyal ve lisanssız içerik araca aktarılmaz. Bu sınır, araç politikasından değil, araştırmacının etik sorumluluğundan doğar. Araç değişse bile bu sorumluluk değişmez.

Üçüncü unsur karar günlüğüdür. Araştırmacının ajanla birlikte aldığı kararlar, hangi araçta çalışıyor olursa olsun arşive kaydedilir. Hangi sürüm, hangi tarih, hangi komut, hangi çıktı. Bu kayıt, araçların değiştiği bir ortamda araştırmanın yeniden üretilebilirliğinin tek güvencesidir.

Dördüncü unsur beyan disiplinidir. Araştırmacı, yapay zekâ destekli araçların akademik üretimdeki rolünü açıkça beyan etmekle yükümlüdür. Bu beyan, yalnızca Claude Code için geçerli değildir. Codex kullanıldıysa, bir API çağrısıyla metin üretildiyse, bir otomasyon betiği çalıştırıldıysa. Bunların hepsi beyan kapsamına girer. Hangi araç olursa olsun.

Beşinci unsur insan denetimidir. Bu rehberin başından sonuna savunulan tek bir ilke varsa odur. Araç özerk görünebilir. Çıktı ikna edici görünebilir. Ama yöntemsel karar araştırmacıya aittir. Araç değiştiğinde bu sorumluluk devredilmez.

## 6. Talimatlar ve Skills

Claude Code'un skills yapısı, tekrar kullanılabilir iş akışlarını kalıcı talimatlar biçiminde tanımlamak için tasarlanmıştır. Codex ve ChatGPT ekosisteminde de benzer bir skills kavramı vardır. OpenAI'nin yardım merkezi, ChatGPT'deki skills'i belirli görevlere karşılık gelen tekrar kullanılabilir yetenekler olarak tanımlar (OpenAI Help Center, 2026a). Bu iki yapı yüzeyde benzerdir. Ama araçtan bağımsız bir çalışma düzeni kurmak isteyen araştırmacı için bu benzerlik bir tuzak da içerir.

Tuzak şudur: bir araçta iyi çalışan bir skill, o aracın izin modeline, dosya erişim davranışına ve dış servis entegrasyonuna göre yazılmıştır. Aynı skill başka bir araca aktarıldığında, teknik biçimi aynı kalmış olsa bile davranışı farklılaşabilir. Bu nedenle skill taşınabilirliği, dosya kopyalamak değildir.

Taşınabilirliğin doğru anlamı şudur: bir skill'in altında yatan mantık, yani hangi adımda ne doğrulanır, hangi koşul sağlanmadan işlem sürmez, çıktı nereye arşivlenir ve başarı nasıl ölçülür, yeni ortama uyarlanarak yeniden kurulur. Bu yeniden kurulum, doğrudan kopyalamaktan çok daha titiz bir çalışma gerektirir. Ama bedelini öder. Çünkü uyarlanmış ve sınanmış bir skill, gerçek taşınabilirliği sağlar.

## 7. Codex'e İlk Geçiş Sağlık Testleri

Yeni bir araca geçişte yapılacak ilk iş üretim başlatmak değildir. Sağlık testleri yapmaktır. Bu testler, Claude Code'da çalışan araştırmacının yeni araca geçerken atlaması gereken minimal doğrulama adımlarıdır.

Birinci test dizin doğrulamasıdır. Araç doğru dizinde mi çalışıyor? Araştırma dosyasına mı, yoksa sistem dosyasına mı erişiyor? Bunu kontrol etmeden gerçek bir dosya üzerinde çalışmak risklidir.

İkinci test onay akışıdır. Araç dosya değiştirmeden ya da komut çalıştırmadan önce araştırmacıdan onay istiyor mu? Varsayılan davranış onay gerektiriyorsa, bu açıkça doğrulanmalıdır. Gerektirmiyorsa, buna göre ek bir denetim katmanı kurulmalıdır.

Üçüncü test diff görünürlüğüdür. Araç yaptığı değişiklikleri diff biçiminde sunuyor mu? Bir dosyada neyin değiştiğini görmeden değişikliği kabul etmek, herhangi bir araçta tehlikelidir.

Dördüncü test erişim sınırıdır. Araç, gizli veri içeren klasörlere erişebiliyor mu? Bu klasörler araçtan açıkça dışarıda bırakılmış mı? Bunu test etmek için küçük bir deneme çalıştırması yeterlidir.

Beşinci test kayıt akışıdır. Araç çalıştırma tarihini, model versiyonunu ve komut geçmişini kaydediyor mu? Kaydediyorsa nereye? Bu bilgi olmadan araştırmanın yeniden üretilebilirliği sağlanamaz.

Bu testler geçilmeden yeni araçla gerçek araştırma dosyası üzerinde çalışılmaz. Bu bir tavsiye değil, metodolojik bir gereklilik.

## 8. İkinci Ajanla Denetim

Codex, Claude Code ile üretilmiş bir analiz betiğini ikinci göz olarak inceleyebilir. Claude Code da Codex çıktısını denetleyebilir. Bu çapraz denetim düzeni cazip görünür. Çünkü iki ayrı araç aynı hatayı aynı anda yapma olasılığı düşüktür.

Ama bu düzenin sınırlarını da görmek gerekir. Birincisi, iki araç da aynı temel eğitim veri setlerinden beslenmiş olabilir. Bu durumda ortak önyargılar, ikinci ajanın denetiminden de sıyrılır. İkincisi, ikinci ajan ikinci hakem değildir. Hakemlik, alanı ve yöntemi anlayan insan değerlendirmesini gerektirir. Araç bu değerlendirmenin yerini alamaz. Üçüncüsü, çapraz denetim yalnızca teknik tutarlılığı artırabilir. Yöntemsel hataları, etik boşlukları ya da kavramsal yanlışları tespit etmek araştırmacının işidir.

Bu düzen, araçlar arası kör güven yerine araçlar arası teknik sağlama üretir. Yeterli bir sağlama mıdır? Değildir. Ama hiç yoktan iyidir. Yeter ki araştırmacı, ikinci ajanın onayını insan incelemesinin yerine koymadığının farkında olsun.

Chang ve Bergen (2024), dil modeli davranışlarının çeşitli bağlamlarda nasıl farklılaştığını kapsamlı biçimde inceler. Bu farklılaşma, aynı aracın farklı sürümleri arasında bile gözlemlenebilir. İki farklı araç arasındaki denetim düzeni, bu farklılaşmayı azaltabilir ama ortadan kaldırmaz.

## 9. Gelecekteki Araçlar

Bugünkü Codex yarın değişecektir. Claude Code da değişecektir. Yeni ajanlar, yeni mimariler, yeni izin modelleri gelecektir. Bu değişim, akademik araştırma için bir tehdit değildir. Ama uyarlanmayı zorunlu kılar.

Uyarlanmanın ne anlama geldiğini anlamak için şunu sormak yeterlidir: bir araştırmacı yeni bir araca ilk kez baktığında hangi soruları sormalıdır?

İlk soru erişimdir: araç hangi verilere ulaşıyor? İkinci soru işlemdir: bu verilerle ne yapıyor, nerede işliyor, ne kadar saklıyor? Üçüncü soru onay eşiğidir: araştırmacıdan ne zaman izin istiyor, ne zaman otonom davranıyor? Dördüncü soru kayıttır: karar ve çıktı nerede arşivleniyor, bu arşiv araştırmacının denetimine açık mı? Beşinci soru beyan gereksinimidir: bu aracın kullanımı etik onay koşullarını, dergi beyan politikalarını ya da kurumsal veri güvenliği gerekliliklerini nasıl etkiliyor?

Bu beş soru, belirli bir aracın adından daha kalıcıdır. Araç ne olursa olsun yanıtlanmaları gerekir. Bir araştırmacı bu soruları içselleştirdiğinde araç bağımsız bir çalışma disiplini kazanmış olur. O disiplin, bir sonraki araca geçişte sıfırdan başlamayı gerektirmez. Yalnızca yeni bağlama uyarlanmayı gerektirir.

## 10. Skill Çıktıları

Bu kitapçık iki skill çerçevesi önerir. Bunlar mevcut araçların komut sözdizimi olarak değil, araştırmacının yeni bir araca geçişte ne üretmesi gerektiğinin şablonu olarak anlaşılmalıdır.

Birinci şablon taşınabilirlik matrisidir. Yeni bir araçla çalışmaya başlamadan önce araştırmacı şu dört sütunu doldurabilen bir belge hazırlar: taşınan unsur, taşıma biçimi, uyarlanacak unsur ve yeniden test edilecek unsur. Bu matris, eski araçta çalışan her iş akışının yeni araçta sessizce çalıştığını varsaymanın önünü keser. Geçişi görünür ve denetlenebilir kılar.

İkinci şablon çapraz ajan ikinci görüş protokolüdür. Bir araştırmacı, Araç A ile ürettiği bir çıktıyı Araç B'ye denetletmek istediğinde ne yapmalıdır? Önce gönderilecek materyalin gizlilik kontrolü yapılır. Sonra denetimden beklenen asgari çıktı belirlenir: hangi kriterlere göre değerlendirme yapılacak, ne bulunursa uyuşmazlık olarak kayıt altına alınacak, bulgular insan incelemesine nasıl taşınacak? Bu protokol olmadan çapraz denetim bir güvence değil, yalnızca ek bir çıktı üretme işlemidir.

Bu kitapçığın kapanışı şudur. Claude Code ile başlayan disiplin, Codex'e ve gelecekteki tüm araçlara taşınabilir. Bu taşınabilirlik kendiliğinden gerçekleşmez. Araştırmacı onu kurar, sınar ve korur. Disiplin araçtan önce gelir. Araç gidince de kalır.

## Kaynakça

Atıflar APA 7 biçimindedir. Tüm DOI'ler Crossref üzerinden, tüm kurumsal URL'ler doğrudan erişimle 2026-06-21 tarihinde doğrulanmıştır. Doğrulanamayan kaynaklar listeye alınmamıştır.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency*, 610–623. https://doi.org/10.1145/3442188.3445922

Chang, T. A., & Bergen, B. K. (2024). Language model behavior: A comprehensive survey. *Computational Linguistics*, *50*(1), 293–350. https://doi.org/10.1162/coli_a_00492

Mialon, G., Dessì, R., Lomeli, M., Nalmpantis, C., Pasunuru, R., Raileanu, R., Rozière, B., Schick, T., Dwivedi-Yu, J., Celikyilmaz, A., Grave, E., LeCun, Y., & Scialom, T. (2023). Augmented language models: A survey. *Transactions on Machine Learning Research*. https://arxiv.org/abs/2302.07842

OpenAI. (2026a). *Codex*. OpenAI Developers. https://developers.openai.com/codex

OpenAI. (2026b). *Codex CLI*. OpenAI Developers. https://developers.openai.com/codex/cli

OpenAI. (2026c). *Agent skills*. OpenAI Developers. https://developers.openai.com/codex/skills

OpenAI Help Center. (2026a). *Skills in ChatGPT*. https://help.openai.com/en/articles/20001066-skills-in-chatgpt

OpenAI Help Center. (2026b). *Using Codex with your ChatGPT plan*. https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan

Wooldridge, M. (2009). *An introduction to multiagent systems* (2nd ed.). Wiley. ISBN 978-0-470-51946-2

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting in language models. *International Conference on Learning Representations*. https://arxiv.org/abs/2210.03629

---

**Kitapçık kimliği.** `014-01-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1950 (Türkçe gövde metni)
**Doğrulanmış atıf sayısı.** 10
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`013-01-0001`](../../013-teaching-supervision/013-01-0001/tr.md). Öğretimde Yapay Zekâ, Ders Tasarımı, Süpervizyon ve Öğrenci Geri Bildirimi
**Sonraki kitapçık.** Yok. Bu, v3.2.0 genişleme dizisinin kapanış kitapçığıdır.
