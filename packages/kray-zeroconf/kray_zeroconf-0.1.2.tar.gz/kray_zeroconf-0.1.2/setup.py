from setuptools import setup,find_packages

setup(name='kray-zeroconf',
      version='0.1.2',
      description='TZeroconf auto networking configuration tool for Kray Works DevOps',
      url='https://gitlab-ua.kray.technology/lanceoflife/kray-zeroconf',
      author='Dmytro Surdu',
      author_email='dmytro.surdu@kray.technology',
      scripts=['zeroconf'],
      install_requires=[
          "setuptools>=61.0","zeroconf == 0.24.4","pyyaml","netifaces","psutil",
      ],
      packages=find_packages(),
      zip_safe=False)