# Stage 1: build
FROM node:18 as build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: copy to volume
FROM alpine:latest
RUN apk add --no-cache cpio
COPY --from=build /app/build /build
CMD cp -r /build/. /static/
