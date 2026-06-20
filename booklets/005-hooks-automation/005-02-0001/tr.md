---
title_en: "Ritual Hooks: Daily Logging, Session Persistence, Idle Time"
title_tr: "Ritüel Hook'lar: Günlük Kayıt, Oturum Kalıcılığı, Boş Zaman"
booklet_id: "005-02-0001"
category: "005-hooks-automation"
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

# Ritüel Hook'lar: Günlük Kayıt, Oturum Kalıcılığı, Boş Zaman

Önceki kitapçık arşivin mimarisini kurdu. Klasör disiplini ve içerik haritalarıyla, yıllarca yaşayacak bir akademik hafızanın iskeleti çizildi. Ne var ki mimari kendi başına yaşamaz. Bir arşiv, her oturumda beslenirse arşivdir. Beslemeyi araştırmacının iradesine bırakan her sistem, yoğun bir dönemde sessizce çürür. Bu kitapçık o yükü iradeden alıp altyapıya veren mekanizmayı anlatır. Hook, oturumun belirli anlarında kendiliğinden çalışan küçük bir otomasyondur ve doğru kurulduğunda araştırma disiplinini bir karaktere değil bir düzeneğe dönüştürür. Üç ritüel üzerinden ilerleyeceğiz. Günlük kayıt, oturum kalıcılığı ve boş zaman bakımı.

## 1. Disiplinden Altyapıya

Araştırma yaşamının en pahalı kayıpları çoğu zaman dramatik değildir. Yazılmayan bir günlük satırı, kapanırken notu alınmayan bir oturum, aylarca kontrol edilmeyen kırık bağlantılar. Tek tek önemsiz görünen bu ihmaller birikir ve arşivin güvenilirliğini içeriden aşındırır. Geleneksel çözüm öz disiplindir. Her oturumun sonunda not alacağım kararı, ilk hafta çalışır, yoğun haftada aksar ve dönem sonunda unutulur.

Mühendislik geleneği aynı soruna başka yerden bakar. Bir davranışın her seferinde gerçekleşmesi isteniyorsa, o davranış bir insana değil bir mekanizmaya bağlanır. Hook tam olarak budur. Oturum açıldığında, bir araç çalıştığında ya da oturum kapanırken tetiklenen ve araştırmacı hatırlamasa da görevini yapan küçük bir betik. İrade gerektiren disiplin, irade gerektirmeyen altyapıya çevrilir.

## 2. Alışkanlık Bilimi ve Ritüelin Yeri

Bu çevirinin psikolojik bir zemini vardır. Wood ve Rünger (2016), alışkanlık psikolojisini gözden geçirdikleri çalışmada alışkanlığın bağlama bağlı tekrarla kurulduğunu ve kurulduktan sonra anlık hedeflerden görece bağımsız, bağlam ipucuyla tetiklenen bir otomatiklik kazandığını ortaya koyar. Hedefler davranışı başlatır, alışkanlıklar sürdürür. Ritüel hook bu mekanizmanın araç katmanındaki karşılığıdır. Oturumun açılışı sabit bir bağlam ipucudur ve o ipucuna bağlanan otomasyon, davranışı araştırmacının o günkü motivasyonundan koparır.

Sword (2017) ise başarılı akademisyenlerin yazma pratiğini incelediği nitel araştırmasında tek bir doğru reçete bulamaz. Üretken yazarları birleştiren şey belirli bir program değil, kendi koşullarına uyan bir ritüeli kurmuş ve korumuş olmalarıdır. Hook altyapısı bu bulguyla uyumlu çalışır. Hangi ritüelin kurulacağını araştırmacı seçer. Altyapının katkısı, seçilen ritüelin kötü bir haftada bile ayakta kalmasıdır.

## 3. Hook Nedir, Ne Zaman Ateşlenir

Claude Code, oturum yaşam döngüsünün belirli anlarında dışarıdan tanımlanmış komutların çalıştırılmasına izin verir ve bu anlara hook denir (Anthropic, 2026). Araştırmacının bilmesi gereken harita sadedir. Oturum açılışında çalışan hook, bağlamı hazırlar. Bir araç çalışmadan önce ya da çalıştıktan sonra devreye giren hook, denetler ve kayıt tutar. Oturum kapanırken çalışan hook, günü mühürler.

Programcı olmayan bir sosyal bilimci için giriş eşiği düşüktür, çünkü hook'un kendisi çoğu zaman tek satırlık bir komuttur. Bugünün tarihiyle bir günlük dosyası aç. Kapanışta şu nota ekle. Şu klasöre dokunulduysa uyar. Karmaşıklık arttıkça betik de büyüyebilir, ancak bu kitapçıktaki üç ritüelin tamamı küçük ve okunabilir parçalarla kurulur.

## 4. Ritüel Bir, Günlük Kayıt

İlk ritüel laboratuvar defterinin ağırlığını taşır. Oturum açılışına bağlanan bir hook, o günün tarihiyle bir günlük dosyası oluşturur ya da varsa açar ve aktif bağlamı içine yazar. Hangi proje, hangi amaç, önceki oturumdan ne devralındı. Araştırmacı oturuma boş bir zihinle değil, dünün kaldığı yerden başlar.

Belcher (2019), akademik yazma programında büyük işin küçük ve bitirilebilir parçalara bölünmesini sürdürülebilirliğin koşulu sayar. Günlük kayıt bu ilkenin kayıt katmanıdır. Günün girdisi birkaç satırdır ve birkaç satır olduğu için yazılır. Aylar sonra bir bulgu, bir karar ya da bir hata arandığında, o küçük satırların toplamı arşivin en çok başvurulan bölümü hâline gelir. Deneyimimiz şudur. Günlük dosyası elle açıldığı dönemde haftada iki üç gün doluyordu. Hook'a bağlandığından beri her oturum bir iz bırakıyor.

## 5. Ritüel İki, Oturum Kalıcılığı

İkinci ritüel, oturumlar arasındaki kopuşu kapatır. Bir araştırma oturumu nadiren tamamlanmış bir bütündür. Analiz yarıda kalır, taslak bir sonraki güne devreder, akılda tutulması gereken bir karar havada asılıdır. Oturum kapanışına bağlanan hook, bu devri otomatikleştirir. Kapanış anında günün özeti ve sonraki oturum için talimat niteliğinde kısa bir not arşive yazılır.

Bu ritüelin değeri, bağlamın kırılgan olduğu gerçeğinde yatar. Araç yeniden başlar, bilgisayar kapanır, araya günler girer. Devir notu varsa hiçbiri kayıp üretmez. Sonraki oturumun açılış hook'u aynı notu bulur ve masaya koyar. İki ritüel birlikte, oturumları birbirine zincirleyen bir kalıcılık katmanı kurar. Tek tek oturumlar unutulabilir. Zincir unutmaz.

## 6. Ritüel Üç, Boş Zaman ve Bakım

Üçüncü ritüel görünmez işleri üstlenir. Bir arşiv yaşadıkça bağlantılar kırılır, biçim tutarsızlıkları birikir, geçici dosyalar çoğalır. Bu bakım işlerinin hiçbiri bir oturumun ortasında yapılmayı hak etmez ve tam bu yüzden hiç yapılmama riski taşır. Çözüm, bakımı boş zamana ya da takvime bağlamaktır. Belirli aralıklarla çalışan bir betik bağlantıları tarar, adlandırma kurallarını denetler ve bulduklarını bir rapora yazar.

Wilson ve diğerleri (2017), bilimsel hesaplama için yeterince iyi pratikleri derledikleri çalışmada, tekrarlanan denetimlerin elle değil otomasyonla yürütülmesini sıradan ama getirisi büyük bir adım olarak tarif eder. İlke arşiv bakımına olduğu gibi taşınır. İnsanın unutacağı işi makineye vermek, mükemmeliyetçilik değil ekonomidir. Raporu okumak ve karar vermek yine insana kalır.

## 7. Koruyucu Hook'lar

Ritüellerin bir de bekçi kanadı vardır. Koruyucu hook, bir işlem gerçekleşmeden önce devreye girer ve belirli koşullarda işlemi durdurur. Arşiv deposuna her kayıt öncesi çalışan bir gizli bilgi taraması bunun en değerli örneğidir. Parola, anahtar ya da kimlik bilgisi içeren bir dosya, tarayıcıyı geçemeden kayıt durur. Aynı desen atıf koruması için de çalışır. Kaynakça dosyalarına dokunan bir değişiklik, DOI biçim denetiminden geçmeden depoya giremez.

Munafò ve diğerleri (2017), yeniden üretilebilir bilim manifestosunda hata ve esnekliğin insan eline bırakıldığı her noktayı bir risk olarak işaretler ve yapısal önlemleri savunur. Koruyucu hook bu yapısal önlemin gündelik biçimidir. Kural bir kez yazılır ve her işlemde, yorgunluktan ve acele etmekten bağımsız, aynı titizlikle uygulanır.

## 8. Sınırlar ve Güvenlik

Hook'lar kod çalıştırır ve bu cümle tek başına bir güvenlik bölümünü hak eder. Okumadığınız ya da anlamadığınız bir hook'u arşivinize bağlamayın. Başkasının yazdığı bir hook'u almadan önce ne yaptığını satır satır görün, göremiyorsanız vazgeçin. İnternetten kopyalanan bir betik, arşivin tamamına dokunabilecek yetkiyle çalışacaktır.

İki sınır daha çizilmelidir. Ham katılımcı verisi içeren klasörlere hiçbir otomasyon kendiliğinden dokunmamalıdır, çünkü onam ve gizlilik yükümlülükleri otomasyon kolaylığından önce gelir. Bir de görünürlük kuralı vardır. Hook sessizce başarısız olmamalıdır. Çalışmayan bir günlük hook'u, çalışmadığını söylemezse arşiv aylarca beslenmeden kalır ve kayıp ancak arandığında fark edilir. Her ritüel, başarısızlığını raporlayacak biçimde kurulur.

## 9. Kendi Ritüelini Kurmak

Kurulumun en yaygın hatası hırstır. Beş ritüeli aynı gün bağlayan araştırmacı, ilk uyumsuzlukta beşini birden kapatır. Doğru başlangıç tek ritüeldir ve en yüksek getirili aday çoğu kişi için günlük kayıttır. Bir hafta çalıştırılır ve haftanın sonunda tek bir soruyla sınanır. Bu hafta kaç oturum açıldı ve kaçında günlük satırı oluştu? İki sayı eşitse ritüel oturmuştur ve sıradaki eklenebilir. Eşit değilse önce neden ayrıştırılır.

Bu sınama yöntemi kitapçığın genel ilkesini tekrarlar. Bir otomasyonun değeri hissedilerek değil sayılarak anlaşılır. Hook'ların kendisi de arşive kayıt düştüğü için sayım zahmetsizdir. Kurulan her yeni ritüel, kendi başarısının kanıtını kendisi üretir.

## 10. Köprü, Oturumun Dışına Uzanmak

Hook'lar oturumun içini düzenler. Açılışı, kapanışı ve aradaki denetim noktalarını. Oturumun dışarıyla kurduğu ilişki ise başka bir mekanizmanın konusudur. Araç, bir veri tabanına, bir kaynak kataloğuna ya da bir referans yöneticisine bağlanacaksa bu bağlantının adı, kapsamı ve güven sınırı ayrıca kurulmalıdır. Bir sonraki kitapçık bu mekanizmayı, Model Context Protocol'ü, araştırmacının gözünden ele alır. Ne olduğu, neden gerektiği ve ne zaman gerekmediği.

## Kaynakça

Atıflar APA 7 biçimindedir. DOI'ler 2026-06-12 tarihinde Crossref üzerinden doğrulanmıştır.

Anthropic. (2026). *Claude Code documentation*. https://docs.claude.com/en/docs/claude-code

Belcher, W. L. (2019). *Writing your journal article in twelve weeks: A guide to academic publishing success* (2nd ed.). University of Chicago Press. ISBN 978-0-226-49991-8

Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J., & Ioannidis, J. P. A. (2017). A manifesto for reproducible science. *Nature Human Behaviour*, 1(1), Article 0021. https://doi.org/10.1038/s41562-016-0021

Sword, H. (2017). *Air & light & time & space: How successful academics write*. Harvard University Press. https://doi.org/10.4159/9780674977617

Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLoS Computational Biology*, 13(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510

Wood, W., & Rünger, D. (2016). Psychology of habit. *Annual Review of Psychology*, 67, 289–314. https://doi.org/10.1146/annurev-psych-122414-033417

---

**Kitapçık kimliği.** `005-02-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-20
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1157 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 6
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`004-01-0001`](../../004-vault-architecture/004-01-0001/tr.md). Klasör Disiplini ve Maps of Content (MOC) Kalıbı
**Sonraki kitapçık.** [`006-01-0001`](../../006-mcp-plugins/006-01-0001/tr.md). Araştırmacı İçin MCP: Ne, Neden, Ne Zaman
