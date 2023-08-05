import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "flask-guard",
    version = "0.0.8",
    author = "Belmin Batic",
    author_email = "baticbelmin10@gmail.com",
    description = "A library for checking if JSON requests have valid data.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/beki1337/FlaskGuard",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.10"
)