from IPython.display import Javascript, display
from ipywidgets import widgets

def start():
    def run_all(ev):
        display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1, IPython.notebook.ncells())'))

    button = widgets.Button(description="Click Here To Start!")
    button.on_click(run_all)
    display(button)
