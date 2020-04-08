#unprinted_designs=['iphone case', 'robot pendant','dodecahedron']
#completed_models=[]
#
#while unprinted_designs:
#    current_design = unprinted_designs.pop()
#    print("Printing Model: "+current_design)
#    completed_models.append(current_design)
#
#print("\nThe following models havee been printed: ")
#for completed_model in completed_models:
#    print(completed_model)

def print_models(unprinted_designs, completed_models):

    """Simula a impressão de cada design, até que nao haja mais nenhum.
        Transfere cada design para completed_models após a impressão"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing Model: "+current_design.title())
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Mostra todos os modelos impressos"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print("\t"+completed_model.title())

unprinted_designs=['iphone case', 'robot pendant','dodecahedron']
completed_models=[]

print_models(unprinted_designs[:], completed_models)
#a notação [:] cria uma cópia da lista
show_completed_models(completed_models)