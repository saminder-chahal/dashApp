import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import subprocess
import logging

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO)

app = dash.Dash(__name__)

# Predefined modules for the dropdown
predefined_modules = ['utility_module_1', 'utility_module_2']

app.layout = html.Div([
    html.H1("Utility Script Runner"),
    dcc.Dropdown(
        id='module-dropdown',
        options=[{'label': module, 'value': module} for module in predefined_modules],
        value=predefined_modules[0],  # Default selected module
        style={'width': '50%'}
    ),
    html.Button('Show Arguments', id='show-arguments-button', n_clicks=0),
    dcc.Input(id='arguments-input', type='text', placeholder='Enter arguments'),
    html.Button('Run Script', id='run-button', n_clicks=0),
    html.Div(id='output-container'),
])

def get_argparse_help(module_name):
    try:
        # Run the script with a dummy argument to capture the argparse help message
        result = subprocess.check_output(['python', '-m', f"my_project.{module_name}", '--help'])
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode('utf-8')}"
    except Exception as e:
        return f"Error: {str(e)}"

def run_script(module_name, arguments):
    try:
        result = subprocess.check_output(['python', '-m', f"my_project.{module_name}"] + arguments.split())
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode('utf-8')}"
    except Exception as e:
        return f"Error: {str(e)}"

@app.callback(
    Output('output-container', 'children'),
    Input('show-arguments-button', 'n_clicks'),
    Input('run-button', 'n_clicks'),
    Input('module-dropdown', 'value'),
    Input('arguments-input', 'value'),  # Pass arguments-input as an input
)
def show_arguments(n_clicks_show, n_clicks_run, module_name, arguments):
    # Log the input values
    logging.info(f"Inputs: n_clicks_show={n_clicks_show}, n_clicks_run={n_clicks_run}, module_name={module_name}, arguments={arguments}")

    # Check which button was clicked
    ctx = dash.callback_context
    triggered_id = ctx.triggered_id.split('.')[0] if ctx.triggered_id else None

    if triggered_id == 'show-arguments-button' and n_clicks_show > 0:
        # If "Show Arguments" button was clicked
        help_message = get_argparse_help(module_name)
        return html.Pre(help_message, style={'whiteSpace': 'pre-wrap'})
    elif triggered_id == 'run-button' and n_clicks_run > 0 and arguments:
        # If "Run Script" button was clicked and arguments are provided

        result = run_script(module_name, arguments)

        # Log the result
        logging.info(f"Result: {result}")

        return result

    # If none of the conditions are met, clear the output
    return ''


if __name__ == '__main__':
    app.run_server(debug=True)
