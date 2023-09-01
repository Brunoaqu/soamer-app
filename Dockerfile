FROM node:18.17.1

WORKDIR /usr/src/app

RUN npm install -g pnpm

COPY package.json ./
COPY pnpm-lock.yaml ./
COPY src ./

RUN pnpm ci

CMD ["pnpm", "run", "start"]
