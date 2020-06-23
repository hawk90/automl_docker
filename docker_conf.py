import docker

def get_client():
    """
    return: client object
    """

    try:
        client = docker.from_env()
    except Exception as e:
        print('Error: ', e)
        return NULL;

    return client

