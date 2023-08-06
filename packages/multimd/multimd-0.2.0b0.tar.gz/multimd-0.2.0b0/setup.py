# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['multimd']

package_data = \
{'': ['*']}

install_requires = \
['natsort>=8.2,<9.0', 'rich>=13.3.5,<14.0.0', 'typer>=0.9,<0.10']

entry_points = \
{'console_scripts': ['multimd = multimd.__main__:mmd_CLI']}

setup_kwargs = {
    'name': 'multimd',
    'version': '0.2.0b0',
    'description': 'This project makes it possible to write separated pieces of `MD` files that will be merged to produce one single final `MD` file.',
    'long_description': 'The `Python` module `multimd`\n=============================\n\n> **I beg your pardon for my english...**\n>\n> English is not my native language, so be nice if you notice misunderstandings, misspellings, or grammatical errors in my documents and codes.\n\n\nThis document is a short tutorial showing the most useful features without being exhaustive.\n\n\nAbout `multimd`\n---------------\n\nWorking with moderate sized `MD` documents in a single file can quickly become tedious. This project allows you to go through separate small `MD` files to be merged into a final single `MD` file.\n\n\n> *At the moment, resources, such as images, are not managed.*\n\n\n`README.md` part by part\n------------------------\n\nWith `multimd`, you can write a `MD` document by typing small section-like parts which are easy to maintain. Consider the `README.md` file from the `src2prod` project which was written using the following tree on 6 May 2023.\n\n~~~\n+ src2prod\n    * README.md\n    + readme\n        * about.yaml\n        * about.md\n        * build.md\n        * cli.md\n        * example-used.md\n        * only-files.md\n        * prologue.md\n        * readme-splitted.md\n    + ...\n~~~\n\n\nThe special `about.yaml` file is used to specify a specific order in which the different `MD` files are put together (without this file, a "natural" order is used). Its content is as follows: we give the list of the files without their extension.\n\n~~~yaml\ntoc:\n  - prologue\n  - about\n  - example-used\n  - build\n  - only-files\n  - readme-splitted\n  - cli\n~~~\n\n\n> ***WARNING!*** *You can use relative paths but you must use the Unix path separator `/`.*\n\n\nBuilding the final `README.md` file is done quickly on the command line using `multimd` after using the `cd` command to go into the `src2prod` folder. We use the option `-e` to allow to erase an existing `README.md` file.\n\n~~~bash\n> multimd -e readme README.md\nSuccessfully built file.\n  + Path given:\n    README.md\n  + Full path used:\n    /full/path/to/README.md\n~~~\n\n\nThere is also an easy-to-use `Python` API.\n\n~~~python\nfrom multimd import MMDBuilder, Path\n\nmybuilder = MMDBuilder(\n    src   = Path("/full/path/to/readme"),\n    dest  = Path("/full/path/to/README.md"),\n    erase = True\n)\nmybuilder.build()\n~~~\n\n\n> ***NOTE.*** *It is possible to work with subfolders containing `MD` files. In this case, `multimd` will work recursively. In the `about.yaml` file, the path to a subfolder simply ends with the Unix path separator `/` like in `one/sub/folder/`.*\n\n\nWithout the special `about.yaml` file\n-------------------------------------\n\nWithout an `about.yaml` file, all the `MD` files will be merged into one after sorting them in a "natural" order.\n\n\n> ***WARNING!*** *Without an `about.yaml` file, it is impossible to work with subfolders containing `MD` files.*',
    'author': 'Christophe BAL',
    'author_email': 'None',
    'maintainer': 'Christophe BAL',
    'maintainer_email': 'None',
    'url': 'https://github.com/bc-tools/for-dev/tree/main/multimd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
