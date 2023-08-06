# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['popv', 'popv.algorithms', 'popv.reproducibility']

package_data = \
{'': ['*']}

install_requires = \
['Markdown==3.3.4',
 'anndata>=0.8,<0.9',
 'bbknn>=1.5.1,<2.0.0',
 'celltypist>=1.3.0,<2.0.0',
 'gdown>=4.6.0,<5.0.0',
 'grpcio>=1.51.1,<2.0.0',
 'h5py>=3.7.0,<4.0.0',
 'huggingface-hub==0.11.1',
 'imgkit==1.2.2',
 'importlib-metadata==4.2.0',
 'ipywidgets',
 'numpy>1.23.5',
 'obonet>=1.0,<2.0',
 'onclass>=1.2,<2.0',
 'pandas>=1.4',
 'rich>=9.1.0',
 'scanorama>=1.7.3,<2.0.0',
 'scanpy>=1.9.1,<2.0.0',
 'scikit-learn>0.21.2,<1.0',
 'scikit-misc>=0.1',
 'scvi-tools>=0.20.0',
 'six==1.15.0',
 'tensorflow>=2.11.0,<3.0.0',
 'tqdm==4.64.0',
 'transformers>=4.25.1,<5.0.0',
 'typing-extensions==4.2.0']

extras_require = \
{'dev': ['black>=22.3',
         'codecov>=2.0.8',
         'flake8>=3.7.7',
         'isort>=5.7',
         'jupyter>=1.0',
         'nbconvert>=5.4.0',
         'nbformat>=4.4.0',
         'pre-commit>=2.7.1',
         'pytest>=4.4']}

setup_kwargs = {
    'name': 'popv',
    'version': '0.2.2',
    'description': 'Automatic annotation of single cell data using a labelled reference dataset including various methods and giving certainty across those methods.',
    'long_description': '\n[![Stars](https://img.shields.io/github/stars/yoseflab/popv?logo=GitHub&color=yellow)](https://github.com/YosefLab/popv/stargazers)\n[![PyPI](https://img.shields.io/pypi/v/popv.svg)](https://pypi.org/project/popv)\n[![PopV](https://github.com/YosefLab/PopV/actions/workflows/test.yml/badge.svg)](https://github.com/YosefLab/PopV/actions/workflows/test.yml)\n[![Coverage](https://codecov.io/gh/YosefLab/popv/branch/main/graph/badge.svg?token=KuSsL5q3l7)](https://codecov.io/gh/YosefLab/popv)\n[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)\n[![Downloads](https://pepy.tech/badge/popv)](https://pepy.tech/project/popv)\n\n# PopV\n\nPopV uses popular vote of a variety of cell-type transfer tools to classify cell-types in a query dataset based on a test dataset.\nUsing this variety of algorithms, we compute the agreement between those algorithms and use this agreement to predict which cell-types are with a high likelihood the same cell-types observed in the reference.\n\n## Algorithms\n\nCurrently implemented algorithms are:\n\n-   K-nearest neighbor classification after dataset integration with [BBKNN](https://github.com/Teichlab/bbknn)\n-   K-nearest neighbor classification after dataset integration with [SCANORAMA](https://github.com/brianhie/scanorama)\n-   K-nearest neighbor classification after dataset integration with [scVI](https://github.com/scverse/scvi-tools)\n-   Random forest classification\n-   Support vector machine classification\n-   [OnClass](https://github.com/wangshenguiuc/OnClass) cell type classification\n-   [scANVI](https://github.com/scverse/scvi-tools) label transfer\n-   [Celltypist](https://www.celltypist.org) cell type classification\n\nAll algorithms are implemented as a class in [popv/algorithms](popv/algorithms/__init__.py).\nTo implement a new method, a class has to have several methods:\n\n-   algorithm.compute_integration: Computes dataset integration to yield an integrated latent space.\n-   algorithm.predict: Computes cell-type labels based on the specific classifier.\n-   algorithm.compute_embedding: Computes UMAP embedding of previously computed integrated latent space.\n\nWe highlight the implementation of a new classifier in a [scaffold](popv/algorithms/_scaffold.py). Adding a new class with those methods will automatically tell PopV to include this class into its classifiers and will use the new classifier as another expert.\n\nAll algorithms that allow for pre-training are pre-trained. This excludes by design BBKNN and SCANORAMA as both construct a new embedding space. Pretrained models are stored on (Zenodo)[https://zenodo.org/record/7580707] and are automatically downloaded in the Colab notebook linked below. We encourage pre-training models when implementing new classes.\n\nAll input parameters are defined during initial call to [Process_Query](popv/preprocessing.py) and are stored in the unstructured field of the generated AnnData object. PopV has three levels of prediction complexities:\n\n-   retrain will train all classifiers from scratch. For 50k cells this takes up to an hour of computing time using a GPU.\n-   inference will use pretrained classifiers to annotate query as well as reference cells and construct a joint embedding using all integration methods from above. For 50k cells this takes in our hands up to half an hour of computing time using a GPU.\n-   fast will use only methods with pretrained classifiers to annotate only query cells. For 50k cells this takes 5 minutes without a GPU (without UMAP embedding).\n\nA user-defined selection of classification algorithms can be defined when calling [annotate_data](popv/annotation.py). Additionally advanced users can define here non-standard parameters for the integration methods as well as the classifiers.\n\n## Output\n\nPopV will output a cell-type classification for each of the used classifiers, as well as the majority vote across all classifiers. Additionally, PopV uses the ontology to go through the full ontology descendants for the OnClass prediction (disabled in fast mode). This method will be further described when PopV is published. PopV additionally outputs a score, which counts the number of classifiers that agreed upon the PopV prediction. This can be seen as the certainty that the current prediction is correct for every single cell in the query data. We generally found disagreement of a single expert to be still highly reliable while disagreement of more than 2 classifiers signifies less reliable results. The aim of PopV is not to fully annotate a data set but to highlight cells that potentially benefit from further manual careful annotation.\nAdditionally, PopV outputs UMAP embeddings of all integrated latent spaces if _compute_embedding==True_ in [Process_Query](popv/preprocessing.py) and computes certainties for every used classifier if _return_probabilities==True_ in [Process_Query](popv/preprocessing.py).\n\n## Installation\n\nWe suggest using a package manager like conda or mamba to install the package. OnClass files for annotation based on Tabula sapiens are deposited in popv/ontology. We use [Cell Ontology](https://obofoundry.org/ontology/cl.html) as an ontology throughout our experiments. PopV will automatically look for the ontology in this folder. If you want to provide your user-edited ontology, we will provide notebooks to create the Natural Language Model used in OnClass for this user-defined ontology.\n\n    conda create -n yourenv python=3.8\n    conda activate yourenv\n    pip install git+https://github.com/czbiohub/PopV\n\n## Example notebook\n\nWe provide an example notebook in Google Colab:\n\n-   [Tutorial demonstrating use of Tabula sapiens as a reference](tabula_sapiens_tutorial.ipynb)\n\nThis notebook will guide you through annotating a dataset based on the annotated [Tabula sapiens reference](https://tabula-sapiens-portal.ds.czbiohub.org) and demonstrates how to run annotation on your own query dataset. This notebook requires that all cells are annotated based on a cell ontology. We strongly encourage the use of a common cell ontology, see also [Osumi-Sutherland et al](https://www.nature.com/articles/s41556-021-00787-7). Using a cell ontology is a requirement to run OnClass as a prediction algorithm.\n\nWe allow running PopV without using a cell ontology.\n',
    'author': 'Galen Xing',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
