from gtts import gTTS
import os
from datetime import datetime
import platform
from pathlib import Path
import time

class RexzeaTextToSpeechConverter:
    
    def __init__(self):
        self.output_dir = Path("saved_audio")
        self.setup_output_directory()
        
    def setup_output_directory(self):
        self.output_dir.mkdir(exist_ok=True)
        
    def clear_screen(self):
        os.system('cls' if platform.system().lower() == "windows" else 'clear')
        
    def get_timestamp(self):
        return datetime.now().strftime("%Y%m%d_%H%M%S") 
        
    def play_audio(self, filename):
        try:
            if platform.system().lower() == "windows":
                os.system(f'start {filename}')
            elif platform.system().lower() == "darwin":  # For macOS
                os.system(f'afplay {filename}')
            else:  # For Linux
                os.system(f'xdg-open {filename}')
            return True
        except Exception as e:
            print(f"\nError playing audio: {str(e)}")
            return False
            
    def display_header(self):
        self.clear_screen()
        print("╔════════════════════════════════════╗")
        print("║      Text-to-Speech Converter      ║")
        print("╚════════════════════════════════════╝")
        
    def get_user_input(self):
        print("\n📝 Enter your text:")
        text = input("➜ ")
        
        print("\n🔊 Select speech speed:")
        print("1. Normal")
        print("2. Slow")
        while True:
            speed_choice = input("➜ Enter your choice (1/2): ")
            if speed_choice in ['1', '2']:
                break
            print("❌ Invalid choice. Please enter 1 or 2.")
            
        return text, speed_choice == '2'
        
    def convert_and_save(self, text, slow):
        try:
            # create filename with timestamp
            filename = self.output_dir / f"speech_{self.get_timestamp()}.mp3"
            
            # show progress indicator
            print("\n⏳ Converting text to speech...")
            
            # create and save audio file
            tts = gTTS(text=text, lang='id', slow=slow)
            tts.save(filename)
            
            print(f"✅ Audio saved as: {filename}")
            return filename
            
        except Exception as e:
            print(f"\n❌ Error during conversion: {str(e)}")
            return None
            
    def run(self):
        while True:
            self.display_header()
            
            # get user input
            text, is_slow = self.get_user_input()
            
            # convert and save
            filename = self.convert_and_save(text, is_slow)
            
            if filename:
                # play the audio
                print("\n▶️ Playing audio...")
                self.play_audio(str(filename))
                time.sleep(1)  #give some time for the audio player to start
            
            # ask to continue
            print("\n🔄 Would you like to convert another text?")
            again = input("➜ Enter 'y' for yes, any other key to exit: ")
            if again.lower() != 'y':
                print("\n👋 Thank you for using Text-to-Speech Converter!")
                break

if __name__ == "__main__":
    converter = RexzeaTextToSpeechConverter()
    converter.run()
