from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='RThreads',
  version='0.0.1',
  description='RThreads Lets you create multiple threads and create loops in it or put a timer to run a function in background. or just run your own function in a thread',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Yashar Chogan',
  author_email='theaspectdev@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='threads', 
  packages=find_packages(),
  install_requires=[''] 
)