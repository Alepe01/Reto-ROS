from setuptools import setup

package_name = 'cinematica_inversa'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tsurus',
    maintainer_email='tsurus@example.com',
    description='Nodo que calcula la cinemática inversa',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cinematica_inversa = cinematica_inversa.cinematica_inversa:main',
        ],
    },
)
