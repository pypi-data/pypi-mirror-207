from setuptools import setup, find_packages

with open('README.txt', 'r') as fh:
    long_description = fh.read()

setup(
    name='JBPhD',
    version='1.0.0',
    description='My project description',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'myproject = myproject.main:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    # Add the following lines to include the manifest and readme files
    include_package_data=True,
    data_files=[('.', ['README.txt', 'MANIFEST.in'])],
    
)

