from setuptools import setup, find_packages

setup(
    name='caixa.gsc',
    version='0.2',
    description='Biblioteca de comunicação com os webservices de Gerenciamento de Serviços da Caixa Econômica',
    author='Clayton A. Alves',
    author_email='clayton.aa@gmail.com',
    url='https://github.com/claytonaalves/caixa.gsc',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests>=2.20.1',
        'zeep>=3.1.0'
    ]
)
