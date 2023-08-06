from setuptools import setup, find_packages

setup(
    name="frequency_feature_map_visualization",
    version="0.6.0",
    description="This code is designed to visualize and save the feature maps of 3D and 2D models. The feature maps can be viewed in the image domain and frequency domain, and saved as .npy files.",
    author="Guanghui FU",
    author_email="aslanfu123@gmail.com",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "torch",
        "matplotlib"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
