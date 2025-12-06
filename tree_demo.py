from tree_design import (
    DecisionNode,
    LeafNode,
    PreOrderIterator,
    DepthVisitor,
    CountLeavesVisitor,
    TreeBuilder,
)


def build_mock_tree() -> DecisionNode:
    print("\n=== Construindo árvore de decisão mock ===")

    root = DecisionNode("root", "feature_x <= 10")
    left_leaf = LeafNode("left_leaf", "Classe A")
    right_decision = DecisionNode("right_decision", "feature_y > 5")
    right_left_leaf = LeafNode("right_left_leaf", "Classe B")
    right_right_leaf = LeafNode("right_right_leaf", "Classe C")

    root.add_child(left_leaf)
    root.add_child(right_decision)
    right_decision.add_child(right_left_leaf)
    right_decision.add_child(right_right_leaf)

    return root


def demo_iterator(root: DecisionNode) -> None:
    print("\n=== Demo Iterator (Pré-Ordem) ===")
    iterator = PreOrderIterator(root)
    for node in iterator:
        print(f"[Demo] Visitando nó via iterator: {node.name}")


def demo_visitors(root: DecisionNode) -> None:
    print("\n=== Demo Visitors ===")

    depth_visitor = DepthVisitor()
    root.accept(depth_visitor)
    print(f"[Demo] Profundidade máxima (mock) da árvore: {depth_visitor.max_depth}")

    count_visitor = CountLeavesVisitor()
    root.accept(count_visitor)
    print(f"[Demo] Número de folhas (mock) na árvore: {count_visitor.count}")


def demo_states(root: DecisionNode) -> None:
    print("\n=== Demo State (TreeBuilder) ===")
    builder = TreeBuilder()
    builder.build(root)


def main() -> None:
    root = build_mock_tree()
    demo_iterator(root)
    demo_visitors(root)
    demo_states(root)


if __name__ == "__main__":
    main()
