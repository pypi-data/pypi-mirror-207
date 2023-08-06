from setuptools import setup,find_packages
setup(name='peodect',
      version='0.0.1',
      description='birds atttributes and functions',
      author='HongPy',
      author_email='mahong0604@163.com',
      requires=[
            'numpy',
            'onnxruntime_gpu','opencv_python',
            'pillow'],  # 定义依赖哪些模块
      packages=['PeopleDetection'],  # 系统自动从当前目录开始找包
      # 如果有的包不用打包，则只能指定需要打包的文件
      # packages=['代码1','代码2','__init__']  #指定目录中需要打包的py文件，注意不要.py后缀
      license="apache 3.0",
      package_dir={'requests': 'requests'},
      )


