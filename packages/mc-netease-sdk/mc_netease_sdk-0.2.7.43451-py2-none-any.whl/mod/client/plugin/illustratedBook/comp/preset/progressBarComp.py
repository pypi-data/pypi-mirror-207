
# -*- coding: utf-8 -*-
from mod.client.plugin.illustratedBook.comp.baseComp import BaseComp
from mod.client.plugin.illustratedBook.bookConfig import BookConfig
from typing import List
from typing import Dict
from typing import Tuple

class ProgressBarComp(BaseComp):

    def __init__(self):
        # type: () -> ProgressBarComp
        """
            工作台合成表组件初始化
        """
        pass

    def SetDataBeforeShow(self, value = 1, emptyImage = BookConfig.Images.progressBar_dark, fillImage = BookConfig.Images.progressBar_light):
        # type: (str, float, str, str) -> ProgressBarComp
        """
            在显示组件之前，设置组件的数据
        """       
        pass
    
