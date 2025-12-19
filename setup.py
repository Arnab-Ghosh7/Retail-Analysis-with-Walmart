import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "Real-Walmart"
AUTHOR_USER_NAME = "Arnab-Ghosh7"
SRC_REPO = "real_walmart"
AUTHOR_EMAIL = "arnabghosh010203@gmail.com"

setuptools.setup(
    name=SRC_REPO,                      # package name (no hyphen)
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="End-to-end Walmart weekly sales prediction system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
