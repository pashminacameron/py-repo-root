import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
      name='py-repo-root',
      version='1.1.2',
      license='MIT',
      description='Python utility for cleaner handling of paths',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/pashminacameron/py-repo-root',
      packages=setuptools.find_packages(),
      python_requires='>=3.7.0',
      include_package_data=True,
      author='Pashmina Cameron, Henry Jackson Flux',
      author_email='pashabhi@yahoo.com',
      install_requires=[],
      zip_safe=False)
