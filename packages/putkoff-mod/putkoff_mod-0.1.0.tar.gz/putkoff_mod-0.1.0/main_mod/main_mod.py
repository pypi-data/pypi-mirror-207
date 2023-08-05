import os
import sys
import json
import importlib
import importlib.util
from collections import defaultdict

# Function to import all modules from a directory
def import_all_from_folder(folder_path):
    modules = []
    functions = defaultdict(list)

    # Append the folder_path and all its subdirectories to sys.path
    for root, dirs, files in os.walk(folder_path):
        sys.path.append(root)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                module_name = file[:-3]
                module_path = os.path.relpath(root, folder_path).replace(os.sep, ".")
                if module_path:
                    module_name = f"{module_path}.{module_name}"
                
                spec = importlib.util.spec_from_file_location(module_name, os.path.join(root, file))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                modules.append(module_name)

                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if callable(attr) and not attr_name.startswith('_'):
                        functions[module_name].append(attr_name)
                        # Add the function directly to the current module's globals
                        globals()[attr_name] = attr
    return modules, functions

# Import all components
components_dir = os.path.join(os.path.dirname(__file__), "components")
modules, functions = import_all_from_folder(components_dir)

# Import additional directories
additional_directory_imports = "/home/hmmm/Documents/python_scripts/shared/components/"
if additional_directory_imports:
    additional_directories = additional_directory_imports.split(",")
    for additional_directory in additional_directories:
        additional_modules, additional_functions = import_all_from_folder(additional_directory)
        modules.extend(additional_modules)
        for key, value in additional_functions.items():
            functions[key].extend(value)

# Save function lists
all_functions_path = os.path.join(os.path.dirname(__file__), "all_functions")
with open(os.path.join(all_functions_path, "all_modules.json"), "w") as f:
    json.dump(modules, f)

with open(os.path.join(all_functions_path, "all_functions.json"), "w") as f:
    json.dump(functions, f)

# Find duplicate functions
duplicates = defaultdict(list)
for module, func_list in functions.items():
    for func in func_list:
        for other_module, other_func_list in functions.items():
            if module != other_module and func in other_func_list:
                duplicates[func].append((module, other_module))

# Save duplicates to JSON
with open(os.path.join(all_functions_path, "all_function_duplicates.json"), "w") as f:
    json.dump(duplicates, f)

