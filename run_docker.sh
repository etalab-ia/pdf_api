echo killing old docker processes
docker-compose rm -fs

echo building docker containers
docker-compose up --build -d #--force-recreate -V

# docker-compose up -d --no-deps --build pdf_app

# Copy output files from container to local

#docker cp <containerId>:/file/path/in/container/file /host/local/path/file