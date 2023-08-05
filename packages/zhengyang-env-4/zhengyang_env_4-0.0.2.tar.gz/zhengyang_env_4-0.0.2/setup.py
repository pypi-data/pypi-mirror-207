import setuptools
from pathlib import Path

setuptools.setup(
    name='zhengyang_env_4',
    version='0.0.2',
    description="A OpenAI Gym Env for foo",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include="zhengyang_env_4*"),
    install_requires=['gym','pybullet']  
)