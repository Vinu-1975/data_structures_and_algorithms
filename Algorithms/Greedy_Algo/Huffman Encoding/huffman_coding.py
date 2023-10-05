from collections import Counter
from heapq import heappush, heappop,heapify

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(s):
    freq_dict = Counter(s)
    pq = [Node(char, freq) for char, freq in freq_dict.items()]
    heapify(pq)
    while len(pq) > 1:
        left = heappop(pq)
        right = heappop(pq)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heappush(pq, merged)

    return pq[0]

def build_huffman_codes(root):
    def _build_huffman_codes_recursive(node, code, result):
        if node is None:
            return
        if node.char is not None:
            result[node.char] = code
            return
        _build_huffman_codes_recursive(node.left, code + '0', result)
        _build_huffman_codes_recursive(node.right, code + '1', result)

    result = {}
    _build_huffman_codes_recursive(root, '', result)
    return result

def huffman_encode(s, codes):
    return ''.join([codes[char] for char in s])

def huffman_decode(encoded_message, root):
    decoded_message = ''
    current_node = root
    for bit in encoded_message:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_message += current_node.char
            current_node = root

    return decoded_message

# Test the Huffman encoding and decoding
s = "geeksforgeeks"
root = build_huffman_tree(s)
codes = build_huffman_codes(root)

encoded_message = huffman_encode(s, codes)
print(f"Encoded: {encoded_message}")

decoded_message = huffman_decode(encoded_message, root)
print(f"Decoded: {decoded_message}")
