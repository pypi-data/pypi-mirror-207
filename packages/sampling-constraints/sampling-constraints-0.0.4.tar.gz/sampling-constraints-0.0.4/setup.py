from setuptools import setup, find_packages


setup(
    name='sampling-constraints',
    version='0.0.4',
    url='https://github.com/IsaacRe/Syntactically-Constrained-Sampling',
    description='Library of incremental parsers used to force syntax constraints on next-token predictions during language model generation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="MIT",
    packages=find_packages("scs", include=["scs", "scs.*"]),
    package_dir={"": "scs"},
)