from wfml import PipelineDecorator

@PipelineDecorator.pipeline(
  name='pipeline', project='examples', version='0.1', 
  args_map={'General':['pickle_url'], 'Mock':['mock_parameter']}
)
def main(pickle_url, mock_parameter='mock'):
    data_frame = step_one(pickle_url)
    X_train, X_test, y_train, y_test = step_two(data_frame)
    model = step_three(X_train, y_train)
    accuracy = 100 * step_four(model, X_data=X_test, Y_data=y_test)
    print(f"Accuracy={accuracy}%")