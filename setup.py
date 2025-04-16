from setuptools import setup, find_packages

setup(
    name="weather-etl",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here, e.g.:
        # 'pandas',
        # 'requests',
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
        ],
    },
    python_requires='>=3.7',
)
