# -*- encoding: utf-8 -*-
"""
实时控制模型的统一接口类。

__author__ = 'Qin zhaoyu'
__email__  = 'zhaoyu.qin@keepsoft.net'
"""
from abc import abstractmethod, ABCMeta


class ABCController(metaclass=ABCMeta):
    """
    实时控制模型的统一接口类。
    """

    @abstractmethod
    def compile(self, env: object, agent: object, processor: object, confs: dict):
        """
        初始化模型，配置模型结构。

        Args
        ----
        + agent(`Agent`): 强化学习引擎;
        + env(`Env`): 强化学习环境;
        + confs(dict): 模型配置。
        """
        raise NotImplementedError()

    @abstractmethod
    def train(self, confs: dict):
        """
        批训练模型。

        Args
        ----
        + confs(dict): 模型训练配置信息，包括训练次数、批次大小，日志等级等。
        """
        raise NotImplementedError()

    @abstractmethod
    def step(self, observation: object) -> object:
        """
        步进模型。

        Args
        ----
        + observation(object): 当前环境观察状态；

        Returns
        ----
        actions(object)下一步动作。
        """
        raise NotImplementedError()

    @abstractmethod
    def run(self) -> object:
        """
        在环境中运行模型直到环境结束。

        Returns
        ----
        actions(object)所有采用的动作。
        """
        raise NotImplementedError()

    @abstractmethod
    def evaluate(self) -> dict:
        """
        评估(测试)模型。

        Args
        ----

        Returns
        ----
        返回各标签的各项评估结果。
        """
        raise NotImplementedError()

    @abstractmethod
    def reset(self):
        """
        重置模型。
        """
        raise NotImplementedError()
