# -*- coding: UTF-8 -*-
"""
  Author:  Jacek Kotlarski --<szumak@virthost.pl>
  Created: 07.05.2023

  Purpose: NoDynamicAttributes class for restricting the dynamic creation
  of attributes in inheriting classes.
"""

from typing import Any


class NoDynamicAttributes:
    """NoDynamicAttributes - base class.

    Class for restricting the dynamic creation of attributes in inheriting
    classes.
    """

    def __setattr__(self, name: str, value: Any) -> None:
        if not hasattr(self, name):
            raise AttributeError(
                f"Cannot add new attribute '{name}' to {self.__class__.__name__} object"
            )
        super().__setattr__(name, value)


# #[EOF]#######################################################################
