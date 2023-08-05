from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='video-de-ferramentas-2023',
    version=1.0,
    description='Este pacote irá fornecer informações de processamento de vídeos',
    long_description=Path('README.md').read_text(),
    author='Wilker',
    author_email='teste@gmail.com',
    keywords=['Camera', 'Video', 'Processamento'],
    packagegs=find_packages()
    )



