import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
def readme():
    with open("README.md", encoding='utf-8') as f:
        README = f.read()
    return README

setuptools.setup(
    name='classification_transformers',                           # should match the package folder
    packages=['classification_transformers'],                     # should match the package folder
    version='0.0.1',                                # important for updates
    #license='MIT',                                  # should match your chosen license
    description='Use the package for easy configuration of the huggingface models',
    long_description=readme(),              # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='Harshad Patil',
    author_email='hhpatil001@gmail.com',
    url='https://github.com/harshad317/custom_transformers', 
    #project_urls = {                                # Optional
    #    "Bug Tracker": "https://github.com/mike-huls/toolbox_public/issues"
    #},
    install_requires=['requests'],                  # list all packages that your package uses
    keywords=["pypi", "mikes_toolbox", "tutorial"], #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    
)   