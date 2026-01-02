from setuptools import setup, find_packages

setup(
    name="CT2MRI",
    version="0.1",
    packages=find_packages(),
    py_modules=["Register", "utils", "main"], # Explicitly include top-level modules
    install_requires=[
        "torch",
        "numpy",
        "nibabel",
        "h5py",
        "pandas",
        "pyyaml",
        "tqdm",
        "scikit-image",
        "albumentations",
        "wandb",
        "einops"
    ]
)