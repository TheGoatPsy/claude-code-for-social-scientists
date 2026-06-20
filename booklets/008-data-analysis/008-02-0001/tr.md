---
title_en: "Statistical Test Selection with AI Consultation Discipline"
title_tr: "Yapay Zekâ Danışma Disipliniyle İstatistiksel Test Seçimi"
booklet_id: "008-02-0001"
category: "008-data-analysis"
language: "tr"
version: "0.1.0"
date_published: "2026-05-29"
date_last_revised: "2026-06-20"
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
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-20"
verified_citations_count: 11
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
translation_notes: "Re-authored from the Turkish version (tr.md) against the same outline and the same verified citation set. The argument and the bibliographic set are identical across both languages. Phrasing is native to each."
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Yapay Zekâ Danışma Disipliniyle İstatistiksel Test Seçimi

Bu kategorinin önceki kitapçığı, ajan tabanlı nicel analizin yeniden üretilebilirlik omurgasını kurdu: spesifikasyon günlüğü, sabit tohum, temiz ortam (kitapçık 008-01-0001). Bu kitapçık, o analizin çıkarımsal kalbine iner. Hangi testin çalıştırılacağı kararına. Anthropic'in 2026 taramasına göre ankete katılan sosyal bilimciler, kodlama ajanını en çok nicel veri analizinde kullandıklarını, bununla birlikte yapay zekânın seçici raporlamayı kötüleştirmesinden kaygı duyduklarını belirtmiştir (Lyttelton ve diğerleri, 2026: bu raporun yayıncısı Anthropic, aynı zamanda bu kitapçığın öğrettiği ürün olan Claude Code'un üreticisidir, gri literatür, hakemli değil). Test seçimi, tam da bu kaygının ya gerçekleştiği ya da disipline edildiği noktadır. Bir ajan her testi anında önerebildiğinde, hangi testi seçtiğiniz artık yavaş bir düşünme sürecinin değil, bir istem uzaklığındaki ani bir kararın ürünüdür. Bu kitapçık, o danışmayı dürüst ve savunulabilir tutmanın disiplinini ele alır.

## 1. Test Seçimi Neden Ajan Tabanlı Çağda Kritik Bir Karardır

Bir istatistiksel test, bir çıkarım taahhüdüdür. Hangi testi çalıştırdığınız, veriden ne iddia edebileceğinizi belirler. Ajan bu kararı tek bir hamlede sıkıştırır: bir test önerir, gerekçesini açıklar, çalıştırır ve sonucu yorumlar. Araştırmacı bir önceki adımın çıktısını henüz okumadan. Lyttelton ve diğerlerinin (2026) taraması, ankete katılanların kullanımının tam bu yönde, otonom analize doğru yoğunlaştığını kayıt altına almaktadır.

Test seçimi eskiden yavaş bir süreçti. Araştırmacı veri yapısı üzerinde uzun uzun düşünür, koridorun karşısındaki istatistik danışmanına uğrar, üzerine uyurdu. İlk regresyon modelini kurmaya çalışan bir doktora öğrencisi, bir yöntembilim ders kitabıyla öğleden sonrasını geçirdikten sonra modeline karar verirdi. Bu yavaşlık, istemeden de olsa bir koruma işlevi görürdü: kararın sürtünmesi, anlamıyla yüzleşmeyi zorunlu kılıyordu. Oysa ajan, her an ulaşılabilir ve hiçbir zaman "yarın arayın" demeyen bir danışmandır.

Hız değişti. Sorumluluk değişmedi.

Danışmanın sürekli kapıda beklemiş olması, araştırmacıdan kararı gerekçelendirme yükünü kaldırmaz. Bir testi seçmek, o testin varsaydığı dünyayı kabul etmektir: gerektirdiği ölçüm düzeyini, önkabul ettiği dağılımsal özellikleri, veri olarak aldığı örneklem yapısını. Bu kabuller epistemik bir ağırlık taşır. Ne iddia edilebileceğini ve ne iddia edilemeyeceğini belirler. Yöntem bölümünde, tez savunmasında ya da hakem yanıt mektubunda bu kabulün altına imzasını koyan araştırmacıdır, ajan değil.

## 2. Araştırmacı Serbestlik Dereceleri ve Test Seçiminin Esnekliği

Araştırmacı her veri setiyle karşılaştığında seçimler yapar. Bu seçimler, yöntemsel literatürün araştırmacı serbestlik dereceleri dediği şeyi oluşturur. Simmons ve diğerleri (2011), bu serbestlik derecelerinin açıkça raporlanmadığında hemen her sonucu istatistiksel olarak anlamlı gösterebileceğini deneysel olarak ortaya koymuştur. Gösterim sert ve nettir: aynı veri seti, farklı ama eşit ölçüde savunulabilir seçimlerle işlendiğinde birbirine zıt sonuçlar verir. Yayımlanan sürüm ise yalnızca işe yarayanı gösterir. Test seçimi, bu serbestlik derecelerinin en büyüklerinden biridir. Aynı hipotez, bir parametrik testle anlamsız, eşit ölçüde savunulabilir bir parametrik olmayan alternatifle anlamlı çıkabilir.

Wicherts ve diğerleri (2016), psikolojik çalışmaların planlanması, yürütülmesi, analizi ve raporlanmasına yayılmış serbestlik derecelerini kapsamlı bir kontrol listesinde toplamış ve her serbestlik derecesinin p-değeri avcılığına nasıl bir yol açtığını göstermiştir. Bu listenin değeri kararları yasaklamasında değildir. Meşru analitik kararlar esneklik gerektirir. Listenin katkısı tam da bu esnekliği önceden görünür kılmasında yatar. Bir ajana hangi testi kullanmalıyım diye sorulduğunda ajan birkaç seçeneği aynı anda sunabilir. En cazip seçenek ise çoğu zaman anlamlılık verendir. Ajana danışmadan önce karar uzayını sayıp dökmemiş bir araştırmacı, ajanın çıktısının kararı yönlendirebileceği bir konumdadır, hem yönlendirmeyi bir seçim olarak kaydetmeden. Wicherts ve diğerlerinin kontrol listesi bu cazibeyi dizginleyen disiplindir. Serbestlik dereceleri, ajana danışmadan önce adlandırılır, danışmadan sonra değil.

## 3. Çatallanan Yolların Bahçesi, Test Seçiminde

Gelman ve Loken (2014), veriye bağlı analitik seçimlerin görünmez bir çoklu karşılaştırmalar ağacı yarattığı durumu çatallanan yolların bahçesi olarak adlandırır. Bu isim önemli bir şeyi yakalar: her çatal, alındığı anda makul görünür. Oysa kümülatif etki, raporlanan p-değerinin artık dürüst bir olasılık sayılmamasıdır.

Test seçimi, bu bahçenin en sık yürünen patikasıdır. Veriye bakmak, dağılımın normallikten saptığını fark etmek, parametrik olmayan bir teste geçmek ve o testin anlamlı çıktığını görmek: niyet bütünüyle dürüst olsa bile bu veriye bağlı bir karardır. Araştırmacı aldatmak için yola çıkmamıştır. Ama karar veriden sonra verildiği için, raporlanan test sonucu artık ileriye dönük seçilmiş bir testin taşıyacağı anlamı taşımaz.

Bu kitapçığın çatallanan yollar sorununa ilişkin okuması şunu ortaya koyar: bir ajan bu yapıyı ortadan kaldırmaz, aksine hızlandırır ve gizler. Araştırmacının saatler harcayacağı test alternatiflerini ajan saniyeler içinde dener ve en temiz görüneni sunabilir. Çatallar kaybolmaz. Çoğalır ve görüş alanından silinir. Bu nedenle test seçimindeki çatallanan yollar sorunu, ajan tabanlı bir akışta daha az dikkat değil, daha çok dikkat ister.

## 4. Çok-Evrenli Analiz: Ajan Tabanlı Hız Erdeme Dönüşünce

Çatallanan yollar sorununa en güçlü yanıt, seçilen yolu gizlemek değil, her yolu aynı anda açığa çıkarmaktır. Steegen ve diğerleri (2016), savunulabilir tüm analitik seçimlerin ürettiği sonuç uzayını sistematik biçimde hesaplayan çok-evrenli analizi önermiştir. Tek bir testten tek bir sonuç yerine araştırmacı, makul spesifikasyonların tamamının verdiği sonuç dağılımını raporlar. Simonsohn ve diğerleri (2020) bunu spesifikasyon eğrisi analizine dönüştürmüştür: her spesifikasyonu ürettiği sonucun yanında gösteren, eğri boyunca elde edilen sonuçların şans beklentisinden farklılaşıp farklılaşmadığını sınayan grafiksel ve çıkarımsal bir teknik. Silberzahn ve diğerleri (2018) ampirik garantiyi sunmuştur: aynı veri setini bağımsız olarak analiz eden yirmi dokuz ekip, farklı analitik seçimler yoluyla belirgin biçimde farklı sonuçlara ulaşmıştır. Ortaya çıkan tablo açıktır: analitik kararlar önemsiz bir ayrıntı değil, bulgunun kendisini biçimlendiren bir güçtür. O güç gizlenmek yerine görünür kılınmalıdır.

İşte tam burada ajan tabanlı hız bir yükümlülükten bir araca dönüşür. Çok-evrenli analiz elle yapıldığında pahalıydı. Onlarca spesifikasyonu tek tek kurmak ve çalıştırmak günler alırdı. Ajan, şikâyet etmeden her makul testi denemeye zaten yatkın olduğundan bu analizi uygulanabilir kılar. Ajanın her şeyi denemesini gizli bir balık avına bırakmak yerine, araştırmacı onu açıkça raporlanan bir spesifikasyon eğrisine yönlendirir. Bunu işlevsel kılan koşul önceden sabittir: savunulabilir spesifikasyonların tam kümesi, herhangi bir sonuca bakılmadan tanımlanmalıdır. Koşul sağlandığında, ajan hız yerine şeffaflık için çalışır.

## 5. Önceden Belirtimi Keşiften Ayırmak

Çok-evrenli raporlama bile doğrulayıcı iddianın veriye dokunulmadan önce sabitlenmesini gerektirir. Nosek ve diğerleri (2018), ön kaydın serbestlik derecelerini tam da doğrulayıcı ile keşfedici analizi birbirinden ayırarak kontrol altına aldığını savunmuştur. Munafò ve diğerleri (2017), yeniden üretilebilir bilim manifestolarında bu ayrımı alanın sağlamlığının yapısal bir temeli olarak ele almıştır. Ajan tabanlı test seçiminde bunun anlamı nettir. Birincil testi ve varsayımlarını ajana danışmadan önce yazın. Ajan keşif sırasında her alternatifi önerdiğinde bu alternatifler açık bir keşfedici etiket taşır. Bunlardan hiçbiri doğrulayıcı sonucun yerine geçmez.

Bu, önceki kitapçığın spesifikasyon günlüğünün test seçimi kararına uygulanmış hâlidir (kitapçık 008-01-0001). Danışma kabul görür. Taahhüt önceden verilmiştir. Ajan oturum ortasında bir test önerdiğinde araştırmacı tek bir soru sorar: bu test, planlama aşamasında mı seçildi, yoksa veriye bakıldıktan sonra mı ortaya çıktı? Bu soru yanıtıyla birlikte günlüğe işlendiğinde, ajanın ürettiği zenginlik bir çıkarım tehdidine değil, belgelenmiş bir duyarlılık analizine dönüşür.

## 6. Bulan Notlayan Olamaz, Testin Varsayımlarına Uygulanmış

Bu rehberin tekrar eden ilkesi şudur: bir bulgu üreten araç, o bulguyu onaylayan otorite olamaz. İstatistiksel test seçiminde bu ilke, özgül ve yaygın bir başarısızlık biçimini keser: bir testi çalıştırıp gerçekten tanıları denetlemeden varsayımlar karşılandı diyen ajan.

Bir doktora öğrencisi, iki grubun psikolojik bir çıktı üzerinde farklılaşıp farklılaşmadığını sınamak için ajandan bağımsız örneklem t-testi ile Mann-Whitney U arasında seçim yapmasını isteyebilir. Ajan t-testini önerir, çıktısını üretir ve bir cümle ekler: "Normallik varsayımı doğrulandı." Çıktı eksiksiz görünür. Oysa ajan bu cümleyi üretmiş olabilir çünkü test seçimiyle ilgili cümlelerin peşinden varsayımların doğrulandığına ilişkin cümleler gelmesi, eğitim verilerindeki istatistiksel bir örüntüdür. Shapiro-Wilk istatistiğini incelediği, Q-Q grafiklerini gözden geçirdiği ya da söz konusu dağılımda merkezi limit teoreminin sağlamlığını örneklem büyüklüğüne karşı denetlediği için değil.

Bu kırılganlığın kökü, modelin yapısında yatar. Dil modeli, anlayışa benzer bir şey olmaksızın istatistiksel örüntüler üretir: bu, stokastik papağan sorunudur (Bender ve diğerleri, 2021). Üretilen metnin epistemik düzeyde bir sorunu olabilir: doğru görünmek ile gerçekten doğru olmak arasındaki farkı kendiliğinden gözetmez (Hicks ve diğerleri, 2024). Akıcılık, doğruluk değildir. Akıcı bir gerekçe, doğrulanmış bir gerekçe değildir. İkisi yüzey biçiminde özdeş, epistemik açıdan bütünüyle farklı olabilir.

Bu nedenle ajanın test önerisi bir hipotezdir ve araştırmacı tarafından bağımsız olarak denetlenir. Araştırmacı, varsayım tanılarını ham çıktıya karşı bağımsız olarak okur: test istatistiğinin kendisini, normallik denetiminin p-değerini, artık grafiğini. Ajanın varsayımların karşılanıp karşılanmadığına ilişkin cümlesi not edilir ve araştırmacı bağımsız bir yargıya ulaşırken bir kenara bırakılır.

## 7. Danışmayı Al, Kararı Devretme

Ajan tabanlı analizde devredilebilen ile devredilemeyen arasındaki çizgi, test seçiminde özellikle keskindir. Devredilebilen, danışmanın kendisidir: ajan aday testleri sıralar, aralarındaki ödünleşimleri açıklar, her birini hesaplar, varsayımların sınırda kaldığı yerleri işaret eder. Devredilemeyen, karardır.

Araştırma sorusuna hangi test yanıt verir? Hangi varsayım, alanın kuramı ve verinin bağlamı göz önüne alındığında savunulabilirdir? Sınırda bir normallik ihlalinin önem taşıyıp taşımadığı, örneklem büyüklüğüne, araştırma geleneğine, öne sürülen iddiaya ve kitlenin beklentilerine bağlıdır. Araştırmacı bunları açıkça sağlamadıkça ajanın hiçbirinden haberi yoktur. Bu yargı araştırmacıya aittir. Ajan, bilgili ama hesap verme sorumluluğu olmayan bir danışman gibi ele alınır: tavsiyesini almak meşrudur, ancak araştırmacının o tavsiyeyi bağımsız olarak savunabilmesi gerekir. Talimat dosyası analitik yordamı dışsallaştırır. Yargı araştırmacıda kalır (kitapçık 001-01-0004). Ajan testi hesaplar. Araştırmacı testi seçer ve yazılı ortamda sonucun arkasında durur.

## 8. Pratikte: Bir Test Seçimi Danışma Protokolü

Bu disiplin, oturum başlamadan önce spesifikasyon günlüğüne işlenebilecek somut ve uygulanabilir bir protokole iner.

Birincil testi ve varsayımlarını, ajana danışmadan önce günlüğe işleyin. Bu tek adım, sonraki her şeyin dürüstlüğünü belirler: ilerleyen aşamada ajanın ürettiği her alternatif, sonradan keşfedilmiş bir seçenek olarak işaretlenebilir. Ajandan ardından savunulabilir alternatiflerin tamamını, makul spesifikasyonların açıkça tanımlanmış çok-evreni olarak sıralamasını isteyin. Herhangi bir sonuca bakmadan önce bu kümeyi kapatın.

Tanımlanan spesifikasyonlar üzerinde çok-evrenli ya da spesifikasyon eğrisi analizini çalıştırın ve sonuçların dağılımını raporlayın. Varsayım tanıları ajanın düz metin özetinden değil, ham sayısal çıktıdan okunur: istatistiğin kendisi konuşur. Günlükte doğrulayıcı ile keşfedici çizgi ayrık tutulur. Önceden belirtilmiş birincil test doğrulayıcı iddiayı taşır, oturum sırasında ortaya çıkan ek testler keşfedici etiket alır. Ajanın danışmanlık rolünü makalenin yöntem bölümünde ya da yapay zekâ katkı beyanında açıklayın: hangi analizde, hangi biçimde ve ne ölçüde yapay zekâya başvurulduğu bu beyan içinde belirtilmelidir.

Bu protokol, Wicherts ve diğerlerinin (2016) serbestlik dereceleri kontrol listesini, çok-evrenli ve spesifikasyon eğrisi raporlamasını ve ön kayıt zihniyetini tek bir ajan tabanlı danışma akışında birleştirir. Protokol olmadan ajanın kolaylığı seçici raporlamayı doğrudan besler: işe yarayan testi sunar, araştırmacı kabul eder, alternatiflerin var olduğunu hiçbir kayıt göstermez. Protokolle birlikte danışma, savunulabilir bir çıkarımsal zincirin parçası olur. Ajan test uzayını hızla tarar. Protokol bu hızı şeffaflığın araçlarından birine dönüştürür. Araştırmacı önceden belirlemediği bir sonucun peşinde değil, savunulabilir bir çıkarımın izinde çalışır.

## 9. Bir Sonraki Kitapçık

Bu kitapçık, test seçimini bir danışma disiplinine bağladı. Protokolün yanıtsız bıraktığı soru, bu rehberin tamamında akan soruyla aynıdır: çıkarımın epistemik sorumluluğunu kim taşır? Ajan önerir. Araştırmacı karar verir. Günlük kayıt altına alır. Makale açıklar.

Ajanın analitik rolünün bu dürüst beyanı, bir sonraki kitapçığın doğrudan ele aldığı daha geniş bir etik çerçeveye oturur. Test seçimi aşamasında verilen kararlar, nicel bir çalışmadaki en sonuç doğurucu kararlar arasındadır. Yalnızca istatistik sosyal bilimin kalbi olduğu için değil, test seçiminin ne iddia edilebileceğini belirlediği, iddianın ise literatürde birikenin ne olduğunu şekillendirdiği için. Disiplin olmaksızın bu seçimi hızlandıran bir ajan, gürültünün birikmesini hızlandırır. Burada tanımlanan disiplin içinde çalışan bir ajan ise savunulabilir kanıtın birikmesini hızlandırır. Bu ayrımın bir etik yükümlülüğe yükselip yükselmediği, kitapçık 009-01-0001'in bu noktadan itibaren ele aldığı sorudur.

---

## Kaynakça

Atıflar APA 7 biçimindedir. Her DOI ve tanımlayıcı, Crossref, doi.org veya yayıncı sayfası üzerinden bağımsız olarak doğrulanmıştır. Doğrulama tarihleri: özgün atıflar 2026-05-29 tarihinde, Simonsohn ve diğerleri (2020) ile Munafò ve diğerleri (2017) 2026-06-04 tarihinde. Lyttelton ve diğerleri (2026), Anthropic'in yayımladığı bir araştırma taraması raporu olup gri literatür kategorisindedir, hakemli bir yayın değildir. Yayıncı URL'si üzerinden 2026-05-29 tarihinde doğrulanmıştır. Anthropic aynı zamanda bu kitapçığın öğrettiği ürün olan Claude Code'un üreticisidir. Bu durum bir satıcı çıkar çatışması oluşturmaktadır.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)* (pp. 610-623). Association for Computing Machinery. https://doi.org/10.1145/3442188.3445922

Gelman, A., & Loken, E. (2014). The statistical crisis in science. *American Scientist*, 102(6), 460. https://doi.org/10.1511/2014.111.460

Hicks, M. T., Humphries, J., & Slater, J. (2024). ChatGPT is bullshit. *Ethics and Information Technology*, 26(2), Article 38. https://doi.org/10.1007/s10676-024-09775-5

Lyttelton, T., Massenkoff, M., & Wilmers, N. (2026). *Coding agents in the social sciences*. Anthropic. https://www.anthropic.com/research/coding-agents-social-sciences

Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J., & Ioannidis, J. P. A. (2017). A manifesto for reproducible science. *Nature Human Behaviour*, 1(1), Article 0021. https://doi.org/10.1038/s41562-016-0021

Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, 115(11), 2600-2606. https://doi.org/10.1073/pnas.1708274114

Silberzahn, R., Uhlmann, E. L., Martin, D. P., Anselmi, P., Aust, F., Awtrey, E., Bahník, Š., Bai, F., Bannard, C., Bonnier, E., Carlsson, R., Cheung, F., Christensen, G., Clay, R., Craig, M. A., Dalla Rosa, A., Dam, L., Evans, M. H., Flores Cervantes, I., ... Nosek, B. A. (2018). Many analysts, one data set: Making transparent how variations in analytic choices affect results. *Advances in Methods and Practices in Psychological Science*, 1(3), 337-356. https://doi.org/10.1177/2515245917747646

Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychological Science*, 22(11), 1359-1366. https://doi.org/10.1177/0956797611417632

Simonsohn, U., Simmons, J. P., & Nelson, L. D. (2020). Specification curve analysis. *Nature Human Behaviour*, 4(11), 1208-1214. https://doi.org/10.1038/s41562-020-0912-z

Steegen, S., Tuerlinckx, F., Gelman, A., & Vanpaemel, W. (2016). Increasing transparency through a multiverse analysis. *Perspectives on Psychological Science*, 11(5), 702-712. https://doi.org/10.1177/1745691616658637

Wicherts, J. M., Veldkamp, C. L. S., Augusteijn, H. E. M., Bakker, M., van Aert, R. C. M., & van Assen, M. A. L. M. (2016). Degrees of freedom in planning, running, analyzing, and reporting psychological studies: A checklist to avoid p-hacking. *Frontiers in Psychology*, 7, Article 1832. https://doi.org/10.3389/fpsyg.2016.01832

---

**Kitapçık kimliği.** `008-02-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-20
**Sözcük sayısı (yaklaşık).** 1797 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 11
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`008-01-0001`](../008-01-0001/tr.md). Yeniden Üretilebilir Nicel İş Akışları
**Sonraki kitapçık.** [`009-01-0001`](../../009-ethics-irb/009-01-0001/tr.md). Yapay Zekâ Destekli Araştırmada Etik, Prensipten Davranışa
