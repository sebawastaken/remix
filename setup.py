import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="remix",
    version="0.0.1",
    author="Mateo Espinosa Zarlenga",
    author_email="me466@cam.ac.uk",
    description="Rule Extraction Methods for Interactive eXplainability",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mateoespinosa/remix",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6, <3.9',
    install_requires=[
        "dill==0.3.6",
        "flexx==0.8.4",
        "Keras-Preprocessing==1.1.2",
        "numpy==1.23.5",
        "pandas==2.0.0",
        "prettytable==3.7.0",
        "pscript==0.7.7",
        "PyYAML==6.0",
        "rpy2==3.5.11",
        "scikit-learn==1.2.2",
        "scipy==1.9.1",
        "tensorboard-plugin-wit==1.8.1",
        "tensorboard==2.12.2",
        "tensorflow-estimator==2.12.0",
        "tensorflow==2.12.0",
        "tqdm==4.65.0",
    ],
)
