from setuptools import setup, find_packages

setup(
    name = "hostel",
    version = "0.1",
    author = "Rob Berry",
    author_email = "",
    url = "http://github.com/rob-b/hostel/",
    zip_safe = False,

    packages = find_packages(),
    license = "MIT License",
    keywords = "django utilities",
    description = "Some reusable components for django apps",
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Utilities',
    ]
)
