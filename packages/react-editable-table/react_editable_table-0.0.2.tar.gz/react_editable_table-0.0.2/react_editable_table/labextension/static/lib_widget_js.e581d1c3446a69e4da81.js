"use strict";
(self["webpackChunkreact_editable_table"] = self["webpackChunkreact_editable_table"] || []).push([["lib_widget_js"],{

/***/ "./lib/react/ReactEditableTable.js":
/*!*****************************************!*\
  !*** ./lib/react/ReactEditableTable.js ***!
  \*****************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
const react_1 = __importStar(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const core_1 = __webpack_require__(/*! @mantine/core */ "./node_modules/@mantine/core/esm/index.js");
const ahooks_1 = __webpack_require__(/*! ahooks */ "./node_modules/ahooks/es/index.js");
const model_1 = __webpack_require__(/*! ./model */ "./lib/react/model.js");
const useStyles = (0, core_1.createStyles)({
    table: {
        borderRadius: 8,
        borderCollapse: 'initial',
        overflow: 'hidden',
        '& thead tr th': {
            height: 50,
            textAlign: 'left',
            padding: '0.4375rem 0.625rem',
        },
        '& thead tr th:nth-of-type(1)': {
            width: 140,
        },
        '& thead tr th:nth-of-type(2)': {
            width: 140,
        },
    },
});
function ReactEditableTable(props) {
    const [columns] = (0, model_1.useModelState)('columns');
    const [meta] = (0, model_1.useModelState)('meta');
    const [data, setData] = (0, model_1.useModelState)('data');
    const send = (0, model_1.useModelMessenger)();
    const { classes } = useStyles();
    const { loading } = props;
    const rows = data.map((item, index) => {
        return (react_1.default.createElement("tr", { key: index }, columns.map((c) => (react_1.default.createElement("td", { key: c.header }, c.editable ? (react_1.default.createElement(core_1.Input, { type: "text", defaultValue: item[c.accessor], onBlur: (e) => {
                const next = e.target.value;
                if (item[c.accessor] !== next) {
                    const data = Object.assign(Object.assign({}, item), { [c.accessor]: e.target.value });
                    setData((prev) => {
                        prev[index] = data;
                    });
                    send({
                        type: 'cell-changed',
                        payload: {
                            row: data,
                            index,
                            meta,
                        },
                    });
                }
            } })) : (item[c.accessor]))))));
    });
    return (react_1.default.createElement("div", null,
        react_1.default.createElement(core_1.ScrollArea, { mah: 400 },
            react_1.default.createElement(core_1.Box, { maw: 600 },
                react_1.default.createElement(core_1.Table, { cellSpacing: 0, className: classes.table },
                    react_1.default.createElement("thead", null,
                        react_1.default.createElement("tr", null, columns.map((i) => (react_1.default.createElement("th", { key: i.header }, i.header))))),
                    react_1.default.createElement("tbody", null, rows)))),
        loading && (react_1.default.createElement(core_1.Loader, { size: "xs", sx: { position: 'absolute', top: 5, right: 0 } }))));
}
function withModelContext(Component) {
    return (props) => {
        const [dark, setDark] = (0, react_1.useState)(() => document.body.dataset.jpThemeLight === 'false');
        (0, ahooks_1.useMutationObserver)((mutationsList) => {
            mutationsList.forEach((i) => {
                if (i.attributeName === 'data-jp-theme-light') {
                    setDark(document.body.dataset.jpThemeLight === 'false');
                }
            });
        }, document.body, {
            attributes: true,
            subtree: false,
        });
        return (react_1.default.createElement(model_1.WidgetModelContext.Provider, { value: props.model },
            react_1.default.createElement(core_1.MantineProvider, { theme: { colorScheme: dark ? 'dark' : 'light' }, withGlobalStyles: true, withNormalizeCSS: true },
                react_1.default.createElement(Component, Object.assign({}, props)))));
    };
}
exports["default"] = withModelContext(ReactEditableTable);


/***/ }),

/***/ "./lib/react/model.js":
/*!****************************!*\
  !*** ./lib/react/model.js ***!
  \****************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.useModelMessenger = exports.useModel = exports.useModelEvent = exports.useModelState = exports.WidgetModelContext = void 0;
const react_1 = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
const immer_1 = __webpack_require__(/*! immer */ "./node_modules/immer/dist/cjs/index.js");
exports.WidgetModelContext = (0, react_1.createContext)(undefined);
// HOOKS
//============================================================================================
/**
 *
 * @param name property name in the Python model object.
 * @returns model state and set state function.
 */
function useModelState(name) {
    const model = useModel();
    const [state, setState] = (0, react_1.useState)(model === null || model === void 0 ? void 0 : model.get(name));
    function setter(updater, options) {
        const next = (0, immer_1.produce)(state, updater);
        model === null || model === void 0 ? void 0 : model.set(name, next, options);
        model === null || model === void 0 ? void 0 : model.save_changes();
    }
    useModelEvent(`change:${name}`, (model) => {
        setState(model.get(name));
    }, [name]);
    return [state, setter];
}
exports.useModelState = useModelState;
/**
 * Subscribes a listener to the model event loop.
 * @param event String identifier of the event that will trigger the callback.
 * @param callback Action to perform when event happens.
 * @param deps Dependencies that should be kept up to date within the callback.
 */
function useModelEvent(event, callback, deps) {
    const model = useModel();
    const dependencies = deps === undefined ? [model] : [...deps, model];
    (0, react_1.useEffect)(() => {
        const callbackWrapper = (e) => {
            model && callback(model, e);
        };
        model === null || model === void 0 ? void 0 : model.on(event, callbackWrapper);
        return () => {
            model === null || model === void 0 ? void 0 : model.unbind(event, callbackWrapper);
        };
    }, dependencies);
}
exports.useModelEvent = useModelEvent;
/**
 * An escape hatch in case you want full access to the model.
 * @returns Python model
 */
function useModel() {
    return (0, react_1.useContext)(exports.WidgetModelContext);
}
exports.useModel = useModel;
function useModelMessenger() {
    const model = useModel();
    function send(message) {
        model === null || model === void 0 ? void 0 : model.send(message);
    }
    return send;
}
exports.useModelMessenger = useModelMessenger;


/***/ }),

/***/ "./lib/version.js":
/*!************************!*\
  !*** ./lib/version.js ***!
  \************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


// Copyright (c) zoubingwu
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MODULE_NAME = exports.MODULE_VERSION = void 0;
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
// eslint-disable-next-line @typescript-eslint/no-var-requires
const data = __webpack_require__(/*! ../package.json */ "./package.json");
/**
 * The _model_module_version/_view_module_version this package implements.
 *
 * The html widget manager assumes that this is the same as the npm package
 * version number.
 */
exports.MODULE_VERSION = data.version;
/*
 * The current package name.
 */
exports.MODULE_NAME = data.name;


/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.TableView = exports.TableModel = void 0;
// Copyright (c) zoubingwu
// Distributed under the terms of the Modified BSD License.
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const ReactEditableTable_1 = __importDefault(__webpack_require__(/*! ./react/ReactEditableTable */ "./lib/react/ReactEditableTable.js"));
const react_1 = __importDefault(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const react_dom_1 = __importDefault(__webpack_require__(/*! react-dom */ "webpack/sharing/consume/default/react-dom"));
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
// Your widget state goes here. Make sure to update the corresponding
// Python state in example.py
const defaultModelProperties = {
    columns: [],
    data: [],
};
class TableModel extends base_1.DOMWidgetModel {
    defaults() {
        return Object.assign(Object.assign(Object.assign({}, super.defaults()), { _model_name: TableModel.model_name, _model_module: TableModel.model_module, _model_module_version: TableModel.model_module_version, _view_name: TableModel.view_name, _view_module: TableModel.view_module, _view_module_version: TableModel.view_module_version }), defaultModelProperties);
    }
    initialize(attributes, options) {
        super.initialize(attributes, options);
        this.on('msg:custom', (message) => {
            this.send(message);
        });
    }
}
TableModel.serializers = Object.assign({}, base_1.DOMWidgetModel.serializers);
TableModel.model_name = 'TableModel';
TableModel.model_module = version_1.MODULE_NAME;
TableModel.model_module_version = version_1.MODULE_VERSION;
TableModel.view_name = 'TableView'; // Set to null if no view
TableModel.view_module = version_1.MODULE_NAME; // Set to null if no view
TableModel.view_module_version = version_1.MODULE_VERSION;
exports.TableModel = TableModel;
class TableView extends base_1.DOMWidgetView {
    render() {
        const component = react_1.default.createElement(ReactEditableTable_1.default, {
            model: this.model,
        });
        react_dom_1.default.render(component, this.el);
    }
}
exports.TableView = TableView;


/***/ }),

/***/ "./package.json":
/*!**********************!*\
  !*** ./package.json ***!
  \**********************/
/***/ ((module) => {

module.exports = JSON.parse('{"name":"react-editable-table","version":"0.1.0","description":"A Custom Jupyter Widget Library","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/tidbcloud/react-editable-table","bugs":{"url":"https://github.com/tidbcloud/react-editable-table/issues"},"license":"BSD-3-Clause","author":{"name":"zoubingwu","email":"zoubingwu@gmail.com"},"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/tidbcloud/react-editable-table"},"scripts":{"build":"npm run build:lib && npm run build:nbextension && npm run build:labextension:dev","build:prod":"npm run build:lib && npm run build:nbextension && npm run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack","clean":"npm run clean:lib && npm run clean:nbextension && npm run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf react_editable_table/labextension","clean:nbextension":"rimraf react_editable_table/nbextension/static/index.js","prepack":"npm run build:lib","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch --mode=development","watch:labextension":"jupyter labextension watch ."},"dependencies":{"@jupyter-widgets/base":"^6.0.4","react":"^17.0.2","react-dom":"^17.0.2"},"devDependencies":{"@babel/core":"^7.21.4","@babel/preset-env":"^7.21.4","@babel/preset-react":"^7.18.6","@babel/preset-typescript":"^7.21.4","@emotion/react":"^11.11.0","@jupyterlab/builder":"^3.6.3","@lumino/application":"^2.1.0","@lumino/widgets":"^2.1.0","@mantine/core":"^6.0.10","@mantine/hooks":"^6.0.10","@types/react":"^17.0.2","@types/react-dom":"^17.0.2","@types/webpack":"^5.28.1","@types/webpack-env":"^1.18.0","ahooks":"^3.7.7","babel-loader":"^9.1.2","css-loader":"^6.7.3","fs-extra":"^11.1.1","immer":"^10.0.1","mkdirp":"^3.0.1","npm-run-all":"^4.1.5","prettier":"^2.8.8","rimraf":"^5.0.0","source-map-loader":"^4.0.1","style-loader":"^3.3.2","ts-loader":"^9.4.2","typescript":"~5.0.4","webpack":"^5.80.0","webpack-cli":"^5.0.2"},"babel":{"presets":["@babel/preset-env","@babel/preset-react","@babel/preset-typescript"]},"jupyterlab":{"extension":"lib/plugin","outputDir":"react_editable_table/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}');

/***/ })

}]);
//# sourceMappingURL=lib_widget_js.e581d1c3446a69e4da81.js.map