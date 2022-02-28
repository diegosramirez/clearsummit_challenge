import { dispatchReducer, runReducers, } from '@clearsummit/radio-dispatch'

import { GetNotificationsResponse, } from './api-payloads'
import { NotificationStoreState, } from './index'

// Notification Actions
export const ACTIONS = {
    GET_NOTIFICATIONS: 'GET_NOTIFICATIONS',
}

export const INITIAL_STATE: NotificationStoreState = {
    notifications: [],
}

const getNotificationsSuccess = (state: NotificationStoreState, payload: GetNotificationsResponse) => ({
    ...state,
    notifications: payload.data.notifications,
})

export const reduxSet = {
    // @ts-ignore
    getNotifications: dispatchReducer<NotificationStoreState, GetNotificationsResponse>(
        ACTIONS.GET_NOTIFICATIONS,
        getNotificationsSuccess
    ),
}

export const reducer = (
    state: NotificationStoreState = { ...INITIAL_STATE, },
    action: StandardAction
): NotificationStoreState => runReducers(state, action, reduxSet)
