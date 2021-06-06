import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sample_command",
    version="0.1.0",
    author="cm-hirano-shigetoshi",
    author_email="hirano.shigetoshi@classmethod.jp",
    description="You can receive the message 'Hello!!!'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cm-hirano-shigetoshi/python_sample_command",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['sample_command = sample_command.sample_command:main']
    },
    python_requires='>=3.7',
)