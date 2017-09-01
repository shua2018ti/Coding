"""
Description:
When a user submis a search query on our platform, we return a list of results
scored according to the specified preferences. The search results are then presented
over several web pages. Given multple listings can belong to the same host though,
we want o be mindful that a host does not dominate the results in a single page.

Problem:
You are given an array of CSV strings representing search results. Each entry is
composed of host_id, listing_id, score and city
"""

def paginate(num, results):
    tmp_page = []
    final_page = []
    added_hosts = set()
    pending = []
    for item in results:
        clean_pending(pending, added_hosts, tmp_page, num)
        if item.split(",")[0] not in added_hosts:
            if len(tmp_page) < num:
                added_hosts.add(item.split(",")[0])
                tmp_page.append(item)
            else:
                tmp_page.append("")
                for entry in tmp_page:
                    final_page.append(entry)
                tmp_page = []
                added_hosts = set()
                clean_pending(pending, added_hosts, tmp_page, num)
                tmp_page.append(item)
                added_hosts.add(item.split(",")[0])
        else:
            pending.append(item)
    counter = 1
    while len(tmp_page) < num:
        tmp_page.append(pending.pop(0))
    tmp_page.append("")
    while len(tmp_page) > 0:
        final_page.append(tmp_page.pop(0))
    while len(pending) > 0:
        final_page.append(pending.pop(0))
        if counter % 5 == 0:
            final_page.append("")
            counter = 0
        counter += 1
    return final_page

def clean_pending(pending, added_hosts, tmp_page, num):
    if len(pending) > 0:
        counter = 0
        length = len(pending)
        while counter < length:
            if pending[0].split(",")[0] not in added_hosts and len(tmp_page) < num:
                added_hosts.add(pending[0].split(",")[0])
                tmp_page.append(pending.pop(0))
            counter += 1

results_per_page = 5
results = [
    "1,28,300.6,San Francisco",
    "4,5,209.1,San Francisco",
    "20,7,203.4,Oakland",
    "6,8,202.9,San Francisco",
    "6,10,199.8,San Francisco",
    "1,16,190.5,San Francisco",
    "6,29,185.3,San Francisco",
    "7,20,180.0,Oakland",
    "6,21,162.2,San Francisco",
    "2,18,161.7,San Jose",
    "2,30,149.8,San Jose",
    "3,76,146.7,San Francisco",
    "2,14,141.8,San Jose"
]

print("Input\n")
for item in results:
    print(item)

print("\nOutput\n")
output = paginate(results_per_page, results)
for item in output:
    print(item)
