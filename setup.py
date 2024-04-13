from setuptools import setup, find_packages

with open('/home/jevaa_kharthik/pythoncli/cinfo-jk_pkg/cinfo-jk/requirements.txt', 'r') as f:
    requirments = f.read().splitlines()

setup(

    name='cinfo',
    version='0.1',
    packages=find_packages(),
    author='Jevaa Kharthik N',
    author_email='jevaasureka@gmail.com',
    description='Cinfo will tell anything about your CPUs',
    url= 'https://git.selfmade.ninja/jevaa_kharthik/cpuinfo_pkg',
    install_requires=[
            requirments
    ],
    entry_points={
        'console_scripts': [
            'cinfo = cinfo-jk.cinfo-jk:main'
        ],
    },
    
)
    