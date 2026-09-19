# Awesome Digital Civil Engineering [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of open source tools, libraries, datasets and projects at the intersection of civil and infrastructure engineering, geospatial analysis, structural engineering, BIM and digital twins. Global projects, plus a dedicated section for Turkiye.

**Inclusion criteria:** every project listed here must be open source, relevant to civil or infrastructure engineering (or a directly adjacent discipline such as geospatial analysis or earthquake engineering), and maintained or documented well enough that a newcomer can tell what it does and how to run it.

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

## Structural Analysis and FEM

- [OpenSees](https://github.com/OpenSees/OpenSees#readme) - Reference open source framework for nonlinear structural and geotechnical simulation, developed at UC Berkeley. Base of most academic earthquake engineering research code, and the primary simulation engine used across the Earthquake Engineering section below.
- [Pynite](https://github.com/JWock82/Pynite#readme) - 3D structural engineering finite element library in Python for beams, frames, plates, load combinations and P Delta analysis. Formerly named PyNite.
- [anaStruct](https://github.com/ritchie46/anaStruct#readme) - 2D structural analysis in Python, suited for quick frame and truss checks without a full FEM stack.
- [section-properties](https://github.com/robbievanleeuwen/section-properties#readme) - Finite element analysis of arbitrary cross sections in Python. Computes warping constants, shear areas and other properties most standard tools do not expose.
- [concrete-properties](https://github.com/robbievanleeuwen/concrete-properties#readme) - Section analysis for reinforced concrete, moment curvature and interaction diagrams, built on top of section-properties.
- [COMPAS](https://github.com/compas-dev/compas#readme) - Computational framework for research and collaboration in architecture, structures and digital fabrication, with CAD integrations for Rhino, Grasshopper and Blender.
- [CalculiX](http://www.calculix.de/) - Free finite element package for linear and nonlinear structural, dynamic and thermal analysis with an Abaqus compatible input format.
- [SfePy](https://github.com/sfepy/sfepy#readme) - Simple finite elements in Python, a general purpose FEM solver for structural, mechanical and coupled physics problems.

## Earthquake Engineering

- [OpenQuake Engine](https://github.com/gem/oq-engine#readme) - Seismic hazard and risk analysis software from the Global Earthquake Model Foundation, used by national hazard agencies worldwide.
- [quoFEM](https://github.com/NHERI-SimCenter/quoFEM#readme) - NHERI SimCenter desktop application that adds uncertainty quantification and optimization routines on top of FEM applications, commonly paired with OpenSees.
- [SimCenterBackendApplications](https://github.com/NHERI-SimCenter/SimCenterBackendApplications#readme) - Backend workflow applications behind the NHERI SimCenter natural hazards engineering tools.
- [eqsig](https://github.com/eng-tools/eqsig#readme) - Signal processing for earthquake engineering, computes response spectra, Fourier spectra and other ground motion intensity measures from field and experimental data.

## Structural Health Monitoring

- [pyOMA2](https://github.com/dagghe/pyOMA2#readme) - Operational modal analysis in Python, extracts natural frequencies, damping ratios and mode shapes from ambient vibration data. Actively maintained successor to the original PyOMA.
- [koma](https://github.com/knutankv/koma#readme) - Operational modal analysis toolbox built for and used in real bridge and civil structure monitoring research.
- [OpenModal](https://github.com/openmodal/OpenModal#readme) - Desktop application for experimental modal analysis with a full GUI. Not actively maintained since 2021, but still one of the few complete open source EMA tools.
- [python-acoustics](https://github.com/python-acoustics/python-acoustics#readme) - Signal processing library aimed at acousticians. A useful building block for vibration and modal analysis pipelines (FFT, filtering, weighting).

This category is still thin compared to the rest of the list. If you know of a maintained, documented open source SHM project, please open a pull request, this is one of the sections where the list can add the most value.

## BIM and IFC

- [IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell#readme) - Open source IFC library and geometry engine. Base of nearly every other open BIM tool, including the Bonsai (formerly BlenderBIM) add on.
- [web-ifc](https://github.com/ThatOpen/engine_web-ifc#readme) - Reads and writes IFC files in the browser at native speed via WebAssembly, from the That Open Company ecosystem.
- [BIMserver](https://github.com/opensourceBIM/BIMserver#readme) - Open source BIM model server. Stores and manages IFC models with versioning and multi user collaboration.
- [xBIM Toolkit](https://github.com/xBimTeam/XbimEssentials#readme) - Open source .NET toolkit for reading, creating, validating and querying IFC building models.
- [IFC4.x-development](https://github.com/buildingSMART/IFC4.x-development#readme) - buildingSMART's own repository for the IFC4.x specification, the standard that every tool above implements.
- [Speckle](https://github.com/specklesystems/speckle-server#readme) - Open source data platform for AEC interoperability, streams geometry and data between design tools in real time, often described as version control for BIM.

## Digital Twins

- [iTwin.js](https://github.com/iTwin/itwinjs-core#readme) - Bentley's open source library for building and visualizing infrastructure digital twins. Ties directly into BIM, GIS and reality capture data.
- [Cesium](https://github.com/CesiumGS/cesium#readme) - Open source JavaScript engine for 3D globes and maps, widely used as the visualization layer under infrastructure and city scale digital twins.
- [PlayCanvas](https://github.com/playcanvas/engine#readme) - Open source WebGL game engine also used for interactive 3D visualization and digital twin front ends.
- [Eclipse Ditto](https://github.com/eclipse-ditto/ditto#readme) - General purpose digital twin framework from Eclipse IoT for managing the state and telemetry of physical assets, applicable beyond buildings to any monitored infrastructure asset.

## Geospatial and Remote Sensing

- [GeoPandas](https://github.com/geopandas/geopandas#readme) - Adds geospatial data types and operations to pandas. Standard entry point for vector GIS work in Python.
- [OSMnx](https://github.com/gboeing/osmnx#readme) - Downloads, models, analyzes and visualizes street networks and other geospatial features from OpenStreetMap. Also the base for the street network work referenced in Infrastructure and Urban Analytics below.
- [xarray](https://github.com/pydata/xarray#readme) - Labeled multi dimensional arrays in Python, the base for most raster and climate data workflows (satellite imagery, weather, hydrology).
- [Rasterio](https://github.com/rasterio/rasterio#readme) - Reads and writes geospatial raster datasets, built on GDAL.
- [leafmap](https://github.com/opengeos/leafmap#readme) - Interactive mapping and geospatial analysis with minimal code in Jupyter. Wraps several mapping backends under one API.
- [TorchGeo](https://github.com/torchgeo/torchgeo#readme) - Datasets, samplers, transforms and pretrained models for applying deep learning to geospatial and satellite data.

## Infrastructure and Urban Analytics

- [Eclipse SUMO](https://github.com/eclipse-sumo/sumo#readme) - Open source, microscopic and continuous traffic simulation package that handles large road networks, including pedestrians.
- [MATSim](https://github.com/matsim-org/matsim-libs#readme) - Agent based multi agent transport simulation framework used for large scale mobility and infrastructure demand studies.
- [UrbanSim](https://github.com/UDST/urbansim#readme) - Simulation platform for modeling land use, real estate and transportation interactions at the metropolitan scale.
- [ActivitySim](https://github.com/ActivitySim/activitysim#readme) - Open platform for activity based travel demand modeling, used by metropolitan planning organizations for infrastructure and transportation planning.
- [momepy](https://github.com/pysal/momepy#readme) - Urban morphology measuring toolkit, quantifies street networks, building form and urban structure from geospatial data.

## AI and Machine Learning for Civil Engineering

- [DeepCrack](https://github.com/yhlleo/DeepCrack#readme) - Deep hierarchical feature learning architecture for crack segmentation on structural surfaces, with code and paper.
- [crack_segmentation](https://github.com/khanhha/crack_segmentation#readme) - Crack segmentation using UNet VGG16, UNet ResNet and Tiramisu architectures. Includes a compiled dataset.
- [xView2 baseline](https://github.com/DIUx-xView/xView2_baseline#readme) - Baseline localization and damage classification models for the xView2 building damage assessment challenge, using satellite imagery from before and after a disaster.

## Climate and Resilience

- [pyincore](https://github.com/IN-CORE/pyincore#readme) - Python client for IN-CORE, a community resilience modeling environment that propagates hazard damage on infrastructure through to social and economic impact.
- [MODFLOW 6](https://github.com/MODFLOW-ORG/modflow6#readme) - USGS open source modular hydrologic model for groundwater flow and groundwater and surface water interaction, relevant to flood and drought resilience studies.
- [Brightway](https://github.com/brightway-lca/brightway2#readme) - Open source Python framework for life cycle assessment, used to evaluate the environmental footprint of infrastructure and construction materials.
- [CLIMADA](https://github.com/CLIMADA-project/climada_python#readme) - Open source framework for climate risk assessment and adaptation option appraisal, models hazard, exposure and vulnerability for infrastructure and other assets.
- [City Energy Analyst](https://github.com/architecture-building-systems/CityEnergyAnalyst#readme) - Urban building energy modeling platform for designing low carbon, energy efficient neighborhoods and cities.
- [EnergyPlus](https://github.com/NatLabRockies/EnergyPlus#readme) - The US DOE's whole building energy simulation engine, models heating, cooling, lighting and water use for individual buildings.
- [OpenStudio](https://github.com/NatLabRockies/OpenStudio#readme) - Cross platform tools built on top of EnergyPlus and Radiance for whole building energy modeling and daylight analysis.

## Open Datasets

- [Global ML Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints#readme) - Building footprint polygons for most of the world, derived from satellite imagery.
- [STEAD](https://github.com/smousavi05/STEAD#readme) - Stanford Earthquake Dataset, over one million seismic waveform samples labeled for earthquake and noise detection research.

## Turkiye

Open source civil and infrastructure engineering activity in Turkiye is still scattered across many small, single author projects, mostly thin wrappers around the AFAD or Kandilli observatory APIs. The entries below are the ones with real engineering or data substance rather than a one off notification bot.

- [Turkiye Deprem Verisi](https://github.com/Ayberkrk/turkiye-deprem-verisi#readme) - Compiled, open earthquake dataset for Turkiye with real waveforms and ground motion parameters (PGA, PGV, Vs30), built for reproducible seismic research rather than live alerting.
- [izmir-heat-risk](https://github.com/Ayberkrk/izmir-heat-risk#readme) - Reproducible urban heat risk pipeline that combines Landsat land surface temperature, OpenStreetMap road network and demographic data into a street level heat sensitivity index. Currently supports Izmir and Eskisehir, architected to extend to other cities.
- [cauren](https://github.com/Ayberkrk/cauren#readme) - Explainable risk diagnostics for civil infrastructure anomaly detection combined with physics based reasoning, trained on real FHWA bridge inspection data.
- [afet-org](https://github.com/acikyazilimagi/afet-org#readme) - Part of the wider [acikyazilimagi](https://github.com/acikyazilimagi) organization, the largest civic tech response to the February 2023 earthquakes. Dozens of repositories covering earthquake relief logistics, needs matching and volunteer coordination. Mostly disaster response tooling rather than structural engineering, but the largest and most active open source cluster to come out of a Turkish earthquake.
- [AFAD TADAS EQ Record Processing](https://github.com/DemirAydin/AFAD-TADAS-EQ-Record-Processing#readme) - Processes strong ground motion records from AFAD's Turkish Accelerometric Database and Analysis System (TADAS). A genuinely engineering focused use of Turkish open seismic data.
- [kandilli-rasathanesi-api](https://github.com/orhanayd/kandilli-rasathanesi-api#readme) - Free, open source, actively maintained API that merges Kandilli Observatory and AFAD earthquake data with real time feeds, GeoJSON output and filtering by city or proximity. The most maintained of the many AFAD and Kandilli data wrapper projects.
- [tdvms_py](https://github.com/rdno/tdvms_py#readme) - Small Python script to request continuous seismic waveform data from AFAD's TDVMS network, useful as a building block for seismology and site response research.

## Related Awesome Lists

This list intentionally does not duplicate the following. Check them out for adjacent scope.

- [awesome-civil-engineering](https://github.com/QuantumNovice/awesome-civil-engineering#readme) - Much broader list that also includes commercial software such as SAP2000, Revit and Civil 3D. Useful if you are not restricted to open source tools.
- [Awesome-AECO](https://github.com/osama-ata/Awesome-AECO#readme) - Open source focused, strong on BIM, CAD and smart building tooling. Does not cover earthquake engineering, structural health monitoring or datasets.
- [Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial#readme) - Very large general purpose geospatial list, not scoped to civil engineering.
- [awesome-gis](https://github.com/sshuair/awesome-gis#readme) - Another broad, general GIS list.

## Contributing

Contributions are welcome. Please read [contributing.md](contributing.md) before submitting a pull request. In short: the project must be open source, must be relevant to civil or infrastructure engineering (or a directly adjacent discipline), and must have documentation good enough that a newcomer can tell what it does and how to run it.
