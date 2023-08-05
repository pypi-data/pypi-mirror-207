# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['q2terminal']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'q2terminal',
    'version': '0.1.4',
    'description': '',
    'long_description': '# Interaction with a terminal session\n\n```python\nfrom q2terminal.q2terminal import Q2Terminal\nimport sys\n\nt = Q2Terminal()\nt.run("programm", echo=True)\nassert t.exit_code is False\n\nassert t.run("$q2 = 123") == []\nassert t.run("echo $q2") == ["123"]\n\n\nif "win32" in sys.platform:\n    t.run("notepad")\n    assert t.exit_code is True\n```\n',
    'author': 'Andrei Puchko',
    'author_email': 'andrei.puchko@gmx.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
