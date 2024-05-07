from setuptools import find_packages, setup

def get_requirements() -> list[str]:
    requirements_list = []
    # Add your requirements here, for example:
    # requirements_list.append('numpy>=1.0')
    return requirements_list

setup(
    name='sensor',
    version='1.0.1',
    author='Somin Ramchiary',
    author_email='sominzex21@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)
