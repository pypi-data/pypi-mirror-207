from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'ChatGPT for healthcare applications'
LONG_DESCRIPTION = 'Akello GPT helps ensure deterministic results for healthcare applications '

setup(
    name="akello",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    include_package_data=True,
    test_suite="akello",
    package_data={'akello': ['*.yaml']},
    author="Vijay Selvaraj",
    author_email="vijay@akellohealth.com",
    license='MIT',
    packages=find_packages(),
    tests_require=['PyYAML', 'responses'],
    install_requires=['PyYAML', 'requests', 'responses'],
    keywords='healthcare, chatgpt, screening',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)