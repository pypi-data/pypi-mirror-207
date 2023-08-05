from setuptools import setup, find_packages

setup(
    name='grahamstools',
    version='0.1.4',
    author='GrahamboJangles',
    author_email='lafebregraham@gmail.com',
    description='Tools and resources for Python developers',
    url = "https://github.com/GrahamboJangles/GrahamsTools",
    download_url = "https://github.com/GrahamboJangles/GrahamsTools/archive/refs/tags/0.1.0.tar.gz",
    packages=find_packages(),
    # This is for required dependencies
    install_requires=[],
    # This is for command line commands
    # entry_points={
    #     'console_scripts': [
    #         'your_command=your_package_name.command_line:main'
    #     ]
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning', 
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    python_requires='>=3.6',
)
