# pyjcosmo

**pyjcosmo** is a Python wrapper for the **JCOSMO** thermodynamics software. It simplifies interaction with the JCOSMO Java gateway by handling data type conversions automatically, allowing researchers to use standard Python lists and floats instead of Java-specific arrays.

## About JCOSMO  

**JCOSMO** is a computational chemistry package designed for predicting thermodynamic properties using COSMO-based models and more.

> **Note:** This repository contains the wrapper code only. The JCOSMO software itself is hosted separately and distributed under a different license.  

## License  

The content in this repository is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0) License**.  
You are free to share and adapt the material as long as you provide proper attribution.  

[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/) 

However, the **JCOSMO software** is distributed under a separate license. For details on its terms and conditions, please refer to the license file included with the JCOSMO installation.

## Contributing  

We welcome contributions to improve the documentation! If you find errors, have suggestions, or want to contribute new content, feel free to open an issue or submit a pull request.

## Features
* **Simplified API**: No need to manage Py4J gateway arrays or Java types manually.
* **Activity Coefficients**: Direct access to ln(gamma) for multi-component mixtures.
* **Excess Properties**: Methods for computing Excess Enthalpy ($H^E/RT$) and Excess Gibbs Energy ($G^E/RT$).
* **Compound Discovery**: Search the JCOSMO database for specific ions or chemical groups.

## Prerequisites
This wrapper requires a running instance of the JCOSMO Java application with the Py4J Gateway enabled (default port: `25333`).

## Installation
`pip install pyjcosmo`

## Quick Start

### 1. List Available Models
```python
import pyjcosmo
jc = pyjcosmo.JCosmoWrapper()
print(jc.list_models())
```

### 2. Compute Activity Coefficients and Excess Properties
```python
from pyjcosmo import JCosmoWrapper

jc = JCosmoWrapper()
model = jc.get_model('COSMO-SAC-HB2 (GAMESS)')

# Set compounds and state
model.set_compounds(['ACETONE', 'CHLOROFORM'])
model.set_temperature(330.15)
model.set_composition([0.5, 0.5])

# Get activity coefficients and other properties
ln_gamma = model.get_gamma_ln()
he_rt = model.get_excess_enthalpy()
ge_rt = model.get_excess_gibbs()

print(f"lnGamma: {ln_gamma}")
print(f"HE/RT: {he_rt}")
```

### 3. Compound Discovery (Screening)
Search the JCOSMO database for specific chemical groups or ion charges, useful for ionic liquid screening:

```python
from pyjcosmo import JCosmoWrapper

# Initialize the wrapper and model
jc = JCosmoWrapper()
model = jc.get_model('CS25')

# Find all cations (+1 charge) in the database
cations = model.find_compounds('+1')

for cat in cations:
    print(f"Found cation: {cat}")
```

## Citation
Please cite the following works if you use JCOSMO in your research:
* Soares et al. (2025), J. Chem. Theory & Comp. DOI:10.1021/acs.jctc.5c01368
* Ferrarini et al. (2018), AIChe J. DOI:10.1002/aic.16194
* Soares and Gerber (2013), Ind. Eng. Chem. Res. DOI:10.1021/ie400170a
* Soares et al. (2013), Ind. Eng. Chem. Res. DOI:10.1021/ie4013979
* Gerber and Soares (2013), Braz. J. Chem. Eng. DOI:10.1590/S0104-66322013000100002
