def paginate(num, results):
    tmp_page = []
    final_page = []
    added_hosts = set()
    pending = []
    for item in results:
        if len(tmp_page) < num:
            if item[0] not in added_hosts:
                tmp_page.append(item)
                added_hosts.add(item[0])
            else:
                pending.append(item)
        else:
            tmp_page.append("")
            for entry in tmp_page:
                final_page.append(entry)
            tmp_page = []
            added_hosts = set()
            for index, entry in enumerate(pending):
                if len(tmp_page) < num:
                    if entry[0] not in added_hosts:
                        tmp_page.append(pending.pop(index))
                        added_hosts.add(entry[0])
            tmp_page.append("")
            for entry in tmp_page:
                final_page.append(entry)
            tmp_page = []
            added_hosts = set()
    for item in pending:
        final_page.append(item)
