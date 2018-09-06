# -*- coding: utf-8 -*-
"""Ansible 一种集成IT 系统的配置管理、应用部署、执行特定任务的开源平台，
由 Paramiko 和 PyYAML 两个关键模块构建。"""

# pip install Paramiko
# pip install PyYAML

# Ansible 聚友如下特点：
# 1.部署简单，只需要在主控端部署 Ansible 环境，被控端无需做任务操作；
# 2.默认使用SSH 协议对设备进行管理；
# 3.主从集中化管理；
# 4.配置简单、功能强大、扩展性强；
# 5.支持API 及自定义模块，可通过Python 轻松扩展；
# 6.通过 Playbooks 来定制强大的配置、状态管理；
# 7.对云计算平台、大数据都有很好的支持；
# 8.提供一个功能强大、操作性强的Web 管理页面和 REST API 接口 -- AWX平台。

# Ansible 架构：
# 用户通过 Ansible 编排引擎操作公共/私有云或 CMDB（配置管理数据库） 中的主机，其中Ansible编排引擎由 Inventory(主机与组规则)、
# API、Modules(模块)、Plugins(插件) 组成。

# -*- Ansible 与 Saltstack 区别：
"""
  Ansible 与 Saltstack 最大区别是 Ansible 无需在被控主机部署任何客户端代理，默认直接通过 SSH 通道进行
远程命令执行或下发配置；
  相同点是：
    都具备功能强大、灵活的系统管理、状态配置，都使用 YAML格式来描述配置，两者都提供丰富的模版及API，对
云计算平台、大数据都有很好的支持。"""
