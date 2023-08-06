from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='datavortex',
    version='1.0.0',
    license='MIT License',
    author='Brayan Robert',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='robertbrayan60@gmail.com',
    keywords='dados, analise de dados, processamento de dados, datahub',
    description=u'Classes para processamento, tratamento e análise de dados',
    packages=['datavortex'],
    install_requires=['pandas', 'numpy', 'seaborn', 'matplotlib', 'Pillow', 'loguru', 'openpyxl'],)