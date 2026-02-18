# Stage 1: build
FROM node:18 as build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: nginx
FROM nginx:1.22.1
COPY --from=build /app/build /usr/share/nginx/html
