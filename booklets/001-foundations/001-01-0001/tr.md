---
title_en: "What is Claude Code? A Social Scientist's Perspective"
title_tr: "Claude Code Nedir? Sosyal Bilimci Bakışıyla"
booklet_id: "001-01-0001"
category: "001-foundations"
language: "tr"
version: "0.1.0"
date_published: "2026-05-19"
date_last_revised: "2026-06-20"
authors:
  - name: "Onour Impram"
    orcid: "0000-0003-1076-3928"
    role: "author, principal reviewer"
ai_assisted: true
ai_tools:
  - name: "Claude Code"
    vendor: "Anthropic"
    model_alias: "claude-opus-4-7"
    model_dated: null  # no dated identifier published by Anthropic for Opus 4.7 as of 2026-05-19
    role: "drafting, verification, citation lookup, bilingual re-authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-20"
verified_citations_count: 13
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Claude Code Nedir? Sosyal Bilimci Bakışıyla

Bu rehberin ilk kitapçığı, Anthropic'in Claude Code aracının sosyal bilimde çalışan bir araştırmacı, bir eğitimci ya da bir klinisyen için gerçekte ne anlama geldiğini kavramsal olarak çerçeveler. Çerçeve yöntemseldir. Asıl mesele, Claude Code'un akademik üretime nerede gerçek bir değer kattığı, nerede kalıcı bir risk taşıdığı ve 2026 yılında bu soruya verilen yanıtın önümüzdeki on yılın pratiğini şekillendirme ihtimali taşıdığıdır.

## 1. Bir Araç mı, Yoksa Bir Dönüşüm mü?

Bir yapay zekâ asistanını yalnızca daha hızlı bir arama motoru olarak görmek, klinik vaka formülasyonunu bir tanı listesine indirgemekle aynı türden bir hatadır. Vaka formülasyonu, tanıdan farklı olarak, semptomun ne olduğunu sormaz. Bu semptomun neden bu hastada, neden bu zamanda ortaya çıktığını sorar. Claude Code'u bir sohbet penceresine ya da bir arama kutusuna indirgemek de sosyal bilimcinin asıl ihtiyacını gözden kaçırır. O ihtiyaç çoğu zaman bir paragrafın kelimesi kelimesine yazdırılması değildir. Bir araştırma sorusunu on kaynak boyunca tutarlı biçimde izleyebilmek, bir analiz protokolünü baştan sona belgeleyebilmek, bir makale revizyonunu on bir hakem yorumuna karşı bir izlenebilirlik matrisi olarak tutabilmektir.

Claude Code, sohbet penceresinin ötesinde durur. Dosya okuyup yazabilen, komut satırını çalıştırabilen, bir oturum boyunca ne yaptığını bağlam içinde tutan, gerektiğinde başka modellere ya da araçlara görev devreden bir ajan arayüzüdür. Bu ayrım yöntemsel olarak önemlidir. Çünkü sosyal bilimci için bu, aracın bir not defterinden bir laboratuvar asistanına doğru kayması demektir. Burada belirleyici olan sürekliliktir. Yıllarca biriken alan notları, hastane gözlemleri, mülakat dökümleri, dergi okumaları, ders izlenceleri, hakem değerlendirmeleri. Bütün bunlar artık tek bir araştırma ekosistemine bağlanabilir.

Ne var ki bu süreklilik, kendiliğinden entelektüel bir kalite üretmez. Bender ve diğerleri (2021), bir dil modelinin gerçek bir anlayış olmaksızın yalnızca istatistiksel kalıpları yeniden üretebildiği riskini, dikkatli bir okurun rahatsız olmasını sağlayacak bir kesinlikle tanımlar: stochastic parrot sorunu. Bu kılavuzun o riskten çıkardığı sonuç kendi sonucudur: sosyal bilimci, aracın nasıl kullanılacağını yöneten açık bir metodolojik çerçeve kurmalıdır. O çerçeve olmadan araç istatistiksel bir ayna olarak kalır. O çerçeveyle araç entelektüel bir ortağa dönüşür. Bu çerçevenin nasıl kurulduğu, rehberin geri kalanının konusudur.

## 2. Teknik Kimlik. Sosyal Bilimci İçin Sadece Gereken

Claude Code'un teknik kimliğini tek bir cümleyle özetlemek mümkündür. Bu, Anthropic'in büyük dil modelleri üzerine kurulu bir komut satırı uygulamasıdır: dosya okur ve yazar, kod çalıştırır, ağ üzerinden veri çeker ve yüksek seviyeli bir hedefi, her oturumun başında kullanıcının açıkça verdiği izin kapsamında, çalıştırıldığı çalışma dizini ile alt klasörleri içinde alt görevlere bölerek yürüten modüler bir ajan sistemi kurar.

Bu teknik kimliğin sosyal bilimci açısından yöntemsel sonuçları vardır.

Önce temel ayrıma bakmak gerekir: bu bir tarayıcı sekmesindeki sohbet kutusu değildir. Tarayıcıdaki bir ChatGPT ya da Claude.ai oturumu, sekme kapandığında biter. Claude Code ise proje klasörünüzün içinde çalışır: önceki bir oturumda yazılmış bir notu okuyabilir, üzerine ekleyebilir, onu başka bir dosyaya bağlayabilir. Bir not defteri ile bir çalışma arşivi arasındaki fark tam da budur. Bu sürekliliği oturumlar arasında taşıyan ek bir mekanizma da vardır: CLAUDE.md. Bu, projenizin içinde duran ve araca oturum bağımsız talimatlar taşıyan düz metin bir dosyadır. Metodolojik kurallarınız, atıf disiplininiz, alan tercihleriniz burada yazar. Bu kitapçık kavramı tanıtıyor. Tam kurulum için 001-01-0004 kitapçığına bakınız.

Bunun yanı sıra, bu bir ajan sistemidir. Buradaki ajan sözcüğü, basit bir komut yanıtlama mekanizmasından fazlasını anlatır. Ajan, kendisine verilen yüksek seviyeli bir hedefi alt görevlere bölebilen, bu alt görevleri sırayla yürüten, gerektiğinde başka bir aracı çağıran, sonuçları toplayıp geri raporlayan bir yapıdır. Bu kılavuzun kullandığı çalışma tanımı, vaka formülasyonundaki biyo-psiko-sosyal modelle (Engel, 1977) işlevsel bir benzerlik kurar. Bu benzerlik yapısal bir özdeşlik iddiası taşımaz. Bir benzetmedir. Klinik pratikte bir hastanın durumu nasıl yalnızca semptomatik bir liste olarak değil, biyolojik, psikolojik ve sosyal düzeyde eşzamanlı işleyen bir sistem olarak ele alınıyorsa, ajan da bir görevi tek bir yanıt olarak değil, birbirinin üstüne inşa edilen bir alt görev silsilesi olarak işler.

Bir de şunu göz önünde tutmak gerekir: bu, genel amaçlı bir modeldir. Sosyal bilim için özelleştirilmiş biçimde tasarlanmamıştır. Türkçe akademik literatür, klinik psikoloji metodolojisi, IRB protokolleri, COPE yayın etiği: bunların hiçbiri araçta yerleşik olarak gelmez. Tamamı sizin yönlendirmenize bağlıdır. Büyük dil modellerinin hesaplamalı sosyal bilimi dönüştürme potansiyeli üzerine yürütülen araştırma, bu yönlendirmenin niteliğinin çıktının niteliğini doğrudan belirlediğini göstermektedir (Ziems ve diğerleri, 2024).

Özetle, sosyal bilimci için Claude Code şudur: her oturumun başında verilen açık izin kapsamında belirlenen proje klasöründe çalışan, çok adımlı görevleri yürütebilen, sizin kurduğunuz çerçeve ölçüsünde derinleşen ve sizin koymadığınız çerçeveyi kendiliğinden kurmayan bir araştırma yardımcısı.

## 3. Kimler İçin, Kimler İçin Değil

Bu kitapçığın açıkça kabul ettiği gerçek şudur: Claude Code herkes için değildir.

Aracın gerçekten değer kazandığı profiller bellidir. Birden fazla araştırma projesini aynı anda yürüten bir doktora öğrencisini düşünün: elinde üç yüze yaklaşan bir Zotero kütüphanesi, birbiriyle çakışan gönderim takvimleri, eş zamanlı yürüyen iki veri toplama süreci. Ya da perşembe günkü ekip toplantısından önce yüz mülakat dökümüne bir kod defterini tutarlılıkla uygulaması gereken bir araştırma görevlisi. Daha önce bir tur ret almış bir makaledeki on bir hakem yorumuna yanıt veren bir doktora sonrası araştırmacı da aynı baskıyla yüzleşir. Öğretim üyesi ise yirmi öğrencinin tezini aynı hafta içinde kavramsal tutarlılık açısından gözden geçirmek durumundadır. IRB başvurusu için elli kaynaklı bir literatür özeti hazırlamak da bu tabloya girer. Bu profillerin ortak yanı tek bir şeydir: yüksek hacimli, tekrar eden, yapılandırılmış ve doğrulanabilir iş. Noy ve Zhang (2023), özellikle mesleki yazılı görevler üzerine kurgulanmış randomize kontrollü bir deneyde, yapay zekâ yardımının hem zaman tasarrufu hem çıktı kalitesi bakımından bu tür görevlerde anlamlı bir etki yarattığını ortaya koymuştur. Bu kılavuzun çıkardığı çıkarım şudur: o kazanımların mülakat dökümü kodlama, IRB başvurusu hazırlama ve sistematik derleme tarama gibi benzer yapıdaki diğer yüksek hacimli akademik görevlere de uzandığı düşünülebilir. Bu çıkarım kılavuzun kendi yorumudur ve o tek çalışmanın kurduğunun ötesine geçmektedir.

Araç, bilmek yerine birlikte olmayı gerektiren her yerde yetersiz kalır.

Aracın değer yitirdiği profiller de aynı açıklıkla söylenmelidir. Tek bir özgül olgu üzerine derinlemesine etnografik bir çalışma yürüten bir araştırmacı için Claude Code, alandaki gözlem hassasiyetinin yerini tutamaz. Alan notlarını düzenlemekte işe yarayabilir, ama gözleme katılma deneyiminin yerine geçemez. Aynı şey, bir klinik vaka çalışmasındaki terapist için de geçerlidir: araç, terapötik ilişkinin o somut anının yerini alamaz. Bu sınır epistemolojiktir. Aracın kavrayamadığı şey, yalnızca araç nasıl yapılandırılmış sorusunun değil, daha köklü bir sorunun cevabıdır: aracın yapısal olarak ne tür bir bilgi üretmeye muktedir olduğu sorusu. Klinik ve etnografik çalışmanın dayandığı bilme biçimi, yerleşik, ilişkisel ve indirgenemez ölçüde tikele bağlıdır. O bilme, ne kadar yapılandırılmış olursa olsun bir ajan sistemine devredilemez.

Yapay zekânın akademik yazımdaki etik sınırlarını sistemli biçimde inceleyen literatür de aracın değerinin görevin yapısına bağlı olduğunu vurgular (Hosseini ve diğerleri, 2023).

Bir sonraki kitapçık (001-01-0002), bu sohbet penceresinden iş ortağına geçişin pratik mekaniğini anlatır. Bu kitapçığın geri kalanı ise ilk temas senaryosunu, bölgesel özgüllükleri, etik katmanı ve başlangıç protokolünü ele alıyor.

## 4. İlk Temas Senaryosu

Bir doktora öğrencisi, ergenlerde sosyal medya kullanımı ile yaygın anksiyete bozukluğu arasındaki ilişki üzerine sistematik bir derleme hazırlıyor. PubMed, Semantic Scholar ve PsycINFO'dan toplanmış, Zotero kütüphanesinde duran iki yüz PDF makale var elinde. Çalışma üç ay önce başladı. Şimdi birbiri ardına gelen sorularla karşı karşıya: hangi makaleler Selvi ve Lewinsohn modelini kullanmış, hangileri boylamsal bir tasarıma sahip, hangileri Türkçe ya da Arapça örneklem kullanmış, hangileri DSM-5-TR güncellemesinden önce yayımlanmış, hangilerinde kontrol grubu yok.

Geleneksel yol bellidir. İki yüz PDF'i tek tek açmak, başlık, özet ve yöntem bölümlerini taramak, bir Excel tablosuna işlemek ve sonra bu tablo üzerinden sorgu çekmek. Kararlı bir doktora öğrencisi için bile bu, iki ila üç haftalık yoğun bir emektir.

Claude Code yaklaşımı, daha ilk gün şunu yapar: Zotero kütüphanesinin üst verisini okuyup işler, her makalenin tam metninde belirli kavramların geçtiği yerleri çıkarır ve bu çıkartıları sorgulanabilir bir yapıda biriktirir. Bunların tamamı tek bir oturumda yapılır, sonuçlar bir tabloya dökülür ve doktora öğrencisi bu tablo üzerinde elle denetimini yapar.

Bu senaryoda göz ardı edilmemesi gereken birkaç nokta var. Araç hiçbir makale için özet üretmez. Tam metni sorgular ve kavramın nerede geçtiğini raporlar. Özetleme adımı doktora öğrencisine aittir. Bu kılavuzun kurduğu iş akışında araca atıf ürettirilmez: atıflar Zotero üzerinden asıl kaynaktan gelir. Bu, kılavuzun koyduğu açık bir kuraldır. Araç atıf üretebilir. Bu iş akışı ona ürettirmez. Böylece hayali atıf riski sıfıra iner. Son olarak, araç elle denetimin yerini almaz. Yapay zekânın ürettiği özetlerin nitelikli okurları bile yanıltabildiğine dair kanıtlar (Else, 2023), bu denetim gerekliliğini hafifletmez. Tersine güçlendirir.

Bu senaryo, Claude Code'un sosyal bilim için yararlı olmasının temel formülünü içinde taşır: yapılandırılmış bir görev, doğrulanabilir bir çıktı ve son adımda insan denetimi.

Aracın asıl risk taşıdığı yer, bu formülün dışına çıkıldığı yerdir. Doktora öğrencisi araca "iki yüz makaleyi özetle ve sistematik derlemeyi yaz" gibi bir komut verirse, çıktı sözdizimsel olarak kusursuz, içerik olarak güvenilmez bir metin olur. Üretici dil modellerinin epistemik niteliğinin, felsefi açıdan titiz bir okumada, "saçmalık" üretimine kadar uzanabildiği ortaya konmuştur (Hicks ve diğerleri, 2024). Bu okumanın kavramsal zemini Frankfurt'un (2005) saçmalığı felsefi bir kategori olarak incelediği çalışmaya dayanır. Dolayısıyla belirleyici olan aracın kendisi değil, onu kullanan araştırmacının metodolojik çerçevesinin niteliğidir.

## 5. Türkiye ve Yunanistan Akademi Ortamının Özgüllükleri

Uluslararası akademik literatür, Türkiye, Yunanistan ve geniş Akdeniz havzasındaki kurumsal gerçekleri çoğu zaman görmezden gelir. Bu rehberin baştan sona koruduğu duruşlardan biri, tam da bu boşluğu açıkça doldurmaktır.

DergiPark, Türkiye'de yüzlerce akademik derginin yayımlandığı kurumsal platformdur. Ücretsiz açık erişim sunar ve Crossref entegrasyonu sayesinde DOI üretir. Claude Code, DergiPark'ta yayımlanmış bir makaleye DOI üzerinden doğrudan erişebilir. Yalnızca ULAKBIM TR Dizin'de dizinlenenler için ayrıca filtreleme yapmak ek bir yapılandırma gerektirir.

ULAKBIM TR Dizin, Türkiye'de kalite denetiminden geçmiş dergilerin listesidir. Doktora değerlendirme ve akademik yükseltme süreçleri için kritik bir referans olmanın ötesinde, bir makalenin ulusal görünürlüğünü ölçen önemli bir göstergedir. Uluslararası araçlar bu göstergeyi kendiliğinden yüzeylemez.

Yunanistan'da HEAL-Link, Yunan üniversite kütüphanelerinin ortak aboneliği üzerinden uluslararası dergilere erişim sağlar. Komotini'deki Demokritos Üniversitesi'nde bir araştırmacı bir makaleye HEAL-Link üzerinden erişebilir. Ne var ki EZproxy yapılandırması her kampüste aynı değildir. Araştırmacı, Claude Code'un PubMed MCP'si üzerinden bir PubMed taraması yapabilir, ama tam metne ulaşması için yerel kütüphane proxy'sinin doğru ayarlanmış olması gerekir.

Bu altyapı ayrıntıları ilk bakışta teknik görünür. Oysa akademik üretim üzerindeki etkileri yöntemseldir. Bir araştırmacı, hangi kaynaklara erişebildiğini bilmeden bir literatür haritası kuramaz. Yapay zekâ aracı bu engelleri kendiliğinden çözmez. Ama nasıl yapılandırılacağına dair tutarlı bir rehber, araştırmacının altyapıyla harcadığı zamanı çarpıcı biçimde azaltır. Bu rehberin 002 kategorisi (Akademik Erişim) tümüyle bu konuya ayrılmıştır.

## 6. Etik Katman. Birinci Düzey Uyarılar

Yapay zekâ destekli akademik üretimde etik, sonradan eklenecek bir bölüm değildir. En baştan kurulması gereken bir çerçevedir. Bu çerçeve neyi yasaklar, neyi zorunlu kılar, neyi izler?

Atıf bütünlüğü bunların en önünde gelir. Claude Code'a "şu konuda kaynak öner" demek, her zaman hayali bir atıf üretme riskini taşır. Bu rehberin temel kuralı açıktır: araç tarafından önerilen hiçbir atıf, bağımsız bir indekste (Crossref, PubMed, Semantic Scholar, ULAKBIM TR Dizin, DergiPark) doğrulanmadan referans listesine giremez.

Gizlilik konusunda uzlaşı tektir, tartışmaya kapalıdır. Klinik veri, mülakat dökümü ya da anonimleştirilmemiş saha notu hiçbir koşulda araçla paylaşılmamalıdır. Araştırma için beş öncelik üzerine yayımlanan uluslararası uzlaşı (van Dis ve diğerleri, 2023), veri minimizasyonunu bu öncelikler arasında sayar. Buradan çıkan kural nettir: klinik veri, kurumsal etik kurulun onayladığı biçimde anonimleştirilmeden araçla paylaşılmaz.

Yazarlık ve beyan yükümlülüğü farklı bir düzlemde durur. COPE, ICMJE ve WAME arasında bir uzlaşı konumu oluşmuştur: yapay zekâ yazar olamaz. Yapay zekâ sistemlerinin makalelerde listelenmesi tartışması, ilgili kuruluşların yayımladığı rehberlerde ele alınmıştır. Kesin normlar ise alan ilerledikçe evrilmeye devam etmektedir. Yerleşmiş olan şu: yapay zekâ yardımının yöntem bölümünde ya da teşekkür kısmında açıkça beyan edilmesi zorunludur (Stokel-Walker, 2023). Oysa bir beyan tek başına yeterli değildir. Yapay zekânın metinde nasıl ve hangi biçimlerde kullanıldığının okura açıkça anlatılması gerekir. Bu rehberin kuralı, her kitapçığın başında yapay zekâ araçlarının da okuyabildiği, onlara işin doğru yapılmasına yön veren yapılandırılmış bir beyan bloğu taşımasıdır.

Dil modellerinin toplumsal yansımaları da bu çerçevenin dışında kalamaz. Büyük dil modellerinin riskleri taksonomik olarak haritalanmıştır (Weidinger ve diğerleri, 2022). Sosyal bilimci için en kritik risk kategorileri yanlış bilgi üretimi, dezenformasyonun yayılması, ölçek etkileri ve kültürel yanlılıktır. Türkçe içerikteki yanlılık, İngilizce içerikten farklı biçimlerde ve kimi boyutlarda daha ağır biçimde belirebilir. Çünkü çok dilli modeller, diller arasında ne dengeli ne de eşit özenle derlenmiş korpuslar üzerinde eğitilmektedir (Xu ve diğerleri, 2025). Bu nedenle Türkçe çıktıların elle denetimi, İngilizce çıktıların denetiminden daha titiz olmalıdır.

Son olarak, yapısal eşitsizlik meselesi gelir. Büyük dil modellerinin yükseköğretimde yarattığı dönüşümün, kaynak eşitsizliğini hafifletmek yerine derinleştirme ihtimali akademik literatürde belgelenmiştir (Milano ve diğerleri, 2023). Bu rehber o eşitsizliği kabul ederek geçiştirmez. Ona açıkça karşı çalışmak için kurulmuştur.

## 7. Pratik Başlangıç Protokolü

İlk haftanın yönünü belirleyen zihinsel hazırlık yöntemsel bir zeminde şekillenir. Teknik kurulum henüz ikinci plandadır.

Başlamadan önce görev türünü netleştirmek gerekir. Aracı hangi akademik üretim sürecinde kullanacaksınız? Literatür taraması mı, sistematik derleme mi, makale revizyonu mu, ders tasarımı mı, IRB başvurusu mu, yoksa hakem yanıt mektubu mu? Her görev türü farklı bir yapılandırma ister. Aracı her işe yarayan genel bir yardımcı gibi kullanmak, niteliği baştan zayıf bir başlangıçtır.

Buna paralel olarak, biriken akademik notlar için kalıcı bir klasör yapısı, bir çalışma arşivi kurulmalıdır. Markdown dosyaları, ön veri bloğu (frontmatter), dosya ağacı, içerik haritaları. Bu rehberin 004 kategorisi tümüyle bu konuya ayrılmıştır. İlk hafta arşivi eksiksiz kurmak gerekmez. Mevcut araştırma, mevcut yazım, mevcut okuma listesi için üç klasör başlangıç olarak yeterlidir.

En çabuk yerleştirilebilecek olan beyan alışkanlığıdır. İlk haftadan başlayarak araç yardımıyla yazılan her metin, ne kadar yardım alındığını açıkça not eden bir alt satır taşımalıdır. Akademik üretim, gün gelir bir hakemin, bir editörün ya da bir öğrencinin önüne çıkar. O an geldiğinde beyan belgesi çoktan orada olmalıdır.

## 8. Sonuç ve Sonraki Adım

Claude Code, sosyal bilimci için bir not defteri ile bir laboratuvar asistanı arasındaki açıklığı kapatan bir araçtır. Ama değeri kullanıcının metodolojik çerçevesiyle orantılıdır. O çerçeve hayali atıfı yasaklar, klinik veriyi korur, beyanı en baştan kurar ve görev türünü netleştirir.

Bir sonraki kitapçık, sohbet penceresinden iş ortağına geçişin pratik mekaniğini anlatıyor: hangi komutlar, hangi izinler, hangi oturum yapısı, hangi başarısızlık biçimleri. 001-01-0002 kitapçığı (Aracın Ötesine Geçiş) tam bu noktadan devam eder.

Bundan sonraki kitapçık dizisinin tamamı, bu ilk kitapçıkta kurulan yapısal duruşun üzerine inşa edilecek. Her kitapçık kendi konusunda derinleşirken bu ilk çerçeveyi varsayar.

---

## Kaynakça

Atıflar APA 7 biçimindedir. Her DOI 2026-05-19 tarihinde Crossref üzerinden bağımsız olarak doğrulanmıştır. Xu ve diğerleri (2025) DOI'si 2026-06-04 tarihinde doğrulanmıştır.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610-623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Else, H. (2023). Abstracts written by ChatGPT fool scientists. *Nature*, 613(7944), 423. https://doi.org/10.1038/d41586-023-00056-7

Engel, G. L. (1977). The need for a new medical model: A challenge for biomedicine. *Science*, 196(4286), 129-136. https://doi.org/10.1126/science.847460

Frankfurt, H. G. (2005). *On bullshit*. Princeton University Press. ISBN 978-0-691-12294-6

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, 26(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Hosseini, M., Rasmussen, L. M., & Resnik, D. B. (2023). Using AI to write scholarly publications. *Accountability in Research*, 31(7), 715–723. https://doi.org/10.1080/08989621.2023.2168535

Milano, S., McGrane, J. A., & Leonelli, S. (2023). Large language models challenge the future of higher education. *Nature Machine Intelligence*, 5(4), 333-334. https://doi.org/10.1038/s42256-023-00644-2

Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. *Science*, 381(6654), 187-192. https://doi.org/10.1126/science.adh2586

Stokel-Walker, C. (2023). ChatGPT listed as author on research papers: many scientists disapprove. *Nature*, 613(7945), 620-621. https://doi.org/10.1038/d41586-023-00107-z

van Dis, E. A. M., Bollen, J., Zuidema, W., van Rooij, R., & Bockting, C. L. (2023). ChatGPT: Five priorities for research. *Nature*, 614(7947), 224-226. https://doi.org/10.1038/d41586-023-00288-7

Weidinger, L., Uesato, J., Rauh, M., Griffin, C., Huang, P.-S., Mellor, J., Glaese, A., Cheng, M., Balle, B., Kasirzadeh, A., Biles, C., Brown, S., Kenton, Z., Hawkins, W., Stepleton, T., Birhane, A., Hendricks, L. A., Rimell, L., Isaac, W., ... Gabriel, I. (2022). Taxonomy of risks posed by language models. In *2022 ACM Conference on Fairness, Accountability, and Transparency* (pp. 214-229). Association for Computing Machinery. https://doi.org/10.1145/3531146.3533088

Xu, Y., Hu, L., Zhao, J., Qiu, Z., Xu, K., Ye, Y., & Gu, H. (2025). A survey on multilingual large language models: Corpora, alignment, and bias. *Frontiers of Computer Science*, 19(11), Article 1911362. https://doi.org/10.1007/s11704-024-40579-4

Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2024). Can large language models transform computational social science? *Computational Linguistics*, 50(1), 237-291. https://doi.org/10.1162/coli_a_00502

---

**Kitapçık kimliği.** `001-01-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-20
**Sözcük sayısı (yaklaşık).** 2301 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 13
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** Yok (ilk kitapçık)
**Sonraki kitapçık.** [`001-01-0002`](../001-01-0002/tr.md). Aracın Ötesine Geçiş: Sohbet Penceresinden İş Ortağına
