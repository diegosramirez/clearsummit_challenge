import { Notification, } from '@challenge/models'

import { NotificationStoreState, StoreState, } from '../redux'

const getNotificationStore = (store: StoreState): NotificationStoreState => store.notification

const getNotifications = (store: StoreState): Notification | null | undefined => getNotificationStore(store).notifications

export default {
    getNotifications,
}
