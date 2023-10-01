from setuptools import find_packages,setup

constant="-e ."
def get_tools(file_path:str)->list:



    with open(file_path) as f:

        requirements=f.readlines()
        requirements=[req.replace("/n",' ') for req in requirements]

        if constant in requirements:
            requirements.remove(constant)

    return requirements





setup(
    name='Car_price_prediction',
    version='0.0.1',
    author='Girish N',
    author_email='girish12n@gmail.com',
    packages=find_packages(),
    install_packages=get_tools('requirements.txt')
    )