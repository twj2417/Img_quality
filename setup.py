from setuptools import setup, find_packages

setup(name='img-quality',
      version='0.0.1',
      description='Image quality index.',
      url='https://github.com/twj2417/Img_quality',
      author='Tao Weijie',
      author_email='twj2417@gmail.com',
      license='MIT',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=[
          'fs',
          'click',
      ],
      entry_points='''
            [console_scripts]
            dxcluster=imgq.cli.main:imgq
      ''',
      scripts=[],
      zip_safe=False)
