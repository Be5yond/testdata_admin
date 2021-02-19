
def transform(data):
    """
    replace json object values
    :param data: json data to be rendered
    :return: schema str
    """
    if isinstance(data, str): 
        return '{% str %}'
    elif isinstance(data, bool): 
        return '{% bool %}'
    elif isinstance(data, int): 
        return '{% int %}'
    elif isinstance(data, dict):
        for k, v in data.items():
            data[k] = transform(v)
    elif isinstance(data, list):
        try:
            data = [transform(data[0])]
        except IndexError:
            data = []
    return data