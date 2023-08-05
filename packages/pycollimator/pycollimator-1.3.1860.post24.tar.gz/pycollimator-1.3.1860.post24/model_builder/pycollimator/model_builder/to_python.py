from pycollimator.model_builder.core import Inport, Outport, ReferenceSubmodel


def to_python_str(model_builder, model_name="model"):
    sub_uuid_to_names = {}
    lines, submodels_func_def = _to_python_str(model_builder, sub_uuid_to_names, model_name=model_name)

    create_submodels = [
        f'submodels["{submodel_name}"] = create_{submodel_name}()' for submodel_name, _ in submodels_func_def.items()
    ]

    submodels_func_def = [line for lines in submodels_func_def.values() for line in lines]

    return "\n".join(["submodels = {}"] + submodels_func_def + create_submodels + lines)


def _to_python_str(model_builder, sub_uuid_to_names, model_name="model"):
    lines = []
    submodels_func_def = {}

    lines.append(f'{model_name} = ModelBuilder("{model_name}")')

    # Parameters
    lines.extend([f'{model_name}.add_parameter("{k}", "{v}")' for k, v in model_builder.parameters.items()])

    lines.append("")

    # Groups
    groups = set()
    for node, group in model_builder.groups.items():
        lines.append(f"def create_{node.name}():")
        group_code, other_submodels = _to_python_str(group, sub_uuid_to_names, model_name=node.name)
        submodels_func_def.update(other_submodels)
        group_code += [f"return {node.name}", ""]
        group_code = "\n".join("    " + line for line in group_code)
        lines.append(group_code)
        groups.add(node.id)

    # Submodels
    for node, submodel in model_builder.submodels.items():
        submodel_code, other_submodels = _to_python_str(submodel, sub_uuid_to_names, model_name=submodel.name)
        submodel_code = "\n".join("    " + line for line in submodel_code)
        submodel_def_str = [
            f"def create_{submodel.name}():",
            submodel_code,
            f"    return {submodel.name}",
            "",
        ]

        submodels_func_def.update(other_submodels)
        submodels_func_def[submodel.name] = submodel_def_str
        sub_uuid_to_names[submodel.uuid] = submodel.name

    # Create nodes
    for node in model_builder.nodes.values():
        node_params = [f'{k}="{v}"' if type(v) is str else f"{k}={v}" for k, v in node.params.items()]
        func_params = [f"model={model_name}", f'name="{node.name}"']
        params = func_params + node_params
        params_str = ", ".join(params)
        lines.append(f"{node.name} = core.{node.__class__.__name__}({params_str})")

        if type(node) is ReferenceSubmodel:
            submodel_name = model_builder.submodels[node].name
            lines.append(f'{model_name}.add_reference_submodel({node.name}, submodels["{submodel_name}"])')

        if node.id in groups:
            lines.append(f"{model_name}.add_group({node.name}, create_{node.name}())")

    lines.append("")

    # Connect nodes
    for link in model_builder.links.values():
        src = f"{link.src.node.name}.{link.src.name}"
        dst = f"{link.dst.node.name}.{link.dst.name}"
        lines.append(f"{model_name}.add_link({src}, {dst})")

    return lines, submodels_func_def
