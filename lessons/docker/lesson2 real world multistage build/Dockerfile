FROM node:10-alpine as nodebuild
WORKDIR /app
COPY . .

# Run unit tests and code coverage
RUN npm install && \
    npm run build && \
    npm run test && \
    npm run coverage

# Build in production mode
FROM node:10-alpine as noderun
WORKDIR /app
COPY --from=nodebuild /app/dist/src/ ./
COPY package*.json ./
RUN npm install --only=prod


#Create image to be deployed
FROM node:10-slim
WORKDIR /app
COPY --from=noderun /app/dist/src/ ./
COPY --from=noderun /app/node_modules/ ./node_modules
EXPOSE 8000
ENTRYPOINT node /app/index.js