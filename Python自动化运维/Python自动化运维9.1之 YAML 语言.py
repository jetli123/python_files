# -*- coding: utf-8 -*-
"""YAML 是一种用来表达数据序列的变成语言，它的主要特点包括：可读性强、语法简单明了、支持丰富的语言解析库、通用性强等。
Ansible 与 Saltstack 环境中配置文件都以YAML 格式存在，熟悉 YAML 结构及语法对我们理解两环境的相关配置至关重要。"""

# 下面的示例定义了在 master 的不同业务环境下文件根路径的描述：
# -*- 示例: -*-
"""
file_roots:
  base:
   - /srv/salt/
  dev:
   - /srv/salt/dev
  prod:
   - /srv/salt/prod
"""

# 块序列与块映射的示例详细说明：
# 块序列就是将描述的元素序列到 Python 的列表（list）中。
import yaml
obj = yaml.load(
    """
    - He
    - Papilionidae
    - Apatelodidae
    """
)
print(obj)

















