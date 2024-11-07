FROM node:alpine as builder

WORKDIR /app

COPY . .

ARG REACT_APP_BACK_HOST=127.0.0.1
ARG REACT_APP_BACK_PORT=8080
ARG REACT_APP_HTTP=http

RUN npm install

RUN npm run build

FROM nginx:alpine

COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]