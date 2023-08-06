This repository includes the commonocean_io python package for representing benchmarks for marine motion planning. In addition, we provide two tutorials to exemplify the usage. For an extensive scenario documentation, consider reading the [documentation for the XML format](https://gitlab.lrz.de/tum-cps/commonocean-io/-/blob/main/documentation/XML_commonOcean.pdf).
​
The structure of the repository is:
​
```
.
├── documentation                   # Documentation of scenario specification
└── commonocean                     # Source files
    ├── common                      # Folders which represent the package structure
    ├── ...                         # ...
    └── doc                         # ´Read the Docs´ documentation for the commonocean-io package
```
​
## Installation instructions
​
Create a new Anaconda environment for Python 3.7 (here called co37). 
​
Run in your Terminal window:
```bash
conda create −n co37 python=3.7
```
Activate your environment
```bash
conda activate co37
```
Install all required packages through requirements.txt and if you want to use the jupyter notebook also install jupyter
```bash
pip install commonocean-io
pip install jupyter
```
Now everything is installed and you can start jupyter notebook to run the [tutorials](https://gitlab.lrz.de/tum-cps/commonocean-io/-/tree/main/commonocean/tutorials)
```
$ jupyter notebook
```
​
# Contibutors and Reference
​
We thank all the contibutors for helping develop this project (see contributors.txt).
​
**If you use our converter for research, please consider citing our paper:**
```
@inproceedings{Krasowski2022a,
	author = {Krasowski, Hanna and Althoff, Matthias},
	title = {CommonOcean: Composable Benchmarks for Motion Planning on Oceans},
	booktitle = {Proc. of the IEEE International Conference on Intelligent Transportation Systems},
	year = {2022},
}
```
