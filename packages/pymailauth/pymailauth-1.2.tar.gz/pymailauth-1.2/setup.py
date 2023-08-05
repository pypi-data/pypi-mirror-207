from setuptools import setup, find_packages

desc = """
pymailauth is a python library which simplifies email setup
for gmail. It is based on google oauth.
Please refer readme for more details
"""

setup(
    name="pymailauth",
    version="1.2",
    description="Python mail service for GMail",
    long_description=desc,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    author="Ankit Kumar Pandey",
    author_email="itsankitkp@gmail.com",
    url="https://github.com/itsankitkp/pymailauth",
    keywords="mail",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "google-auth==2.17.3",
        "google-auth-oauthlib==1.0.0",
        "google-auth-httplib2==0.1.0",
        "google-api-python-client==2.86.0",
    ],
)
