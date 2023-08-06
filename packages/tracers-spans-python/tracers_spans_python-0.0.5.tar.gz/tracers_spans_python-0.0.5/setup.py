from setuptools import setup

setup(
    name = 'tracers_spans_python',
    version = '0.0.5',
    author = 'Otávio Mascarenhas',
    author_email = 'otaviomascarenhaspessoal@gmail.com',
    packages = ['tracers_spans_python'],
    description = 'Projeto para facilitar a criação e envios de tracers e spans.',
    license = 'MIT',
    keywords = 'Tracers Spans tracers spans tracer span OpenTelemetry Zipkin',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    install_requires=['aiozipkin']
    )