# Student ToDo App - Version Control
# by Sal Code
# GitHub Repository: https://github.com/Salazar34/Student-ToDo-App

# Global Var 
start = None
choose = None
event = None
to_do_list = []
# Menu function -> Start
def menu(start, choose):
    print('----- MENU INIZIALE -----')
    print('** Ben Tornato nel menu inizale. Selezionare l\'azioone che si desidera compiere **')
    print('1: Visualizzare gli eventi salvati\n2: Aggiungere un evento\n3: Eliminare un evento')
    start = int(input(''))

    if start == 1:
        event_checker(to_do_list, choose)
    
    elif start == 2:
        event_add(to_do_list, choose, event)
    
    elif start == 3:
        event_del(to_do_list, choose, event)
    
    else:
        print('Perfetto! Aspetto che tu mi dia delle direttive.')
        choose = input('Vuoi uscire o tornare al menu principale? (uscire - menu) ')
        if choose == 'menu':
            menu(start)
        else:
            print('Arrivederci! ')
    
# Visualizing events -> event_checker
def event_checker(to_do_list, choose):
    print('----- HAI SELEZIONATO LA VOCE PER VISIONARE GLI EVENTI -----')
    print(f'ECCO A TE TUTTI GLI EVENTI: {to_do_list}', sep='')
    choose = input('VUOI USCIRE O TORNARE AL MENU PRINCIPALE? (uscire - menu) ')
    if choose == 'menu':
        menu(start, choose)
    else:
        print('Arrivederci! ')

# Adding events to the ToDo List -> event_add
def event_add(to_do_list, choose, event):
    print('----- HAI SELEZIONATO LA VOCE PER AGGIUNGERE DEGLI EVENTI -----')
    event = input('INSERIRE L\'EVENTO DA AGGIUNGERE:')
    to_do_list.append(event)
    print(f'ECCO LA TUA LISTA AGGIORNATA: {to_do_list}', sep='')
    choose = input('VUOI USCIRE O TORNARE AL MENU PRINCIPALE? (uscire - menu) ')
    if choose == 'menu':
        menu(start, choose)
    else:
        print('Arrivederci! ')

# Deleting events to the ToDO List -> event_del()
def event_del(to_do_list, choose, event):
    print('----- HAI SELEZIONATO LA VOCE PER ELIMINARE DEGLI EVENTI -----')
    print(f'LA TUA LISTA DEGLI EVENTI: {to_do_list}', sep='')
    event = input('QUALE EVENTO VUOI ELIMINARE? (Indicare l\'elemento con l\'appropriata posizione, partendo da 0) ')
    to_do_list.remove(event)
    choose = input('VUOI USCIRE O TORNARE AL MENU PRINCIPALE? (uscire - menu) ')
    if choose == 'menu':
        menu(start, choose)
    else:
        print('Arrivederci! ')

menu(start, choose)