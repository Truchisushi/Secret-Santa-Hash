#from sets import Set

def read_input():
    '''
    Read input
    Return: People and rules
    '''
    f = open("data.dat", "r")
    people = set()
    rules = []
    for line in f:
        entry = line.split()
        people.update(entry)
        rules.append(entry)
    return people, rules

def generate(people, rules):
    rules = sorted(rules, key=len)
    output = dict()

    for rule in reversed(rules):
        temp_set = people.copy()
        for peep in rule:
            temp_set = temp_set - set([peep])
        output[rule[0]] =  temp_set.pop()
        people.remove(output[rule[0]])

    return output

if __name__ == '__main__':
    f = open("output.out", "w+")
    people, rules = read_input()
    output = generate(people, rules)
    for peep, match in output.items():
        f.write(peep + " " + match + "\n")
    f.close()
