import { JupyterFrontEnd } from "@jupyterlab/application";
import { ToolbarButton } from "@jupyterlab/apputils";
import { DocumentRegistry } from "@jupyterlab/docregistry";
import { INotebookModel, NotebookPanel } from "@jupyterlab/notebook";
import { DisposableDelegate, IDisposable } from "@lumino/disposable";

export class ButtonExtension
  implements DocumentRegistry.IWidgetExtension<NotebookPanel, INotebookModel>
{
  app: JupyterFrontEnd;
  constructor(app: JupyterFrontEnd) {
    this.app = app;
  }
  /**
   * Create a new extension for the notebook panel widget.
   *
   * @param panel Notebook panel
   * @param context Notebook context
   * @returns Disposable on the added button
   */
  createNew(panel: NotebookPanel): IDisposable {
    const clearOutput = () => {
      console.log(this.app);
      console.log("Inside button click");

      this.app.commands.execute(
        "lsp:test-first-jl-extension:show-hello-world-file_editor"
      );
    };
    const button = new ToolbarButton({
      label: "Show hello world",
      onClick: clearOutput,
      tooltip: "Show hello world",
    });

    panel.toolbar.insertItem(10, "clearOutputs", button);

    return new DisposableDelegate(() => {
      button.dispose();
    });
  }
}
