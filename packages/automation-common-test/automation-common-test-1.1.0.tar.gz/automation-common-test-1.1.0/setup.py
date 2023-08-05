from  setuptools import setup, find_packages

# with open('requirements.txt') as f:
#     requirements = f.read().splitlines()

ignore_init_rgx = "[!__init__]"

setup(
    name='automation-common-test',
    version='1.1.0',
    author='Chitranjan Kumar',
    author_email='chitranjan.kumar@kyndryl.com',
    description='This is the common automation framework',
    # url='https://github.kyndryl.net/MCMP-IST/MCMP-Performance-Test-Foundation',
    license='Kyndryl',
    include_package_data=True,
    packages=find_packages(),
    # install_requires=requirements
)