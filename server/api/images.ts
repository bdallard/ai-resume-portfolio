import { defineEventHandler, sendError, getQuery } from 'h3'
import { getMinioFileUrls } from './minio'

export default defineEventHandler(async (event) => {
    try {
        const query = getQuery(event)
        const prefix = typeof query.prefix === 'string' ? query.prefix : ''
        const bucketName = process.env.BUCKET_NAME || ''
        if (!prefix) {
            throw new Error('Prefix is required')
        }
        //console.log('Fetching image URLs from Minio')
        const urls = await getMinioFileUrls(bucketName, prefix)
        //console.log('Fetched URLs:', urls)
        return { urls }
    } catch (error) {
        //console.error('Failed to fetch image URLs:', error)
        return sendError(event, new Error('Failed to fetch image URLs'))
    }
})