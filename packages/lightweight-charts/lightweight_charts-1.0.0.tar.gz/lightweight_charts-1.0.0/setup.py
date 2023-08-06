from setuptools import setup, find_packages

setup(
    name='lightweight_charts',
    version='1.0.0',
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        'pandas',
        'pywebview',
    ],
    author='louisnw',
    license='MIT',
    description="Python framework for TradingView's Lightweight Charts JavaScript library.",
    url='https://github.com/louisnw01/lightweight-charts-python',
)
