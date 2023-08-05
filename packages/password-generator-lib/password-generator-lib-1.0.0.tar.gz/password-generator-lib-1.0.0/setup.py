from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="password-generator-lib",
    version="1.0.0",
    description="A library for generating secure passwords",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/salimovm/password-generator",
    author="Mahammad Salimov",
    author_email="salimovm.7@gmail.com",
    license="MIT",
    packages=["password_generator"],
    install_requires=[
        "black==23.3.0",
        "click==8.1.3",
        "colorama==0.4.6",
        "mypy-extensions==1.0.0",
        "packaging==23.1",
        "pathspec==0.11.1",
        "platformdirs==3.5.0",
        "tomli==2.0.1",
        "typing-extensions==4.5.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)