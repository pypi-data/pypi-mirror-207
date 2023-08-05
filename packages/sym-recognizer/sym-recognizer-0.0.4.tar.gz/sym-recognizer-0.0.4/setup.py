from distutils.core import setup


setup(
    name="sym-recognizer",
    version="0.0.4",
    description="Python Symbol recognition library",
    author="Mixx3",
    author_email="mmiikkllee@yandex.ru",
    url="https://github.com/mixx3/SymRecognizer",
    license='BSD 2-Clause "Simplified"',
    packages=["recognizer", "recognizer.methods", "recognizer.data"],
    include_package_data=True,
    install_requires=["numpy", "matplotlib", "opencv-python"],
)
