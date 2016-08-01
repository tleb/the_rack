from setuptools import setup, find_packages
import the_rack

setup(
    name='the_rack',
    version=the_rack.__version__,
    packages=find_packages(),
    author="tleb",
    author_email="tleb@openmailbox.org",
    description="A simpler DI Container",
    long_description=open('README.md').read(),
    include_package_data=True,
    url='http://github.com/tleb/the_rack',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Topic :: Communications",
    ],
    license="WTFPL",
)
