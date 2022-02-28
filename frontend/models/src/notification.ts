import BaseModel from './base-model'
import { defaultBoolean, defaultObject, defaultString } from './defaults'

export type NotificationDataType = {
    id: string | null | undefined,
    createdAt: string | null | undefined,
    seen: boolean,
    type: string | null | undefined,
}

export default class Notification extends BaseModel {
    id: string

    createdAt: string

    seen: boolean

    type: string

    constructor(
        data: NotificationDataType = {
            id: null,
            createdAt: null,
            seen: false,
            type: null,
        },
    ) {
        super()
        this.id = defaultString(data.id)
        this.createdAt = defaultString(data.createdAt)
        this.seen = defaultBoolean(data.seen)
        this.type = defaultObject(data.type)
    }

    get valid(): boolean {
        return !!this.id
    }
}
