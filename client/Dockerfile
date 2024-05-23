FROM node:16.20.2-alpine AS build-stage
WORKDIR /client
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# --- Production Stage ---
FROM nginx:alpine
COPY --from=build-stage /client/build /usr/share/nginx/html
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]