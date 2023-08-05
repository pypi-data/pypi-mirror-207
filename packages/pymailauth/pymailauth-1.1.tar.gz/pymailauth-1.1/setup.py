from setuptools import setup, find_packages

setup(
    name="pymailauth",
    version="1.1",
    description="Python mail service for GMail",
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
