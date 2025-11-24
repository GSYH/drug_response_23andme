from setuptools import setup, find_packages

setup(
    name="drug_response_23andme",
    version="0.1.0",
    description="A package to annotate 23andMe data with PharmGKB drug response information.",
    author="Shuoyuan Gao",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
    ],
    python_requires=">=3.6",
)
