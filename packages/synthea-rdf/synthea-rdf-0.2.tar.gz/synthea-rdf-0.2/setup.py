from setuptools import setup

setup(
    name="synthea-rdf",
    version="0.2",
    description="Semantic web representation for the Synthea.",
    author="Dae-young Kim, James Clavin",
    author_email="leroy.kim@umbc.edu, jclavin@umbc.edu",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    project_urls={"Source Code": "https://github.com/leroykim/synthea-rdf"},
    license="GPLv3",
    packages=["synthea_rdf", "dua", "trustscore", "abstract"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "rdflib",
        "pandas",
        "alive_progress",
        "panel",
        "lorem_text",
        "pyyaml",
    ],
)
