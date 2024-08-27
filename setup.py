from setuptools import setup, find_packages

setup(
    name="EmotionDetection",  # Name of your package
    version="1.0.0",  # Initial version
    author="tristan lim",  # Your name or the name of the package author
    author_email="tris02[at]gmail.com",  # Author's email
    description="A package for detecting emotions in text using a sentiment analysis service.",  # Short description
    long_description=open('README.md').read(),  # Long description read from README.md
    long_description_content_type="text/markdown",
    url="https://github.com/tris02/emotion_detection",  # URL to the package source code or documentation
    packages=find_packages(),  # Automatically find packages in your project
    include_package_data=True,  # Include additional files specified in MANIFEST.in or by the package data directive
    install_requires=[
        "requests",  # Add any external packages required
        "Flask",     # Flask for the server
    ],
    classifiers=[
        "Programming Language :: Python :: 3",  # Specify Python version
        "License :: OSI Approved :: Apache Software License",  # License type
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
    entry_points={
        'console_scripts': [
            'emotion-detector=EmotionDetection.emotion_detection:emotion_detector',
        ],
    },
    license="Apache License 2.0",  # License type
)
