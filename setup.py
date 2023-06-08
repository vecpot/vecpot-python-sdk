from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='vecpot',
    version='0.1.1',
    author='VecPot',
    author_email='contact@vecpot.com',
    description='Python SDK for Vecpot(Embedding as a Service)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vecpot/vecpot-python-sdk',
    packages=["vecpot"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    python_requires='>=3.7',
    install_requires=[
        'requests==2.31.0'
    ],
    project_urls={
        'Bug Reports': 'https://github.com/vecpot/vecpot-python-sdk/issues',
        'Source': 'https://github.com/vecpot/vecpot-python-sdk',
        'Documentation': 'https://docs.vecpot.com/introduction'
    },
)
