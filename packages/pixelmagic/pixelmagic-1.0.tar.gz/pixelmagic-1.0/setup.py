from setuptools import setup, find_packages

setup(
    name='pixelmagic',
    version='1.0',
    author='madhawap',
    author_email='madhawa.perera@anu.edu.au',
    description='A package for creating pixelated GIFs from images',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/madhawap/pixelmagic',
    packages=['pixelmagic'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='pixelated gif imageio pillow',
    install_requires=[
        'imageio',
        'Pillow',
    ],
)
