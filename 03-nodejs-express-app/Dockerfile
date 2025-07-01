# Use an official Node.js runtime as a parent image
# Using Alpine version for a smaller image size
FROM node:18-alpine

# Optional: Add a maintainer label
LABEL maintainer="Lukas Pavelka <your-email@example.com>" # Please replace with your actual email if desired

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json (if available)
# This is done first to leverage Docker's build cache.
# If these files don't change, subsequent npm install won't rerun unless necessary.
COPY package*.json ./

# Install app dependencies
# Using `npm ci` is generally recommended for production builds if you have a package-lock.json,
# as it provides faster and more reliable installs.
# `npm install` can be used if package-lock.json is not present or for development.
# `--only=production` ensures only production dependencies are installed (if devDependencies are listed in package.json)
RUN npm ci --only=production

# Bundle app source by copying all files from the current directory to the working directory in the container
COPY . .

# The 'node' user is created in the official Node.js images.
# Running as a non-root user is a security best practice.
USER node

# Your app binds to port 3000 (or the port specified by the PORT env var in server.js)
EXPOSE 3000

# Define the command to run your app using CMD which defines the runtime command.
# This will execute `npm start` which in turn runs `node server.js` as defined in package.json.
CMD [ "npm", "start" ]
