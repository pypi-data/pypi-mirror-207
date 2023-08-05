# interactive-multi-category-table

In many different scenarios, contents are single-categorized and multi-tagged, by which I mean there are multiple tags but one single (though may be hierarchical) category system, e.g., file systems, blogs, etc. However, sometimes contents can be categorized from different category views. For storage or lookup, one category system is OK; but for visualization and analysis, flexibly organizing the contents with different category views will be very handy.

This repo targets addressing such demand by creating interactive tables with alternative category views, from formatted json input, based on dash.

# usage

Simply run
```python
import interactive_multi_category_table as imct

imct.run_app(json_file_path)
```
and the generated webpage can be accessed at http://127.0.0.1:8050/.

Refer to the provided examples for the json file format.

# requirements

- dash

# known limitations

- Leaf category items in the same category tree cannot be the same.
