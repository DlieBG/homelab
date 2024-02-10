# Setup
Run the following container to create the configuration file:
```
mkdir config
sudo docker run -it --rm --mount type=bind,source=./config/,destination=/root/.local/share/storj/gateway/ --name gateway storjlabs/gateway setup
```
