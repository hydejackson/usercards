from setuptools import setup, find_packages

setup(
    name='cardsmaker',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'python-docx',
        'pandas',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'cardsmaker=cardsmaker.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A project to generate namecards for new hires.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/cardsmaker',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
