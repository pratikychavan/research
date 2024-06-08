from wfml import PipelineController

pipeline = PipelineController(
    name="some-pipeline",
    project="some-project",
    always_create_from_code=True
)

pipeline.add_parameter(
    name="a",
    default=2,
    param_type="integer"
)

def step1(a):
    
    import pandas as pd
    df = pd.DataFrame()
    for num in range(int(a)):
        df[str(num)] = range(1,11)
    
    return df

pipeline.add_function_step(
    name="step1",
    execution_queue="pratik",
    function=step1,
    function_kwargs={"a":"${pipeline.a}"},
    function_return=["df"],
)

def step2(df):
    
    import pandas as pd 
    import matplotlib.pyplot as plt 
    df = pd.DataFrame() 
    for a in range(2):
        df[str(a)] = range(0,10)
    fig = df.plot(x="0", y="1", kind="bar").figure
    fig.savefig("x.png")
    
    return fig

pipeline.add_function_step(
    name="step2",
    execution_queue="pratik",
    parents=["step1"],
    function=step2,
    function_return=["fig"],
)

import os
if os.environ.get("I_AM_CLEARML_SERVER") == "TRUE":
    pipeline.create_draft()
else:
    pipeline.start_locally(run_pipeline_steps_locally=True)