from setuptools import setup

package_name = 'solicitud_servicio'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tsurus',
    maintainer_email='tsurus@example.com',
    description='Nodo que solicita posiciones y las envía a cinematica_inversa',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'solicitud_servicio = solicitud_servicio.solicitud_servicio:main',
        ],
    },
)
