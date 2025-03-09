from setuptools import setup

package_name = 'motor_drive'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tsurus',
    maintainer_email='tsurus@example.com',
    description='Nodo que maneja el motor en la ESP32',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motor_drive = motor_drive.motor_drive:main',
        ],
    },
)
