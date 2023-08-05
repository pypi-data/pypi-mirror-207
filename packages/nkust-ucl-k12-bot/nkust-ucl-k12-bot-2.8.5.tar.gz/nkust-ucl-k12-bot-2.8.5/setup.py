import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()


setuptools.setup(
    name="nkust-ucl-k12-bot",
    version="2.8.5",
    author="Ethan Cheng",
    author_email="asdewq45445@gmail.com",
    description="一個用於k12的bot包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xinbow99/k12-telegram",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)