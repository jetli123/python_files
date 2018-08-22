def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
def lookup(data, label, name):
    return data.get(label, name)
def store(data, *full_name):
    for full_na in full_name:
        names = full_na.split()
       # cc = len(names)
    if len(names) == 2:
        names.insert(1,'')
        print names
    labels = 'first', 'middel', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        print people
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


d = {}
init(d)
print lookup(d, 'last', 'Magnus Lie')
store(d, 'Magnus Lie', 'andk in skdk')


