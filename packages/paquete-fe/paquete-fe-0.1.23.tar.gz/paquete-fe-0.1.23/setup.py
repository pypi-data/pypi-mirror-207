from setuptools import setup, find_packages

setup(
    name='paquete-fe',
    packages=["paquetefe"],
    version='0.1.23',
    description='Facturación Electrónica',
    author='Mateo Nunez',
    author_email='mateo@idl.com.py',
    url='https://cds.com.py',
    include_package_data=True,
    install_requires=[
        'lxml',
        'SQLAlchemy',
        'pyOpenSSL',
        'zeep',
        'requests',
        'pytz',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)