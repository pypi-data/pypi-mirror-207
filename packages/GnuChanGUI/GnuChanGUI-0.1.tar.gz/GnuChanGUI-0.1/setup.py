from setuptools import setup, find_packages
setup(
    name="GnuChanGUI",
    version="0.1",
    author="archkubi",
    author_email="gnuchanos@gmail.com",
    description="pysimplegui base gui for beginner",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gnuchanos/GnuChanGUI",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="PySimpleGUI,GnuChanGUI,beginner gui",
    install_requires=[
        "pysimplegui",
    ],
    extras_require={},
    python_requires=">=3.11.3",
)



"""
pip install twine
pip install setuptools

python setup.py sdist bdist_wheel


pacman -S twine
twine upload --repository-url https://upload.pypi.org/legacy/ -u __token__ -p pypi-AgEIcHlwaS5vcmcCJDMyOWVhYjFjLTkxOWUtNGE1Ni1iNDg1LWJhMTIyYmJjOTRiNwACKlszLCI5MzI5OWQyNC03MjdhLTQ5YTEtODQ2My02Y2JjMDE2NTY4NmIiXQAABiCRj5aRueCzEXmbxd9AipLxEJ4ZgV9aJ4ynGfc4RB-mpw  dist/*
"""