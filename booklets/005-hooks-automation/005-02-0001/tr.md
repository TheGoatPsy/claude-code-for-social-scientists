---
title_en: "Ritual Hooks. Daily Logging, Session Persistence, and Idle Time"
title_tr: "Ritüel Hook'lar. Günlük Kayıt, Oturum Kalıcılığı ve Boş Zaman Bakımı"
booklet_id: "005-02-0001"
category: "005-hooks-automation"
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

# Ritüel Hook'lar. Günlük Kayıt, Oturum Kalıcılığı ve Boş Zaman Bakımı

Günlük Kayıt, Oturum Kalıcılığı ve Boş Zaman Bakımı

## Giriş

Önceki kitapçık arşivin mimarisini kurmuştu. Klasör disiplini ve içerik haritalarıyla, yıllarca yaşayabilecek bir akademik hafızanın iskeleti çizildi. Ancak mimari kendi başına yaşamaz. Bir arşiv, her oturumda beslenirse arşivdir. Beslenmeyen arşiv zamanla yalnızca iyi niyetle kurulmuş bir dosya yığınına dönüşür.

Bu kitapçık, araştırmacının her oturumda tekrarlaması gereken küçük ama kritik işlemleri altyapıya bağlayan ritüel hook'ları ele alır. Hook, oturumun belirli anlarında kendiliğinden çalışan küçük bir otomasyondur. Doğru kurulduğunda araştırma disiplinini yalnızca araştırmacının o günkü motivasyonuna bırakmaz. Günlük kayıt, oturum kalıcılığı ve boş zaman bakımı gibi işlemleri düzenli, görünür ve denetlenebilir bir iş akışı parçasına dönüştürür.

Bu kitapçığın temel iddiası şudur. Akademik arşivin güvenilirliği yalnızca iyi klasör yapısıyla değil, bu yapının her oturumda düzenli olarak beslenmesiyle korunur. Hook'lar, bu düzenliliği araştırmacının hafızasına ve iradesine bırakmadan altyapıya bağlayan pratik araçlardır.

## 1. Disiplinden Altyapıya

Araştırma yaşamındaki en pahalı kayıplar çoğu zaman dramatik değildir. Yazılmayan bir günlük satırı, kapanırken özetlenmeyen bir oturum, kontrol edilmeyen kırık bağlantılar ya da fark edilmeden biriken geçici dosyalar tek başına küçük görünür. Ancak bu küçük ihmaller birikerek arşivin güvenilirliğini içeriden aşındırır.

Geleneksel çözüm öz disiplindir. Araştırmacı her oturumun sonunda not alacağına, her dosyayı doğru yere koyacağına, her kaynağı kontrol edeceğine karar verir. Bu karar çoğu zaman ilk hafta işler. Yoğun haftada aksar. Dönem sonunda unutulur. Sorun araştırmacının kötü niyetinde değil, akademik iş yükünün sürekliliğindedir.

Mühendislik geleneği aynı soruna başka bir yerden bakar. Bir davranışın her seferinde gerçekleşmesi isteniyorsa, o davranış yalnızca insan iradesine değil, mekanizmaya bağlanır. Hook tam olarak bu işlevi görür. Oturum açıldığında, bir araç çalıştığında ya da oturum kapanırken tetiklenen küçük bir betik, araştırmacı hatırlamasa da görevi yerine getirir. Böylece irade gerektiren disiplin, irade gerektirmeyen bir altyapı bileşenine dönüşür.

## 2. Alışkanlık Bilimi ve Ritüelin Yeri

Bu yaklaşımın psikolojik bir zemini vardır. Wood ve Rünger (2016), alışkanlığın bağlama bağlı tekrarla kurulduğunu ve yerleştikten sonra anlık hedeflerden görece bağımsız bir otomatiklik kazandığını gösterir. Davranışı başlatan çoğu zaman hedeftir. Davranışı sürdüren ise bağlam ipuçlarıyla kurulmuş alışkanlıklardır.

Ritüel hook, bu mekanizmanın araç katmanındaki karşılığıdır. Oturumun açılması sabit bir bağlam ipucudur. Bu ipucuna bağlanan otomasyon, davranışı araştırmacının o günkü enerjisinden, motivasyonundan ve hatırlama kapasitesinden bir ölçüde bağımsızlaştırır. Günlük dosyasını açmak ya da kapanış notunu oluşturmak artık araştırmacının ayrıca hatırlaması gereken bir iş olmaktan çıkar.

Sword (2017), başarılı akademisyenlerin yazma pratiklerini incelediği çalışmada tek bir doğru reçete bulmaz. Üretken yazarları birleştiren şey, kendi koşullarına uygun bir ritüel kurmuş ve bu ritüeli sürdürebilmiş olmalarıdır. Hook altyapısı bu bulguyla uyumludur. Hangi ritüelin kurulacağına araştırmacı karar verir. Altyapının katkısı, seçilen ritüelin yoğun ve dağınık haftalarda bile ayakta kalmasına yardım etmektir.

## 3. Hook Nedir, Ne Zaman Çalışır?

Claude Code, oturum yaşam döngüsünün belirli anlarında dışarıdan tanımlanmış komutların çalıştırılmasına izin verir ve bu komut noktalarına hook denir (Anthropic, 2026). Araştırmacı açısından temel harita sadedir. Oturum açılışında çalışan hook bağlamı hazırlar. Bir araç çalışmadan önce ya da çalıştıktan sonra devreye giren hook denetim ve kayıt işlevi görebilir. Oturum kapanırken çalışan hook ise günün izini arşive aktarabilir.

Programcı olmayan bir sosyal bilimci için giriş eşiği düşünüldüğünden daha düşüktür. Hook çoğu zaman tek satırlık bir komutla başlar. Bugünün tarihiyle bir günlük dosyası aç. Kapanışta şu notu güncelle. Belirli bir klasöre dokunulduysa uyar. Karmaşıklık arttıkça betikler büyüyebilir, ancak bu kitapçıkta ele alınan üç ritüel küçük ve okunabilir otomasyonlar olarak tasarlanmalıdır.

Bu nedenle hook kavramı, araştırmacının kontrolünü azaltan bir otomasyon değil, tekrarlanan küçük işleri daha güvenilir hâle getiren bir iş akışı bileşeni olarak düşünülmelidir.

## 4. Ritüel Bir. Günlük Kayıt

İlk ritüel, laboratuvar defteri geleneğinin dijital arşivdeki karşılığıdır. Oturum açılışına bağlanan bir hook, o günün tarihiyle bir günlük dosyası oluşturur ya da varsa mevcut dosyayı açar. Ardından aktif bağlamı bu dosyaya işler. Hangi proje üzerinde çalışılıyor? Oturumun amacı ne? Önceki oturumdan ne devralındı? Bugün hangi kararlar izlenmeli?

Belcher (2019), akademik yazma sürecinde büyük işlerin küçük ve tamamlanabilir parçalara bölünmesini sürdürülebilirliğin koşulu olarak ele alır. Günlük kayıt bu ilkenin kayıt katmanıdır. Günün girdisi birkaç satırdır. Birkaç satır olduğu için yazılır. Aylar sonra bir kararın, hatanın ya da bulgunun kökeni arandığında bu küçük satırlar arşivin en değerli parçalarından birine dönüşür.

Burada amaç uzun bir günlük tutmak değildir. Amaç, her oturumun iz bırakmasıdır. İyi günlük hook'u araştırmacıya roman yazdırmaz. Yalnızca o günün akademik izini kaybolmayacak kadar görünür kılar.

## 5. Ritüel İki. Oturum Kalıcılığı

İkinci ritüel, oturumlar arasındaki kopuşu azaltır. Bir araştırma oturumu çoğu zaman tamamlanmış bir bütün olarak bitmez. Analiz yarıda kalır, yazı ertesi güne devreder, bir yöntem kararı henüz kesinleşmemiştir ya da bir kaynak daha sonra kontrol edilmek üzere beklemektedir. Oturum kapanışına bağlanan hook, bu devri otomatikleştirir.

Kapanış anında günün kısa özeti ve sonraki oturum için talimat niteliğinde bir not arşive yazılır. Ertesi oturum açıldığında, açılış hook'u bu notu araştırmacının önüne getirir. Böylece araç yeniden başlasa, bilgisayar kapansa ya da araya günler girse bile bağlam bütünüyle kaybolmaz.

Bu ritüelin değeri, bağlamın kırılgan olduğu gerçeğinde yatar. İnsan zihni yoğun dönemlerde neyin nerede kaldığını unutabilir. Oturum kalıcılığı ritüeli, unutmayı ahlaki bir kusur olarak değil, tasarım sorunu olarak ele alır. Çözümü de hatırlamaya değil, kayıt ve geri çağırmaya bağlar.

## 6. Ritüel Üç. Boş Zaman Bakımı

Üçüncü ritüel, arşivin görünmez bakım işlerini üstlenir. Arşiv büyüdükçe bağlantılar kırılır, biçim tutarsızlıkları birikir, geçici dosyalar çoğalır ve bazı notlar yetim kalır. Bu işlerin hiçbiri bir yazı oturumunun ortasında öncelikli görünmez. Tam da bu nedenle hiç yapılmama riski taşır.

Çözüm, bakımı boş zamana ya da takvimlenmiş aralıklara bağlamaktır. Belirli aralıklarla çalışan küçük bir betik bağlantıları tarayabilir, dosya adlandırma kurallarını denetleyebilir, geçici dosyaları raporlayabilir ve uyumsuzlukları bir bakım notuna yazabilir.

Wilson ve diğerleri (2017), bilimsel hesaplama için yeterince iyi pratikleri tartışırken tekrarlanan denetimlerin elle değil otomasyonla yürütülmesini sıradan ama getirisi yüksek bir ilke olarak ele alır. Aynı ilke akademik arşiv bakımına da uygulanabilir. İnsanın unutacağı işi makineye vermek mükemmeliyetçilik değildir. İyi düzenlenmiş bir emek ekonomisidir. Karar vermek yine araştırmacıda kalır. Otomasyon yalnızca neyin dikkat istediğini görünür kılar.

## 7. Koruyucu Hook'lar

Ritüel hook'ların bir de koruyucu işlevi vardır. Koruyucu hook, belirli bir işlem gerçekleşmeden önce devreye girer ve riskli koşullarda işlemi durdurur. Arşiv deposuna kayıt yapılmadan önce çalışan bir gizli bilgi taraması bunun önemli örneklerinden biridir. Parola, API anahtarı ya da kimlik bilgisi içeren bir dosya depoya girmeden önce yakalanabilir.

Aynı mantık atıf koruması için de kullanılabilir. Kaynakça dosyalarına dokunan bir değişiklik, DOI biçim denetiminden geçmeden arşive alınmayabilir. Böylece atıf disiplini yalnızca araştırmacının dikkatine bırakılmaz, teknik bir denetim noktasına bağlanır.

Munafò ve diğerleri (2017), yeniden üretilebilir bilim manifestosunda hata ve esnekliğin yalnızca bireysel dikkatle yönetilmesini risk olarak görür ve yapısal önlemleri savunur. Koruyucu hook, bu yapısal önlemin gündelik çalışma düzeyindeki karşılığıdır. Kural bir kez yazılır ve yorgunluktan, aceleden ya da unutkanlıktan bağımsız biçimde her işlemde aynı titizlikle uygulanır.

## 8. Sınırlar ve Güvenlik

Hook'lar kod çalıştırır. Bu nedenle güvenlik meselesi ikincil değildir. Araştırmacı okumadığı, anlamadığı ya da kaynağından emin olmadığı bir hook'u arşivine bağlamamalıdır. İnternetten kopyalanan bir betik, arşivin tamamına dokunabilecek yetkiyle çalışabilir. Bu nedenle her hook, kullanılmadan önce ne yaptığı açısından açıkça denetlenmelidir.

İlk sınır hassas veriye ilişkindir. Ham katılımcı verisi, kimlik içeren mülakat dökümleri ya da klinik materyal içeren klasörlere hiçbir otomasyon kendiliğinden dokunmamalıdır. Onam, gizlilik ve veri güvenliği yükümlülükleri otomasyon kolaylığından önce gelir.

İkinci sınır görünürlüktür. Hook sessizce başarısız olmamalıdır. Çalışmayan bir günlük hook'u çalışmadığını bildirmezse arşiv haftalarca beslenmeden kalabilir. Bu kayıp ancak ihtiyaç anında fark edilir. Bu nedenle her ritüel, başarısızlığını raporlayacak biçimde kurulmalıdır.

## 9. Kendi Ritüelini Kurmak

Kurulumun en yaygın hatası hırstır. Araştırmacı aynı gün beş farklı ritüel kurar. İlk uyumsuzlukta hepsini kapatır. Daha doğru başlangıç tek ritüeldir. Çoğu araştırmacı için en yüksek getirili aday günlük kayıttır.

Bir hafta boyunca yalnızca günlük kayıt ritüeli çalıştırılır. Haftanın sonunda basit bir soru sorulur. Bu hafta kaç oturum açıldı ve kaçında günlük satırı oluştu? İki sayı eşitse ritüel yerleşmiştir. Eşit değilse önce sorun ayrıştırılır. Hook mu çalışmadı, dosya yolu mu yanlıştı, araştırmacı mı oturumu farklı yerden başlattı?

Bu sınama yöntemi kitapçığın genel ilkesini tekrarlar. Bir otomasyonun değeri hissedilerek değil, izlenerek anlaşılır. Hook'ların kendisi de arşive kayıt düşebildiği için sayım zahmetsizdir. Kurulan her yeni ritüel, kendi başarısının kanıtını üretmelidir.

## 10. Köprü. Oturumun Dışına Uzanmak

Hook'lar oturumun içini düzenler. Açılışı, kapanışı ve aradaki denetim noktalarını daha güvenilir hâle getirir. Ancak araştırma yalnızca oturumun içinde gerçekleşmez. Bir veri tabanına, kaynak kataloğuna, referans yöneticisine ya da başka bir dış hizmete bağlanmak gerekiyorsa, bu bağlantının adı, kapsamı ve güven sınırı ayrıca kurulmalıdır.

Bir sonraki kitapçık bu mekanizmayı, Model Context Protocol'ü, araştırmacının gözünden ele alır. MCP'nin ne olduğunu, neden gerekli olabileceğini ve ne zaman gereksiz bir karmaşıklık yaratacağını tartışır.

## Kaynakça

Atıflar APA 7 biçimindedir. DOI'ler 2026-06-21 tarihinde Crossref üzerinden doğrulanmıştır.

Anthropic. (2026). *Claude Code documentation*. https://docs.claude.com/en/docs/claude-code

Belcher, W. L. (2019). *Writing your journal article in twelve weeks: A guide to academic publishing success* (2nd ed.). University of Chicago Press. ISBN 978-0-226-49991-8

Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J., & Ioannidis, J. P. A. (2017). A manifesto for reproducible science. *Nature Human Behaviour*, 1(1), Article 0021. https://doi.org/10.1038/s41562-016-0021

Sword, H. (2017). *Air & light & time & space: How successful academics write*. Harvard University Press. https://doi.org/10.4159/9780674977617

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLoS Computational Biology*, 13(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510

Wood, W., & Rünger, D. (2016). Psychology of habit. *Annual Review of Psychology*, 67, 289–314. https://doi.org/10.1146/annurev-psych-122414-033417

---

**Kitapçık kimliği.** `005-02-0001`
**Sürüm.** `0.2.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1398 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 6
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`004-01-0001`](../../004-vault-architecture/004-01-0001/tr.md). Klasör Disiplini ve Maps of Content (MOC) Kalıbı
**Sonraki kitapçık.** [`006-01-0001`](../../006-mcp-plugins/006-01-0001/tr.md). Araştırmacı İçin MCP. Ne, Neden, Ne Zaman
