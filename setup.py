from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="Covid-19-India-Graphical-Analysis",
    version="1.0.0",
    description="Gui application is used for Analysis of Covid-19 in India Graphicaly",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/nvakhilnair/Covid-19-India-Graphical-Analysis",
    author="Akhil",
    author_email="developmentuse009r@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=[],
    include_package_data=False,
    install_requires=["PyQt4>=4.11.4","pandas>=1.0.3"],
    entry_points={
    },
)
