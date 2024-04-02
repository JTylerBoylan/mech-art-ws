from setuptools import find_packages, setup

package_name = 'wishing_well'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='jtylerboylan@outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'wish_extraction_node = wishing_well.wish_extraction_node:main',
            'prompt_generation_node = wishing_well.prompt_generation_node:main',
            'image_generation_node = wishing_well.image_generation_node:main',
            'image_display_node = wishing_well.image_display_node:main'
        ],
    },
)
