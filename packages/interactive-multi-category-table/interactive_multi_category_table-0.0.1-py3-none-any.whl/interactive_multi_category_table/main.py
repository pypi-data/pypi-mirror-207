import os
from dash import Dash, html, dcc, callback, Output, Input
from utils import parse_json, gen_html_table, get_radioitems_options

def run_app(json_file_path):
    json_data, category_list, tag_list, category_dict = parse_json(json_file_path)

    row_category_value_init = category_list[0]
    column_category_value_init = category_list[1]
    row_category_options, column_category_options = get_radioitems_options(category_list, row_category_value_init, column_category_value_init)
    checklist_options = ['all'] + tag_list
    checklist_value_init = ['all']
    global checklist_value_previous
    checklist_value_previous = checklist_value_init

    app = Dash()
    app.title = os.path.split(json_file_path)[-1][:-5]
    app.layout = html.Div([
        html.Div([
            html.Div([
                html.H3('Categories:'),
                'Row:',
                dcc.RadioItems(row_category_options, row_category_value_init,
                                id='radioitems_row_category', inline=True),
                'Column:',
                dcc.RadioItems(column_category_options, column_category_value_init,
                                id='radioitems_column_category', inline=True),
            ], style={"padding": "10px", "margin": "10px"}),
            html.Div([
                html.H3('Tags:'),
                dcc.Checklist(checklist_options, checklist_value_init,
                                id='checklist_tags', inline=True),
            ], style={"padding": "10px", "margin": "10px"}),
        ], id='div-console',
           style={"display": "flex", "flex-direction": "row",
                  "padding": "10px", "margin": "10px",
                  "background": "#f1f1f1"}),
        html.Div([gen_html_table(json_data, category_dict, row_category_value_init, column_category_value_init, checklist_value_init)],
           id='div-table',
           style={"padding": "10px", "margin": "10px",
                  "background": "#f1f1f1"})
    ], id='div-container',
    style={"max-width": "1000px",
           "display": "flex", "flex-direction": "column"})

    @callback(
        Output('div-table', 'children'),
        Output('radioitems_row_category', 'options'),
        Output('radioitems_column_category', 'options'),
        Output('checklist_tags', 'value'),
        Input('radioitems_row_category', 'value'),
        Input('radioitems_column_category', 'value'),
        Input('checklist_tags', 'value')
    )
    def update_table(row_category_value, column_category_value, checklist_value):
        row_category_options, column_category_options = get_radioitems_options(category_list, row_category_value, column_category_value)
        global checklist_value_previous
        if 'all' not in checklist_value_previous and 'all' in checklist_value:
            checklist_value_previous = ['all']
        elif 'all' in checklist_value_previous and 'all' in checklist_value:
            if checklist_value_previous != checklist_value:
                checklist_value_previous = [i for i in checklist_value if i!='all']
        elif 'all' in checklist_value_previous and 'all' not in checklist_value:
            checklist_value_previous = ['all']
        else:
            checklist_value_previous = checklist_value
        return [gen_html_table(json_data, category_dict, row_category_value, column_category_value, checklist_value_previous)], row_category_options, column_category_options, checklist_value_previous

    app.run_server(debug=True)

if __name__=='__main__':
    json_file_path = "../examples/dinner.json"
    run_app(json_file_path)
