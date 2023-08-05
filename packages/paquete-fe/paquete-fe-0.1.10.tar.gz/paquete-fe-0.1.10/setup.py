from setuptools import setup, find_packages

setup(
    name='paquete-fe',
    packages=["paquetefe"],
    version='0.1.10',
    description='Descripcion corta del paquete',
    author='Andres Ortiz',
    author_email='tu@email.com',
    url='https://tu-url.com/',
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