import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

with open("requirements.txt", 'r', encoding='utf-8') as f:
    requirements = f.read().split()

setuptools.setup(
    name="air-df",  					# pip install name
    version="0.1.3",					# 版本，每次更新需修改，否则无法上传
    author="Damon",
    author_email="527439841@qq.com",
    description="常用插件",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Air-df",  	# git-hup 项目地址, 这里只放了主页地址，这个参数不重要
    packages=['air'],					# 文件夹名
    install_requires=requirements,  	# 依赖库,发布后，pip install过程中自动安装该参数下的依赖
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=[						# 打包的具体文件
        'air.base_handler', 'air.plugins'
    ]
)
