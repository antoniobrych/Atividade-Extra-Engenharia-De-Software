from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    """Classe base abstrata para todos os nós da árvore."""

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def add_child(self, child: "Node") -> None:
        """Adiciona um filho ao nó"""
        ...

    @abstractmethod
    def remove_child(self, child: "Node") -> None:
        """Remove um filho do nó """
        ...

    @abstractmethod
    def get_children(self) -> List["Node"]:
        """Retornara a lista de filhos do nó """
        ...

    @abstractmethod
    def accept(self, visitor: "NodeVisitor") -> None:
        """
        Ponto de entrada para o padrão Visitor.
        """
        ...
