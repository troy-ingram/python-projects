import journal

def main():
    print_header()
    run_event_loop()
    
def print_header():
    print('------------------')
    print('   JOURNAL APP')
    print('------------------')

def run_event_loop():
    print("What do you want to do with your journal?")
    question = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)
    
    while question != 'x' and question:
        question = input('What do you want to do? [L]ist, [A]dd, or E[x]it? ')
        cmd = question.lower().strip()
        
        if cmd == 'a':
            add_entry(journal_data)
        elif cmd == 'l':
            list_entries(journal_data)
        elif cmd != 'x' and question:
            print("Sorry, we don't understand '{}'.".format(cmd))
    
    print('exiting...')
    journal.save(journal_name, journal_data)

def list_entries(data):
    print('Your journal entries: ')
    for x, item in enumerate(data):
        print('{}. {}'.format(x+1, item))
    
def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)

if __name__ == '__main__':
    main()