import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name='wikihowapi_pk',
    version='0.0.4',
    description='API to extract more data from wikiHow',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/p1k0pan/AdaptiveStoryFinder.git',
    author='p1k0pan',
    author_email='pan.jingheng1998@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=['bs4', 'tqdm'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6'
)
