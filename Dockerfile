#TODO: see how to build images 
ARG NODE_VERSION=20
FROM node:${NODE_VERSION}-alpine as base

WORKDIR /src
# Build
FROM base as build
ARG NUXT_UI_PRO_LICENSE
COPY . .
RUN yarn install --frozen-lockfile

ENV NUXT_UI_PRO_LICENSE=${NUXT_UI_PRO_LICENSE}

RUN yarn build

ENV NODE_ENV=production

EXPOSE 3000

# https://nuxt.com/docs/getting-started/deployment#entry-point
ENTRYPOINT ["node", ".output/server/index.mjs"]