#!/usr/bin/env python
# coding: utf-8

# Copyright (c) zoubingwu.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget, CallbackDispatcher
from traitlets import Unicode, List, Dict, validate

from ._frontend import module_name, module_version


class TableWidget(DOMWidget):
    """A Grid Widget with filter, sort and selection capabilities.

    Attributes
    ----------
    columns : List of dict
        A list of dict with "accessor", "header", "editable" key, to control each row,
    data : List of dict
        Data to display
    meta : dict
        A dict containing any meta info, will be passed to on_cell_change callback when cell changed
    """

    _model_name = Unicode("TableModel").tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode("TableView").tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    # Your widget state goes here. Make sure to update the corresponding
    # JavaScript widget state (defaultModelProperties) in widget.ts
    columns = List(Dict()).tag(sync=True)
    data = List(Dict()).tag(sync=True)
    meta = Dict().tag(sync=True)

    def __init__(self, columns, data, meta, **kwargs):
        self.columns = columns
        self.data = data
        self.meta = meta
        super().__init__(**kwargs)
        self._cell_change_handlers = CallbackDispatcher()
        self._cell_change_handlers.callbacks
        self.on_msg(self.__handle_custom_msg)

    @validate("columns")
    def _validate_columns(self, proposal):
        value = proposal["value"]
        if not all(
            isinstance(item, dict)
            and all(key in item for key in ["accessor", "header"])
            for item in value
        ):
            raise ValueError("columns should have `accessor` and `header` key")
        return value

    @validate("data")
    def _validate_columns(self, proposal):
        value = proposal["value"]
        return value

    @validate("meta")
    def _validate_meta(self, proposal):
        value = proposal["value"]
        return value

    def __handle_custom_msg(self, widget, content, buffers):
        if content["type"] == "cell-changed":
            self._cell_change_handlers(content["payload"])

    def on_cell_change(self, callback, remove=False):
        """Register a callback to execute when a cell value changed.

        The callback will be called with one argument, the dictionary
        containing cell information with keys
        "row", "column", "column_index", "value".

        Parameters
        ----------
        remove: bool (optional)
            Set to true to remove the callback from the list of callbacks.
        """
        self._cell_change_handlers.register_callback(callback, remove=remove)

    def set_row_value(self, row):
        self._cell_change_handlers(row)
