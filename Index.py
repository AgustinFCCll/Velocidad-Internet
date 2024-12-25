import speedest as st



# Para ejecutar, escribir en la terminal ---> speedtest-cli

server = st.Speedtest()
server.get_best_server()

# Download Speed
down = server.download()
down = down / 1000000
print(f"Download Speed: {down} Mb/s")



# Upload Speed
up = server.upload()
up = up / 1000000
print(f"Upload Speed: {up} Mb/s")


# Ping Speed
ping = server.result.ping
print(f"Ping speed: {ping}")