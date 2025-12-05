from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Iterator
from typing import Optional

class Node(ABC):
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


class PreOrderIterator(Iterator[Node]):
    def __init__(self, root: Node) -> None:
        self._stack: List[Node] = [root]
        print("[PreOrderIterator] Inicializado com raiz:", root.name)

    def __iter__(self) -> "PreOrderIterator":
        return self

    def __next__(self) -> Node:
        if not self._stack:
            print("[PreOrderIterator] Fim da iteração.")
            raise StopIteration

        current = self._stack.pop()
        print(f"[PreOrderIterator] Retornando nó '{current.name}' e empilhando filhos.")

        children = current.get_children()
        for child in reversed(children):
            self._stack.append(child)

        return current


# ======================
# padrão Visitor
# ======================

class NodeVisitor(ABC):
    """Interface base para visitantes da árvore."""

    @abstractmethod
    def visit_decision_node(self, node: DecisionNode) -> None:
        ...

    @abstractmethod
    def visit_leaf_node(self, node: LeafNode) -> None:
        ...


class DepthVisitor(NodeVisitor):
    """
    Visitor que calcula a profundidade máxima (mock) da árvore.
    Usa prints para mostrar o fluxo da travessia.
    """

    def __init__(self) -> None:
        self.max_depth = 0
        self._current_depth = 0

    def visit_decision_node(self, node: DecisionNode) -> None:
        print(f"[DepthVisitor] Entrando em nó de decisão '{node.name}' na profundidade {self._current_depth}.")
        self._current_depth += 1
        self.max_depth = max(self.max_depth, self._current_depth)

        for child in node.get_children():
            child.accept(self)

        self._current_depth -= 1
        print(f"[DepthVisitor] Saindo do nó de decisão '{node.name}' para profundidade {self._current_depth}.")

    def visit_leaf_node(self, node: LeafNode) -> None:
        print(f"[DepthVisitor] Visitando nó folha '{node.name}' na profundidade {self._current_depth + 1}.")
        self.max_depth = max(self.max_depth, self._current_depth + 1)

class TreeBuilderState(ABC):
    """
    Interface base para os estados do processo de construção da árvore.
    """

    @abstractmethod
    def handle(self, builder: "TreeBuilder", node: Node) -> None:
        """
        Executa a lógica do estado atual sobre o nó.
        Tudo mock, apenas com prints.
        """
        ...


class SplittingState(TreeBuilderState):
    """
    Estado responsável pela fase de 'divisão' dos nós (mock).
    """

    def handle(self, builder: "TreeBuilder", node: Node) -> None:
        print(f"[SplittingState] Avaliando se o nó '{node.name}' deve ser dividido...")
        print(f"[SplittingState] 'Dividindo' (mock) o nó '{node.name}'.")

class StoppingState(TreeBuilderState):
    def handle(self, builder: "TreeBuilder", node: Node) -> None:
        print(f"[StoppingState] Verificando critério de parada para o nó '{node.name}'.")
        print(f"[StoppingState] Critério de parada atingido (mock). Iniciando poda.")
        builder.change_state(PruningState())


class PruningState(TreeBuilderState):
    def handle(self, builder: "TreeBuilder", node: Node) -> None:
        print(f"[PruningState] Avaliando se o nó '{node.name}' deve ser podado.")
        print(f"[PruningState] Poda (mock) concluída para o nó '{node.name}'. Processo de construção encerrado.")
        builder.change_state(None)
