---
title_en: "Research Protocol and Preregistration, Deciding Before Analysis"
title_tr: "Araştırma Protokolü ve Ön Kayıt, Analizden Önce Karar Vermek"
booklet_id: "008-05-0001"
category: "008-data-analysis"
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
    role: "drafting, verification, citation lookup, bilingual authoring"
    interaction_mode: "interactive console"
ai_contribution_level: "substantial-drafting"
human_review: "complete"
human_review_date: "2026-06-21"
verified_citations_count: 10
fabricated_citations_count: 0
disclosure_standard: "COPE 2023 + WAME 2023 + ICMJE 2024 + STM 2025 + EU AI Act 2024/1689 Art. 50 + ENAI"
license:
  - "CC-BY-NC-SA-4.0 (prose)"
status: "release"
---

# Araştırma Protokolü ve Ön Kayıt, Analizden Önce Karar Vermek

Analizden önce karar vermek, sosyal bilim araştırmasında en çok ertelenen disiplindir. Hipotezi veri gelmeden önce kaydetmek, analiz planını model çalıştırılmadan önce yazmak, birincil sonucu en ilginç çıkan değişken değil, en başta belirlenen değişken olarak raporlamak. Bu adımlar araştırmacının özgürlüğünü kısıtlamaz. Aksine, veriye baktıktan sonra aldığı kararları baştan almış gibi gösterme riskini görünür kılar. Ajan tabanlı analiz bu riski büyütür: bir model saniyeler içinde onlarca belirtim deneyebilir, en temiz görünen sonucu öne çıkarabilir ve hiçbir kararı kayıt dışı bırakmadan analitik serbestlik derecelerini genişletebilir. Bu kitapçık, araştırma protokolü ve ön kayıt disiplinini ajan tabanlı iş akışına taşır. Yerel bir protokol dosyasından açık ön kayıt platformlarına, hipotez-keşif ayrımından sapma günlüğüne, analiz planından yöntem bölümüne aktarıma kadar uzanan bu çerçeve, analizden önce düşünmeyi somut bir iş akışına bağlar.

## 1. Protokol ile yöntem bölümü arasındaki fark

Yöntem bölümü çalışma bittikten sonra yazılır. Geçmişi anlatır. Protokol ise çalışma başlamadan önce yazılır. Taahhüdü kaydeder. Bu ayrım, akademik yazımda sıklıkla gözden kaçar. Çünkü son hâliyle sunulan bir yöntem bölümü, o yöntemin ne zaman kurulduğunu ele vermez.

Ajan tabanlı analizde bu mesafe daha kritik bir anlam kazanır. Model önerileri üretir, kod yazar, alternatif belirtimler dener. Araştırmacı bu önerileri kabul ettiğinde, hangi kararın analizden önce hangi kararın veriye bakıldıktan sonra verildiği belirsizleşir. Protokol, tam da bu belirsizliği ortadan kaldırmak için vardır. Neyin planlandığını, ne zaman planlandığını ve kimin kararlaştırdığını kaydeden belgedir. Wagenmakers ve diğerleri (2012), doğrulayıcı araştırmanın güvenilirliğinin ancak bu tür bir kayıtla sağlanabileceğini ve hipotez ile analiz planının veriden önce sabitlenmesinin bilimsel çıkarımın geçerliliği için zorunlu olduğunu savunur. Münferit bir protokol dosyası, resmi ön kayıt platformlarına açılmadan önce bile bu işlevi yerine getirebilir.

Yöntem bölümü protokolün ardından gelir, onun yerine geçmez. Protokol neyin planlandığını gösterir. Yöntem bölümü neyin yapıldığını anlatır. İkisi örtüşüyorsa bu güçtür. Örtüşmediğinde sapmalar kaydedilmeli ve gerekçelendirilmelidir.

## 2. Hipotez ve keşif sorusu arasındaki sınır

Hipotez doğrulayıcı bir iddiadır: veriye bakmadan önce öngörülen, belirli bir yönde test edilebilir bir ilişki ya da etki. Keşif sorusu ise alanı anlamaya yönelik açık bir arayıştır. Hangi örüntülerin çıkacağı önceden belirlenmemiştir. İkisi de meşrudur, ikisi de bilimsel değer taşır. Ama birbirinin yerine geçemez ve aynı analizde aynı statüde sunamaz.

Kerr (1998), bu sınırın silinmesini HARKing kavramıyla adlandırır: Hypothesizing After the Results are Known, yani sonuçlar bilinip keşfedildikten sonra hipotez gibi sunmak. HARKing, kasıtlı sahtekârlıkla başlamaz. Veriye baktıktan sonra ortaya çıkan örüntünün baştan öngörülmüş gibi sunulması, araştırmacılar tarafından çoğu zaman farkında olmadan yapılır. Ajan tabanlı analizde risk daha da katmanlıdır: model, araştırmacının henüz sormadığı soruların cevaplarını sunabilir. O cevaplar dikkat çekici görünebilir. Bunları baştan planlanmış hipotez gibi çerçevelemek kolaydır.

Güvenli bir iş akışı bu iki kategoriyi yazılı biçimde ayırır. Hangi soruların doğrulayıcı, hangilerinin keşfedici olduğu protokolde işaretlenir. Ajan çalışırken keşfettiği desenler doğrulayıcı analizin yerini almaz. Keşfedici ek analiz olarak etiketlenir ve ayrı raporlanır. Open Science Collaboration (2015), psikolojide yüz çalışmanın yeniden yürütüldüğü kapsamlı replikasyon projesinde, sonuçların önemli bir bölümünün yeniden üretilememesinin ardında bu hipotez-keşif sınırının sistematik olarak bulanıklaştırılmasının yattığını gösterir.

## 3. Birincil ve ikincil sonuç değişkeninin önceden belirlenmesi

Birincil sonuç değişkeni çalışmanın ana iddiasını taşır. İkincil sonuçlar destekleyici ve tamamlayıcı bilgi sağlar. Bu ayrım analiz planında önceden yazılmazsa, en anlamlı çıkan değişken geriye dönük olarak birincil sonuç gibi sunulabilir. Bu, seçici raporlama sorunudur ve istatistiksel anlamlılık oranlarını şişirir.

Simmons ve diğerleri (2011), araştırmacı serbestlik derecelerinin, yani bağımlı değişken seçimi, veri dışlama ölçütleri, örneklem büyüklüğü kararları ve kontrol değişkeni dahil etme gibi açıklanmayan tercihlerinin, gerçekte anlamsız olan sonuçları yüzde beş anlamlılık eşiğinin altına taşıyacak biçimde birikebildiğini deneysel olarak göstermiştir. Wicherts ve diğerleri (2016), bu serbestlik derecelerinin çalışma planlamasından analize ve rapora kadar her aşamada birikebildiğini sistematik bir kontrol listesiyle ortaya koyar. Araştırmacıların veri toplamadan önce hangi değişkenlerin birincil olduğunu yazılı olarak kaydetmesini önerir.

Ajan tabanlı analizde bu risk özellikle belirginleşir. Model, araştırmacının başta düşünmediği değişkenler arasındaki ilişkileri hesaplayabilir, tablolar üretebilir ve bunları öne çıkarabilir. Analiz planı yoksa, hangi değişkenin baştan birincil sayıldığı bilinemez. Planın varlığı ise bu tuzağı kapatır: birincil sonuç baştan yazılmıştır, modelin sonradan ürettikleri ikincil ya da keşfedici olarak işaretlenir.

## 4. Dahil etme ve dışlama ölçütlerinin analizden önce yazılması

Hangi katılımcıların analize dahil edileceği, hangilerinin dışlanacağı, eksik verilerin nasıl ele alınacağı ve uç değerlerin hangi ölçütle değerlendirileceği, araştırmanın metodolojik omurgasını oluşturan kararlardır. Bu kararların veriye bakılmadan önce yazılması, hem yeniden üretilebilirlik hem de araştırma dürüstlüğü açısından temel bir gerekliliktir.

Veriye bakıldıktan sonra alınan dışlama kararları, istatistiksel anlamlılık oranlarını artırma yönünde sistematik bir baskı altında şekillenebilir. Bu baskı çoğu zaman kasıtlı değildir. Araştırmacı, dışlama için meşru bir metodolojik gerekçe bulabilir. Ancak bu gerekçenin veriye bakmadan önce mi, sonra mı oluştuğu dışarıdan ayırt edilemez. Protokol bu dışarıdan gözlem sorununu çözer: kararların tarihini ve sırasını kaydeder.

Ajan tabanlı akışta dışlama kararları özellikle akışkan hâle gelebilir. Model, farklı dışlama ölçütlerinin analizde nasıl farklı sonuçlar ürettiğini saniyelerde hesaplayabilir. Araştırmacı, en temiz görünen sonucu veren dışlama ölçütünü seçerse ve bu seçim kayıt dışı kalırsa, bu seçici raporlamadır. Ölçütlerin analizden önce protokolde yazılı olması bu riski ortadan kaldırır. Değişiklik gerekirse, bu değişiklik sapma günlüğüne gerekçesiyle birlikte işlenir.

## 5. Analiz planının önceden belirlenmesi

Analiz planı, hangi istatistiksel modelin, hangi değişkenlerle, hangi varsayım denetimleriyle ve hangi sırayla çalıştırılacağını belirtir. Bu plan, araştırma sorusundan ve teorik çerçeveden türetilir. Veriye baktıktan sonra en uygun görünen modeli bulmaya çalışmaktan değil.

Gelman ve Loken (2014), araştırmacıların tek bir hipotezi test ettiklerini düşünürken aslında görünmez bir çatallanan yollar bahçesinde ilerlediklerini gösterir. Veri bağımlı kararlar, her biri savunulabilir görünen ama biriktiğinde sistematik bir çoklu karşılaştırma ağacı oluşturan seçimler zinciridir. Munafò ve diğerleri (2017), analiz planının veriden önce sabitlenmesini yeniden üretilebilir bilimin yapısal temellerinden biri olarak konumlandırır. Bu olmadan şeffaf raporlama da tek başına yeterli değildir.

Yapay zekâ bu planlama sürecine katkı sağlayabilir. Model, varsayım denetim listesi çıkarabilir, farklı test seçeneklerinin teorik gerekçelerini karşılaştırabilir, taslak bir analiz planı yazabilir. Ancak planın kuramsal savunusu ve istatistiksel gerekçesi araştırmacıya aittir. Ajan bir test önerebilir. O testin bu veriye ve bu araştırma sorusuna uygunluğuna karar vermek araştırmacının işidir. Plan kurulduktan sonra ajan planı uygular. Planı planın yerine geçecek sonuçlar üretmek için kullanamaz.

## 6. Sapma günlüğü: plandan ayrılmanın kaydı

Protokolden sapmak her zaman yanlış değildir. Veri beklenmedik bir örüntü içerebilir. Varsayım denetimi, planlanan modelin uygulanamayacağını gösterebilir. Ölçüm, öngörülenden farklı davranabilir. Bilim bu tür yeniden değerlendirmelere kapalı değildir. Sorun sapmak değil, sapmayı kayıt dışı bırakmaktır.

Sapma günlüğü bu riski yönetmek için açılan bir belgedir. Her ayrılışın tarihi, gerekçesi, kararı veren kişi ve bu değişikliğin analize beklenen etkisi günlüğe işlenir. Böylece okurun gördüğü yöntem bölümü, araştırmacının baştan kurduğu planı değil, o plandan ne şekilde sapıldığını da yansıtır.

Van 't Veer ve Giner-Sorolla (2016), sosyal psikoloji araştırmaları için geliştirdikleri ön kayıt şablonunda sapmaların şeffaf biçimde raporlanmasını zorunlu bir bileşen olarak tanımlar. Protokolden ayrılmanın açıklanmasının, araştırmayı zayıflatmadığını, aksine bilimsel dürüstlüğün somut göstergesi olduğunu vurgular. Ajan tabanlı akışta bu ilke daha da önem kazanır: model veriye bağlı kararları otomatik olarak alabilir ve araştırmacı fark etmeden planı değiştirebilir. Sapma günlüğü bu değişiklikleri görünür kılan tek mekanizmadır.

## 7. Yapay zekânın analiz sürecindeki danışma sınırı

Yapay zekâ ajan tabanlı analizde üç farklı rolde çalışabilir: teknik yürütücü, metodolojik danışman ve analitik karar verici. Bu rollerin ilki devredilebilir, ikincisi sınırlı biçimde kullanılabilir, üçüncüsü ise araştırmacıya aittir.

Teknik yürütme devredebilirdir. Kod yazmak, tablolar biçimlendirmek, grafik üretmek, varsayım denetimleri çalıştırmak, analiz dosyasını temiz bir oturumda baştan çalıştırmak bu gruptadır. Metodolojik danışma, sınırları net çizildiğinde yararlıdır: ajan, belirli bir test için varsayımları listeleyebilir, alternatif yaklaşımların literatürdeki kullanımını özetleyebilir. Ancak bu öneriler araştırmacının bağımsız değerlendirmesinden geçer. Doğrudan benimsenmez.

Analitik karar verme devredilemez. Hangi testin bu veriye uygun olduğu, hangi dışlamanın kuramsal olarak savunulabilir olduğu, hangi etki büyüklüğünün bu alanda anlamlı sayıldığı kararları araştırmacıda kalır. Ajan bu kararları önerebilir. Kararın geçerliliğini onaylayamaz. Chambers (2013), kayıtlı rapor modelini tam da bu ayrımı kurumsal düzeyde güvence altına almak için geliştirmiştir: analiz planı yayına kabul sürecine bağlanmakta, böylece veriye bakıldıktan sonra alınan kararların yöntem bölümüne gizlice işlenmesinin önüne geçilmektedir.

## 8. Ön kayıt platformları ve yerel protokol alternatifleri

Ön kayıt, analitik kararların veriye bakılmadan önce kamuya erişilebilir bir biçimde ya da doğrulanabilir bir kayıtta sabitlenmesi uygulamasıdır. OSF (Open Science Framework) ve AsPredicted bu amaçla yaygın biçimde kullanılan platformlardır. OSF, zaman damgalı ön kayıt belgesi oluşturmaya ve bunları serbestçe ya da ambargo dönemine bağlı olarak yayımlamaya olanak tanır. AsPredicted ise daha kısa ve yapılandırılmış bir form sunar.

Nosek ve diğerleri (2018), ön kaydın yaygınlaşmasının araştırmacı serbestlik derecelerini görünür kılmak, doğrulayıcı ve keşfedici analizleri birbirinden ayırt etmek ve yayın yanlılığını azaltmak için yapısal bir çözüm sunduğunu savunur. Munafò ve diğerleri (2017), ön kaydın yeniden üretilebilir bilimin beş temel reformundan biri olduğunu ve şeffaf raporlama, açık veri ve yöntem paylaşımı ile birlikte düşünülmesi gerektiğini vurgular.

Hassas veri içeren çalışmalarda, kurumsal kısıtlar nedeniyle tam açık ön kayıt her zaman uygun olmayabilir. Bu durumlarda kurumsal etik kurulu dosyası, araştırma ekibinin kendi arşivi ya da zaman damgalı yerel protokol dosyası işlevsel bir alternatif sunar. Önemli olan platform değil, kararların analiz öncesinde sabitlenmesi ve bu sabitlemenin doğrulanabilir biçimde kayıt altına alınmasıdır.

## 9. Yöntem bölümüne aktarım ve raporlama şeffaflığı

Çalışma tamamlandığında protokol, yöntem bölümünün iskeletini oluşturur. Ancak bu aktarım doğrudan kopya değildir. Yöntem bölümü üç tabakayı açıkça birbirinden ayırmalıdır: planlanan analiz, plandan sapmalar ve keşfedici ek analizler.

Planlanan analiz, protokolde baştan yazılmış olan ve doğrulayıcı statüde yürütülen çalışmayı kapsar. Sapmalar, gerekçeleriyle birlikte ve sapma günlüğüne dayanarak raporlanır. Keşfedici analizler ise bir hipotezi test etmek için değil, ileriki araştırma sorularını oluşturmak için yürütülmüş bölümler olarak açıkça etiketlenir.

Bu şeffaflık okur için değer taşır. Hangi sonucun doğrulayıcı statüde olduğunu, hangisinin keşfedici nitelik taşıdığını ve plandan hangi noktalarda neden ayrılındığını bilen okur, bulguların bilimsel ağırlığını daha doğru değerlendirebilir. Van 't Veer ve Giner-Sorolla (2016), bu katmanlı raporlama yaklaşımının makaleyi zayıflatmadığını, tam tersine hakem değerlendirmesinde güçlendirdiğini gösterir. Çünkü araştırmacı kararlarını veriden önce aldığını belgeleyen bir iz bırakmıştır.

## 10. Skill çıktıları: /preregistration-analysis-plan-ledger

`/preregistration-analysis-plan-ledger` skill'i bu kitapçıkta tanımlanan iş akışını bir dosya altyapısına bağlar. Skill dört bileşen üretir.

Birincisi ön kayıt taslağıdır. Araştırma sorusu, hipotezler, birincil ve ikincil sonuç değişkenleri, dahil etme ve dışlama ölçütleri ile ön kayıt platformu seçimi için yapılandırılmış bir taslak sunar.

İkincisi analiz planıdır. Hangi istatistiksel modelin çalıştırılacağını, hangi değişkenlerin kullanılacağını, hangi varsayım denetimlerinin yapılacağını ve rastgelelik tohumunu belirten bir Markdown dosyasıdır. Bu dosya ajana talimat olarak verilir. Ajanın ürettiği öneriler bu dosyanın yerini almaz.

Üçüncüsü sapma günlüğü şablonudur. Her sapma için tarih, gerekçe, karar sahibi ve tahmini etki alanlarından oluşan bir izleme belgesidir.

Dördüncüsü yöntem bölümüne aktarım özetidir. Planlanan analiz, sapmalar ve keşfedici analizlerin yöntem bölümünde nasıl ayrı ayrı raporlanacağını gösteren bir taslaktır.

Skill, analizden önce düşünmeyi bir alışkanlık değil, dosya düzeyinde izlenebilir bir iş akışı hâline getirir.

## Kaynakça

Atıflar APA 7 biçimindedir. Her DOI 2026-06-21 tarihinde Crossref üzerinden bağımsız olarak doğrulanmıştır.

Chambers, C. D. (2013). Registered reports: A new publishing initiative at Cortex. *Cortex*, *49*(3), 609–610. https://doi.org/10.1016/j.cortex.2012.12.016

Gelman, A., & Loken, E. (2014). The statistical crisis in science. *American Scientist*, *102*(6), 460. https://doi.org/10.1511/2014.111.460

Kerr, N. L. (1998). HARKing: Hypothesizing after the results are known. *Personality and Social Psychology Review*, *2*(3), 196–217. https://doi.org/10.1207/s15327957pspr0203_4

Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J., & Ioannidis, J. P. A. (2017). A manifesto for reproducible science. *Nature Human Behaviour*, *1*(1), Article 0021. https://doi.org/10.1038/s41562-016-0021

Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, *115*(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114

Open Science Collaboration. (2015). Estimating the reproducibility of psychological science. *Science*, *349*(6251), Article aac4716. https://doi.org/10.1126/science.aac4716

Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology: Undisclosed flexibility in data collection and analysis allows presenting anything as significant. *Psychological Science*, *22*(11), 1359–1366. https://doi.org/10.1177/0956797611417632

van 't Veer, A. E., & Giner-Sorolla, R. (2016). Pre-registration in social psychology: A discussion and suggested template. *Journal of Experimental Social Psychology*, *67*, 2–12. https://doi.org/10.1016/j.jesp.2016.03.004

Wagenmakers, E.-J., Wetzels, R., Borsboom, D., van der Maas, H. L. J., & Kievit, R. A. (2012). An agenda for purely confirmatory research. *Perspectives on Psychological Science*, *7*(6), 632–638. https://doi.org/10.1177/1745691612463078

Wicherts, J. M., Veldkamp, C. L. S., Augusteijn, H. E. M., Bakker, M., van Aert, R. C. M., & van Assen, M. A. L. M. (2016). Degrees of freedom in planning, running, analyzing, and reporting psychological studies: A checklist to avoid p-hacking. *Frontiers in Psychology*, *7*, Article 1832. https://doi.org/10.3389/fpsyg.2016.01832

---

**Kitapçık kimliği.** `008-05-0001`
**Sürüm.** `0.1.0`
**Tarih.** 2026-06-21
**Lisans.** Bu kitapçık CC BY-NC-SA 4.0 ile lisanslanmıştır. https://creativecommons.org/licenses/by-nc-sa/4.0/
**Sözcük sayısı (yaklaşık).** 1728 (Türkçe gövde metni, wc ile ölçüldü)
**Doğrulanmış atıf sayısı.** 10
**Uydurma atıf sayısı.** 0
**Önceki kitapçık.** [`008-04-0001`](../008-04-0001/tr.md). Hassas Veriyi Hazırlamak, Anonimleştirme, Maskeleme ve Yerel Ön İşleme
**Sonraki kitapçık.** [`009-01-0001`](../../009-ethics-irb/009-01-0001/tr.md). Yapay Zekâ Destekli Araştırmada Etik, İlkeden Davranışa
