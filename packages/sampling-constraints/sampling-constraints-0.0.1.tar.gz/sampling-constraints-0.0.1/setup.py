from distutils.core import setup


setup(
    name='sampling-constraints',
    version='0.0.1',
    url='https://github.com/IsaacRe/Syntactically-Constrained-Sampling',
    description='Library of incremental parsers used to force syntax constraints on next-token predictions during language model generation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="MIT",
    packages=["scs"],
)