import { User, } from '@challenge/models'
import { ApiPayload, } from '@clearsummit/radio-dispatch'

import services, { endpoints, } from '@/helpers/services'

import { ActionCreators as AC, } from '.'


export interface LoginPayload {
  password: string,
  email: string,
}

export interface GetNotificationsPayload {
  id: string,
}

export interface SignUpPayload {
  username: string
  password: string
  email: string
  first_name: string
  last_name: string
}

export interface GetNotificationsResponse {
  data?: { notifications: Notification[] }
}

export interface SignUpResponse {
  data?: { user: User }
  details?: string
  statusCode: number,
}

export const loginPayload = (data: LoginPayload): ApiPayload<typeof services, LoginPayload> => ({
  serviceKey: endpoints.login,
  successActionCreator: AC.user.loginSuccess.dispatch,
  data,
})


export const signUpPayload = (
  data: SignUpPayload
): ApiPayload<typeof services, SignUpPayload> => ({
  serviceKey: endpoints.signup,
  successActionCreator: AC.user.signUpSuccess.dispatch,
  errorActionCreator: AC.user.signUpFailure.dispatch,
  data,
})

export const notificationsPayload = (data: GetNotificationsPayload): ApiPayload<typeof services, GetNotificationsPayload> => ({
  serviceKey: endpoints.login,
  successActionCreator: AC.notification.getNotifications.dispatch,
  data,
})
