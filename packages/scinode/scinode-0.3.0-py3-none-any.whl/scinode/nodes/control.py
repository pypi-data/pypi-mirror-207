from scinode.core.node import Node


class ScinodeSwitch(Node):
    identifier: str = "Switch"
    node_type: str = "Switch"
    catalog = "Control"

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("General", "Input")
        self.inputs.new("General", "Switch")
        self.outputs.new("General", "Result")
        self.kwargs = ["Input", "Switch"]

    def get_executor(self):
        return {
            "path": "scinode.executors.controls.switch_node",
            "name": "ScinodeSwitch",
            "type": "class",
        }


class ScinodeUpdate(Node):
    identifier: str = "Update"
    node_type: str = "Update"
    catalog = "Control"

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("General", "Input")
        self.inputs.new("General", "Update")
        self.outputs.new("General", "Result")
        self.kwargs = ["Input", "Update"]

    def get_executor(self):
        return {
            "path": "scinode.executors.controls.update_node",
            "name": "ScinodeUpdate",
            "type": "class",
        }


class ScinodeScatter(Node):
    identifier = "Scatter"
    node_type = "Scatter"
    catalog = "Control"

    def create_properties(self):
        self.properties.new("String", "DataType", data={"default": "General"})

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        socket = self.inputs.new("General", "Input")
        socket.link_limit = 100
        socket = self.inputs.new("General", "Stop")
        self.outputs.new("General", "Result")
        self.kwargs = ["Input", "Stop"]

    def get_executor(self):
        return {
            "path": "scinode.executors.controls.scatter_node",
            "name": "ScinodeScatter",
            "type": "class",
        }


node_list = [
    ScinodeSwitch,
    ScinodeUpdate,
    ScinodeScatter,
]
