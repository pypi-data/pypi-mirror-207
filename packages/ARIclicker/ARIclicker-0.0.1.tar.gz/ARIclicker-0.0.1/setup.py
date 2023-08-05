from setuptools import setup, find_packages

setup(
    name = 'ARIclicker',
    version = '0.0.1',
    maintainer='lin_zhe',
    keywords='AutoRandomIntervalClicker',
    description = 'A random interval clicker who can DIY:AutoRandomIntervalClicker',
    license = 'MIT License',
    author = 'lin_zhe',
    author_email = '2081812728@qq.com',
    packages = find_packages(),
    include_package_data = True,
    python_requires='>=3.0',
    platforms = 'any',
    install_requires = [
        'pynput'
    ],
)
