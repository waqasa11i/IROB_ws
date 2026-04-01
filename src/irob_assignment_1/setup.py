from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'irob_assignment_1'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),  # This will automatically find all packages
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),

        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Maciej Wozniak',
    maintainer_email='maciejw@kth.se',
    description='The irob_assignment_1 package for ROS 2',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'explorer = irob_assignment_1.explorer:main',
        ],
    },
)