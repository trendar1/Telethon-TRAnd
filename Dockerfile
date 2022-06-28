FROM trendar1/Telethon-TRAnd:slim-buster

#clonning repo 
RUN git clone https://github.com/trendar1/Telethon-TRAnd.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
# Trand
