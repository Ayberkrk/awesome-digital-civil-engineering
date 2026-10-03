# Awesome Digital Civil Engineering [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of open source tools, libraries, datasets and projects at the intersection of civil and infrastructure engineering, structural and geotechnical engineering, water and hydraulics, geospatial analysis, reality capture, BIM and digital twins. Global projects, plus a dedicated section for Turkiye.

English | [Türkçe](README.tr.md)

![Overview of the open source digital civil engineering list](media/social-preview.png)

**Inclusion criteria:** every project listed here must be open source, or have its source or content publicly available with any license restriction stated in its entry. It must be relevant to civil or infrastructure engineering (or a directly adjacent discipline such as geospatial analysis or earthquake engineering) and maintained or documented well enough that a newcomer can tell what it does and how to run it.

## Contents

- [Structural Analysis and FEM](#structural-analysis-and-fem)
- [Design Codes and Calculation Tools](#design-codes-and-calculation-tools)
- [Earthquake Engineering](#earthquake-engineering)
- [Geotechnical Engineering](#geotechnical-engineering)
- [Structural Health Monitoring](#structural-health-monitoring)
- [BIM and IFC](#bim-and-ifc)
- [CAD and Parametric Modeling](#cad-and-parametric-modeling)
- [Digital Twins](#digital-twins)
- [Point Clouds and Photogrammetry](#point-clouds-and-photogrammetry)
- [Geospatial and Remote Sensing](#geospatial-and-remote-sensing)
- [Water and Hydraulics](#water-and-hydraulics)
- [Infrastructure and Urban Analytics](#infrastructure-and-urban-analytics)
- [AI and Machine Learning for Civil Engineering](#ai-and-machine-learning-for-civil-engineering)
- [Climate and Resilience](#climate-and-resilience)
- [Open Datasets](#open-datasets)
- [Learning Resources](#learning-resources)
- [Turkiye](#turkiye)
- [Related Awesome Lists](#related-awesome-lists)

## Structural Analysis and FEM

- [OpenSees](https://github.com/OpenSees/OpenSees#readme) - Reference framework for nonlinear structural and geotechnical simulation, developed at UC Berkeley. Base of most academic earthquake engineering research code, and the primary simulation engine used across the Earthquake Engineering section below. The source is public, but the license limits use to noncommercial and internal purposes, commercial distribution needs a separate license. C++, Custom.
- [OpenSeesPy](https://github.com/zhuminjie/OpenSeesPy#readme) - Python interpreter build of OpenSees distributed through pip, the usual entry point for scripting OpenSees models today. Carries the same license restrictions as OpenSees. Python, Custom.
- [opstool](https://github.com/yexiang92/opstool#readme) - Pre processing, post processing and visualization helpers for OpenSeesPy models, including fiber section meshing and result plotting. Python, GPL-3.0.
- [ospgrillage](https://github.com/ssp-research/ospgrillage#readme) - Builds bridge deck grillage models on top of OpenSeesPy, with moving load and load combination support. Python, MIT.
- [Pynite](https://github.com/JWock82/Pynite#readme) - 3D structural engineering finite element library in Python for beams, frames, plates, load combinations and P Delta analysis. Formerly named PyNite. Python, MIT.
- [anaStruct](https://github.com/anastruct/anaStruct#readme) - 2D structural analysis in Python, suited for quick frame and truss checks without a full FEM stack. Python, LGPL-3.0.
- [PyCBA](https://github.com/ccaprani/pycba#readme) - Continuous beam analysis in Python with influence lines and moving vehicle envelopes, aimed at bridge assessment. Python, AGPL-3.0.
- [section-properties](https://github.com/robbievanleeuwen/section-properties#readme) - Finite element analysis of arbitrary cross sections in Python. Computes warping constants, shear areas and other properties most standard tools do not expose. Python, MIT.
- [concrete-properties](https://github.com/robbievanleeuwen/concrete-properties#readme) - Section analysis for reinforced concrete, moment curvature and interaction diagrams, built on top of section-properties. Python, MIT.
- [COMPAS](https://github.com/compas-dev/compas#readme) - Computational framework for research and collaboration in architecture, structures and digital fabrication, with CAD integrations for Rhino, Grasshopper and Blender. Python, MIT.
- [CalculiX](https://www.calculix.de/) - Free finite element package for linear and nonlinear structural, dynamic and thermal analysis with an Abaqus compatible input format.
- [SfePy](https://github.com/sfepy/sfepy#readme) - Simple finite elements in Python, a general purpose FEM solver for structural, mechanical and coupled physics problems. Python, BSD-3-Clause.
- [DOLFINx](https://github.com/FEniCS/dolfinx#readme) - Computational core of the FEniCS project, solves partial differential equations with the finite element method from a high level Python or C++ interface. C++, LGPL-3.0.
- [Kratos Multiphysics](https://github.com/KratosMultiphysics/Kratos#readme) - Parallel multiphysics framework from CIMNE with structural, geomechanics, fluid and fluid structure interaction applications. C++, BSD-4-Clause.
- [XC](https://github.com/xcfem/xc#readme) - Finite element package written specifically for civil engineering structures, with code checking routines for concrete and steel members. C++, GPL-3.0.

## Design Codes and Calculation Tools

- [structuralcodes](https://github.com/fib-international/structuralcodes#readme) - Python library from fib (International Federation for Structural Concrete) that implements design code models such as Eurocode 2 and fib Model Code, together with section analysis. Python, Apache-2.0.
- [Blueprints](https://github.com/Blueprints-org/blueprints#readme) - Collection of Eurocode formulas, tables and checks as tested Python functions, each tied to the clause it implements. Python, MIT.
- [handcalcs](https://github.com/connorferster/handcalcs#readme) - Renders Python calculations as LaTeX with the symbolic formula, substituted values and result, the way a hand calculation sheet reads. Python, Apache-2.0.
- [forallpeople](https://github.com/connorferster/forallpeople#readme) - SI units library for engineering calculations that keeps units attached to values and simplifies them automatically. Python, Apache-2.0.
- [efficalc](https://github.com/youandvern/efficalc#readme) - Writes structural calculation reports from plain Python, with inputs, assumptions and checks laid out for review. Python, MIT.

## Earthquake Engineering

- [OpenQuake Engine](https://github.com/gem/oq-engine#readme) - Seismic hazard and risk analysis software from the Global Earthquake Model Foundation, used by national hazard agencies worldwide. Python, AGPL-3.0.
- [quoFEM](https://github.com/NHERI-SimCenter/quoFEM#readme) - NHERI SimCenter desktop application that adds uncertainty quantification and optimization routines on top of FEM applications, commonly paired with OpenSees. C++, BSD-2-Clause.
- [Pelicun](https://github.com/NHERI-SimCenter/pelicun#readme) - Probabilistic damage and loss estimation for buildings and infrastructure, implements the FEMA P-58 and Hazus methodologies. Python, BSD-3-Clause.
- [R2DTool](https://github.com/NHERI-SimCenter/R2DTool#readme) - NHERI SimCenter application for regional scale simulation of earthquake and hurricane damage across building and infrastructure inventories. C++, BSD-3-Clause.
- [OpenSHA](https://github.com/opensha/opensha#readme) - Java platform for seismic hazard analysis, the code base behind the UCERF earthquake rupture forecasts for California. Java, BSD-3-Clause.
- [eqsig](https://github.com/eng-tools/eqsig#readme) - Signal processing for earthquake engineering, computes response spectra, Fourier spectra and other ground motion intensity measures from field and experimental data. Python, MIT.
- [pyrotd](https://github.com/arkottke/pyrotd#readme) - Computes rotated response spectra such as RotD50 and RotD100 from two horizontal ground motion components. Python, MIT.
- [ObsPy](https://github.com/obspy/obspy#readme) - Python framework for seismology, reads and processes waveform data in every common format and talks to data center web services. Python, LGPL-3.0.
- [SeisBench](https://github.com/seisbench/seisbench#readme) - Toolbox for machine learning in seismology with benchmark datasets and pretrained phase picking models. Python, GPL-3.0.

## Geotechnical Engineering

- [pyStrata](https://github.com/arkottke/pystrata#readme) - Site response analysis in Python, covers equivalent linear and random vibration theory methods. Formerly named pysra. Python, MIT.
- [liquepy](https://github.com/eng-tools/liquepy#readme) - Soil liquefaction assessment tools, including CPT based triggering procedures and helpers for effective stress analysis. Python, MIT.
- [Groundhog](https://github.com/snakesonabrain/groundhog#readme) - General purpose geotechnical library covering site investigation data processing, soil correlations and foundation calculations. Python, GPL-3.0.
- [pygef](https://github.com/cemsbv/pygef#readme) - Parses CPT and borehole files in the GEF and BRO XML formats into dataframes and plots them. Python, MIT.
- [pySlope](https://github.com/JesseBonanno/PySlope#readme) - Slope stability analysis with Bishop's method of slices, supports layered soils, water tables and surcharge loads. Python, MIT.
- [OpenGeoSys](https://gitlab.opengeosys.org/ogs/ogs) - Finite element simulator for coupled thermo hydro mechanical and chemical processes in porous and fractured media.

## Structural Health Monitoring

- [pyOMA2](https://github.com/dagghe/pyOMA2#readme) - Operational modal analysis in Python, extracts natural frequencies, damping ratios and mode shapes from ambient vibration data. Actively maintained successor to the original PyOMA. Python, MIT.
- [koma](https://github.com/knutankv/koma#readme) - Operational modal analysis toolbox built for and used in real bridge and civil structure monitoring research. Python, MIT.
- [OpenModal](https://github.com/openmodal/OpenModal#readme) - Desktop application for experimental modal analysis with a full GUI. Not actively maintained since 2021, but still one of the few complete open source EMA tools. Python, GPL-3.0.
- [SDyPy](https://github.com/sdypy/sdypy#readme) - Umbrella package for structural dynamics in Python that bundles modal analysis, frequency response and excitation tools under one namespace. Python, MIT.
- [pyEMA](https://github.com/ladisk/pyEMA#readme) - Experimental and operational modal analysis from measured frequency response functions, using the LSCF and LSFD methods. Python, MIT.
- [pyidi](https://github.com/ladisk/pyidi#readme) - Identifies displacements from high speed camera footage, a base for camera based vibration measurement of structures. Python, MIT.
- [structural_health_monitoring](https://github.com/MarcoParola/structural_health_monitoring#readme) - Vibration-based structural damage localisation using IoT sensor data and machine learning, including autoencoder and convolutional models. Python, MIT.
- [FAT-SM](https://github.com/FAT-SM/App#readme) - Fatigue assessment tool for structural monitoring with stress-time processing, rainflow cycle counting, Miner's-rule damage accumulation and remaining fatigue life prediction. C++, GPL-3.0.
- [munich-bridge-data](https://github.com/imcs-compsim/munich-bridge-data#readme) - Visualisation and analysis routines for real test-bridge sensor data, with sample acceleration, strain, force and inclination measurements and preprocessing tools. Python, MIT.
- [BridgeScan-SHM](https://github.com/okimsz/BridgeScan-SHM#readme) - Real-time bridge structural health monitoring dashboard with telemetry ingestion, anomaly detection, historical sensor-data storage, WebSocket alerts and an edge inference pipeline. Python/TypeScript, MIT.

This category is still thin compared to the rest of the list. If you know of a maintained, documented open source SHM project, please open a pull request, this is one of the sections where the list can add the most value.

## BIM and IFC

- [IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell#readme) - Open source IFC library and geometry engine. Base of nearly every other open BIM tool, including the Bonsai (formerly BlenderBIM) add on. C++, LGPL-3.0.
- [web-ifc](https://github.com/ThatOpen/engine_web-ifc#readme) - Reads and writes IFC files in the browser at native speed via WebAssembly, from the That Open Company ecosystem. TypeScript, MPL-2.0.
- [That Open Components](https://github.com/ThatOpen/engine_components#readme) - Component library for building browser based BIM applications on top of web-ifc and Three.js. TypeScript, MIT.
- [xeokit SDK](https://github.com/xeokit/xeokit-sdk#readme) - WebGL viewer toolkit for large BIM and AEC models in the browser, with support for IFC, glTF and point cloud formats. JavaScript, AGPL-3.0.
- [BIMserver](https://github.com/opensourceBIM/BIMserver#readme) - Open source BIM model server. Stores and manages IFC models with versioning and multi user collaboration. Java, AGPL-3.0.
- [xBIM Toolkit](https://github.com/xBimTeam/XbimEssentials#readme) - Open source .NET toolkit for reading, creating, validating and querying IFC building models. C#, CDDL-1.0.
- [IFC4.x-development](https://github.com/buildingSMART/IFC4.x-development#readme) - buildingSMART's own repository for the IFC4.x specification, the standard that every tool above implements. Modified versions may not be redistributed. CC-BY-ND-4.0.
- [Speckle](https://github.com/specklesystems/speckle-server#readme) - Open source data platform for AEC interoperability, streams geometry and data between design tools in real time, often described as version control for BIM. Two server modules are under a separate enterprise license. TypeScript, Apache-2.0.
- [BHoM](https://github.com/BHoM/BHoM#readme) - Buildings and Habitats object Model, a shared data schema and set of adapters that connect structural, environmental and BIM software. C#, LGPL-3.0.
- [topologicpy](https://github.com/wassimj/topologicpy#readme) - Spatial modeling library that represents buildings as topological cells, faces and graphs for analysis. Python, LGPL-3.0.

## CAD and Parametric Modeling

- [FreeCAD](https://github.com/FreeCAD/FreeCAD#readme) - Parametric 3D modeler with built in BIM and FEM workbenches and a full Python API. C++, LGPL-2.1.
- [CadQuery](https://github.com/CadQuery/cadquery#readme) - Python framework for scripting parametric CAD models on the Open CASCADE kernel. Python, Apache-2.0.
- [LibreCAD](https://github.com/LibreCAD/LibreCAD#readme) - 2D CAD application for drafting that reads and writes DXF. C++, GPL-2.0.

## Digital Twins

- [iTwin.js](https://github.com/iTwin/itwinjs-core#readme) - Bentley's open source library for building and visualizing infrastructure digital twins. Ties directly into BIM, GIS and reality capture data. TypeScript, MIT.
- [Cesium](https://github.com/CesiumGS/cesium#readme) - Open source JavaScript engine for 3D globes and maps, widely used as the visualization layer under infrastructure and city scale digital twins. JavaScript, Apache-2.0.
- [Eclipse Ditto](https://github.com/eclipse-ditto/ditto#readme) - General purpose digital twin framework from Eclipse IoT for managing the state and telemetry of physical assets, applicable beyond buildings to any monitored infrastructure asset. Java, EPL-2.0.
- [Orion-LD](https://github.com/FIWARE/context.Orion-LD#readme) - FIWARE context broker implementing the NGSI-LD standard, a common data backbone for smart city and infrastructure digital twin platforms. C++, AGPL-3.0.

## Point Clouds and Photogrammetry

- [OpenDroneMap](https://github.com/OpenDroneMap/ODM#readme) - Command line toolkit that turns drone imagery into orthophotos, point clouds, textured meshes and elevation models. Python, AGPL-3.0.
- [WebODM](https://github.com/WebODM/WebODM#readme) - Web interface and API for OpenDroneMap for managing projects and processing tasks. Python, AGPL-3.0.
- [OpenSfM](https://github.com/mapillary/OpenSfM#readme) - Structure from motion library that reconstructs camera poses and 3D scenes from overlapping images. Python, BSD-2-Clause.
- [COLMAP](https://github.com/colmap/colmap#readme) - Structure from motion and multi view stereo pipeline with a graphical and a command line interface. C++, BSD-3-Clause.
- [Meshroom](https://github.com/alicevision/Meshroom#readme) - Node based photogrammetry application built on the AliceVision framework. Python, MPL-2.0.
- [PDAL](https://github.com/PDAL/PDAL#readme) - Point Data Abstraction Library, translates and processes point cloud data through configurable pipelines. C++, BSD-3-Clause.
- [laspy](https://github.com/laspy/laspy#readme) - Reads, modifies and writes LAS and LAZ lidar files in Python. Python, BSD-2-Clause.
- [Open3D](https://github.com/isl-org/Open3D#readme) - Library for 3D data processing with registration, surface reconstruction and visualization for point clouds and meshes. C++, MIT.
- [CloudCompare](https://github.com/CloudCompare/CloudCompare#readme) - Desktop application for point cloud and mesh processing, widely used for cloud to cloud comparison and deformation measurement. C++, GPL-2.0-or-later.
- [Potree](https://github.com/potree/potree#readme) - WebGL renderer for very large point clouds in the browser. JavaScript, BSD-2-Clause.

## Geospatial and Remote Sensing

- [QGIS](https://github.com/qgis/QGIS#readme) - Desktop geographic information system for viewing, editing and analyzing spatial data, extensible with Python plugins. C++, GPL-2.0.
- [GDAL](https://github.com/OSGeo/gdal#readme) - Translator library for raster and vector geospatial formats that most other open geospatial tools depend on. C++, MIT.
- [GRASS](https://github.com/OSGeo/grass#readme) - Geospatial processing engine with a large set of raster, vector, terrain and hydrology modules. C, GPL-2.0-or-later.
- [GeoPandas](https://github.com/geopandas/geopandas#readme) - Adds geospatial data types and operations to pandas. Standard entry point for vector GIS work in Python. Python, BSD-3-Clause.
- [OSMnx](https://github.com/gboeing/osmnx#readme) - Downloads, models, analyzes and visualizes street networks and other geospatial features from OpenStreetMap. Also the base for the street network work referenced in Infrastructure and Urban Analytics below. Python, MIT.
- [xarray](https://github.com/pydata/xarray#readme) - Labeled multi dimensional arrays in Python, the base for most raster and climate data workflows (satellite imagery, weather, hydrology). Python, Apache-2.0.
- [Rasterio](https://github.com/rasterio/rasterio#readme) - Reads and writes geospatial raster datasets, built on GDAL. Python, BSD-3-Clause.
- [leafmap](https://github.com/opengeos/leafmap#readme) - Interactive mapping and geospatial analysis with minimal code in Jupyter. Wraps several mapping backends under one API. Python, MIT.
- [TorchGeo](https://github.com/torchgeo/torchgeo#readme) - Datasets, samplers, transforms and pretrained models for applying deep learning to geospatial and satellite data. Python, MIT.

## Water and Hydraulics

- [EPANET](https://github.com/OpenWaterAnalytics/EPANET#readme) - Community maintained version of the EPANET toolkit for hydraulic and water quality simulation of pressurized water distribution networks. C, MIT.
- [WNTR](https://github.com/USEPA/WNTR#readme) - Water Network Tool for Resilience, simulates and analyzes water distribution networks under earthquakes, power outages and other disruptions. Python, BSD-3-Clause.
- [SWMM](https://github.com/USEPA/Stormwater-Management-Model#readme) - Storm Water Management Model from the US EPA for runoff quantity and quality in urban drainage systems, released in the public domain. C, Public-Domain.
- [PySWMM](https://github.com/pyswmm/pyswmm#readme) - Python interface to SWMM that allows stepping through a simulation and changing controls while it runs. Python, BSD-2-Clause.
- [ANUGA](https://github.com/anuga-community/anuga_core#readme) - Shallow water equation solver for modeling floods, dam breaks, tsunamis and storm surges. Python, Apache-2.0.
- [SFINCS](https://github.com/Deltares/SFINCS#readme) - Reduced complexity model from Deltares for fast simulation of compound flooding in coastal areas. Fortran, GPL-3.0.
- [LISFLOOD](https://github.com/ec-jrc/lisflood-code#readme) - Distributed rainfall runoff and routing model from the European Commission Joint Research Centre, used in European and global flood forecasting systems. Python, EUPL-1.2.
- [Wflow.jl](https://github.com/Deltares/Wflow.jl#readme) - Distributed hydrological modeling framework in Julia for catchment scale simulations. Julia, MIT.
- [HydroMT](https://github.com/Deltares/hydromt#readme) - Builds and analyzes hydrological and hydrodynamic model setups from global datasets in a reproducible way. Python, MIT.
- [pysheds](https://github.com/pysheds/pysheds#readme) - Watershed delineation, flow direction and flow accumulation from digital elevation models in Python. Python, GPL-3.0.
- [Pywr](https://github.com/pywr/pywr#readme) - Network resource allocation model for water resources systems such as reservoirs, transfers and abstractions. Python, GPL-3.0.
- [MODFLOW 6](https://github.com/MODFLOW-ORG/modflow6#readme) - USGS open source modular hydrologic model for groundwater flow and groundwater and surface water interaction, relevant to flood and drought resilience studies. Fortran, CC0-1.0.
- [FloPy](https://github.com/modflowpy/flopy#readme) - Python package to create, run and post process MODFLOW based groundwater models. Python, CC0-1.0.
- [Landlab](https://github.com/landlab/landlab#readme) - Toolkit for building 2D numerical models of earth surface processes such as overland flow, erosion and sediment transport. Python, MIT.

## Infrastructure and Urban Analytics

- [Eclipse SUMO](https://github.com/eclipse-sumo/sumo#readme) - Open source, microscopic and continuous traffic simulation package that handles large road networks, including pedestrians. C++, EPL-2.0.
- [MATSim](https://github.com/matsim-org/matsim-libs#readme) - Agent based multi agent transport simulation framework used for large scale mobility and infrastructure demand studies. Java, GPL-2.0-or-later.
- [UrbanSim](https://github.com/UDST/urbansim#readme) - Simulation platform for modeling land use, real estate and transportation interactions at the metropolitan scale. Python, BSD-3-Clause.
- [ActivitySim](https://github.com/ActivitySim/activitysim#readme) - Open platform for activity based travel demand modeling, used by metropolitan planning organizations for infrastructure and transportation planning. Python, BSD-3-Clause.
- [momepy](https://github.com/pysal/momepy#readme) - Urban morphology measuring toolkit, quantifies street networks, building form and urban structure from geospatial data. Python, BSD-3-Clause.

## AI and Machine Learning for Civil Engineering

- [xView2 baseline](https://github.com/DIUx-xView/xView2_baseline#readme) - Baseline localization and damage classification models for the xView2 building damage assessment challenge, using satellite imagery from before and after a disaster. Python, BSD-3-Clause.
- [BRAILS++](https://github.com/NHERI-SimCenter/BrailsPlusPlus#readme) - NHERI SimCenter framework that builds regional building and infrastructure inventories from satellite and street level imagery using deep learning. Python, BSD-3-Clause.
- [RoadDamageDetector](https://github.com/sekilab/RoadDamageDetector#readme) - Road damage datasets from several countries with trained detection models for cracks and potholes in smartphone imagery. Python, MIT.
- [segment-geospatial](https://github.com/opengeos/segment-geospatial#readme) - Applies the Segment Anything Model to satellite and aerial imagery, useful for extracting buildings, roads and other features. Python, MIT.
- [DeepXDE](https://github.com/lululxvi/deepxde#readme) - Library for physics informed neural networks and operator learning, used for surrogate modeling of mechanics problems. Python, LGPL-2.1.

## Climate and Resilience

- [pyincore](https://github.com/IN-CORE/pyincore#readme) - Python client for IN-CORE, a community resilience modeling environment that propagates hazard damage on infrastructure through to social and economic impact. Python, MPL-2.0.
- [Brightway](https://github.com/brightway-lca/brightway25#readme) - Open source Python framework for life cycle assessment, used to evaluate the environmental footprint of infrastructure and construction materials. Python, BSD-3-Clause.
- [CLIMADA](https://github.com/CLIMADA-project/climada_python#readme) - Open source framework for climate risk assessment and adaptation option appraisal, models hazard, exposure and vulnerability for infrastructure and other assets. Python, GPL-3.0.
- [City Energy Analyst](https://github.com/architecture-building-systems/CityEnergyAnalyst#readme) - Urban building energy modeling platform for designing low carbon, energy efficient neighborhoods and cities. Python, MIT.
- [EnergyPlus](https://github.com/NatLabRockies/EnergyPlus#readme) - The US DOE's whole building energy simulation engine, models heating, cooling, lighting and water use for individual buildings. C++, BSD-3-Clause-style.
- [OpenStudio](https://github.com/NatLabRockies/OpenStudio#readme) - Cross platform tools built on top of EnergyPlus and Radiance for whole building energy modeling and daylight analysis. C++, BSD-3-Clause-style.
- [Ladybug](https://github.com/ladybug-tools/ladybug#readme) - Core library of Ladybug Tools for importing and analyzing weather data in environmental building design. Python, AGPL-3.0.

## Open Datasets

- [Global ML Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints#readme) - Building footprint polygons for most of the world, derived from satellite imagery. CDLA-Permissive-2.0.
- [Open Buildings](https://sites.research.google/gr/open-buildings/) - Building footprints with confidence scores for Africa, South and Southeast Asia, Latin America and the Caribbean.
- [Overture Maps](https://github.com/OvertureMaps/data#readme) - Open map data with buildings, transportation networks, places and administrative boundaries in cloud native formats. MIT.
- [GEM Global Exposure Model](https://github.com/gem/global_exposure_model#readme) - Country level counts, replacement costs and structural classes of buildings, compiled for seismic risk assessment. Noncommercial use only. CC-BY-NC-SA-4.0.
- [GEM Global Active Faults](https://github.com/GEMScienceTools/gem-global-active-faults#readme) - Harmonized global database of active fault traces with slip rate and kinematic attributes. CC-BY-SA-4.0.
- [STEAD](https://github.com/smousavi05/STEAD#readme) - Stanford Earthquake Dataset, over one million seismic waveform samples labeled for earthquake and noise detection research. CC-BY-4.0.
- [Engineering Strong Motion Database](https://esm-db.eu/) - Processed strong motion waveforms and metadata for earthquakes in Europe and the Middle East.
- [National Bridge Inventory](https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm) - Yearly FHWA records for more than 600,000 bridges in the United States, with condition ratings and structural attributes.
- [LTPP InfoPave](https://infopave.fhwa.dot.gov/) - Long Term Pavement Performance program data on pavement structure, traffic, climate and distress.
- [xBD](https://xview2.org/) - Satellite image pairs from before and after disasters with building damage labels, the dataset behind the xView2 challenge.
- [SDNET2018](https://digitalcommons.usu.edu/all_datasets/48/) - Over 56,000 annotated images of cracked and intact concrete bridge decks, walls and pavements.
- [munich-bridge-data](https://github.com/imcs-compsim/munich-bridge-data#readme) - Real test-bridge sensor data with acceleration, strain, force and inclination measurements, plus Python and MATLAB routines for preprocessing, visualization and analysis. MIT.
- [OpenTopography](https://opentopography.org/) - Portal for high resolution topography, hosts lidar point clouds and global elevation models.

## Learning Resources

- [MUDE](https://github.com/TUDelft-MUDE/book#readme) - Open textbook for Modelling, Uncertainty and Data for Engineers, a core module of the civil engineering and geosciences master programs at TU Delft. Covers numerical modeling, probability, reliability and data analysis with worked Python examples. CC-BY-4.0.
- [comet-fenicsx](https://github.com/bleyerj/comet-fenicsx#readme) - Numerical tours of computational mechanics with FEniCSx, worked examples from linear elasticity, beams and plates to plasticity, buckling and dynamics. CC-BY-SA-4.0.
- [CE394M](https://github.com/kks32-courses/ce394m#readme) - Notebooks for the UT Austin course on advanced analysis in geotechnical engineering, covering the finite element method, constitutive models and consolidation. CC-BY-SA-4.0.
- [soil_mechanics](https://github.com/AppliedMechanics-EAFIT/soil_mechanics#readme) - Notes and interactive notebooks for the undergraduate soil mechanics course at EAFIT University, organized as a Jupyter Book. In Spanish. MIT.
- [slope_stability](https://github.com/AppliedMechanics-EAFIT/slope_stability#readme) - Digital book and reproducible tools for the graduate slope stability course at EAFIT University. In Spanish. MIT.
- [Hydro-Informatics](https://github.com/hydro-informatics/jupyter-python-course#readme) - Notebooks behind the Python courses on hydro-informatics.com, written for water resources and hydraulic engineers. MIT.
- [Introduction to GIS Programming](https://github.com/giswqs/geog-312#readme) - University of Tennessee course on GIS programming with Python and open source geospatial libraries. CC-BY-4.0.
- [Automating GIS Processes](https://github.com/Automating-GIS-processes/site#readme) - University of Helsinki course on geospatial analysis in Python, with lessons and exercises as notebooks. MIT.
- [Geocomputation with Python](https://github.com/geocompx/geocompy#readme) - Open book on working with vector and raster geographic data in Python. Noncommercial use only. CC-BY-NC-SA-4.0.
- [OpenSeesPy-Tutorials](https://github.com/Ashim-Paudel/OpenSeesPy-Tutorials#readme) - Documented Python tutorials for structural dynamics and earthquake engineering, covering eigen/modal analysis, time-history analysis, pushover, nonlinear analysis and structural modeling. MIT.
- [Response_spectra](https://github.com/lviens/Response_spectra#readme) - Python and MATLAB examples for computing response spectra from earthquake ground-motion records, including real KiK-net data from the 2011 Tohoku-Oki earthquake. MIT.
- [ifcopenshell-notebooks](https://github.com/jakob-beetz/ifcopenshell-notebooks#readme) - Interactive Jupyter notebooks for learning IFC processing with IfcOpenShell, covering IFC documentation, model creation and modification, import/export and IFC internals. MIT.

Open course material for earthquake engineering, structural dynamics and BIM is still growing here. If you know of a documented, openly licensed resource, pull requests are welcome.

## Turkiye

Open source civil and infrastructure engineering activity in Turkiye is still scattered across many small, single author projects, mostly thin wrappers around the AFAD or Kandilli observatory APIs. The entries below are the ones with real engineering or data substance rather than a one off notification bot.

- [Turkiye Deprem Verisi](https://github.com/Ayberkrk/turkiye-deprem-verisi#readme) - Compiled, open earthquake dataset for Turkiye with real waveforms and ground motion parameters (PGA, PGV, Vs30), built for reproducible seismic research rather than live alerting. Python, MIT.
- [turkiye-heat-risk](https://github.com/Ayberkrk/turkiye-heat-risk#readme) - City-independent urban heat-risk pipeline using Landsat temperature data, OpenStreetMap roads, and demographic data to calculate a street-level heat sensitivity index. Supports Izmir, Eskisehir, and Sanliurfa. Python, MIT.
- [cauren](https://github.com/Ayberkrk/cauren#readme) - Explainable risk diagnostics for civil infrastructure anomaly detection combined with physics based reasoning, trained on real FHWA bridge inspection data. Python, Apache-2.0.
- [afet-org](https://github.com/acikyazilimagi/afet-org#readme) - Part of the wider [acikyazilimagi](https://github.com/acikyazilimagi) organization, the largest civic tech response to the February 2023 earthquakes. Dozens of repositories covering earthquake relief logistics, needs matching and volunteer coordination. Mostly disaster response tooling rather than structural engineering, but the largest and most active open source cluster to come out of a Turkish earthquake. Apache-2.0.
- [AFAD TADAS EQ Record Processing](https://github.com/DemirAydin/AFAD-TADAS-EQ-Record-Processing#readme) - Processes strong ground motion records from AFAD's Turkish Accelerometric Database and Analysis System (TADAS). A genuinely engineering focused use of Turkish open seismic data. Python, MIT.
- [TSC2018_Design](https://github.com/muhammedsural/TSC2018_Design#readme) - Python package for the Turkish Building Earthquake Code (TBDY 2018) and TS500, covers design spectra, confined concrete models and column confinement design. Last updated in 2024. Python, MIT.
- [sap2000-tbdy2018](https://github.com/krmsari/sap2000-tbdy2018#readme) - Open source Windows application that generates parametric SAP2000 models following TS500 and TBDY 2018. The tool is open, SAP2000 itself is commercial. C#, MIT.
- [2023-Turkey-EQ](https://github.com/yunjunz/2023-Turkey-EQ#readme) - Notebooks and data for the coseismic ground deformation of the 2023 Kahramanmaras earthquake from ALOS-2, LuTan-1 and Sentinel-1 radar imagery. Python, Apache-2.0.
- [kandilli-rasathanesi-api](https://github.com/orhanayd/kandilli-rasathanesi-api#readme) - Free, actively maintained API that merges Kandilli Observatory and AFAD earthquake data with real time feeds, GeoJSON output and filtering by city or proximity. The most maintained of the many AFAD and Kandilli data wrapper projects. The source is public under a custom license that forbids commercial use without permission. JavaScript, Custom.
- [tdvms_py](https://github.com/rdno/tdvms_py#readme) - Small Python script to request continuous seismic waveform data from AFAD's TDVMS network, useful as a building block for seismology and site response research. Python, GPL-3.0.

## Related Awesome Lists

This list intentionally does not duplicate the following. Check them out for adjacent scope.

- [awesome-civil-engineering](https://github.com/QuantumNovice/awesome-civil-engineering#readme) - Much broader list that also includes commercial software such as SAP2000, Revit and Civil 3D. Useful if you are not restricted to open source tools.
- [Awesome-AECO](https://github.com/osama-ata/Awesome-AECO#readme) - Open source focused, strong on BIM, CAD and smart building tooling. Does not cover earthquake engineering, structural health monitoring or datasets.
- [Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial#readme) - Very large general purpose geospatial list, not scoped to civil engineering.
- [awesome-gis](https://github.com/sshuair/awesome-gis#readme) - Another broad, general GIS list.

## Contributing

Contributions are welcome. Please read [contributing.md](contributing.md) before submitting a pull request. In short: the project must be open source (or state its license restriction in the entry), must be relevant to civil or infrastructure engineering (or a directly adjacent discipline), and must have documentation good enough that a newcomer can tell what it does and how to run it.
