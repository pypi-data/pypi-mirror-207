import setuptools
from pathlib import Path


VERSION = '0.0.5'
DESCRIPTION = 'A Python package to analyze multivalent biomolecular clustering.'
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


# Setting up
setuptools.setup(
    name="molclustpy",
    version=VERSION,
    author="Aniruddha Chattaraj, Michael Blinov, Indivar Nalagandla",
    author_email="chattarajaniruddha@gmail.com",
    url = "https://molclustpy.github.io/",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=['bionetgen', 'numpy', 'matplotlib', 'pandas'],
    keywords=['BioNetGen', 'NumPy', 'Matplotlib', 'pandas', '', ''],
    license= "MIT License",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)