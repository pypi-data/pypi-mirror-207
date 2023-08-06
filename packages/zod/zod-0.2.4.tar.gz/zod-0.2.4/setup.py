# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zod',
 'zod.anno',
 'zod.anno.tsr',
 'zod.cli',
 'zod.data_classes',
 'zod.eval',
 'zod.eval.detection',
 'zod.eval.detection._experimental',
 'zod.eval.detection._nuscenes_eval.common',
 'zod.eval.detection._nuscenes_eval.detection',
 'zod.utils',
 'zod.visualization']

package_data = \
{'': ['*'], 'zod.eval.detection': ['_nuscenes_eval/*']}

install_requires = \
['dataclass-wizard>=0.22.2',
 'h5py>=3.1',
 'numpy-quaternion>=2022.4.2',
 'numpy>=1.19,<2.0',
 'pillow>=7',
 'pyquaternion>=0.9',
 'scipy>=1.5,<2.0',
 'tqdm>=4.60']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata', 'typing-extensions'],
 'all': ['typer[all]>=0.7.0',
         'dropbox>=11.36.0',
         'opencv-python>=4',
         'matplotlib>=3',
         'plotly>=5,<6',
         'dash-bootstrap-components>=1.1',
         'pandas>=1.3,<2.0',
         'notebook>=5',
         'imageio>=2,<3'],
 'cli': ['typer[all]>=0.7.0', 'dropbox>=11.36.0']}

entry_points = \
{'console_scripts': ['zod = zod.cli.main:app']}

setup_kwargs = {
    'name': 'zod',
    'version': '0.2.4',
    'description': 'Zenseact Open Dataset',
    'long_description': '# Zenseact Open Dataset\n\n[![Stable Version](https://img.shields.io/pypi/v/zod?label=stable)](https://pypi.org/project/zod/#history)\n[![Python Versions](https://img.shields.io/pypi/pyversions/zod)](https://pypi.org/project/zod/)\n[![Download Stats](https://img.shields.io/pypi/dm/zod)](https://pypistats.org/packages/zod)\n\nThe Zenseact Open Dataset (ZOD) is a large multi-modal autonomous driving dataset developed by a team of researchers at [Zenseact](https://zenseact.com/). The dataset is split into three categories: *Frames*, *Sequences*, and *Drives*. For more information about the dataset, please refer to our [coming soon](), or visit our [website](https://zod.zenseact.com).\n\n## Examples\nFind examples of how to use the dataset in the [examples](examples/) folder. Here you will find a set of jupyter notebooks that demonstrate how to use the dataset, as well as an example of how to train an object detection model using [Detectron2](https://github.com/facebookresearch/detectron2).\n\n## Installation\n\nThe install the library with minimal dependencies, for instance to be used in a training environment without need for interactivity och visualization, run:\n```bash\npip install zod\n```\n\nTo install the library along with the CLI, which can be used to download the dataset, convert between formats, and perform visualization, run:\n```bash\npip install "zod[cli]"\n```\n\nTo install the full devkit, with the CLI and all dependencies, run:\n```bash\npip install "zod[all]"\n```\n\n## Download using the CLI\n\nThis is an example of how to download the ZOD Frames mini-dataset using the CLI. Prerequisites are that you have applied for access and received a download link.\nThe simplest way to download the dataset is to use the CLI interactively:\n```bash\nzod download\n```\nThis will prompt you for the required information, present you with a summary of the download, and then ask for confirmation. You can of course also specify all the required information directly on the command line, and avoid the confirmation using `--no-confirm` or `-y`. For example:\n```bash\nzod download -y --url="<download-link>" --output-dir=<path/to/outputdir> --subset=frames --version=mini\n```\nBy default, all data streams are downloaded for ZodSequences and ZodDrives. For ZodFrames, DNAT versions of the images, and surrounding (non-keyframe) lidar scans are excluded. To download them as well, run:\n```bash\nzod download -y --url="<download-link>" --output-dir=<path/to/outputdir> --subset=frames --version=full --num-scans-before=-1 --num-scans-after=-1 --dnat\n```\nIf you want to exclude some of the data streams, you can do so by specifying the `--no-<stream>` flag. For example, to download only the DNAT images, infos, and annotations, run:\n```bash\nzod download --dnat --no-blur --no-lidar --no-oxts --no-vehicle-data\n```\nFinally, for a full list of options you can of course run:\n```bash\nzod download --help\n```\n\n## Anonymization\nTo preserve privacy, the dataset is anonymized. The anonymization is performed by [brighterAI](https://brighter.ai/), and we provide two separate modes of anonymization: deep fakes (DNAT) and blur. In our paper, we show that the performance of an object detector is not affected by the anonymization method. For more details regarding this experiment, please refer to our [coming soon]().\n\n## Citation\nIf you publish work that uses Zenseact Open Dataset, please cite [our arxiv paper](https://arxiv.org/abs/2305.02008):\n\n```\n@article{zod2023,\n  author = {Alibeigi, Mina and Ljungbergh, William and Tonderski, Adam and Hess, Georg and Lilja, Adam and Lindstr{\\"o}m, Carl and Motorniuk, Daria and Fu, Junsheng and Widahl, Jenny and Petersson, Christoffer},\n  title = {Zenseact Open Dataset: A large-scale and diverse multimodal dataset for autonomous driving},\n  year = {2023},\n  journal = {arXiv preprint arXiv:2305.02008},\n}\n```\n\n## Contact\nFor questions about the dataset, please [Contact Us](mailto:opendataset@zenseact.com).\n\n## Contributing\nWe welcome contributions to the development kit. If you would like to contribute, please open a pull request.\n\n## License\n**Dataset**:\nThis dataset is the property of Zenseact AB (© 2023 Zenseact AB) and is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Any public use, distribution, or display of this dataset must contain this notice in full:\n\n> For this dataset, Zenseact AB has taken all reasonable measures to remove all personally identifiable information, including faces and license plates. To the extent that you like to request the removal of specific images from the dataset, please contact [privacy@zenseact.com](mailto:privacy@zenseact.com).\n\n\n**Development kit**:\nThis development kit is the property of Zenseact AB (© 2023 Zenseact AB) and is licensed under [MIT](https://opensource.org/licenses/MIT).\n',
    'author': 'Zenseact',
    'author_email': 'opendataset@zenseact.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://zod.zenseact.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
