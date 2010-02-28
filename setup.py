from setuptools import setup, find_packages

setup(
    name = "hostel",
    version = "0.1",
    author = "Rob Berry",
    author_email = "",
    url = "http://github.com/rob-b/hostel/",

    packages = find_packages('hostel'),
    license = "MIT License",
    keywords = "django utilitiess",
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
