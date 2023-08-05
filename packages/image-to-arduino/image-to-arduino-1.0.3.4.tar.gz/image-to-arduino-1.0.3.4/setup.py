from setuptools import setup, find_packages, Command
import os

REQUIREMENTS = [i.strip() for i in open("/home/wiktor/Image_Converter_App/requirements.txt").readlines()]
LONG_DESCRIPTION = 'About Image converter GUI App to arduino oled display ssd1306 128x64'
class MyCommand(Command):
    description = 'Runs myscript.py'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('python3 image-to-arduino.py')
setup(
   name='image-to-arduino',
   version='1.0.3.4',
   description='Image converter to arduino',
   license="MIT",
   author='WiktorK02',
   author_email='wiktor.kidon@hotmail.com',
   url="https://github.com/WiktorK02/Image_Converter_App.git",
   long_description_content_type="text/markdown",
   long_description=LONG_DESCRIPTION,
   packages=['src'],
   package_data={'src': ['data/*.dat']},
   install_requires=REQUIREMENTS, 
   entry_points={
        'console_scripts': [
            'mycommand = mypackage.mycommand:MyCommand'
        ]
    },
   cmdclass={
        'mycommand': MyCommand
    }

)

