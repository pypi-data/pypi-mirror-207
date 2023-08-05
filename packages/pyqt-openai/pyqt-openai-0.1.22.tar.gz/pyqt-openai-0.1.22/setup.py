from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-openai',
    version='0.1.22',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_openai.ico': ['close.svg', 'openai.svg', 'help.svg', 'customize.svg', 'user.svg',
                                      'sidebar.svg', 'prompt.svg', 'download.svg', 'stackontop.svg',
                                      'add.svg', 'delete.svg', 'setting.svg', 'search.svg']},
    description='PyQt OpenAI example',
    url='https://github.com/yjg30737/pyqt-openai.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.14',
        'PySide6',
        'qtpy',
        'aiohttp',
        'openai',
        'pyperclip'
    ]
)