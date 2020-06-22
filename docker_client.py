import docker_conf as dc

def main():
    client = dc.get_client()
    print(client)


if __name__ == "__main__":
    main()
