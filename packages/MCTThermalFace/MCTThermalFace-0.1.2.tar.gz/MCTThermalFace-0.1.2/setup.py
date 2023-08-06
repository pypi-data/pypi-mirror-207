from setuptools import setup, find_packages

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='MCTThermalFace',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'torch',
        'torchvision',
        'opencv-python',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
