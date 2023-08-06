#Markdown Guide :

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="earthquakereport-indonesia",
    version="0.1.4",
    author="Hasan Gani",
    author_email="ganirh0612@gmail.com",
    description="This package will provide the most update of Indonesian bureau of Forecast (BMKG)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ganirh0612/indonesiaEarthquakeReport",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    #package_dir={"": "src"},
    #packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_reuires=">=3.6",
)