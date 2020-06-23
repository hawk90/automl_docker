import docker
import docker_conf as dc

class Client:
    def __init__(self):
        print("* Init global client")
        self.client = dc.get_client()

    def get_client(self):
        return self.client

class Handler:
    def __init__(self):
        print("* Init global container handler's list")
        self.container_handler_list = []

    def get_handler_list(self):
        return self.container_handler_list

    def set_handler_list(self, new_handler):
        try:
            self.container_handler_list.append(new_handler)
        except Exception as e:
            return False
        else:
            return True

###############################################################
def download_images_from_repo():
    """
    """

###############################################################
def remove_images_in_local():
    """
    """

###############################################################
def remove_image_in_local():
    """
    """

###############################################################
def create_container_handler_attribute(config):
    """
        config
         - owner
         - container id
         - container name
    """
    fmt = "Hellow"

    return fmt

###############################################################
def create_container(client, handler, config):
    """
    """
    try: 
        client.containers.run("ubuntu:latest",
                "echo hello world")
        container_handler = create_container_handler_attribute(config)
        handler.set_handler_list(container_handler)
    except docker.errors.ContainerError as e:
        print("Error: ", e) 
    except docker.errors.ImageNotFound as e:
        print("Error: ", e)
    except docker.errors.APIError as e:
        print("Error: ", e)
        

###############################################################
def start_container(client, handler, c_id_or_name):
    """
    """
    try:
    


###############################################################
def stop_container(client, handler, c_id_or_name):
    """
    """


###############################################################
def prune_containers()
    """
    """
    try:
        client.containers.prune()
    except docker.errors.APIError as e:
        print("Error: ", e)
