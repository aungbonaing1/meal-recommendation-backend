def filter_by_keys(dict_item, select_keys = None, process = None):
    if select_keys == None:
        select_keys = dict_item.keys()
    if len(select_keys) == 0:
        return {}
    new_item = {}
    for key in dict_item:
        if not key in select_keys:
            continue
        new_item[key] = dict_item[key] if process == None else process(dict_item[key])
    return new_item

def get_dynamodb_dict_arr(items, select_keys = None, process = None):
    rows = []
    for item in items:
        if process:
            item = process(item)
        if item == None:
            continue
        row = get_dynamodb_put_request_dict(item, select_keys)
        rows.append(row)
    return rows

def get_dynamodb_dict(item, select_keys = None):
    return filter_by_keys(item, select_keys, lambda x: {'S': str(x)})

def get_dynamodb_put_request_dict(item, select_keys = None):
    item = get_dynamodb_dict(item, select_keys)
    return {'PutRequest': { 'Item': item}}