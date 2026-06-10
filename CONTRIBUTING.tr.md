# Katkıda Bulunma

Bu belge, `claude-code-for-social-scientists` deposuna nasıl değişiklik önereceğinizi, deponun zorunlu kıldığı iki dilli eşleşme kuralını ve her katkı sahibinin uymak zorunda olduğu yapay zekâ beyan beklentilerini açıklar.

İngilizce sürüm için [`CONTRIBUTING.md`](./CONTRIBUTING.md) dosyasına bakınız.

## Hangi tür katkılar bekleniyor

- Herhangi bir kitapçıktaki olgusal hata, atıf ya da DOI düzeltmeleri.
- Mevcut Türkçe kitapçıkların İngilizce çevirisi, mevcut İngilizce kitapçıkların Türkçe çevirisi.
- [`CATALOG.md`](./CATALOG.md) içinde planlanan slotlara karşılık önerilen yeni kitapçıklar.
- Sürekli bütünleşme iş akışlarında, belge araç setinde ve beyan şemasında iyileştirmeler.
- Diğer ülkeler için örneklerin veya bölgesel akademik altyapı referanslarının yerelleştirilmesi: örneğin Yunan HEAL-Link entegrasyonunun, Meksika CONACyT'ın ya da Hindistan Shodhganga'nın nasıl kullanılacağına dair bir bölüm.

Sürdürücü katkıları ayda bir kez gözden geçirir, yeni kitapçık önerilerini katalog içine yerleştirir.

## Başlamadan önce

Bir konu (issue) açın ve önerinizi iki ya da üç paragrafta tarif edin. Yeni bir kitapçık öneriyorsanız önerdiğiniz `KKK-AA-SSSS` kimliğini (uygun kategorideki bir sonraki boş seri), bir paragraf kapsamı ve bir taslak ana hattı eklemeniz gerekir.

Bu adım on beş dakikanızı alır. Karşılığında hem sizi hem de sürdürücüyü uyumsuz iş saatlerinden kurtarır.

## İki dilli eşleşme kuralı

Her kitapçık klasörü `tr.md` ve `en.md` dosyalarını yan yana içerir. `main` dalına yapılan her commit'te bunu zorunlu kılan bir sürekli bütünleşme denetimi çalışır.

Yalnızca bir dilde katkıda bulunuyorsanız pull request'iniz yine de incelenir ve bir özellik dalına merge edilebilir. Sürdürücü, dal `main`'e merge edilmeden önce diğer dil sürümünün yazılmasını ayarlar. `main` dalı kısmi iki dilli kapsamı kabul etmez.

Anadili Türkçe olan ve Türkçe sürümü yazıyorsanız önce Türkçe sürümü yazın. İngilizce sürümü sürdürücü ya da başka bir katkı sahibi üstlenir. Tersi de geçerlidir. Çeviri kelime kelime değildir: aynı ana hat üzerinde yeniden yazımdır.

## Yapay zekâ beyan beklentileri

Taslağında yapay zekâ kullanan her katkı sahibi, dokunduğu kitapçığın yapay zekâ katkı beyanı frontmatter alanlarını (ön veri bloğu) doldurmalıdır. Şema [`AI-AUTHORSHIP.md`](./AI-AUTHORSHIP.md) içinde belgelenir. `template/booklet-template.{tr,en}.md` yolundaki kitapçık şablon dosyaları, `human_review: "pending"` değeriyle önceden doldurulmuş şemayı içerir. Katkı sahipleri bu şablonu kopyalayıp uyarlayabilir. `main`'e merge etmeden önce `pending` değerini `partial` ya da `complete` olarak güncelleyin. CI, `main` üzerinde hâlâ `pending` taşıyan herhangi bir kitapçığı reddeder.

Buradaki yapılandırılmış blok yalnızca insan okuyucular için değildir. Yapay zekâ araçları da bu bloğu okur ve metnin hangi standarda göre üretildiğini görür. Blok, aracın işi doğru yapmasına yön verir. Bir beyan tek başına yeterli değildir: yapay zekânın metinde nasıl ve hangi biçimlerde kullanıldığı açıkça anlatılır.

Asgari zorunlu alanlar:

- `ai_assisted: true` (yapay zekâ kullanıldıysa) ya da `false`.
- `ai_tools` (model sürümleriyle birlikte araç listesi).
- `ai_contribution_level` (`editing-only`, `light-assistance`, `co-drafting`, `substantial-drafting`, `full-draft` değerlerinden biri).
- `human_review` (`complete`, `partial`, `pending` değerlerinden biri).
- `verified_citations_count` ve `fabricated_citations_count`.

`human_review: pending` ile bir kitapçık ekleyen pull request'ler `main` dalına merge edilmez. Bu durumu CI iş akışı engeller.

## Atıf disiplini

Katkınızdaki her DOI, her yazar adı, her yıl, her sayfa aralığı ve her dergi adı, pull request açmadan önce yetkili bir indekse (Crossref, PubMed, Semantic Scholar, ULAKBIM TR Dizin veya DergiPark) bağımsız olarak doğrulanmalıdır.

Bir atıfı genişletmek için yapay zekâ yardımı aldıysanız yapay zekânın ilk yanıtı bir adaydır, atıf değildir. Her adayı bir indekse karşı çözün. Yazar ve sürdürücü, atıf uydurmasını sürüm engelleyici bir hata olarak değerlendirir.

## Proje skill önerme

Proje skill'leri `.claude/skills/<skill-adı>/SKILL.md` altında yaşar ve sabit bir şemaya uyar: `name` ve `description` frontmatter çifti, ardından tam olarak şu bölümler: When to use, Inputs, Workflow, Output, Verification, Safety, Example prompt ve Türkçe kullanım notu. [`template/skill-template.md`](./template/skill-template.md) dosyasından başlayın. Description en az seksen karakter olmalı ve skill'i tetikleyecek kullanım anlarını adlandırmalıdır. Türkçe bölüm zorunludur ve kitapçıklardaki iki dillilik ilkesini skill katmanında sürdürür. Yeni bir skill ayrıca CATALOG skill tablosunda bir satır, iki README'de birer giriş ve doğrulayıcının beklenen listesinde adını gerektirir. Bu yüzden önce bir issue açın, sürdürücü dokunulacak noktalarda size eşlik eder.

## Pull request iş akışı

1. Depoyu GitHub üzerinde forklayın.
2. `main` dalından, kitapçık kimliği ya da dokunduğunuz alanın adıyla bir özellik dalı oluşturun (örneğin `feat/008-02-0001-test-selection` ya da `fix/catalog-typo`).
3. Değişiklikleri atomik commit'lerle yapın. Uygun olan Conventional Commits ön ekini kullanın (`feat:`, `fix:`, `docs:`, `chore:`, `ci:`, `refactor:`).
4. Yerelde `npx markdownlint-cli2 "**/*.md"` çalıştırarak lint kontrolünü teyit edin.
5. `main`'e karşı pull request açın. Daha önce açtığınız konuya atıfta bulunun.
6. Sürdürücü incelemesine yanıt verin. Asli katkılarda en az bir tur geri bildirim bekleyin.
7. Onay sonrası ve iki dilli eşleşme tamamlandığında sürdürücü değişikliği, büyüklüğüne göre squash ya da rebase ile merge eder.

## Geliştirici Köken Sertifikası

Katkıda bulunarak katkının size ait olduğunu, ya da deponun lisans koşulları altında sunma hakkını taşıdığınızı beyan etmiş olursunuz. Geliştirici Köken Sertifikası (DCO) sürüm 1.1 bu beyanı yönetir ve her merge edilen değişiklik için zımnen geçerlidir. Pull request'lerin `Signed-off-by` ile imzalanması zorunlu değildir.

## Davranış

Tüm etkileşimler [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md) tarafından yönetilir. Okuyunuz. Sürdürücü uygular.

## Tanınma

Merge edilen dış katkı sahipleri, katkı türü belirtilerek [`meta/contributors.md`](./meta/contributors.md) içinde listelenir.

## Sorular

Sorunuz burada yanıtlanmadıysa GitHub Discussions etkinleştirildiğinde (v1.5) tartışma açın, bir konu açın ya da sürdürücünün GitHub profilindeki iletişim yüzeyini kullanınız.

---

**Son güncelleme.** 2026-06-05.
