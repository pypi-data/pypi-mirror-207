from setuptools import find_packages, setup

setup(
    name="wombatoo",
    version="0.0.3",
    packages=find_packages(exclude=["tests", "examples", "docs"]),
    include_package_data=True,
    description="A Data-Ops tool for devs",
    long_description="Please refer to: README",
    long_description_content_type="text/markdown",
    url="https://github.com/prashdash112/wombat",
    author="Prashant Singh",
    # classifiers=[
    #     "Programming Language :: Python :: 3 :: Only",
    #     "Programming Language :: Python :: 3.8",
    #     "Programming Language :: Python :: 3.9"
    # ],
    license="Please refer to the readme",
    python_requires=">=3.6",
    install_requires=["numpy==1.23.5",
                      "pandas==1.5.2",
                      "pyhtml2pdf==0.0.6",
                      "ydata-profiling==4.1.1"]
                      )