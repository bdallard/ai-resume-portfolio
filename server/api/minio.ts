import * as Minio from 'minio'
// from: https://min.io/docs/minio/linux/developers/javascript/API.html#presignedUrl 
const minioClient = new Minio.Client({
    endPoint: process.env.MINIO_URL || 'your-minio-endpoint-here',
    port: 443,
    useSSL: true,
    accessKey: process.env.MINIO_ACCESS_KEY || '',
    secretKey: process.env.MINIO_SECRET_KEY || '',
})

export const getMinioFileUrls = async (bucketName: string, prefix: string): Promise<string[]> => {
    const objectsStream = minioClient.listObjects(bucketName, prefix, true)
    const urls: string[] = []

    return new Promise((resolve, reject) => {
        objectsStream.on('data', async (obj: any) => {
            try {
                //console.log('Object found:', obj.name) // Log object key
                const url = await minioClient.presignedUrl('GET', bucketName, obj.name, 24 * 60 * 60)
                //console.log('Generated URL:', url) // Log generated URL
                urls.push(url)
            } catch (err) {
                //console.error('Error generating URL for object:', obj.name, err) // Log errors
                reject(err)
            }
        })
        objectsStream.on('end', () => {
            //console.log('Finished processing all objects')
            resolve(urls)
        })
        objectsStream.on('error', (err) => {
            //console.error('Error listing objects:', err)
            reject(err)
        })
    })
}
