import { Notification } from "@jupyterlab/apputils";
import { Logger } from '../logging/logger';
import { pino } from 'pino';
import { loadState, saveState } from "../utils/utils";
import { message } from "../messages";
import { UPDATE_NOTIFICATION_DO_NOT_SHOW_AGAIN } from "../utils/stateKeys";

export class NotificationManager {

    private static instance: NotificationManager;
    private _notifiedErrors: string[] = [];
    private logger: pino.Logger;


    private constructor() {
        this.logger = Logger.getInstance({
            "name": "codewhisperer",
            "component": "notifications"
        });
    }

    public static getInstance(): NotificationManager {
        if (!NotificationManager.instance) {
            NotificationManager.instance = new NotificationManager();
        }
        return NotificationManager.instance;
    }

    public async postNotificationForApiExceptions(notificationMessage: string, actionName: string, actionUrl: string): Promise<void> {

        if (!this._notifiedErrors.includes(notificationMessage)) {
            Notification.error("CodeWhisperer:\n" + notificationMessage, {
                autoClose: 10000,
                actions: [
                    {
                        label: actionName,
                        callback: () => {
                            window.open(actionUrl, '_blank');
                        },
                    },
                ]
            })
            this._notifiedErrors.push(notificationMessage);
        } else {
            this.logger.error(`Skipping previous error notification`, notificationMessage);
        }
    }

    public async postNotificationForUpdateInformation(notificationMessage: string,
        latestVersion: string,
        actionName: string,
        actionUrl: string): Promise<void> {
        const isDoNotShowAgainVersions : string[] = await loadState(UPDATE_NOTIFICATION_DO_NOT_SHOW_AGAIN);

        if(isDoNotShowAgainVersions !== undefined){
            if(isDoNotShowAgainVersions.includes(latestVersion)){
                return;
            }
        }
        const id = Notification.info(notificationMessage, {
            autoClose: 5000,
            actions: [
                {
                    label: actionName,
                    callback: () => {
                        window.open(actionUrl, '_blank');
                    },
                },
                {
                    label: message("codewhisperer_update_notification_skip_this_version"),
                    callback: () => {
                        Notification.dismiss(id);
                        saveState(UPDATE_NOTIFICATION_DO_NOT_SHOW_AGAIN, [...isDoNotShowAgainVersions , latestVersion]);
                        this.logger.debug(`Setting update notification do not show again`);
                    }
                }
            ]
        })
    }
}
