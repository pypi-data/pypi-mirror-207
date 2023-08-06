# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['qload']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26.34,<2.0.0',
 'ftputil>=5.0.4,<6.0.0',
 'jmespath>=1.0.1,<2.0.0',
 'jsonpath-ng>=1.5.3,<2.0.0',
 'pandas>=2.0.1,<3.0.0',
 'pyarrow>=12.0.0,<13.0.0',
 'pyyaml>=6.0,<7.0']

setup_kwargs = {
    'name': 'qload',
    'version': '1.0.1',
    'description': 'python library to perform assertion on files',
    'long_description': "# qload : better assertion on files\n\nqload is a library to load or extract content of a file to perform assertion in automatic tests without\nboilerplate. It support file from filesystem, ftp, s3, ...\n\n## Benefits\n\n* oneliner to assert on the content of a file\n* useful differential when the test fails thanks to subpart extraction\n* support for the most common formats (yaml, csv, json, txt)\n* support for multiple file systems and protocols (local, ftp, s3)\n* rich expression engine to extract part of a file ([regexp](https://docs.python.org/3/library/re.html#regular-expression-syntax) for `text` and [jmespath](https://jmespath.org) for `csv`, `json` and `yaml` to improve differential) \n\n## Gettings started\n\n```bash\npip install qload\n```\n\n## Usage\n\n```python\nimport qload\n\nassert 'database_url: postgresql://127.0.0.1:5432/postgres' in qload.text('file.txt')\nassert qload.text('file.txt', expression='Hello .*') == 'Hello Fabien'\n\nassert qload.json('file.json') == {}\nassert qload.json('s3://mybucket/file1.json') == {}\nassert qload.json('file.json', expression='$.id') == ''\nassert len(qload.json('file.json', expression='$.id')) == 4\n\nassert qload.yaml('file.yml')  == {}\nassert qload.yaml('file.yml', expression='$.id')  == ''\n\nassert qload.csv('file.csv', expression='[*].Account') == ['ALK', 'BTL', 'CKL']\nassert qload.csv('file.csv', expression='[*].Account')[0] == 'ALK'\n\nassert qload.parquet('file.parquet', expression='[*].Account')[0] == 'ALK'\n\nassert qload.ftp(host='localhost', port=21, login='admin', password='admin').csv(path='dir/file.csv', expression='') == []\nassert qload.s3(bucket='bucket', aws_access_key_id='', aws_secret_access_key='', region_name='eu-west-1', endpoint_url='http://localhost:9090').json(path='dir/file.csv') == {}\n\n\nassert qload.isfile('file.json') is True\nassert qload.s3(bucket='bucket').isfile('file.json') is True\n```",
    'author': 'Fabien Arcellier',
    'author_email': 'fabien.arcellier@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
