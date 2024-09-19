import path from 'path'
import { promises as fs } from 'fs'

export default eventHandler(async (event) => {
    const query = getQuery(event)
    const { prefix } = query

    if (!prefix) {
        return { error: 'Prefix is required' }
    }

    const dirPath = path.join(process.cwd(), 'public', prefix)

    try {
        const files = await fs.readdir(dirPath)
        const images = files.filter(file => /\.(png|jpe?g|svg)$/.test(file))
        const imageUrls = images.map(file => `/${prefix}/${file}`)
        return { urls: imageUrls }
    } catch (error) {
        return { error: 'Failed to list images' }
    }
})