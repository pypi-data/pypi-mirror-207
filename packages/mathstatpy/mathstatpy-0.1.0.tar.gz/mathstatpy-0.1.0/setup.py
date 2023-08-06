from setuptools import setup, find_packages

setup(
    name='mathstatpy',
    version='0.1.0',
    description='Librería de Python para análisis estadístico.',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'pandas',
        'seaborn'
    ],
    entry_points={
        'console_scripts': [
        ]
    },
    url='https://github.com/OscarPalominoC/py-stat/',
    author='Oscar Palomino',
    author_email='ing.oscarp1@gmail.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3'
    ]
)