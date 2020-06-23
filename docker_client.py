import docker_conf as dc
import docker_exec as de
import docker_monitor as dm
from docker_exec import Handler
from docker_exec import Client

def main():
    g_client = Client().get_client()
    g_handler = Handler()

    print("* Start - run container")
    de.create_container(g_client, g_handler, 0)
    print("* Done - run container")

    print("* Start - get contaienr list")
    dm.get_container_all_list(g_client, g_handler)
    print("* Done - get container list")

###############################################################
if __name__ == "__main__":
    main()
