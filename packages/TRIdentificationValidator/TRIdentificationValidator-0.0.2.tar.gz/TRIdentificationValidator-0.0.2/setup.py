import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='TRIdentificationValidator',
    version="0.0.2",
    author="Yaşar Özyurt",
    author_email="blueromans@gmail.com",
    description='TRIdentificationValidator Python package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/blueromans/TRIdentificationValidator.git',
    project_urls={
        "Bug Tracker": "https://github.com/blueromans/TRIdentificationValidator/issues",
    },
    install_requires=['zeep', 'urllib3==1.26.6'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['TRIdentification', 'TRIdentification.service'],
    python_requires=">=3.6",
)
