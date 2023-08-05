import pathlib
import os

from setuptools import setup
from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig


HERE = pathlib.Path(__file__).parent
#ruta_paquete = "PDFVisor/src/img/*.png"
#relImags = os.path.relpath(ruta_paquete, r"img/*.png")

class register(register_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

class upload(upload_orig):

    def _get_rc_file(self):#
        return os.path.join('.', '.pypirc')


#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
      "PyPDF2",
      "Pillow",
      "numpy",
      "PyMuPDF",
      "opencv-contrib-python",
      ] 

setup(
    name= "PDFVisor",
    version= '0.1.5',
    description= 'Recurso para moverse por documentos PDF',
    long_description=  (HERE / "README.md").read_text(encoding='utf-8'),
    long_description_content_type= "text/markdown",
    author= 'Antonio San Román',
    author_email= 'asanro46@gmail.com',
    install_requires=INSTALL_REQUIRES,
    license= 'MIT',
    packages= ['PDFVisor'],
    package_dir= {'PDFVisor': 'src'},
    package_data = {
        'PDFVisor': ['README.md', "LICENSE.rst"]
    },
    include_package_data=True,
    python_requires='>=3.4',
    cmdclass={
         'register': register,
         'upload': upload
         }
)

keywords=['python', 'pdf'],

classifiers= [
            "Development Status :: 4 - Beta",
            "Intended Audience :: private",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]