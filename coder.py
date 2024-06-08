

def create_code(data):
    initial_code_block = f"""
from wfml import PipelineController

pipeline = PipelineController(
    name="{data['pipeline_name']}",
    project="{data['project_name']}",
    always_create_from_code=True
)
"""
    code = initial_code_block
    for parameter in data['pipeline_parameters']:
        code += f"""
pipeline.add_parameter(
    name="{parameter['name']}",
    default={parameter['default']},
    param_type="{parameter['type']}",
    description="{parameter['description']}"
)
"""