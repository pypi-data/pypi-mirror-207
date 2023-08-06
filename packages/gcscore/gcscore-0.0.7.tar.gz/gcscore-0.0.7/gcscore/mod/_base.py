"""
Base classes and component to build a gcs module.
"""
from __future__ import annotations

from typing import TypeVar, Type

T = TypeVar('T')

__all__ = ['add_child', 'HasName', 'HasDescription', 'HasChildren', 'AcceptAnonymousChild', 'AcceptMerge']


class HasName:
    """
    Provide the node with a name. This is also the base trait to use for all the nodes.
    """
    gcscore_name: str

    def __init__(self, name: str = None, **kwargs):
        if name is None:
            raise AttributeError('Missing required argument "name"')
        self.gcscore_name = name
        super().__init__(**kwargs)


class HasChildren:
    """
    Allow the node to have children. If used, create a __init__ method calling this one HasChildren.__init__(self)
    """
    gcscore_children: list

    def __init__(self, **kwargs):
        self.gcscore_children = []
        super().__init__(**kwargs)


class HasDescription:
    gcscore_description: str = ''

    def description(self: T, text: str) -> T:
        """
        Provide the node with a description.
        :param text: text of the description.
        :return: the node
        """
        self.gcscore_description = text
        return self

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class AcceptMerge:
    def merge(self: HasChildren, other: HasChildren) -> HasChildren:
        """
        Merges the other's children in its own (the order is kept).
        :param other: other node with children
        :return: self
        """
        self.gcscore_children.extend(other.gcscore_children)
        return self

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class AcceptAnonymousChild:
    def child(self: HasChildren, other: HasName) -> HasChildren:
        """
        Adds the other as its own child.
        :param other: any kind of node
        :return: self
        """
        self.gcscore_children.append(other)
        return self

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def add_child(parent: HasChildren, klass: Type[T], name: str) -> T:
    """
    Create and add a child to the given parent node.
    :param parent: the parent node
    :param klass: the class of the child node
    :param name: name of the child node
    :return: the child node
    """
    child = klass(name)
    parent.gcscore_children.append(child)
    return child
