from setuptools import setup

setup(
    name='flask_cloud_function',
    packages=['flask_cloud_function'],
    include_package_data=True,
    install_requires=[
        "Flask==2.3.2",
        "joblib==1.3.2",
        "numpy==1.24.3",
        "scikit-learn==1.3.0",
        "gensim==4.3.0",
        "tensorflow-cpu==2.13.0",
        "scipy==1.11.2",
        'gunicorn==20.1.0'
    ],
)