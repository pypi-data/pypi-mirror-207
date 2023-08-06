from setuptools import setup, find_packages
package_name = "chinese_onnx"
setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "numpy>=1.19.5",
        "onnxruntime>=1.12.1",
        "opencv-python"
    ],
    package_data={
        package_name: ["data/*"],
    },
    author="lywen",
    author_email="lywen@chineseocr.com",
    description="onnx模型发布",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)