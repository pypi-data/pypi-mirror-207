from setuptools import setup, find_packages



VERSION = '0.0.1'
DESCRIPTION = 'Testing hello world'


# Setting up
setup(
    name="kotatsu",
    version=VERSION,
    author="Kotatsu",
    author_email="<nikitakotatsu@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)