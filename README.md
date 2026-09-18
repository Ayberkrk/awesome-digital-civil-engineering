# Awesome Digital Civil Engineering

A curated list of open source tools, libraries, datasets and projects at the intersection of civil/infrastructure engineering, geospatial analysis, structural engineering, BIM and digital twins. Global projects plus a dedicated section for Turkiye.

**Inclusion criteria:** every project listed here must be open source, relevant to civil/infrastructure engineering (or a directly adjacent discipline such as geospatial analysis or earthquake engineering), and sufficiently documented or usable (a README that explains what the tool does and how to run it, at minimum). Pure research code with no documentation and abandoned, unmaintained wrappers are not included.

## Contents

- [Structural Analysis and FEM](#structural-analysis-and-fem)
- [Earthquake Engineering](#earthquake-engineering)
- [Structural Health Monitoring](#structural-health-monitoring)
- [BIM and IFC](#bim-and-ifc)
- [Digital Twins](#digital-twins)
- [Geospatial and Remote Sensing](#geospatial-and-remote-sensing)
- [Infrastructure and Urban Analytics](#infrastructure-and-urban-analytics)
- [AI and Machine Learning for Civil Engineering](#ai-and-machine-learning-for-civil-engineering)
- [Climate and Resilience](#climate-and-resilience)
- [Open Datasets](#open-datasets)
- [Turkiye](#turkiye)
- [Related Awesome Lists](#related-awesome-lists)
- [Contributing](#contributing)

## Structural Analysis and FEM

- [OpenSees](https://github.com/OpenSees/OpenSees). The reference open source framework for nonlinear structural and geotechnical simulation, developed at UC Berkeley. The base of most academic earthquake engineering research code.
- [Pynite](https://github.com/JWock82/Pynite) (formerly PyNite). A 3D structural engineering finite element library in Python for beams, frames, plates, load combinations and P Delta analysis.
- [anaStruct](https://github.com/ritchie46/anaStruct). 2D structural analysis in Python, good for quick frame and truss checks without a full FEM stack.
- [section-properties](https://github.com/robbievanleeuwen/section-properties). Finite element analysis of arbitrary cross sections in Python, computes warping constants, shear areas and other properties standard tools do not expose.
- [concrete-properties](https://github.com/robbievanleeuwen/concrete-properties). Section analysis for reinforced concrete, moment curvature and interaction diagrams, built on top of section-properties.
- [COMPAS](https://github.com/compas-dev/compas). A computational framework for research and collaboration in architecture, structures and digital fabrication, with CAD integrations for Rhino, Grasshopper and Blender.
- [CalculiX](http://www.calculix.de/). A free finite element package for linear and nonlinear structural, dynamic and thermal analysis with an Abaqus compatible input format.

## Earthquake Engineering

- [OpenQuake Engine](https://github.com/gem/oq-engine). Developed by the Global Earthquake Model Foundation, software for seismic hazard and risk analysis used by national hazard agencies worldwide.
- [OpenSees](https://github.com/OpenSees/OpenSees). Also the core simulation engine for nonlinear seismic response of structures and soil.
- [quoFEM](https://github.com/NHERI-SimCenter/quoFEM). NHERI SimCenter desktop application that adds uncertainty quantification and optimization routines on top of FEM applications, commonly paired with OpenSees.
- [SimCenterBackendApplications](https://github.com/NHERI-SimCenter/SimCenterBackendApplications). Backend workflow applications behind the NHERI SimCenter natural hazards engineering tools.

## Structural Health Monitoring

- [PyOMA](https://github.com/dagghe/PyOMA). Operational modal analysis in Python, extracts natural frequencies, damping ratios and mode shapes from ambient vibration data.
- [python-acoustics](https://github.com/python-acoustics/python-acoustics). A signal processing library aimed at acousticians, useful building block for vibration and modal analysis pipelines (FFT, filtering, weighting).

This category is genuinely thin across the whole open source ecosystem right now. If you know of a maintained, documented open source SHM project, please open a PR, this is one of the sections where this list can add the most value.

## BIM and IFC

- [IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell). The open source IFC library and geometry engine, the base of nearly every other open BIM tool including the Bonsai (formerly BlenderBIM) add on.
- [web-ifc](https://github.com/ThatOpen/engine_web-ifc). Reads and writes IFC files in the browser at native speed via WebAssembly, from the That Open Company ecosystem.
- [BIMserver](https://github.com/opensourceBIM/BIMserver). Open source BIM model server, stores and manages IFC models with versioning and multi user collaboration.
- [xBIM Toolkit](https://github.com/xBimTeam/XbimEssentials). An open source .NET toolkit for reading, creating, validating and querying IFC building models.
- [IFC4.x-development](https://github.com/buildingSMART/IFC4.x-development). buildingSMART's own repository for the IFC4.x specification, the standard that every tool above implements.

## Digital Twins

- [iTwin.js](https://github.com/iTwin/itwinjs-core). Bentley's open source library for building and visualizing infrastructure digital twins, ties directly into BIM, GIS and reality capture data.
- [Cesium](https://github.com/CesiumGS/cesium). The open source JavaScript engine for 3D globes and maps, widely used as the visualization layer under infrastructure and city scale digital twins.
- [PlayCanvas](https://github.com/playcanvas/engine). An open source WebGL game engine also used for interactive 3D visualization and digital twin front ends.

## Geospatial and Remote Sensing

- [GeoPandas](https://github.com/geopandas/geopandas). Adds geospatial data types and operations to pandas, the standard entry point for vector GIS work in Python.
- [OSMnx](https://github.com/gboeing/osmnx). Downloads, models, analyzes and visualizes street networks and other geospatial features from OpenStreetMap, heavily used in transportation and urban analytics.
- [xarray](https://github.com/pydata/xarray). Labeled multi dimensional arrays in Python, the base for most raster and climate data workflows (satellite imagery, weather, hydrology).
- [Rasterio](https://github.com/rasterio/rasterio). Reads and writes geospatial raster datasets, built on GDAL.
- [leafmap](https://github.com/opengeos/leafmap). Interactive mapping and geospatial analysis with minimal code in Jupyter, wraps several mapping backends under one API.
- [TorchGeo](https://github.com/torchgeo/torchgeo). Datasets, samplers, transforms and pretrained models for applying deep learning to geospatial and satellite data.

## Infrastructure and Urban Analytics

- [Eclipse SUMO](https://github.com/eclipse-sumo/sumo). Open source, microscopic and continuous traffic simulation package that handles large road networks including pedestrians.
- [MATSim](https://github.com/matsim-org/matsim-libs). Agent based multi agent transport simulation framework used for large scale mobility and infrastructure demand studies.
- [OSMnx](https://github.com/gboeing/osmnx). Also central here: street network analysis, connectivity and accessibility metrics for urban infrastructure research.

## AI and Machine Learning for Civil Engineering

- [DeepCrack](https://github.com/yhlleo/DeepCrack). A deep hierarchical feature learning architecture for crack segmentation on structural surfaces, with code and paper.
- [crack_segmentation](https://github.com/khanhha/crack_segmentation). Crack segmentation using UNet VGG16, UNet ResNet and Tiramisu architectures, includes a compiled dataset.
- [xView2 baseline](https://github.com/DIUx-xView/xView2_baseline). Baseline localization and damage classification models for the xView2 building damage assessment challenge, satellite imagery before and after a disaster.
- [Global ML Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints). Worldwide building footprints extracted from satellite imagery with machine learning, released by Microsoft, directly usable as an infrastructure inventory input.

## Climate and Resilience

- [pyincore](https://github.com/IN-CORE/pyincore). Python client for IN-CORE, a community resilience modeling environment that propagates hazard damage on infrastructure through to social and economic impact.
- [MODFLOW 6](https://github.com/MODFLOW-ORG/modflow6). USGS open source modular hydrologic model for groundwater flow and groundwater and surface water interaction, relevant to flood and drought resilience studies.
- [Brightway](https://github.com/brightway-lca/brightway2). Open source Python framework for life cycle assessment, used to evaluate the environmental footprint of infrastructure and construction materials.

## Open Datasets

- [Global ML Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints). Building footprint polygons for most of the world, derived from satellite imagery.
- [xView2 dataset](https://github.com/DIUx-xView/xview2-baseline) (see repository for dataset access). Pre and post disaster satellite imagery pairs with building damage labels.
- [Turkiye Deprem Verisi](https://github.com/Ayberkrk/turkiye-deprem-verisi). An open earthquake dataset compiled specifically for Turkiye from public sources: over 84,000 events with real waveforms, PGA, PGV and Vs30.

## Turkiye

Open source civil/infrastructure engineering activity in Turkiye is still scattered across many small, single author projects (mostly thin wrappers around the AFAD or Kandilli observatory APIs). The entries below are the ones with real engineering or data substance rather than a one off notification bot.

- [Turkiye Deprem Verisi](https://github.com/Ayberkrk/turkiye-deprem-verisi). Compiled, open earthquake dataset for Turkiye with real waveforms and ground motion parameters (PGA, PGV, Vs30), built for reproducible seismic research rather than live alerting.
- [izmir-heat-risk](https://github.com/Ayberkrk/izmir-heat-risk). A reproducible urban heat risk pipeline that combines Landsat land surface temperature, OpenStreetMap road network and demographic data into a street level heat sensitivity index. Currently supports Izmir and Eskisehir, architected to extend to other cities.
- [cauren](https://github.com/Ayberkrk/cauren). Explainable risk diagnostics for civil infrastructure anomaly detection combined with physics based reasoning, trained on real FHWA bridge inspection data.
- [afet-org](https://github.com/acikyazilimagi/afet-org) and the wider [acikyazilimagi](https://github.com/acikyazilimagi) organization. The largest civic tech response to the February 2023 earthquakes, dozens of repositories covering earthquake relief logistics, needs matching and volunteer coordination. Mostly disaster response tooling rather than structural engineering, but the largest and most active open source cluster to come out of a Turkish earthquake.
- [AFAD TADAS EQ Record Processing](https://github.com/DemirAydin/AFAD-TADAS-EQ-Record-Processing). Processes strong ground motion records from AFAD's Turkish Accelerometric Database and Analysis System (TADAS), a genuinely engineering focused use of Turkish open seismic data.
- [kandilli-rasathanesi-api](https://github.com/orhanayd/kandilli-rasathanesi-api). A free, open source, actively maintained API that merges Kandilli Observatory and AFAD earthquake data with real time feeds, GeoJSON output and filtering by city or proximity. The most maintained of the many AFAD and Kandilli data wrapper projects.
- [tdvms_py](https://github.com/rdno/tdvms_py). A small Python script to request continuous seismic waveform data from AFAD's TDVMS network, useful as a building block for seismology and site response research.

## Related Awesome Lists

This list intentionally does not duplicate the following. Check them out for adjacent scope.

- [awesome-civil-engineering](https://github.com/QuantumNovice/awesome-civil-engineering). A much broader list that also includes commercial software (SAP2000, Revit, Civil 3D and similar), useful if you are not restricted to open source tools.
- [Awesome-AECO](https://github.com/osama-ata/Awesome-AECO). Open source focused, strong on BIM, CAD and smart building tooling, does not cover earthquake engineering, structural health monitoring or datasets.
- [Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial). A very large general purpose geospatial list, not scoped to civil engineering.
- [awesome-gis](https://github.com/sshuair/awesome-gis). Another broad, general GIS list.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request. In short: the project must be open source, must be relevant to civil or infrastructure engineering (or a directly adjacent discipline), and must have documentation good enough that a newcomer can tell what it does and how to run it.

## License

[CC0](LICENSE). To the extent possible under law, the contributors have waived all copyright and related rights to this list.
