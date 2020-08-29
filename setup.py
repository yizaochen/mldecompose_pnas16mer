from setuptools import setup, find_packages

setup(name='mldecompose', 
      version='0.1',
      packages=find_packages(),
      url='https://github.com/yizaochen/mldecompose_pnas16mer.git',
      author='Yizao Chen',
      author_email='yizaochen@gmail.com',
      install_requires=[
          'numpy',
          'matplotlib',
          'pandas'
      ]
      )