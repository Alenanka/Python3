with open('nginx_logs.txt', 'r') as f:
    parsed_log = []
    for line in f:
        parsed_log.append((line.split()[0], line.replace('"', '').split()[5], line.replace('"', '').split()[6]))
    print(parsed_log)
    dict_parset_log = {}
    for parsed in parsed_log:
         dict_parset_log[parsed[0]] = dict_parset_log.get(parsed[0], 0) + 1
    spamer = (sorted(dict_parset_log.items(), key=lambda x: x[1], reverse=True))[0]
    print(f'IP-адрес спамера: {spamer[0]}, количество запросов: {spamer[1]}')