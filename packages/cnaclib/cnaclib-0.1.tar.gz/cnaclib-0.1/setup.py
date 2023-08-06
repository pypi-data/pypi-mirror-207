import setuptools

setuptools.setup(
    name = 'cnaclib',
    version = '0.1',
    author= 'Nadir',
    description='Simulateur RAC',
    packages=setuptools.find_packages(),
    python_requires=">=3.8", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)