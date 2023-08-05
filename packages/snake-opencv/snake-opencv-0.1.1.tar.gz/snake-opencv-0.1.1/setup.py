# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snake_opencv',
 'snake_opencv.core',
 'snake_opencv.dnn',
 'snake_opencv.highgui',
 'snake_opencv.imgcodecs',
 'snake_opencv.imgproc',
 'snake_opencv.photo',
 'snake_opencv.videoio']

package_data = \
{'': ['*']}

install_requires = \
['opencv-python>=4.0,<5.0', 'typing-extensions>=4.5.0,<5.0.0']

setup_kwargs = {
    'name': 'snake-opencv',
    'version': '0.1.1',
    'description': 'Snake case opencv with type annotations',
    'long_description': "# Snake-OpenCV\nSnake case OpenCV with type annotations for Python.\n\nNote: still in early development\n\n## Install\n\nStable version\n```sh\npip install snake-opencv\n```\n\nLatest version from git\n```sh\npip install git+https://github.com/cospectrum/snake-opencv.git\n```\n\n## Usage\n```py\nimport snake_opencv as cv\n\npath = '...'\nimage = cv.imread(path)\nassert image is not None\ngray_image = cv.cvt_color(image, cv.COLOR_BGR2GRAY)\n\ncv.imshow(window_name, gray_image) \n```\n",
    'author': 'cospectrum',
    'author_email': 'severinalexeyv@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/cospectrum/snake-opencv',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
