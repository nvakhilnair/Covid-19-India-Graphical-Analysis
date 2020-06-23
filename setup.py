from setuptools import setup
def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="covid_19_graphical_analysis",
    version="1.0.1",
    description="Gui application is used for Analysis of Covid-19 in India Graphical (cmd command: covid_19_graphical_analysis.py)",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/nvakhilnair/Covid-19-India-Graphical-Analysis",
    author="Akhil",
    author_email="MadeWithPY009@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=["PyQt4>=4.11.4","pandas>=1.0.3","docutils>=0.3"],
    scripts=["covid_19_graphical_analysis.py"],
    packages=[],
    
)
