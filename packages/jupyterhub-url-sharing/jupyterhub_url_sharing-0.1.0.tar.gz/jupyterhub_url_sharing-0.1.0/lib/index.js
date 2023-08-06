// libraries for copying to systems clipboard
import { Clipboard, ICommandPalette } from '@jupyterlab/apputils';
// libraries for getting and modifying a URL
import { PageConfig, URLExt } from '@jupyterlab/coreutils';
/**
 * Initialization data for JupyterHub URL sharing.
 */
const extension = {
    id: 'jupyterhub-url-sharing',
    autoStart: true,
    requires: [ICommandPalette],
    activate: (app, palette) => {
        const { commands } = app;
        const commandID = 'jupyterhub-url-sharing:copy-url'; // command id for plugin.json
        // add command with commandID
        commands.addCommand(commandID, {
            label: 'Copy shareable URL',
            execute: (args) => {
                let url;
                // get current URL with PageConfig and normalize
                url = new URL(URLExt.normalize(`${PageConfig.getUrl({
                    workspace: PageConfig.defaultWorkspace
                })}`));
                // copy URL to systems clipboard
                Clipboard.copyToSystem(url.toString());
            },
        });
    },
};
export default extension;
