# --- Build Stage ---
FROM node:16.20.2-alpine AS build-stage
WORKDIR /client

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the client files
COPY . ./

# Build the client app
RUN npm run build

# --- Production Stage ---
FROM nginx:alpine
COPY --from=build-stage /client/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
