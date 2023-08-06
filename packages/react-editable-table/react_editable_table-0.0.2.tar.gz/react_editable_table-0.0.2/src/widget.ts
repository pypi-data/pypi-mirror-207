// Copyright (c) zoubingwu
// Distributed under the terms of the Modified BSD License.
import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
} from '@jupyter-widgets/base';
import ReactEditableTable from './react/ReactEditableTable';
import React from 'react';
import ReactDOM from 'react-dom';

import { MODULE_NAME, MODULE_VERSION } from './version';

interface Column {
  header: string;
  accessor: string;
  editable?: boolean;
}

export interface WidgetModelState {
  columns: Column[];
  data: any[];
  loading?: boolean;
  meta?: Record<string, any>;
}

// Your widget state goes here. Make sure to update the corresponding
// Python state in example.py
const defaultModelProperties: WidgetModelState = {
  columns: [],
  data: [],
};

export class TableModel extends DOMWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      _model_name: TableModel.model_name,
      _model_module: TableModel.model_module,
      _model_module_version: TableModel.model_module_version,
      _view_name: TableModel.view_name,
      _view_module: TableModel.view_module,
      _view_module_version: TableModel.view_module_version,
      ...defaultModelProperties,
    };
  }

  static serializers: ISerializers = {
    ...DOMWidgetModel.serializers,
    // Add any extra serializers here
  };

  static model_name = 'TableModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'TableView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;

  initialize(attributes: any, options: any) {
    super.initialize(attributes, options);

    this.on('msg:custom', (message) => {
      this.send(message);
    });
  }
}

export class TableView extends DOMWidgetView {
  render() {
    const component = React.createElement(ReactEditableTable, {
      model: this.model,
    });
    ReactDOM.render(component, this.el);
  }
}
