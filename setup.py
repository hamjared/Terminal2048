from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='Terminal Based 2048 Gane',
      url='http://github.com/storborg/funniest',
      author='Jared',
      author_email='',
      license='MIT',
      packages=['gamelogic', "graphics"],
      install_requires=[
          "blessed",
          "numpy",
          "pytest"
      ],
      zip_safe=False)