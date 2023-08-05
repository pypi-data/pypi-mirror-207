# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import sys
from pathlib import Path

import setuptools
# from get_pypi_latest_version import GetPyPiLatestVersion


def get_readme():
    root_dir = Path(__file__).resolve().parent
    readme_path = str(root_dir / 'README.md')
    print(readme_path)
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


MODULE_NAME = 'rapidocr_openvinogpu'

# obtainer = GetPyPiLatestVersion()
# latest_version = obtainer(MODULE_NAME)
VERSION_NUM = "0.0.1"#obtainer.version_add_one(latest_version)

# 优先提取commit message中的语义化版本号，如无，则自动加1
# if len(sys.argv) > 2:
#     match_str = ' '.join(sys.argv[2:])
#     matched_versions = obtainer.extract_version(match_str)
#     if matched_versions:
#         VERSION_NUM = matched_versions
#sys.argv = sys.argv[:2]

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
        'console_scripts': [f'{MODULE_NAME}=src.{MODULE_NAME}.rapid_ocr_api:main'],
    }
)
