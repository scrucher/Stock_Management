FROM node:alpine

# Set the working directory in the container
WORKDIR /client

# Copy package.json and package-lock.json separately to leverage Docker caching
COPY package.json ./

# Install dependencies
RUN npm install

# Copy the rest of your app's source code
COPY . .

# Expose port 3000
EXPOSE 3000