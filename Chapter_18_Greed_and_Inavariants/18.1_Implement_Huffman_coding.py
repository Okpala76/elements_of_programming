## Fairly black Ninja

# This problem want to take in a pair of symbol and frequency list of tuples and return teh most effcient way to
# get them encoded so that the a most effcient when decoding, making use of binary strings for storage

# The bruteforce is a extrinous one with will require that we test every possible out come of the combination of all
# values and frequencies and before determning which one is the best and most efficient pick

# Problem 18.1: Given a set of symbols with corresponding frequencies, find a code
# book that has the smallest average code length.


from dataclasses import dataclass
import heapq
from itertools import count


@dataclass
class Node:
    symbol: str | None
    frequency: int
    left: "Node| None" = None
    right: "Node | None" = None


def huffman_code(frequency_symbol: list[tuple[int, int]]) -> dict:
    min_heap = []
    unique_id = count()

    for sym, fre in frequency_symbol:  # O(n)
        curr_node = Node(sym, fre)

        heapq.heappush(min_heap, (fre, next(unique_id), curr_node))  # O(log n)

    while len(min_heap) > 1:  # O(n) and O(log n)

        fre_1, _, node_1 = heapq.heappop(min_heap)
        fre_2, _, node_2 = heapq.heappop(min_heap)

        combine_fre = fre_1 + fre_2

        curr_node = Node(symbol=None, frequency=combine_fre, left=node_1, right=node_2)

        heapq.heappush(min_heap, (combine_fre, next(unique_id), curr_node))

    # The left node will be the head Node
    # the we go

    _, _, root = min_heap[0]

    code_book = {}

    def code_dict_creator(
        node: Node, binary_str: str
    ) -> None:  # Space = O(h) height of the tree, time o(n becase we visit all man)
        if node is None:
            return None

        if node.symbol is not None:
            code_book[node.symbol] = binary_str or "0"

        code_dict_creator(node.left, binary_str + "0")
        code_dict_creator(node.right, binary_str + "1")

    code_dict_creator(root, "")

    return code_book


if __name__ == "__main__":
    print(
        huffman_code(
            [
                ("A", 5),
                ("B", 3),
                ("C", 2),
                ("D", 1),
            ]
        )
    )


## Complexity
# Time = O(n log n ) .. n is for the heap population, log n is for the combination solution in getting the root heap
# Space = O(n) the size of the heap

# Pattern = Huffman code + heap +binary tree
