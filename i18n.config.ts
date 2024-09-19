import en from './locales/en.json'
import fr from './locales/fr.json'
//TODO: add es + pt
export default defineI18nConfig(() => ({
    legacy: false,
    locale: 'en',
    messages: {
        en,
        fr,
    },
}))
