import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(name='ISY993 to Homie 3 Bridge',
      version='0.1.3',
      description='Homie 3 for Universal Devices ISY994',
      author='Michael Cumming',
      author_email='mike@4831.com',
      long_description=long_description,
      long_description_content_type="text/markdown",      
      url='https://github.com/mjcumming/ISY-Homie-Bridge',
      keywords = ['HOMIE','MQTT','ISY99','Universal Devices'],  
      packages=setuptools.find_packages(exclude=("test.py",)),
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],      
    install_requires=[
        'Homie3',
        'ISY994v5',
        'pyyaml',
    ],
    scripts=['isy_homie_start.py'],
)