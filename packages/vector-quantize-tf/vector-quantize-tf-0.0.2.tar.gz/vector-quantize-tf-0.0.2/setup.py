from setuptools import setup

import vector_quantize_tf

setup(
    name="vector-quantize-tf",
    author="anime-song",
    description="tensorflowでの残差ベクトル量子化の実装",
    license="MIT license",
    version="0.0.2",
    install_requires=["tensorflow"],
    packages=["vector_quantize_tf"]
)
