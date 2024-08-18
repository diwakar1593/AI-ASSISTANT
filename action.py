import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather


def Action(data):
    user_data = data.lower()
    
    if "what is your name" in  user_data :
        text_to_speech.text_to_speech("My name is Virtual Assistant")
        return 'My name is Virtual Assistant'

    elif "hello" in user_data or "hey" in user_data or "hay" in user_data:
        text_to_speech.text_to_speech("Hey, Sir How i can help you?")
        return 'Hey, Sir How i can help you?'
    
    elif "Good Morning" in user_data or "good morning" in user_data or "Morning" in user_data or "morning" in user_data:
        text_to_speech.text_to_speech("Good Morning Sir")
        return 'Good Morning Sir'
    
    elif "how are you" in user_data :
        text_to_speech.text_to_speech("I am doing great these days Sir")
        return 'I am doing great these days Sir'
    
    elif "Thank You" in user_data or "thank you" in user_data or "thanku" in user_data :
        text_to_speech.text_to_speech("Its my pleasure sir to stay with you")
        return 'Its my pleasure sir to stay with you'
    
    elif "time now" in user_data :
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + " Hour :", (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time
    
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return 'ok sir'
    
    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("gaana.com is now ready for you, enjoy your music")
        return 'gaana.com is now ready for you, enjoy your music'
    
    elif "youtube" in user_data or "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("You Tube open!")
        return 'You Tube open!'
    
    elif "open google" in user_data or "google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("Google Open!")
        return 'Google Open!'
        
    elif "weather" in user_data:
        ans = weather.Weather()
        text_to_speech.text_to_speech(ans)
        return ans
        
    else:
        text_to_speech.text_to_speech("I'm not able to understand.")
        return "I'm not able to understand."