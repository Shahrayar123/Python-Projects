def ipValidate(ip: str) -> bool:
    """
    Gets an ip: returns True if ip is valid, and False else.
    """

    from ipaddress import ip_address

    try:
        assert ip_address(ip)
    except:
        return False
    return True


