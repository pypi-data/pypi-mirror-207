from setuptools import setup, find_packages
requirements = ['requests>=2.4']
setup(
    name='GramGetter',
    version='0.3.0',    # Update this for new versions
    packages=find_packages(include=['GramGetter*']),
    include_package_data=True,
    description='A crawler for scraping instagram content',
    author='Mohamed Amine Said',
    author_email='amine8said@gmail.com',
    url='https://github.com/instaloader/instaloader',
    python_requires='>=3.8',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
