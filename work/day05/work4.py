def print_model(unprinted_designs, completed_models):
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print("Printing model :" + current_designs)
        completed_models.append(current_designs)


def show_completed_models(completed_models):
    print("\nThe following models have printed:")
    for i in completed_models:
        print(i)


unprinted_designs = ['iphone', 'robot', 'doc']
completed_models =[]

print_model(unprinted_designs[:],completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
