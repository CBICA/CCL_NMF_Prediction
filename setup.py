"""Setup tool for DLICV."""

from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="ccl_nmf_prediction",
    version="0.0.1",
    description="CCL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ioanna Skampardoni, Kyunglok Baik",
    author_email="ioannaki2010@gmail.com",
    maintainer="Kyunglok Baik",
    maintainer_email="kyunglok.baik@pennmedicine.upenn.edu",
    download_url="https://github.com/CBICA/CCL_NMF_Prediction/",
    url="https://github.com/CBICA/CCL_NMF_Prediction/",
    packages=find_packages(exclude=["tests", ".github"]),
    python_requires=">=3.6",
    install_requires=required,
    entry_points={"console_scripts": ["ccl_nmf_prediction = ccl_nmf_prediction.__main__:main"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    license="By installing/using CCL NMF Prediction, the user agrees to the following license: See https://www.med.upenn.edu/cbica/software-agreement-non-commercial.html",
    keywords=[
        "deep learning",
        "medical image analysis",
        "brain aging"
    ],
    package_data={"ccl_nmf_prediction": ["VERSION"]},
)