from setuptools import setup, find_packages

setup(
    name='RapeSegmentation',  # 与项目文件夹结构中的包名相同
    version='0.1.13',
    description='Segmentation any rape',
    author='PingYang',
    author_email='PingYang97@163.com',
    # url='https://github.com/yourusername/your_project',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Add your project's dependencies here, e.g., 'numpy', 'pandas', etc.
        # 'numpy', 'torch', 'tqdm', 'argparse',
    ],
    classifiers=[

        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
