FROM node:lts-alpine

# Install a simple http server to serve static content
RUN npm install -g http-server

# Set the 'front' folder as the working directory
WORKDIR /front

# Copy 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy project files and folders into the working directory (e.g., the 'app' folder)
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to start the HTTP server from the 'dist' directory
CMD [ "http-server", "dist" ]
