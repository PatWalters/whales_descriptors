This is a very minor fork of the WHALES descriptor code.  I made a few small changes. 
* Ported to Python 3, this was just a matter of running 2to3 on the source files
* Added the molecule name, mol.GetProp("_Name"), to the output
* Added a progress bar using tqdm, need to do "pip install tqdm" to run

The original README.md is below, ignore the bit about Python 2.7, this fork is Python 3.
To install just do this. 
```
 conda create -c rdkit -n rdkit-whales-env rdkit
 source activate rdkit-whales-env
 git clone https://github.com/PatWalters/whales_descriptors.git
 cd whales_descriptors
 python setup.py install
```


# WHALES descriptors

This repository contains all the necessary files to compute Weighted Holistic Atom Localization and Entity Shape (WHALES) descriptors starting from an rdkit supplier file.

For more information regarding the method, have a look at:

Francesca Grisoni, Daniel Merk, Viviana Consonni, Jan A. Hiss, Sara Giani Tagliabue, Roberto Todeschini & Gisbert Schneider "Scaffold hopping from natural products to synthetic mimetics by holistic molecular similarity", *Nature Communications Chemistry* 1, 44, 2018. (Freely available at this [link](https://www.nature.com/articles/s42004-018-0043-x))

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

The following prerequisites are needed:

*[Python 2.7*](https://www.python.org/download/releases/2.7/)

*[RDKit](http://www.rdkit.org/docs/Install.html)

*[NumPy](https://scipy.org/install.html)

*[pandas](https://pandas.pydata.org)

A guide to the correct installation is provided in the following paragraph.

### Preliminary steps

Install conda from the [official website](https://www.anaconda.com/download/). Once conda is installed, it can be used to generate the environment and download RDKit. If you already have RDKit and pandas up and running, you can move to the next paragraph. 

It is suggested to run all the calculations within an RDKit environment. 
The environment can be created with conda as follows:
```
conda create -n whales_env python=2.7*
activate whales_env
```
The RDKit repositories can be listed with the following command:
```
anaconda search -t conda rdkit
```
Choose then the best installation for py27 according to the platform. For instance:
```
conda install -c https://conda.anaconda.org/nickvandewiele rdkit
```
Now install the necessary prerequisites
```
sudo apt-get install python-setuptools
sudo apt install git
python -m pip install --user pandas
```

### Installing WHALES repository

The repository can be cloned as follows

```
git clone https://github.com/grisoniFr/WHALES_descriptors.git
```

Change directory to your local Git repository and to the main WHALES folder e.g., < git_repository\current_user>\WHALES-descriptors\ 

Then, install the package as follows:
```
sudo python setup.py install
```
To check whether the installation went well, type 
```
python 
import whales_descriptors
quit()
```
If no errors are displayed, WHALES package has been succesfully installed. 

## Using the package

### Importing molecular files
RDKit suppliers have to be used as the input for WHALES calculation, for instance:

```
from rdkit import Chem # imports package
suppl = Chem.SDMolSupplier(filename) # generates an rdkit supplier file
```
If the molecules are more than approx. 10,000, it is suggested to use ForwardMolSupplier, instead:
```
suppl = Chem.ForwardSDMolSupplier(filename) 
```
Note that geometrical coordinates have to be specified/computed in order to calculate WHALES descriptors.

### Utilizing WHALES descriptors
The WHALES package can be imported as follows:
```
from whales_descriptors import do_whales
```
and used to calculate the descriptors for the supplier molecules

```
x, labels = do_whales.main(suppl, charge_threshold=0, do_charge=True, property_name='')
```
Specified parameters:
* suppl: rdkit supplier
*    charge_threshold: to neglect atoms with absolute partial charges lower than the threshold (default = 0)
*    do_charge: if True, Gasteiger-Marsili partial charges are computed with rdkit
*    property_name: name of the column containing partial charges of the sdf file (mandatory if do_charge is False)

Returns:
* x (n_mol,p): descriptor matrix, each row corresponds to a molecule
* labels (1,p): descriptor labels

N.B. If a calculation error occurs for a given molecule (e.g., no partial charges computed), the corresponding descriptor values are set to -999. 

### Export descriptors values as a .txt file

The results can be exported as a plain txt file as follows:

```
import numpy as np
save_name = 'results' # example name
np.savetxt([save_name + '_whales.txt'], res, delimiter=' ', newline='\n') # for descriptors
np.savetxt([save_name + '_labels.txt'], labels, delimiter=' ', newline='\n') # for labels
```

## Authors

* **Francesca Grisoni** (https://github.com/grisoniFr)

Contributors to the WHALES descriptors project:
* Francesca Grisoni, University of Milano-Bicocca & ETH-Zurich
* Prof. Dr. Gisbert Schneider, ETH Zurich, gisbert.schneider@pharma.ethz.ch
* Dr. Viviana Consonni, University of Milano-Bicocca
* Prof. Roberto Todeschini, University of Milano-Bicocca
* Dr. Daniel Merk, ETH Zurich


See also the list of [contributors](https://github.com/FrancescaGrisoni/whales_descriptors/contributors) who participated in this project.

## Publications that used WHALES descriptors
* Grisoni et al. "Scaffold hopping from natural products to synthetic mimetics by holistic molecular similarity", *Nature Communications Chemistry* 1, 44, 2018. ([link](https://www.nature.com/articles/s42004-018-0043-x))
* Merk et al. "Scaffold hopping from synthetic RXR modulators by virtual screening and de novo design", *Med. Chem. Commun.*, 2018, 9, 1289-1292. ([link](https://pubs.rsc.org/en/content/articlepdf/2018/md/c8md00134k))
* Merk et al. "De Novo Design of Bioactive Small Molecules by Artificial Intelligence", *Mol. Inf.*, 2018, 1700153. ([link](https://onlinelibrary.wiley.com/doi/epdf/10.1002/minf.201700153))

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
See the [LICENSE.md](LICENSE.md) file for additional details. 

