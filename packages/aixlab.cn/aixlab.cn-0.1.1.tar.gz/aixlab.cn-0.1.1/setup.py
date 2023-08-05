from setuptools import setup, find_packages

setup(
    name='aixlab.cn',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'opencv-contrib-python', 
        'Flask' ,
        'scipy',
        'matplotlib==3.2.2' ,
        'flask-cors',
        'torch==1.6.0+cpu', 
        'torchvision==0.7.0+cpu '
    ],
    author='Xu Ziyi',
    author_email='759946140@qq.com',
    description='Support for aixlab.cn',
    url='https://github.com/xuzycuan/aixlab.cn',
    license='MIT'
)
