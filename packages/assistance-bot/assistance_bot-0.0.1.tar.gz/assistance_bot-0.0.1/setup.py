from setuptools import setup, find_namespace_packages

setup(name='assistance_bot', 
      version='0.0.1',
      description='assistance_bot',
      url='https://github.com/melser68/my-bot',
      author='Python Core12 Team2',
      author_email='msprivate68@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=['py7zr'],
      include_package_data=True,
      entry_points={'console_scripts': [
          'bot = bot_folder.start_bot:main']}
      )
