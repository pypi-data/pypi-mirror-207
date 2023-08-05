from setuptools import setup, find_packages

setup(
    name='edidsdfsxccqqsc',
    version="0.1",
    author="John Doe",
    author_email="john.doe@example.com",
    description="My awesome Python package",
    packages=find_packages(),
    install_requires=[

        'PyQt5'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'main = csv_editor.main:main',
        ],
    }
)