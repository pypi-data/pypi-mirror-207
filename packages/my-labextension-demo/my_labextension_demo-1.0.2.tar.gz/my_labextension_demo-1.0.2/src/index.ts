import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { ISettingRegistry } from '@jupyterlab/settingregistry';

/**
 * Initialization data for the my-labextension-demo extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'my-labextension-demo:plugin',
  autoStart: true,
  optional: [ISettingRegistry],
  activate: (app: JupyterFrontEnd, settingRegistry: ISettingRegistry | null) => {
    console.log('JupyterLab extension my-labextension-demo is activated!');

    if (settingRegistry) {
      settingRegistry
        .load(plugin.id)
        .then(settings => {
          console.log('my-labextension-demo settings loaded:', settings.composite);
        })
        .catch(reason => {
          console.error('Failed to load settings for my-labextension-demo.', reason);
        });
    }
  }
};

export default plugin;
