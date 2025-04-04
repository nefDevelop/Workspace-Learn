import os
import yaml

from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = "compose_templates"
OUTPUT_DIR = "output"
VARIABLES_FILE = "variables.yml"

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

vars = yaml.safe_load(open(VARIABLES_FILE))

for filename in os.listdir(TEMPLATE_DIR):
    if filename.endswith(".j2"):
        template_name = filename
        base_name = filename[:-3]
        template = env.get_template(template_name)

        output_text = template.render(vars)

        with open(os.path.join(OUTPUT_DIR, base_name), "w") as out_file:
            out_file.write(output_text)

        print(f"Generado: {base_name}")