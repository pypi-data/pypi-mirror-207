import setuptools

with open("README.md", "r") as descfile:
    longdesc = descfile.read()

setuptools.setup(name="gravipython",
                 version="0.0.5",
                 author="Tom Brandt",
                 author_email="latomateultime@gmail.com",
                 description="A python module for simulating planets trajectories in 2D.",
                 long_description_content_type="text/markdown",
                 long_description=longdesc,
                 license="MIT license",
                 packages=setuptools.find_packages("gravipython"),
#                  package_dir={'': "gravitypython"},
                 install_requires=["pygame", "numpy"],
                 include_package_data = True)