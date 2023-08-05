from setuptools import setup

with open('readme.md', 'r') as f:
    long_description = f.read()

setup(
    name='apininja',
    version='0.1.9',
    author='Alex Academia',
    author_email='alexius.sayco.academia@gmail.com',
    description='An api module generator.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/alexiusacademia/apininja',
    py_modules=['apininja'],
    entry_points={
        'console_scripts': [
            'apininja = apininja:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='api generator'
)
