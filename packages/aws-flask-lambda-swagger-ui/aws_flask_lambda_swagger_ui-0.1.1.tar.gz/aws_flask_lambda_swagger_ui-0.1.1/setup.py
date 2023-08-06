from setuptools import setup, find_packages

setup(
    name='aws_flask_lambda_swagger_ui',
    version='0.1.1',
    description='Adding swagger ui on your AWS Lambda Function using a Flask blueprint',
    author='Seven Clouds Technologies',
    author_email='admin@seventechnologies.cloud',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==2.0.2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
