# Awesome Digital Civil Engineering [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | Türkçe

İnşaat ve altyapı mühendisliği, yapı ve geoteknik mühendisliği, su ve hidrolik, coğrafi analiz, gerçeklik yakalama, BIM ve dijital ikiz alanlarının kesişimindeki açık kaynak araçların, kütüphanelerin, veri setlerinin ve projelerin derlenmiş listesi. Dünya genelindeki projelere ek olarak Türkiye için ayrı bir bölüm içerir.

**Listeye alınma ölçütleri:** burada yer alan her proje açık kaynak olmalı ya da kaynağı veya içeriği herkese açık olup lisans kısıtı girişinde belirtilmelidir. Proje ayrıca inşaat veya altyapı mühendisliğiyle (ya da coğrafi analiz, deprem mühendisliği gibi doğrudan komşu bir disiplinle) ilgili olmalı ve yeni başlayan birinin ne yaptığını ve nasıl çalıştırılacağını anlayabileceği kadar bakımlı veya belgelenmiş olmalıdır.

Bu dosya [README.md](README.md) dosyasının çevirisidir. İkisi arasında fark olursa İngilizce sürüm esas alınır.

## İçindekiler

- [Yapısal analiz ve sonlu elemanlar](#yapısal-analiz-ve-sonlu-elemanlar)
- [Tasarım yönetmelikleri ve hesap araçları](#tasarım-yönetmelikleri-ve-hesap-araçları)
- [Deprem mühendisliği](#deprem-mühendisliği)
- [Geoteknik mühendisliği](#geoteknik-mühendisliği)
- [Yapı sağlığı izleme](#yapı-sağlığı-izleme)
- [BIM ve IFC](#bim-ve-ifc)
- [CAD ve parametrik modelleme](#cad-ve-parametrik-modelleme)
- [Dijital ikizler](#dijital-ikizler)
- [Nokta bulutu ve fotogrametri](#nokta-bulutu-ve-fotogrametri)
- [Coğrafi bilgi sistemleri ve uzaktan algılama](#coğrafi-bilgi-sistemleri-ve-uzaktan-algılama)
- [Su ve hidrolik](#su-ve-hidrolik)
- [Altyapı ve kent analitiği](#altyapı-ve-kent-analitiği)
- [Yapay zeka ve makine öğrenmesi](#yapay-zeka-ve-makine-öğrenmesi)
- [Dayanıklılık ve iklim](#dayanıklılık-ve-iklim)
- [Açık veri setleri](#açık-veri-setleri)
- [Öğrenme kaynakları](#öğrenme-kaynakları)
- [Türkiye](#türkiye)
- [Benzer awesome listeleri](#benzer-awesome-listeleri)

## Yapısal analiz ve sonlu elemanlar

- [OpenSees](https://github.com/OpenSees/OpenSees#readme) - UC Berkeley'de geliştirilen, doğrusal olmayan yapısal ve geoteknik simülasyon için referans çatı. Akademik deprem mühendisliği araştırma kodlarının çoğunun temeli ve aşağıdaki deprem mühendisliği bölümünde kullanılan ana simülasyon motoru. Kaynak kodu herkese açık, ancak lisans kullanımı ticari olmayan ve kurum içi amaçlarla sınırlar, ticari dağıtım için ayrı lisans gerekir. C++, Custom.
- [OpenSeesPy](https://github.com/zhuminjie/OpenSeesPy#readme) - OpenSees'in pip ile dağıtılan Python yorumlayıcı sürümü, bugün OpenSees modellerini betiklemenin olağan giriş noktası. OpenSees ile aynı lisans kısıtlarını taşır. Python, Custom.
- [opstool](https://github.com/yexiang92/opstool#readme) - OpenSeesPy modelleri için ön işlem, son işlem ve görselleştirme yardımcıları, fiber kesit ağı oluşturma ve sonuç çizimi dahil. Python, GPL-3.0.
- [ospgrillage](https://github.com/ssp-research/ospgrillage#readme) - OpenSeesPy üzerinde köprü tabliyesi ızgara modelleri kurar, hareketli yük ve yük kombinasyonu desteği vardır. Python, MIT.
- [Pynite](https://github.com/JWock82/Pynite#readme) - Kirişler, çerçeveler, plaklar, yük kombinasyonları ve P Delta analizi için Python'da 3B yapısal sonlu eleman kütüphanesi. Eski adı PyNite. Python, MIT.
- [anaStruct](https://github.com/anastruct/anaStruct#readme) - Python'da 2B yapısal analiz, tam bir sonlu eleman altyapısı kurmadan hızlı çerçeve ve kafes kontrolleri için uygun. Python, LGPL-3.0.
- [PyCBA](https://github.com/ccaprani/pycba#readme) - Python'da sürekli kiriş analizi, tesir çizgileri ve hareketli taşıt zarflarıyla köprü değerlendirmesine yönelik. Python, AGPL-3.0.
- [section-properties](https://github.com/robbievanleeuwen/section-properties#readme) - Python'da keyfi kesitlerin sonlu eleman analizi. Çarpılma sabitleri, kayma alanları ve çoğu standart aracın vermediği diğer özellikleri hesaplar. Python, MIT.
- [concrete-properties](https://github.com/robbievanleeuwen/concrete-properties#readme) - Betonarme kesit analizi, moment eğrilik ve etkileşim diyagramları, section-properties üzerine kurulu. Python, MIT.
- [COMPAS](https://github.com/compas-dev/compas#readme) - Mimarlık, yapı ve dijital üretim alanlarında araştırma ve iş birliği için hesaplamalı çatı, Rhino, Grasshopper ve Blender için CAD bütünleştirmeleriyle. Python, MIT.
- [CalculiX](https://www.calculix.de/) - Doğrusal ve doğrusal olmayan yapısal, dinamik ve ısıl analiz için ücretsiz sonlu eleman paketi, Abaqus uyumlu girdi biçimi kullanır.
- [SfePy](https://github.com/sfepy/sfepy#readme) - Python'da basit sonlu elemanlar, yapısal, mekanik ve bağlaşık fizik problemleri için genel amaçlı bir çözücü. Python, BSD-3-Clause.
- [DOLFINx](https://github.com/FEniCS/dolfinx#readme) - FEniCS projesinin hesaplama çekirdeği, kısmi diferansiyel denklemleri üst düzey bir Python veya C++ arayüzünden sonlu eleman yöntemiyle çözer. C++, LGPL-3.0.
- [Kratos Multiphysics](https://github.com/KratosMultiphysics/Kratos#readme) - CIMNE tarafından geliştirilen paralel çoklu fizik çatısı, yapısal, jeomekanik, akışkan ve akışkan yapı etkileşimi uygulamalarıyla. C++, BSD-4-Clause.
- [XC](https://github.com/xcfem/xc#readme) - Özellikle inşaat mühendisliği yapıları için yazılmış sonlu eleman paketi, beton ve çelik elemanlar için yönetmelik kontrol rutinleri içerir. C++, GPL-3.0.

## Tasarım yönetmelikleri ve hesap araçları

- [structuralcodes](https://github.com/fib-international/structuralcodes#readme) - fib (Uluslararası Yapısal Beton Federasyonu) tarafından geliştirilen, Eurocode 2 ve fib Model Code gibi tasarım yönetmeliği modellerini kesit analiziyle birlikte uygulayan Python kütüphanesi. Python, Apache-2.0.
- [Blueprints](https://github.com/Blueprints-org/blueprints#readme) - Eurocode formülleri, tabloları ve kontrollerinin test edilmiş Python fonksiyonları olarak derlemesi, her biri uyguladığı maddeye bağlı. Python, MIT.
- [handcalcs](https://github.com/connorferster/handcalcs#readme) - Python hesaplarını sembolik formül, yerine konmuş değerler ve sonuçla birlikte LaTeX olarak gösterir, tıpkı elle yazılmış bir hesap föyü gibi. Python, Apache-2.0.
- [forallpeople](https://github.com/connorferster/forallpeople#readme) - Mühendislik hesapları için SI birim kütüphanesi, birimleri değerlere bağlı tutar ve kendiliğinden sadeleştirir. Python, Apache-2.0.
- [efficalc](https://github.com/youandvern/efficalc#readme) - Düz Python kodundan yapısal hesap raporları üretir, girdiler, kabuller ve kontroller incelemeye uygun biçimde dizilir. Python, MIT.

## Deprem mühendisliği

- [OpenQuake Engine](https://github.com/gem/oq-engine#readme) - Global Earthquake Model Vakfı'nın sismik tehlike ve risk analizi yazılımı, dünya genelinde ulusal tehlike kurumlarınca kullanılır. Python, AGPL-3.0.
- [quoFEM](https://github.com/NHERI-SimCenter/quoFEM#readme) - Sonlu eleman uygulamalarının üzerine belirsizlik ölçümü ve optimizasyon rutinleri ekleyen NHERI SimCenter masaüstü uygulaması, çoğunlukla OpenSees ile birlikte kullanılır. C++, BSD-2-Clause.
- [Pelicun](https://github.com/NHERI-SimCenter/pelicun#readme) - Binalar ve altyapı için olasılıksal hasar ve kayıp tahmini, FEMA P-58 ve Hazus yöntemlerini uygular. Python, BSD-3-Clause.
- [R2DTool](https://github.com/NHERI-SimCenter/R2DTool#readme) - Bina ve altyapı envanterleri üzerinde deprem ve kasırga hasarının bölgesel ölçekte simülasyonu için NHERI SimCenter uygulaması. C++, BSD-3-Clause.
- [OpenSHA](https://github.com/opensha/opensha#readme) - Sismik tehlike analizi için Java platformu, Kaliforniya için UCERF deprem kırılma tahminlerinin arkasındaki kod tabanı. Java, BSD-3-Clause.
- [eqsig](https://github.com/eng-tools/eqsig#readme) - Deprem mühendisliği için sinyal işleme, saha ve deney verilerinden tepki spektrumları, Fourier spektrumları ve diğer yer hareketi şiddet ölçülerini hesaplar. Python, MIT.
- [pyrotd](https://github.com/arkottke/pyrotd#readme) - İki yatay yer hareketi bileşeninden RotD50 ve RotD100 gibi döndürülmüş tepki spektrumlarını hesaplar. Python, MIT.
- [ObsPy](https://github.com/obspy/obspy#readme) - Sismoloji için Python çatısı, yaygın tüm biçimlerdeki dalga formu verisini okur, işler ve veri merkezi web servisleriyle konuşur. Python, LGPL-3.0.
- [SeisBench](https://github.com/seisbench/seisbench#readme) - Sismolojide makine öğrenmesi için araç kutusu, karşılaştırma veri setleri ve önceden eğitilmiş faz belirleme modelleriyle. Python, GPL-3.0.

## Geoteknik mühendisliği

- [pyStrata](https://github.com/arkottke/pystrata#readme) - Python'da saha tepki analizi, eşdeğer doğrusal ve rastgele titreşim teorisi yöntemlerini kapsar. Eski adı pysra. Python, MIT.
- [liquepy](https://github.com/eng-tools/liquepy#readme) - Zemin sıvılaşması değerlendirme araçları, CPT tabanlı tetiklenme yöntemleri ve efektif gerilme analizi yardımcıları dahil. Python, MIT.
- [Groundhog](https://github.com/snakesonabrain/groundhog#readme) - Saha araştırması verisinin işlenmesi, zemin korelasyonları ve temel hesaplarını kapsayan genel amaçlı geoteknik kütüphanesi. Python, GPL-3.0.
- [pygef](https://github.com/cemsbv/pygef#readme) - GEF ve BRO XML biçimlerindeki CPT ve sondaj dosyalarını veri çerçevelerine dönüştürür ve çizer. Python, MIT.
- [pySlope](https://github.com/JesseBonanno/PySlope#readme) - Bishop dilim yöntemiyle şev stabilitesi analizi, tabakalı zeminleri, yeraltı su seviyesini ve sürşarj yüklerini destekler. Python, MIT.
- [OpenGeoSys](https://gitlab.opengeosys.org/ogs/ogs) - Gözenekli ve çatlaklı ortamlardaki bağlaşık termo hidro mekanik ve kimyasal süreçler için sonlu eleman simülatörü.

## Yapı sağlığı izleme

- [pyOMA2](https://github.com/dagghe/pyOMA2#readme) - Python'da operasyonel modal analiz, ortam titreşimi verisinden doğal frekansları, sönüm oranlarını ve mod şekillerini çıkarır. Özgün PyOMA'nın etkin biçimde bakımı yapılan ardılı. Python, MIT.
- [koma](https://github.com/knutankv/koma#readme) - Gerçek köprü ve inşaat yapısı izleme araştırmaları için geliştirilmiş ve orada kullanılan operasyonel modal analiz araç kutusu. Python, MIT.
- [OpenModal](https://github.com/openmodal/OpenModal#readme) - Tam grafik arayüzlü, deneysel modal analiz için masaüstü uygulaması. 2021'den beri etkin bakımı yapılmıyor, ancak hâlâ az sayıdaki eksiksiz açık kaynak deneysel modal analiz aracından biri. Python, GPL-3.0.
- [SDyPy](https://github.com/sdypy/sdypy#readme) - Python'da yapı dinamiği için çatı paket, modal analiz, frekans tepkisi ve uyarım araçlarını tek ad alanında toplar. Python, MIT.
- [pyEMA](https://github.com/ladisk/pyEMA#readme) - Ölçülmüş frekans tepki fonksiyonlarından LSCF ve LSFD yöntemleriyle deneysel ve operasyonel modal analiz. Python, MIT.
- [pyidi](https://github.com/ladisk/pyidi#readme) - Yüksek hızlı kamera görüntülerinden yer değiştirmeleri belirler, yapıların kamera tabanlı titreşim ölçümü için bir temel. Python, MIT.

Bu bölüm listenin geri kalanına göre hâlâ zayıf. Bakımı yapılan, belgelenmiş bir açık kaynak yapı sağlığı izleme projesi biliyorsanız lütfen pull request açın, listenin en çok değer katabileceği bölümlerden biri burası.

## BIM ve IFC

- [IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell#readme) - Açık kaynak IFC kütüphanesi ve geometri motoru. Bonsai (eski adıyla BlenderBIM) eklentisi dahil neredeyse tüm diğer açık BIM araçlarının temeli. C++, LGPL-3.0.
- [web-ifc](https://github.com/ThatOpen/engine_web-ifc#readme) - That Open Company ekosisteminden, IFC dosyalarını tarayıcıda WebAssembly ile yerel hızda okur ve yazar. TypeScript, MPL-2.0.
- [That Open Components](https://github.com/ThatOpen/engine_components#readme) - web-ifc ve Three.js üzerinde tarayıcı tabanlı BIM uygulamaları kurmak için bileşen kütüphanesi. TypeScript, MIT.
- [xeokit SDK](https://github.com/xeokit/xeokit-sdk#readme) - Tarayıcıda büyük BIM ve AEC modelleri için WebGL görüntüleyici araç takımı, IFC, glTF ve nokta bulutu biçimlerini destekler. JavaScript, AGPL-3.0.
- [BIMserver](https://github.com/opensourceBIM/BIMserver#readme) - Açık kaynak BIM model sunucusu. IFC modellerini sürümleme ve çok kullanıcılı iş birliğiyle saklar ve yönetir. Java, AGPL-3.0.
- [xBIM Toolkit](https://github.com/xBimTeam/XbimEssentials#readme) - IFC bina modellerini okumak, oluşturmak, doğrulamak ve sorgulamak için açık kaynak .NET araç takımı. C#, CDDL-1.0.
- [IFC4.x-development](https://github.com/buildingSMART/IFC4.x-development#readme) - buildingSMART'ın IFC4.x şartnamesi için kendi deposu, yukarıdaki her aracın uyguladığı standart. Değiştirilmiş sürümler yeniden dağıtılamaz. CC-BY-ND-4.0.
- [Speckle](https://github.com/specklesystems/speckle-server#readme) - AEC birlikte çalışabilirliği için açık kaynak veri platformu, tasarım araçları arasında geometri ve veriyi gerçek zamanlı aktarır, sıklıkla BIM için sürüm kontrolü olarak tanımlanır. İki sunucu modülü ayrı bir kurumsal lisans altındadır. TypeScript, Apache-2.0.
- [BHoM](https://github.com/BHoM/BHoM#readme) - Buildings and Habitats object Model, yapısal, çevresel ve BIM yazılımlarını birbirine bağlayan ortak bir veri şeması ve bağdaştırıcı seti. C#, LGPL-3.0.
- [topologicpy](https://github.com/wassimj/topologicpy#readme) - Binaları analiz için topolojik hücreler, yüzeyler ve çizgeler olarak temsil eden mekansal modelleme kütüphanesi. Python, LGPL-3.0.

## CAD ve parametrik modelleme

- [FreeCAD](https://github.com/FreeCAD/FreeCAD#readme) - Yerleşik BIM ve sonlu eleman çalışma tezgahları ve eksiksiz bir Python arayüzü olan parametrik 3B modelleyici. C++, LGPL-2.1.
- [CadQuery](https://github.com/CadQuery/cadquery#readme) - Open CASCADE çekirdeği üzerinde parametrik CAD modellerini betiklemek için Python çatısı. Python, Apache-2.0.
- [LibreCAD](https://github.com/LibreCAD/LibreCAD#readme) - DXF okuyup yazan, teknik çizim için 2B CAD uygulaması. C++, GPL-2.0.

## Dijital ikizler

- [iTwin.js](https://github.com/iTwin/itwinjs-core#readme) - Bentley'nin altyapı dijital ikizleri kurmak ve görselleştirmek için açık kaynak kütüphanesi. BIM, GIS ve gerçeklik yakalama verisine doğrudan bağlanır. TypeScript, MIT.
- [Cesium](https://github.com/CesiumGS/cesium#readme) - 3B küreler ve haritalar için açık kaynak JavaScript motoru, altyapı ve kent ölçeğindeki dijital ikizlerin görselleştirme katmanı olarak yaygın biçimde kullanılır. JavaScript, Apache-2.0.
- [Eclipse Ditto](https://github.com/eclipse-ditto/ditto#readme) - Eclipse IoT'nin fiziksel varlıkların durumunu ve telemetrisini yönetmek için genel amaçlı dijital ikiz çatısı, binaların ötesinde izlenen her altyapı varlığına uygulanabilir. Java, EPL-2.0.
- [Orion-LD](https://github.com/FIWARE/context.Orion-LD#readme) - NGSI-LD standardını uygulayan FIWARE bağlam aracısı, akıllı kent ve altyapı dijital ikiz platformları için yaygın bir veri omurgası. C++, AGPL-3.0.

## Nokta bulutu ve fotogrametri

- [OpenDroneMap](https://github.com/OpenDroneMap/ODM#readme) - İnsansız hava aracı görüntülerini ortofotolara, nokta bulutlarına, dokulu ağ modellerine ve yükseklik modellerine dönüştüren komut satırı araç takımı. Python, AGPL-3.0.
- [WebODM](https://github.com/WebODM/WebODM#readme) - OpenDroneMap için projeleri ve işleme görevlerini yöneten web arayüzü ve API. Python, AGPL-3.0.
- [OpenSfM](https://github.com/mapillary/OpenSfM#readme) - Örtüşen görüntülerden kamera konumlarını ve 3B sahneleri yeniden kuran hareketten yapı kütüphanesi. Python, BSD-2-Clause.
- [COLMAP](https://github.com/colmap/colmap#readme) - Grafik ve komut satırı arayüzlü, hareketten yapı ve çok bakışlı stereo işlem hattı. C++, BSD-3-Clause.
- [Meshroom](https://github.com/alicevision/Meshroom#readme) - AliceVision çatısı üzerine kurulu, düğüm tabanlı fotogrametri uygulaması. Python, MPL-2.0.
- [PDAL](https://github.com/PDAL/PDAL#readme) - Point Data Abstraction Library, nokta bulutu verisini yapılandırılabilir işlem hatlarıyla dönüştürür ve işler. C++, BSD-3-Clause.
- [laspy](https://github.com/laspy/laspy#readme) - Python'da LAS ve LAZ lidar dosyalarını okur, değiştirir ve yazar. Python, BSD-2-Clause.
- [Open3D](https://github.com/isl-org/Open3D#readme) - Nokta bulutları ve ağ modelleri için çakıştırma, yüzey oluşturma ve görselleştirme içeren 3B veri işleme kütüphanesi. C++, MIT.
- [CloudCompare](https://github.com/CloudCompare/CloudCompare#readme) - Nokta bulutu ve ağ modeli işleme için masaüstü uygulaması, buluttan buluta karşılaştırma ve deformasyon ölçümünde yaygın biçimde kullanılır. C++, GPL-2.0-or-later.
- [Potree](https://github.com/potree/potree#readme) - Tarayıcıda çok büyük nokta bulutları için WebGL görüntüleyici. JavaScript, BSD-2-Clause.

## Coğrafi bilgi sistemleri ve uzaktan algılama

- [QGIS](https://github.com/qgis/QGIS#readme) - Mekansal veriyi görüntülemek, düzenlemek ve analiz etmek için masaüstü coğrafi bilgi sistemi, Python eklentileriyle genişletilebilir. C++, GPL-2.0.
- [GDAL](https://github.com/OSGeo/gdal#readme) - Raster ve vektör coğrafi veri biçimleri için dönüştürücü kütüphane, diğer açık coğrafi araçların çoğu buna dayanır. C++, MIT.
- [GRASS](https://github.com/OSGeo/grass#readme) - Geniş bir raster, vektör, arazi ve hidroloji modülü setine sahip coğrafi işleme motoru. C, GPL-2.0-or-later.
- [GeoPandas](https://github.com/geopandas/geopandas#readme) - pandas'a coğrafi veri tipleri ve işlemleri ekler. Python'da vektör GIS çalışmaları için standart giriş noktası. Python, BSD-3-Clause.
- [OSMnx](https://github.com/gboeing/osmnx#readme) - OpenStreetMap'ten sokak ağlarını ve diğer coğrafi nesneleri indirir, modeller, analiz eder ve görselleştirir. Aşağıdaki altyapı ve kent analitiği bölümünde anılan sokak ağı çalışmalarının da temeli. Python, MIT.
- [xarray](https://github.com/pydata/xarray#readme) - Python'da etiketli çok boyutlu diziler, çoğu raster ve iklim verisi iş akışının (uydu görüntüleri, hava durumu, hidroloji) temeli. Python, Apache-2.0.
- [Rasterio](https://github.com/rasterio/rasterio#readme) - GDAL üzerine kurulu, coğrafi raster veri setlerini okur ve yazar. Python, BSD-3-Clause.
- [leafmap](https://github.com/opengeos/leafmap#readme) - Jupyter'da az kodla etkileşimli haritalama ve coğrafi analiz. Birkaç haritalama altyapısını tek bir arayüz altında toplar. Python, MIT.
- [TorchGeo](https://github.com/torchgeo/torchgeo#readme) - Coğrafi veriye ve uydu verisine derin öğrenme uygulamak için veri setleri, örnekleyiciler, dönüşümler ve önceden eğitilmiş modeller. Python, MIT.

## Su ve hidrolik

- [EPANET](https://github.com/OpenWaterAnalytics/EPANET#readme) - Basınçlı su dağıtım şebekelerinin hidrolik ve su kalitesi simülasyonu için EPANET araç takımının topluluk tarafından sürdürülen sürümü. C, MIT.
- [WNTR](https://github.com/USEPA/WNTR#readme) - Water Network Tool for Resilience, su dağıtım şebekelerini deprem, elektrik kesintisi ve diğer aksaklıklar altında simüle ve analiz eder. Python, BSD-3-Clause.
- [SWMM](https://github.com/USEPA/Stormwater-Management-Model#readme) - ABD Çevre Koruma Ajansı'nın kentsel drenaj sistemlerinde yüzeysel akış miktarı ve kalitesi için Storm Water Management Model'i, kamu malı olarak yayımlanmıştır. C, Public-Domain.
- [PySWMM](https://github.com/pyswmm/pyswmm#readme) - SWMM için Python arayüzü, simülasyonu adım adım ilerletmeye ve çalışırken kontrolleri değiştirmeye olanak tanır. Python, BSD-2-Clause.
- [ANUGA](https://github.com/anuga-community/anuga_core#readme) - Taşkınları, baraj yıkılmalarını, tsunamileri ve fırtına kabarmalarını modellemek için sığ su denklemleri çözücüsü. Python, Apache-2.0.
- [SFINCS](https://github.com/Deltares/SFINCS#readme) - Deltares'in kıyı alanlarındaki bileşik taşkınların hızlı simülasyonu için indirgenmiş karmaşıklıkta modeli. Fortran, GPL-3.0.
- [LISFLOOD](https://github.com/ec-jrc/lisflood-code#readme) - Avrupa Komisyonu Ortak Araştırma Merkezi'nin dağıtık yağış akış ve öteleme modeli, Avrupa ve küresel taşkın tahmin sistemlerinde kullanılır. Python, EUPL-1.2.
- [Wflow.jl](https://github.com/Deltares/Wflow.jl#readme) - Havza ölçeğindeki simülasyonlar için Julia'da dağıtık hidrolojik modelleme çatısı. Julia, MIT.
- [HydroMT](https://github.com/Deltares/hydromt#readme) - Küresel veri setlerinden hidrolojik ve hidrodinamik model kurulumlarını tekrarlanabilir biçimde oluşturur ve analiz eder. Python, MIT.
- [pysheds](https://github.com/pysheds/pysheds#readme) - Python'da sayısal yükseklik modellerinden havza sınırı belirleme, akış yönü ve akış birikimi. Python, GPL-3.0.
- [Pywr](https://github.com/pywr/pywr#readme) - Rezervuarlar, aktarımlar ve su çekimleri gibi su kaynakları sistemleri için ağ tabanlı kaynak tahsis modeli. Python, GPL-3.0.
- [MODFLOW 6](https://github.com/MODFLOW-ORG/modflow6#readme) - USGS'nin yeraltı suyu akışı ve yeraltı ile yüzey suyu etkileşimi için açık kaynak modüler hidrolojik modeli, taşkın ve kuraklık dayanıklılığı çalışmalarıyla ilgilidir. Fortran, CC0-1.0.
- [FloPy](https://github.com/modflowpy/flopy#readme) - MODFLOW tabanlı yeraltı suyu modellerini oluşturmak, çalıştırmak ve son işlemek için Python paketi. Python, CC0-1.0.
- [Landlab](https://github.com/landlab/landlab#readme) - Yüzeysel akış, erozyon ve sediment taşınımı gibi yeryüzü süreçlerinin 2B sayısal modellerini kurmak için araç takımı. Python, MIT.

## Altyapı ve kent analitiği

- [Eclipse SUMO](https://github.com/eclipse-sumo/sumo#readme) - Yayalar dahil büyük yol ağlarını ele alabilen açık kaynak, mikroskobik ve sürekli trafik simülasyon paketi. C++, EPL-2.0.
- [MATSim](https://github.com/matsim-org/matsim-libs#readme) - Büyük ölçekli hareketlilik ve altyapı talebi çalışmalarında kullanılan ajan tabanlı ulaşım simülasyon çatısı. Java, GPL-2.0-or-later.
- [UrbanSim](https://github.com/UDST/urbansim#readme) - Metropol ölçeğinde arazi kullanımı, gayrimenkul ve ulaşım etkileşimlerini modellemek için simülasyon platformu. Python, BSD-3-Clause.
- [ActivitySim](https://github.com/ActivitySim/activitysim#readme) - Aktivite tabanlı yolculuk talebi modellemesi için açık platform, metropol planlama kuruluşlarınca altyapı ve ulaşım planlamasında kullanılır. Python, BSD-3-Clause.
- [momepy](https://github.com/pysal/momepy#readme) - Kentsel morfoloji ölçüm araç takımı, coğrafi veriden sokak ağlarını, bina biçimini ve kentsel yapıyı sayısallaştırır. Python, BSD-3-Clause.

## Yapay zeka ve makine öğrenmesi

- [xView2 baseline](https://github.com/DIUx-xView/xView2_baseline#readme) - xView2 bina hasar değerlendirme yarışması için afet öncesi ve sonrası uydu görüntülerini kullanan temel konumlandırma ve hasar sınıflandırma modelleri. Python, BSD-3-Clause.
- [BRAILS++](https://github.com/NHERI-SimCenter/BrailsPlusPlus#readme) - Derin öğrenmeyle uydu ve sokak düzeyi görüntülerden bölgesel bina ve altyapı envanterleri oluşturan NHERI SimCenter çatısı. Python, BSD-3-Clause.
- [RoadDamageDetector](https://github.com/sekilab/RoadDamageDetector#readme) - Birkaç ülkeden yol hasarı veri setleri ve akıllı telefon görüntülerinde çatlak ve çukur tespiti için eğitilmiş modeller. Python, MIT.
- [segment-geospatial](https://github.com/opengeos/segment-geospatial#readme) - Segment Anything Model'i uydu ve hava görüntülerine uygular, binaları, yolları ve diğer nesneleri çıkarmak için kullanışlıdır. Python, MIT.
- [DeepXDE](https://github.com/lululxvi/deepxde#readme) - Fizik bilgili sinir ağları ve operatör öğrenmesi için kütüphane, mekanik problemlerinin vekil modellemesinde kullanılır. Python, LGPL-2.1.

## Dayanıklılık ve iklim

- [pyincore](https://github.com/IN-CORE/pyincore#readme) - Tehlike kaynaklı altyapı hasarını sosyal ve ekonomik etkiye kadar taşıyan topluluk dayanıklılığı modelleme ortamı IN-CORE için Python istemcisi. Python, MPL-2.0.
- [Brightway](https://github.com/brightway-lca/brightway25#readme) - Yaşam döngüsü değerlendirmesi için açık kaynak Python çatısı, altyapının ve yapı malzemelerinin çevresel ayak izini değerlendirmekte kullanılır. Python, BSD-3-Clause.
- [CLIMADA](https://github.com/CLIMADA-project/climada_python#readme) - İklim riski değerlendirmesi ve uyum seçeneklerinin incelenmesi için açık kaynak çatı, altyapı ve diğer varlıklar için tehlike, maruziyet ve kırılganlığı modeller. Python, GPL-3.0.
- [City Energy Analyst](https://github.com/architecture-building-systems/CityEnergyAnalyst#readme) - Düşük karbonlu, enerji verimli mahalleler ve kentler tasarlamak için kentsel bina enerji modelleme platformu. Python, MIT.
- [EnergyPlus](https://github.com/NatLabRockies/EnergyPlus#readme) - ABD Enerji Bakanlığı'nın bütün bina enerji simülasyon motoru, tek tek binalar için ısıtma, soğutma, aydınlatma ve su kullanımını modeller. C++, BSD-3-Clause-style.
- [OpenStudio](https://github.com/NatLabRockies/OpenStudio#readme) - Bütün bina enerji modellemesi ve gün ışığı analizi için EnergyPlus ve Radiance üzerine kurulu, platformdan bağımsız araçlar. C++, BSD-3-Clause-style.
- [Ladybug](https://github.com/ladybug-tools/ladybug#readme) - Çevresel bina tasarımında hava verisini içe aktarmak ve analiz etmek için Ladybug Tools'un çekirdek kütüphanesi. Python, AGPL-3.0.

## Açık veri setleri

- [Global ML Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints#readme) - Uydu görüntülerinden türetilmiş, dünyanın büyük bölümü için bina oturum alanı poligonları. CDLA-Permissive-2.0.
- [Open Buildings](https://sites.research.google/gr/open-buildings/) - Afrika, Güney ve Güneydoğu Asya, Latin Amerika ve Karayipler için güven puanlı bina oturum alanları.
- [Overture Maps](https://github.com/OvertureMaps/data#readme) - Bulut yerel biçimlerde binalar, ulaşım ağları, yerler ve idari sınırlar içeren açık harita verisi. MIT.
- [GEM Global Exposure Model](https://github.com/gem/global_exposure_model#readme) - Sismik risk değerlendirmesi için derlenmiş, ülke düzeyinde bina sayıları, yenileme maliyetleri ve yapısal sınıflar. Yalnızca ticari olmayan kullanım. CC-BY-NC-SA-4.0.
- [GEM Global Active Faults](https://github.com/GEMScienceTools/gem-global-active-faults#readme) - Kayma hızı ve kinematik özniteliklerle uyumlaştırılmış küresel diri fay izleri veritabanı. CC-BY-SA-4.0.
- [STEAD](https://github.com/smousavi05/STEAD#readme) - Stanford Earthquake Dataset, deprem ve gürültü tespiti araştırmaları için etiketlenmiş bir milyondan fazla sismik dalga formu örneği. CC-BY-4.0.
- [Engineering Strong Motion Database](https://esm-db.eu/) - Avrupa ve Orta Doğu'daki depremler için işlenmiş kuvvetli yer hareketi dalga formları ve üst verisi.
- [National Bridge Inventory](https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm) - Amerika Birleşik Devletleri'ndeki 600.000'den fazla köprü için durum puanları ve yapısal özniteliklerle yıllık FHWA kayıtları.
- [LTPP InfoPave](https://infopave.fhwa.dot.gov/) - Üstyapı yapısı, trafik, iklim ve bozulmalar üzerine Long Term Pavement Performance programı verisi.
- [xBD](https://xview2.org/) - Bina hasar etiketli, afet öncesi ve sonrası uydu görüntü çiftleri, xView2 yarışmasının arkasındaki veri seti.
- [SDNET2018](https://digitalcommons.usu.edu/all_datasets/48/) - Çatlaklı ve sağlam beton köprü tabliyeleri, duvarlar ve kaplamalara ait 56.000'den fazla etiketli görüntü.
- [OpenTopography](https://opentopography.org/) - Yüksek çözünürlüklü topoğrafya portalı, lidar nokta bulutları ve küresel yükseklik modelleri barındırır.

## Öğrenme kaynakları

- [MUDE](https://github.com/TUDelft-MUDE/book#readme) - TU Delft inşaat mühendisliği ve yer bilimleri yüksek lisans programlarının temel modülü olan Modelling, Uncertainty and Data for Engineers için açık ders kitabı. Sayısal modelleme, olasılık, güvenilirlik ve veri analizini çözümlü Python örnekleriyle işler. CC-BY-4.0.
- [comet-fenicsx](https://github.com/bleyerj/comet-fenicsx#readme) - FEniCSx ile hesaplamalı mekanik üzerine sayısal turlar, doğrusal elastisite, kirişler ve plaklardan plastisite, burkulma ve dinamiğe uzanan çözümlü örnekler. CC-BY-SA-4.0.
- [CE394M](https://github.com/kks32-courses/ce394m#readme) - UT Austin'in geoteknik mühendisliğinde ileri analiz dersinin not defterleri, sonlu eleman yöntemini, bünye modellerini ve konsolidasyonu kapsar. CC-BY-SA-4.0.
- [soil_mechanics](https://github.com/AppliedMechanics-EAFIT/soil_mechanics#readme) - EAFIT Üniversitesi lisans zemin mekaniği dersi için Jupyter Book olarak düzenlenmiş notlar ve etkileşimli not defterleri. Dili İspanyolca. MIT.
- [slope_stability](https://github.com/AppliedMechanics-EAFIT/slope_stability#readme) - EAFIT Üniversitesi lisansüstü şev stabilitesi dersi için dijital kitap ve tekrarlanabilir araçlar. Dili İspanyolca. MIT.
- [Hydro-Informatics](https://github.com/hydro-informatics/jupyter-python-course#readme) - hydro-informatics.com üzerindeki Python derslerinin arkasındaki not defterleri, su kaynakları ve hidrolik mühendisleri için yazılmıştır. MIT.
- [Introduction to GIS Programming](https://github.com/giswqs/geog-312#readme) - Tennessee Üniversitesi'nin Python ve açık kaynak coğrafi kütüphanelerle GIS programlama dersi. CC-BY-4.0.
- [Automating GIS Processes](https://github.com/Automating-GIS-processes/site#readme) - Helsinki Üniversitesi'nin Python ile coğrafi analiz dersi, dersler ve alıştırmalar not defteri olarak sunulur. MIT.
- [Geocomputation with Python](https://github.com/geocompx/geocompy#readme) - Python'da vektör ve raster coğrafi veriyle çalışma üzerine açık kitap. Yalnızca ticari olmayan kullanım. CC-BY-NC-SA-4.0.

Deprem mühendisliği, yapı dinamiği ve BIM için açık ders malzemesi burada hâlâ eksik, pull request'ler memnuniyetle karşılanır.

## Türkiye

Türkiye'deki açık kaynak inşaat ve altyapı mühendisliği çalışmaları hâlâ çok sayıda küçük, tek yazarlı projeye dağılmış durumda ve bunların çoğu AFAD veya Kandilli Rasathanesi API'lerinin ince sarmalayıcıları. Aşağıdakiler, tek seferlik bir bildirim botu olmanın ötesinde gerçek mühendislik veya veri içeriği taşıyan projelerdir.

- [Turkiye Deprem Verisi](https://github.com/Ayberkrk/turkiye-deprem-verisi#readme) - Türkiye için gerçek dalga formları ve yer hareketi parametreleriyle (PGA, PGV, Vs30) derlenmiş açık deprem veri seti, canlı uyarı için değil tekrarlanabilir sismik araştırma için hazırlanmıştır. Python, MIT.
- [turkiye-heat-risk](https://github.com/Ayberkrk/turkiye-heat-risk#readme) - Landsat yer yüzey sıcaklığını, OpenStreetMap yol ağını ve demografik veriyi sokak düzeyinde bir sıcaklık duyarlılık indeksinde birleştiren, kentten bağımsız ve tekrarlanabilir kentsel sıcaklık riski iş akışı. Şu an Izmir, Eskisehir ve Sanliurfa destekleniyor. Python, MIT.
- [cauren](https://github.com/Ayberkrk/cauren#readme) - İnşaat altyapısında anomali tespitini fizik tabanlı akıl yürütmeyle birleştiren açıklanabilir risk tanılaması, gerçek FHWA köprü denetim verisiyle eğitilmiştir. Python, Apache-2.0.
- [afet-org](https://github.com/acikyazilimagi/afet-org#readme) - Şubat 2023 depremlerine verilen en büyük sivil teknoloji yanıtı olan [acikyazilimagi](https://github.com/acikyazilimagi) organizasyonunun parçası. Deprem yardım lojistiği, ihtiyaç eşleştirme ve gönüllü koordinasyonunu kapsayan onlarca depo. Yapı mühendisliğinden çok afet müdahale araçları, ancak bir Türkiye depreminden çıkan en büyük ve en etkin açık kaynak kümesi. Apache-2.0.
- [AFAD TADAS EQ Record Processing](https://github.com/DemirAydin/AFAD-TADAS-EQ-Record-Processing#readme) - AFAD'ın Türkiye İvme Veri Tabanı ve Analiz Sistemi'nden (TADAS) kuvvetli yer hareketi kayıtlarını işler. Türkiye'nin açık sismik verisinin gerçekten mühendislik odaklı bir kullanımı. Python, MIT.
- [TSC2018_Design](https://github.com/muhammedsural/TSC2018_Design#readme) - Türkiye Bina Deprem Yönetmeliği (TBDY 2018) ve TS500 için Python paketi, tasarım spektrumlarını, sargılı beton modellerini ve kolon sargı donatısı tasarımını kapsar. Son güncelleme 2024. Python, MIT.
- [sap2000-tbdy2018](https://github.com/krmsari/sap2000-tbdy2018#readme) - TS500 ve TBDY 2018'e uygun parametrik SAP2000 modelleri üreten açık kaynak Windows uygulaması. Araç açık, SAP2000'in kendisi ticaridir. C#, MIT.
- [2023-Turkey-EQ](https://github.com/yunjunz/2023-Turkey-EQ#readme) - 2023 Kahramanmaraş depreminin ALOS-2, LuTan-1 ve Sentinel-1 radar görüntülerinden elde edilen kosismik yer deformasyonu için not defterleri ve veri. Python, Apache-2.0.
- [kandilli-rasathanesi-api](https://github.com/orhanayd/kandilli-rasathanesi-api#readme) - Kandilli Rasathanesi ve AFAD deprem verisini gerçek zamanlı akışlar, GeoJSON çıktısı ve kente veya yakınlığa göre süzmeyle birleştiren ücretsiz, etkin bakımı yapılan API. Çok sayıdaki AFAD ve Kandilli veri sarmalayıcısı arasında en bakımlı olanı. Kaynak kodu, izinsiz ticari kullanımı yasaklayan özel bir lisansla herkese açık. JavaScript, Custom.
- [tdvms_py](https://github.com/rdno/tdvms_py#readme) - AFAD'ın TDVMS ağından sürekli sismik dalga formu verisi istemek için küçük bir Python betiği, sismoloji ve saha tepkisi araştırmaları için yapı taşı olarak kullanışlıdır. Python, GPL-3.0.

## Benzer awesome listeleri

Bu liste aşağıdakileri bilerek tekrarlamaz. Komşu kapsamlar için onlara göz atın.

- [awesome-civil-engineering](https://github.com/QuantumNovice/awesome-civil-engineering#readme) - SAP2000, Revit ve Civil 3D gibi ticari yazılımları da içeren çok daha geniş bir liste. Açık kaynak araçlarla sınırlı değilseniz kullanışlıdır.
- [Awesome-AECO](https://github.com/osama-ata/Awesome-AECO#readme) - Açık kaynak odaklı, BIM, CAD ve akıllı bina araçlarında güçlü. Deprem mühendisliğini, yapı sağlığı izlemeyi veya veri setlerini kapsamaz.
- [Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial#readme) - Çok büyük, genel amaçlı bir coğrafi liste, inşaat mühendisliğiyle sınırlı değildir.
- [awesome-gis](https://github.com/sshuair/awesome-gis#readme) - Bir başka geniş, genel GIS listesi.

## Katkı

Katkılar memnuniyetle karşılanır. Pull request göndermeden önce lütfen [contributing.md](contributing.md) dosyasını okuyun. Kısaca: proje açık kaynak olmalı (ya da lisans kısıtı girişte belirtilmeli), inşaat veya altyapı mühendisliğiyle (ya da doğrudan komşu bir disiplinle) ilgili olmalı ve yeni başlayan birinin ne yaptığını ve nasıl çalıştırılacağını anlayabileceği kadar iyi belgelenmiş olmalıdır. Yeni girişleri yalnızca İngilizce [README.md](README.md) dosyasına eklemeniz yeterlidir, Türkçe çeviri bakımcılar tarafından güncellenir.
