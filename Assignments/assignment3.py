from typing import List

def insert(data, s: str)-> None:
    if s == "":
        return
    if len(s) == 1:
        if s in data:
            data[s][1] = True
        else:
            data[s] = [{}, True]
    if s[0] in data:
        insert(data[s[0]][0], s[1:])
    else:
        data[s[0]]= [{}, False]
        insert(data[s[0]][0], s[1:])


def count_words(data)->int:
    """
    Returns the number of words encoded in data. You may assume
    data is a valid trie.

    >>> data = {}
    >>> insert(data, "test")
    >>> insert(data, "testing")
    >>> insert(data, "doc")
    >>> insert(data, "docs")
    >>> insert(data, "document")
    >>> insert(data, "documenting")

    >>> count_words(data)
    6
    """
    count = 0

    for char in data:
        if data[char][1]:
            count += 1
        count += count_words(data[char][0])

    return count


def contains(data, s: str)-> bool:
    """
    Returns True if and only if s is encoded within data. You may
    assume data is a valid trie.

    >>> data = {}
    >>> insert(data, "tree")
    >>> insert(data, "trie")
    >>> insert(data, "try")
    >>> insert(data, "trying")
    
    >>> contains(data, "try")
    True
    >>> contains(data, "trying")
    True
    >>> contains(data, "the")
    False
    """
    if s == "":
        return True

    if s[0] not in data:
        return False

    if len(s) == 1:
        return data[s[0]][1]

    return contains(data[s[0]][0], s[1:])


def height(data)->int:
    """
    Returns the length of longest word encoded in data. You may
    assume that data is a valid trie.

    >>> data = {}
    >>> insert(data, "test")
    >>> insert(data, "testing")
    >>> insert(data, "doc")
    >>> insert(data, "docs")
    >>> insert(data, "document")
    >>> insert(data, "documenting")

    >>> height(data)
    11
    """
    if not data:
        return 0

    max_height = 0

    for char in data:
        # Get height of subtrie and add 1 for current character
        subtrie_height = height(data[char][0])
        max_height = max(max_height, 1 + subtrie_height)
    return max_height
    

def count_from_prefix(data, prefix: str)-> int:
    """
    Returns the number of words in data which starts with the string
    prefix, but is not equal to prefix. You may assume data is a valid
    trie.

    data = {}
    >>> insert(data, "python")
    >>> insert(data, "pro")
    >>> insert(data, "professionnal")
    >>> insert(data, "program")
    >>> insert(data, "programming")
    >>> insert(data, "programmer")
    >>> insert(data, "programmers")

    >>> count_from_prefix(data, 'pro')
    5
    """
    if prefix == "":
        return 0

    current = data
    is_prefix_word = False

    for i, char in enumerate(prefix):
        if char not in current:
            return 0
        if i == len(prefix) - 1:
            is_prefix_word = current[char][1]
        current = current[char][0]

    total = count_words(current)
    return total - 1 if is_prefix_word else total
    

def get_suggestions(data, prefix:str)-> List[str]:
    """
    Returns a list of words which are encoded in data, and starts with
    prefix, but is not equal to prefix. You may assume data is a valid
    trie.

    data = {}
    >>> insert(data, "python")
    >>> insert(data, "pro")
    >>> insert(data, "professionnal")
    >>> insert(data, "program")
    >>> insert(data, "programming")
    >>> insert(data, "programmer")
    >>> insert(data, "programmers")

    >>> get_suggestions(data, "progr")
    ['program', 'programming', 'programmer', 'programmers']
    """
    if prefix == "":
        return []

    current = data
    for char in prefix:
        if char not in current:
            return []
        current = current[char][0]

    suggestions = []

    def collect_words(node, current_word):
        for char in node:
            new_word = current_word + char
            if node[char][1]:
                suggestions.append(new_word)
            collect_words(node[char][0], new_word)

    collect_words(current, prefix)

    if prefix in suggestions:
        suggestions.remove(prefix)

    return suggestions
    




    

    
