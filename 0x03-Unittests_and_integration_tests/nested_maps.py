def access_nested_maps(nested_map, path):
    """Accesses a nested dictionary structure by a list of keys.
    
    Args:
        nested_map (dict): The nested dictionary to access.
        path (list): A list of keys representing the path to the desired value.
    
    Returns:
        The value found at the specified path in the nested_map.
    
    Raises:
        KeyError: If a key in the path doesn't exist.
    """
    for key in path:
        nested_map = nested_map[key]  # Go one level deeper with each key
    return nested_map
