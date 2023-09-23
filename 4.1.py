import networkx as nx


#print(graph.in_edges("e")) # => [('a', 'e'), ('d', 'e')]

# iterator =graph.__iter__()


# print(graph.successors('a'))
# for x in iterator:

#     if( graph.in_edges(x) == graph. ) :   



#bu kod onemli recursivede istedigimiz sonucu bulmaya yariyor. 
#else return yapinca hata verdi elsein altina bir if daha koyarak durdurmayi basardin.
def isRoute(graph,letter,letter2):
    iterator = graph.successors(letter)

    for x in iterator:
        if x  == letter2:
            return "buldu"
        else:
            result = isRoute(graph,x,letter2)
            if result == "buldu":
                return result





graph = nx.DiGraph()
graph.add_edges_from ( [("a", "b"), ("a", "e"), ("e", "d"), ("b", "c")] )

print(isRoute(graph,'a','c'))
