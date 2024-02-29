from setuptools import setup, find_packages

setup(
    name='nonconvexoptimzationfunclib',
    version='0.1',
    author='Dr.Thanos and Satyam Mittal',
    author_email='satyam101905@gmail.com',
    packages=find_packages(),
    description='A library of non-convex optimization functions containing continuous and non-conitnuous functions implemented inn higher dimensions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'numpy',
    ],
    classifiers=[
        'Development Status :: 1-Alpha',
        'Intended Audience :: Researchers, Developers, Students',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)