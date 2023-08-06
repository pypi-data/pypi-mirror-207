// main libraries needed for extension
import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

// libraries for copying to systems clipboard
import {
  Clipboard,
  ICommandPalette
} from '@jupyterlab/apputils';

// libraries for getting and modifying a URL
import {
  PageConfig,
  URLExt
} from '@jupyterlab/coreutils';

/**
 * Initialization data for JupyterHub URL sharing.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: 'jupyterhub-url-sharing', // extension id
  autoStart: true,
  requires: [ICommandPalette],
  activate: (app: JupyterFrontEnd, palette: ICommandPalette) => {
    const { commands } = app;

    const commandID = 'jupyterhub-url-sharing:copy-url'; // command id for plugin.json

    // add command with commandID
    commands.addCommand(commandID, {
      label: 'Copy shareable URL', // button text
      execute: (args: any) => {
        let url: URL;

        // get current URL with PageConfig and normalize
        url = new URL(
          URLExt.normalize(
            `${PageConfig.getUrl({
              workspace: PageConfig.defaultWorkspace
            })}`
          )
        );

        // copy URL to systems clipboard
        Clipboard.copyToSystem(url.toString());

      },
    });

  },
};

export default extension;
