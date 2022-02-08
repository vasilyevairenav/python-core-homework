def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    categories = mapping["categories"]
    roles = mapping['roles']
    sorted_sequences = mapping['categoryIdsSorted']

    sorted_categories = [categories[ctgr] for ctgr in sorted_sequences]
    roles_tree = [new_category(ctgr, roles) for ctgr in sorted_categories]
    return {'categories': roles_tree}

def find_role(role_id, roles):
    """
    :param role_id: key id in roles dictionary
    :param roles: roles dictionary
    """
    role = roles[role_id]
    return {'id': role['id'], 'text': role['name']}

def new_category(catergory, roles):
    """
    :param category: category object
    :param roles: roles dictionary
    """
    new_id = 'category-' + catergory['id']
    text = catergory['name']
    items = [find_role(role, roles) for role in catergory['roleIds']]
    return {'id': new_id, 'text': text, 'items': items}
