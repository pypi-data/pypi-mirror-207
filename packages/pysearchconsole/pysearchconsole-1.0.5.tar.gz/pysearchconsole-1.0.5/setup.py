from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='pysearchconsole',
    version='1.0.5',
    description="PySearchConsole is a Python library that  allows you to get query and analyze data from your website's Search Console account, including search analytics, crawl errors, sitemaps, and more.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rahul Katoch, Harish kumar',
    author_email='rahulkatoch99@gmail.com',
    maintainer_email='rahulkatoch99@gmail.com, echkayweb@gmail.com',
    url='https://github.com/Rahulkatoch99/py_searchconsole',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'google-api-python-client',
        'httplib2',
        'oauth2client'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    keywords='search console api google seo python libraries API integration web traffic analysis',
    python_requires='>=3.6',
    license='MIT',
)
