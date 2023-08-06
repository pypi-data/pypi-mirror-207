import setuptools

setuptools.setup(
    name="based-metric",
    version="0.0.2",
    url="",
    author="Nick Alutis",
    author_email="",
    description="BASED metric for deblurring assesement",
    packages=setuptools.find_packages(),
    long_description="",
    install_requires=["numpy",
                    "lpips",
                    "torchsummary",
                    "opencv-contrib-python",
                    "opencv-python",
                    "pandas",
                    "scikit-image",
                    "scikit-learn",
                    "matplotlib",
                    "seaborn",
                    "scipy",
                    "pathos",
                    "tqdm"
                ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    include_package_data=True,
    package_data={'model': ['*.joblib']},
)