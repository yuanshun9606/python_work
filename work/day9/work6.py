from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


graph = {'you': ['alice', 'bob', "claire"], 'bob': ['anuj', 'peggy'], 'alice': ['peggy'], 'claire': ['thom', 'jonny'],
         'anuj': [], 'peggy': [], "thom": [], 'jonny': []}


def search(name):
    search_deque = deque()
    search_deque += graph[name]
    searched = []
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                # break
                return True
            else:
                search_deque += graph[person]
                searched.append(person)
    return False



search('you')