# Atividade Extra Engneharia de Software

Este projeto demonstra uma arquitetura (mock) de árvore de decisão construída com alguns padrões de projeto em Python.  

---

# Padrões de Projeto Implementados

## 1. Composite — Estrutura de Nós
Permite modelar uma árvore por composição:

- `DecisionNode`: nós internos que possuem filhos.
- `LeafNode`: nós folha que não possuem filhos.

Ambos seguem a interface abstrata `Node`.

---

## 2. Iterator — PreOrderIterator
Implementa uma travessia **pré-ordem** da árvore:

- Visita o nó atual.
- Empilha os filhos em ordem inversa.
- Itera até a pilha esvaziar.

---

## 3. Visitor — NodeVisitor
Permite adicionar operações externas sem modificar a estrutura da árvore.

Implementado:

- `DepthVisitor`: calcula a profundidade máxima da árvore (mock).

---

## 4. State — Máquina de Estados do Processo de Construção
O processo de construção da árvore é modelado como uma máquina de estados:

- `SplittingState`: responsável por avaliar e "dividir" nós.
- `StoppingState`: verifica critérios de parada.
- `PruningState`: executa a etapa final de "poda".

Coordenado pelo contexto:

- `TreeBuilder`

## Exemplo de Uso
```python
root = DecisionNode("Raiz", "x > 10")
child1 = DecisionNode("Nó A", "y < 5")
child2 = LeafNode("Nó B", "Classe 1")
child3 = LeafNode("Nó C", "Classe 2")

root.add_child(child1)
root.add_child(child2)
child1.add_child(child3)

