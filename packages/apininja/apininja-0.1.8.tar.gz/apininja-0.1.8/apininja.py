import argparse

def pascal_to_snake(string: str):
    snake_string = ''

    for i, char in enumerate(string):
        if char.isupper() and i > 0:
            snake_string += '_'
        snake_string += char.lower()

    return snake_string


def generate_module(model_name):
    # Convert model name to snake case
    model_name = pascal_to_snake(model_name)

    serialize_single = f'def serialize_{model_name}(data):\n'
    serialize_single += f'\treturn {{"id": data.id}}\n\n'

    serialize_multitple = f'def serialize_{model_name}s(lst):\n'
    serialize_multitple += f'\tserialized = []\n'
    serialize_multitple += f'\tfor item in lst:\n'
    serialize_multitple += f'\t\tserialized.append(serialize_{model_name}(item))\n'
    serialize_multitple += f'\treturn serialized\n\n'

    api_list = f'def {model_name}_list_api(lst):\n'
    api_list += f'\treturn serialize_{model_name}s(lst)\n\n'

    api_detail = f'def {model_name}_detail_api(data):\n'
    api_detail += f'\treturn serialize_{model_name}(data)\n\n'

    api_create = f'def {model_name}_create_api(*args, **kwargs):\n'
    api_create += f'\tpass\n\n'

    api_update = f'def {model_name}_update_api(*args, **kwargs):\n'
    api_update += f'\tpass\n\n'

    api_delete = f'def {model_name}_delete_api(*args):\n'
    api_delete += f'\tpass\n\n'

    functions = [
        serialize_single,
        serialize_multitple,
        api_list,
        api_detail,
        api_create,
        api_update,
        api_delete
    ]

    module_code = f"# API Created for {model_name}\n\n{''.join(functions)}"

    with open(f"{model_name}_api.py", "w") as file:
        file.write(module_code)

    print(f'API module {model_name}_api.py created successfully!')

def main():
    parser = argparse.ArgumentParser(description='Python module generator')
    parser.add_argument('model_name', type=str, help='Name of the model')
    args = parser.parse_args()

    generate_module(args.model_name)

if __name__ == '__main__':
    main()
