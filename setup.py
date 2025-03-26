import setuptools

# Package Metadata
__version__ = "0.0.0"
REPO_NAME = "Data-Science-Project-with-MLFlow"
AUTHOR_USER_NAME = "farshadabdulazeez"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "farshadabdulazeez@gmail.com"

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Setup Configuration
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for ML app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)