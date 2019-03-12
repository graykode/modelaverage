from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup_info = dict(
    name='modelaverage',
    version='1.0.1',
    author='Tae Hwan Jung(@graykode)',
    author_email='nlkey2022@gmail.com',
    url='https://github.com/graykode/modelaverage',
    description='tf-keras, make the average of model weight in same models',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    install_requires=[ 'tqdm', 'tensorflow', 'numpy'],
    keywords='pytorch model summary model.summary()',
    packages=["modelaverage"],
)

setup(**setup_info)