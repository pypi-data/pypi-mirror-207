# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ableton_helpers', 'ableton_helpers.change_version']

package_data = \
{'': ['*'],
 'ableton_helpers.change_version': ['example_als/all-tracks-set-11-1-5.als',
                                    'example_als/all-tracks-set-11-1-5.als',
                                    'example_als/all-tracks-set.als',
                                    'example_als/all-tracks-set.als']}

entry_points = \
{'console_scripts': ['ableton-change-version = '
                     'ableton_helpers.change_version.run:main']}

setup_kwargs = {
    'name': 'ableton-helpers',
    'version': '0.1.0',
    'description': 'Scripts to ease work with ableton',
    'long_description': '# Ableton Scripts\n\nUsefull scripts to operate ableton\n\n## ableton-change-version\n\nChanges version of ableton project (now supports only > 11.1.5 and to 11.1.5 only)\n',
    'author': 'bc30138',
    'author_email': 'sasori.axele@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
