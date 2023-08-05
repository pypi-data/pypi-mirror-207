import json
from dash import Dash, html, dcc, callback, Output, Input

def parse_json(file_path):
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)

    assert type(json_data['categories'])==dict
    assert type(json_data['tags'])==list
    category_list = list(json_data['categories'].keys())
    tag_list = json_data['tags']

    def category_json2list(json_category, current_index_lists, prefix):
        if type(json_category)==str:
            current_index_lists += [prefix+[json_category]]
        elif type(json_category)==list:
            for item in json_category:
                current_index_lists = category_json2list(item, current_index_lists, prefix)
        elif type(json_category)==dict:
            for key, values in json_category.items():
                current_index_lists = category_json2list(values, current_index_lists, prefix+[key])
        return current_index_lists

    category_dict = {}
    for category in list(json_data['categories'].keys()):
        category_dict[category] = category_json2list(json_data['categories'][category], [], [category,])

    return json_data, category_list, tag_list, category_dict

def get_radioitems_options(category_list, row_category_value, column_category_value):
    row_category_options = [{'label': category,
                             'value': category,
                             'disabled': True if category==column_category_value else False} for category in category_list]
    column_category_options = [{'label': category,
                                'value': category,
                                'disabled': True if category==row_category_value else False} for category in category_list]
    return row_category_options, column_category_options

def gen_html_table(json_data, category_dict, row_category, column_category, checklist_value):
    width_row_category = len(category_dict[row_category])
    width_column_category = len(category_dict[column_category])
    depth_row_category = max([len(cl) for cl in category_dict[row_category]])
    depth_column_category = max([len(cl) for cl in category_dict[column_category]])

    def find_index_from_category(category, category_list_list):
        for i, category_list in enumerate(category_list_list):
            if category == category_list[-1]:
                return i
        raise RuntimeError
    content_list = [['']*width_column_category for _ in range(width_row_category)]
    for content in json_data['contents']:
        assert 'name' in content.keys()
        assert 'categories' in content.keys()
        assert set(content['categories'].keys())==set((category_dict.keys()))
        if checklist_value==['all'] or len(set(content['tags']) & set(checklist_value)) > 0:
            row_index = find_index_from_category(content['categories'][row_category], category_dict[row_category])
            column_index = find_index_from_category(content['categories'][column_category], category_dict[column_category])
            if content_list[row_index][column_index]=='':
                content_list[row_index][column_index] = content['name']
            else:
                content_list[row_index][column_index] += '\n'+content['name']

    html_table = []
    for row in range(depth_column_category+width_row_category):
        html_tr = []
        for column in range(depth_row_category+width_column_category):
            if row<depth_column_category and column<depth_row_category:
                if row==0 and column==0:
                    html_tr.append(html.Td('', colSpan=depth_row_category, rowSpan=depth_column_category,
                                           style={"text-align": "center", "border":"1px solid", "white-space": "pre"}))
            elif row<depth_column_category and column>=depth_row_category:
                if len(category_dict[column_category][column-depth_row_category])<=row or \
                   (column-depth_row_category>0 and category_dict[column_category][column-depth_row_category][:(row+1)]==category_dict[column_category][column-depth_row_category-1][:(row+1)]):
                    pass
                else:
                    html_tr.append(html.Td(category_dict[column_category][column-depth_row_category][row],
                                           rowSpan=depth_column_category-len(category_dict[column_category][column-depth_row_category])+1 if len(category_dict[column_category][column-depth_row_category])==row+1 else 1,
                                           colSpan=sum([True if (len(category_dict[column_category][ci])>row)
                                                                and (category_dict[column_category][ci][:(row+1)] ==
                                                                     category_dict[column_category][column-depth_row_category][:(row+1)])
                                                        else False
                                                        for ci in range(column-depth_row_category, width_column_category)]),
                                           style={"text-align":"center", "border":"1px solid", "white-space": "pre"}))
            elif row>=depth_column_category and column<depth_row_category:
                if len(category_dict[row_category][row-depth_column_category])<=column or \
                   (row-depth_column_category>0 and category_dict[row_category][row-depth_column_category][:(column+1)]==category_dict[row_category][row-depth_column_category-1][:(column+1)]):
                    pass
                else:
                    html_tr.append(html.Td(category_dict[row_category][row-depth_column_category][column],
                                           colSpan=depth_row_category-len(category_dict[row_category][row-depth_column_category])+1 if len(category_dict[row_category][row-depth_column_category])==column+1 else 1,
                                           rowSpan=sum([True if (len(category_dict[row_category][ri])>column)
                                                                and (category_dict[row_category][ri][:(column+1)] ==
                                                                     category_dict[row_category][row-depth_column_category][:(column+1)])
                                                        else False
                                                        for ri in range(row-depth_column_category, width_row_category)]),
                                           style={"text-align":"center", "border":"1px solid", "white-space": "pre"}))
            elif row>=depth_column_category and column>=depth_row_category:
                html_tr.append(html.Td(content_list[row-depth_column_category][column-depth_row_category], style={"border": "1px solid", "white-space": "pre"}))
        html_table.append(html.Tr(html_tr))
    table = html.Table(html_table)
    return table

if __name__=="__main__":
    file_path = "../examples/dinner.json"
    json_data, category_list, tag_list, category_dict = parse_json(file_path)
    row_category, column_category = 'Course', 'Cook'
    show_tag_list = tag_list
    gen_html_table(json_data, category_dict, row_category, column_category, show_tag_list)
