#!env python3

import collections

import pycollimator.model_builder.core as core
from pycollimator.model_builder.model import ModelBuilder


def _parse_parameters(parameters, model_builder, value_key):
    if type(parameters) is list:
        for param in parameters:
            model_builder.add_parameter(param["name"], param[value_key])
    elif type(parameters) is dict:
        for key, val in parameters.items():
            model_builder.add_parameter(key, val[value_key])


def parse_json(data):
    uuids = {}
    uiprops = {}
    root_model_builder = ModelBuilder(data["name"])
    uuids[root_model_builder.id] = data["uuid"]
    core_vars = vars(core)

    nodes = {}

    _parse_parameters(data["parameters"], root_model_builder, "value")

    submodels = {}

    def _handle_group(model_builder, node):
        diagram_uuid = data["submodels"]["references"][node["uuid"]]["diagram_uuid"]
        group_builder = ModelBuilder(node["name"])
        parse_diagram(group_builder, data["submodels"]["diagrams"][diagram_uuid])
        model_builder.add_group(nodes[node["uuid"]], group_builder)

    def _handle_submodel(model_builder, node):
        submodel_uuid = node["submodel_reference_uuid"]

        if submodel_uuid not in submodels:
            submodel_json = data["reference_submodels"][submodel_uuid]
            submodels[submodel_uuid] = ModelBuilder(submodel_json["name"])
            _parse_parameters(submodel_json["parameters"], submodels[submodel_uuid], "default_value")
            parse_diagram(
                submodels[submodel_uuid],
                submodel_json["diagram"],
            )
        submodel = submodels[submodel_uuid]
        model_builder.add_reference_submodel(nodes[node["uuid"]], submodel)

    def parse_diagram(model_builder, diagram):
        for node in diagram["nodes"]:
            params = {param_name: param_data["value"] for param_name, param_data in node["parameters"].items()}
            node_type = "".join(node["type"].split(".")[1:])

            if node_type in ("Submodel", "Group"):
                params["input_names"] = tuple(i["name"] for i in node["inputs"])
                params["output_names"] = tuple(i["name"] for i in node["outputs"])
            elif node_type == "ReferenceSubmodel":
                params["input_names"] = tuple(i["name"] for i in node["inputs"])
                params["output_names"] = tuple(i["name"] for i in node["outputs"])

            node_obj = core_vars[node_type](model=model_builder, name=node["name"], **params)
            nodes[node["uuid"]] = node_obj
            uuids[node_obj.id] = node["uuid"]
            uiprops[node_obj.id] = node["uiprops"]

            if node_type in ("Submodel", "Group"):
                _handle_group(model_builder, node)
            elif node_type == "ReferenceSubmodel":
                _handle_submodel(model_builder, node)

        node_inputs = collections.defaultdict(list)
        for link in diagram["links"]:
            src_node = nodes[link["src"]["node"]]
            src_port_id = link["src"]["port"]
            dst_node = nodes[link["dst"]["node"]]
            dst_port_id = link["dst"]["port"]
            node_inputs[dst_node].append((src_node, src_port_id))
            out_port = src_node.output_port(src_port_id)
            in_port = dst_node.input_port(dst_port_id)
            l = model_builder.add_link(out_port, in_port)
            uuids[l.id] = link["uuid"]
            uiprops[l.id] = link["uiprops"]

    parse_diagram(root_model_builder, data["diagram"] if "diagram" in data else data["rootModel"])
    return root_model_builder, uuids, uiprops
