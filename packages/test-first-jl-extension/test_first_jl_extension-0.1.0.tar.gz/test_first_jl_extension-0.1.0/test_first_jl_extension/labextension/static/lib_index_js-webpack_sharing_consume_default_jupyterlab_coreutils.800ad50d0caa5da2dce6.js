"use strict";
(self["webpackChunktest_first_jl_extension"] = self["webpackChunktest_first_jl_extension"] || []).push([["lib_index_js-webpack_sharing_consume_default_jupyterlab_coreutils"],{

/***/ "./lib/JlButton.js":
/*!*************************!*\
  !*** ./lib/JlButton.js ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ButtonExtension": () => (/* binding */ ButtonExtension)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_1__);


class ButtonExtension {
    constructor(app) {
        this.app = app;
    }
    /**
     * Create a new extension for the notebook panel widget.
     *
     * @param panel Notebook panel
     * @param context Notebook context
     * @returns Disposable on the added button
     */
    createNew(panel) {
        const clearOutput = () => {
            console.log(this.app);
            console.log("Inside button click");
            this.app.commands.execute("lsp:test-first-jl-extension:show-hello-world-file_editor");
        };
        const button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ToolbarButton({
            label: "Show hello world",
            onClick: clearOutput,
            tooltip: "Show hello world",
        });
        panel.toolbar.insertItem(10, "clearOutputs", button);
        return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_1__.DisposableDelegate(() => {
            button.dispose();
        });
    }
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "COMMANDS": () => (/* binding */ COMMANDS),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyter_lsp_jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyter-lsp/jupyterlab-lsp */ "webpack/sharing/consume/default/@jupyter-lsp/jupyterlab-lsp");
/* harmony import */ var _jupyter_lsp_jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyter_lsp_jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyter_lsp_jupyterlab_lsp_lib_editor_integration_codemirror__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyter-lsp/jupyterlab-lsp/lib/editor_integration/codemirror */ "./node_modules/@jupyter-lsp/jupyterlab-lsp/lib/editor_integration/codemirror.js");
/* harmony import */ var _JlButton__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./JlButton */ "./lib/JlButton.js");



class AdopCM extends _jupyter_lsp_jupyterlab_lsp_lib_editor_integration_codemirror__WEBPACK_IMPORTED_MODULE_1__.CodeMirrorIntegration {
}
const COMMANDS = [
    {
        id: 'test-first-jl-extension:show-hello-world',
        label: 'Show hello world',
        execute: ({ connection, document }) => {
            if (connection === null || connection === void 0 ? void 0 : connection.isConnected) {
                // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                // @ts-ignore
                const wsConnection = connection.connection;
                void wsConnection.sendRequest('workspace/executeCommand', {
                    command: 'manthan.show_hello_world',
                    arguments: [document.document_info.uri]
                });
            }
        },
        is_enabled: () => true,
        rank: 4
    }
];
/**
 * Initialization data for the test-first-jl-extension extension.
 */
const plugin = {
    id: 'test-first-jl-extension:plugin',
    autoStart: true,
    optional: [_jupyter_lsp_jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__.ILSPFeatureManager],
    activate: (app, featureManager) => {
        featureManager.register({
            feature: {
                editorIntegrationFactory: new Map([['CodeMirrorEditor', AdopCM]]),
                id: 'jle:show_hello_world',
                name: 'hello world',
                commands: COMMANDS
            }
        });
        const button = new _JlButton__WEBPACK_IMPORTED_MODULE_2__.ButtonExtension(app);
        console.log('JupyterLab extension test-first-jl-extension is activated!');
        app.docRegistry.addWidgetExtension('Notebook', button);
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js-webpack_sharing_consume_default_jupyterlab_coreutils.800ad50d0caa5da2dce6.js.map