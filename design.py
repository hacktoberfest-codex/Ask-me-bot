css = '''
<style>

.css-fg4pbf{
    background:black;
    color:white;
}

.chat-message {
    padding: 1.2rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 15%;
}
.chat-message .avatar img {
  max-width: 48px;
  max-height: 48px;
  border-radius: 25%;
  object-fit: cover;
}
.chat-message .message {
  width: 40%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://scalebranding.com/wp-content/uploads/2022/02/Cute-Robot-Diver-Logo-1024x1024.png" style="max-height: 48px; max-width: 48px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://www.pngmart.com/files/21/Account-PNG-HD.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''