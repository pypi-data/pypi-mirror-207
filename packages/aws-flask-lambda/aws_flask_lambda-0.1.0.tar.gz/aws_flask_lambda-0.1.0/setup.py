from setuptools import setup, find_packages

setup(
    name='aws_flask_lambda',
    version='0.1.0',
    description='Library to run applications on AWS Lambda Function using Flask',
    author='Seven Clouds Technologies',
    author_email='admin@seventechnologies.cloud',
    packages=find_packages(),
    install_requires=[
        'Flask==2.0.2',
        'werkzeug==2.0.2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
