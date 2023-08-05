import docker


class JLDocker:
    def __init__(self, env_file=None):
        if not env_file:
            self.client = docker.from_env()

    def __get_pretty_ports_output(self, ports):
        pretty_ports = []
        for cont_port, host_port in ports.items():
            if host_port:
                ip, port = host_port[0]['HostIp'].replace('0.0.0.0', '*'), host_port[0]['HostPort']
                host_port =  f"{ip}:{port}->"
            pretty_ports.append(host_port+cont_port)

        # ", ".join(pretty_ports)
        return pretty_ports

    def ps(self):

        # 猜测网络名, 默认使用bridge. [#docker network ls]
        # 由docker-compose创建的一般名为docker_default或services_default之类，除非在docker-compose.yml中自定义
        networks = [n.name for n in self.client.networks.list()]
        if "bridge" in networks:
            Network = "bridge"

        for network in networks:
            if "_default" in network:
                Network = network

        for c in self.client.containers.list(all=all):
            for network in c.attrs['NetworkSettings']['Networks'].keys():
                Network = network
                break

        assert Network is not None

        None2EmptyList = lambda s: [] if not s else s

        containers = []
        for c in self.client.containers.list(all=all):
            name = c.name[:12].ljust(14)
            image = c.image.tags[0][:12].ljust(14)
            status =  "\033[1;32m{}\033[0m".format(c.status) if "runnin" in c.status else c.status
            cmd = " ".join(None2EmptyList(c.attrs['Config']['Cmd'])+None2EmptyList(c.attrs['Config']['Entrypoint']))[:38].ljust(40)
            ip = c.attrs['NetworkSettings']['Networks'][Network]['IPAddress'][:12].ljust(14)
            ports = ", ".join(self.__get_pretty_ports_output(c.ports))[:56].ljust(50)
            containers.append(f"|  {name}|  {image}|  {ip}|  {status}  |  {cmd}|  {ports}|")

        SPLIT = "-"*160
        titles = ["name".ljust(14),
                "image".ljust(14),
                "ip address".ljust(14),
                "status".ljust(9),
                "command".ljust(40),
                "ports".ljust(50)]
        HEADER = "|  "+"|  ".join(titles) +"|"

        print(SPLIT)
        print(HEADER)
        print("="*160)
        for c in containers:
            print(c)
        print(SPLIT)



if __name__ == "__main__":
    dock = JLDocker()
    dock.ps()
