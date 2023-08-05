import sys
from pathlib import Path

import setuptools


def get_readme():
    root_dir = Path(__file__).resolve().parent
    readme_path = str(root_dir / 'README.md')
    print(readme_path)
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


MODULE_NAME = 'rapidocr_openvinogpu'


VERSION_NUM = "0.0.3"#obtainer.version_add_one(latest_version)


setuptools.setup(
    name=MODULE_NAME,
    version=VERSION_NUM,
    platforms="Any",
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    package_dir={'': MODULE_NAME},
    packages=setuptools.find_namespace_packages(where=MODULE_NAME),
    package_data={'': ['*.onnx', '*.yaml', '*.txt']},
    python_requires='>=3.6,<=3.11',
    entry_points={
        'console_scripts': [f'{MODULE_NAME}={MODULE_NAME}.rapid_ocr_api'],
    }
)
