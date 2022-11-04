async def send_audio(message: types.Message):
    # os.execvp(sys.executable,[sys.executable,"/home/owner/py/run/padre/padre.py"])
    subj = f"""
    User INFO
    File Message id   {message.message_id}
    Sender id         {message.from_id}
    Sender user id    {message.from_user.id}
    Sender first name {message.from_user.first_name}
    Sender Username   {message.from_user.username}
    
    File INFO
    UPLOAD DATE            {message.date}
    AUDIO DURATION         {message.audio.duration}
    AUDIO FILE NAME        {message.audio.file_name}
    AUDIO MIME TYPE        {message.audio.mime_type}
    AUDIO TITLE            {message.audio.title}
    AUDIO FILE ID          {message.audio.file_id}
    AUDIO FILE UNIQUE ID   {message.audio.file_unique_id}
    AUDIO FILE SIZE        {message.audio.file_size}
    AUDIO FILE CAPTION     {message.caption}

def register_hendlers_admin(dp: dp):
  dp.register_message_handler(send_audio, content_types=['audio'])
