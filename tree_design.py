from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Node(ABC):
    """Classe base abstrata para todos os nós da árvore."""

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def add_child(self, child: "Node") -> None:
        ...

    @abstractmethod
    def remove_child(self, child: "Node") -> None:
        ...

    @abstractmethod
    def get_children(self) -> List["Node"]:
        ...

    @abstractmethod
    def accept(self, visitor: "NodeVisitor") -> None:
        ...


class DecisionNode(Node):
    """Nó interno da árvore, responsável por tomar decisões (mock)."""

    def __init__(self, name: str, condition: str) -> None:
        super().__init__(name)
        self.condition = condition
        self._children: List[Node] = []

    def add_child(self, child: Node) -> None:
        print(f"[DecisionNode] Adicionando filho '{child.name}' ao nó de decisão '{self.name}'.")
        self._children.append(child)

    def remove_child(self, child: Node) -> None:
        print(f"[DecisionNode] Removendo filho '{child.name}' do nó de decisão '{self.name}'.")
        self._children.remove(child)

    def get_children(self) -> List[Node]:
        return list(self._children)

    def accept(self, visitor: "NodeVisitor") -> None:
        print(f"[DecisionNode] Visitando nó de decisão '{self.name}'.")
        visitor.visit_decision_node(self)


class LeafNode(Node):
    """Nó folha da árvore, representando uma previsão ou rótulo (mock)."""

    def __init__(self, name: str, prediction: str) -> None:
        super().__init__(name)
        self.prediction = prediction

    def add_child(self, child: Node) -> None:
        print(
            f"[LeafNode] Tentativa de adicionar filho ao nó folha '{self.name}' ignorada "
            "(folhas não possuem filhos)."
        )

    def remove_child(self, child: Node) -> None:
        print(
            f"[LeafNode] Tentativa de remover filho do nó folha '{self.name}' ignorada "
            "(folhas não possuem filhos)."
        )

    def get_children(self) -> List[Node]:
        return []

    def accept(self, visitor: "NodeVisitor") -> None:
        print(f"[LeafNode] Visitando nó folha '{self.name}'.")
        visitor.visit_leaf_node(self)
