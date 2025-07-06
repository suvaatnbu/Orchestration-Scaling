FROM node:16

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json first (best practice for caching)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy rest of the application files
COPY . .

# Expose port (example: 5000)
EXPOSE 5000

# Start the application
CMD ["npm", "start"]
