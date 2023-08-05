import { ILSPFeatureManager } from '@jupyter-lsp/jupyterlab-lsp';
import { CodeMirrorIntegration } from '@jupyter-lsp/jupyterlab-lsp/lib/editor_integration/codemirror';
import { IFeatureCommand } from '@jupyter-lsp/jupyterlab-lsp/lib/feature';
import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { ButtonExtension } from './JlButton';

class AdopCM extends CodeMirrorIntegration {}
export const COMMANDS: IFeatureCommand[] = [
  {
    id: 'test-first-jl-extension:show-hello-world',
    label: 'Show hello world',
    execute: ({ connection, document }) => {
      if (connection?.isConnected) {
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
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'test-first-jl-extension:plugin',
  autoStart: true,
  optional: [ILSPFeatureManager],
  activate: (app: JupyterFrontEnd, featureManager: ILSPFeatureManager) => {
    featureManager.register({
      feature: {
        editorIntegrationFactory: new Map([['CodeMirrorEditor', AdopCM]]),
        id: 'jle:show_hello_world',
        name: 'hello world',
        commands: COMMANDS
      }
    });

    const button = new ButtonExtension(app);
    console.log('JupyterLab extension test-first-jl-extension is activated!');
    app.docRegistry.addWidgetExtension('Notebook', button);
  }
};

export default plugin;
