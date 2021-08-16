FROM node:13.12.0-alpine as build
WORKDIR /usr/src/app
COPY ./package.json ./
COPY package-lock.json ./
RUN npm ci --silent
RUN npm install react-scripts@4.0.3 -g --silent
COPY . ./

RUN npm run build

FROM nginx

COPY --from=build /usr/src/app/build /usr/share/nginx/html
COPY default.conf /etc/nginx/nginx.conf

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
