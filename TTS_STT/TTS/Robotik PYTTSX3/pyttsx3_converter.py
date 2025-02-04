import pyttsx3
import os
from datetime import datetime
import platform
from pathlib import Path
import time # next updt

class RexzeaTTS:
    
    def __init__(self):
        self.output_dir = Path("saved_audio")
        self.setup_output_directory()
        self.engine = pyttsx3.init()
        self.voices = self.setup_engine()
        
    def setup_output_directory(self):
        self.output_dir.mkdir(exist_ok=True)
        
    def setup_engine(self):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('rate', 150)
        return voices
        
    def list_available_voices(self):
        voice_list = []
        for idx, voice in enumerate(self.voices, 1):
            voice_info = f"{idx}. {voice.name}"
            if hasattr(voice, 'gender'):
                voice_info += f" ({voice.gender})"
            if hasattr(voice, 'languages'):
                try:
                    voice_info += f" - {voice.languages[0]}"
                except:
                    pass
            voice_list.append(voice_info)
        return voice_list
        
    def clear_screen(self):
        os.system('cls' if platform.system().lower() == "windows" else 'clear')
        
    def get_timestamp(self):
        return datetime.now().strftime("%Y%m%d_%H%M%S")
        
    def display_header(self):
        self.clear_screen()
        print("╔════════════════════════════════════╗")
        print("║      Text-to-Speech Converter      ║")
        print("║     (with Multiple Voice Types)    ║")
        print("╚════════════════════════════════════╝")
        
    def get_user_input(self):
        print("\n📝 Enter your text:")
        text = input("➜ ")
        
        print("\n🎭 Available Voices:")
        voice_list = self.list_available_voices()
        for voice_info in voice_list:
            print(voice_info)
            
        while True:
            try:
                voice_choice = int(input(f"\n➜ Select voice (1-{len(self.voices)}): "))
                if 1 <= voice_choice <= len(self.voices):
                    break
                print("❌ Invalid choice. Please select from available voices.")
            except ValueError:
                print("❌ Please enter a valid number")
        
        print("\n🔊 Select speech rate:")
        print("1. Very Slow (80 wpm)")
        print("2. Slow (100 wpm)")
        print("3. Normal (150 wpm)")
        print("4. Fast (200 wpm)")
        print("5. Very Fast (250 wpm)")
        
        while True:
            rate_choice = input("➜ Enter your choice (1-5): ")
            if rate_choice in ['1', '2', '3', '4', '5']:
                break
            print("❌ Invalid choice. Please enter 1-5.")
            
        rates = {'1': 80, '2': 100, '3': 150, '4': 200, '5': 250}
        selected_rate = rates[rate_choice]
        
        print("\n🔈 Select volume (0.1 - 1.0):")
        while True:
            try:
                volume = float(input("➜ Enter volume (default 1.0): ") or 1.0)
                if 0.1 <= volume <= 1.0:
                    break
                print("❌ Volume must be between 0.1 and 1.0")
            except ValueError:
                print("❌ Please enter a valid number")
                
        return text, voice_choice - 1, selected_rate, volume
        
    def convert_and_save(self, text, voice_idx, rate, volume):
        try:
            voice_name = self.voices[voice_idx].name.split()[-1]  # get last part of voice name
            filename = self.output_dir / f"speech_{voice_name}_{self.get_timestamp()}.mp3"
            
            self.engine.setProperty('voice', self.voices[voice_idx].id)
            self.engine.setProperty('rate', rate)
            self.engine.setProperty('volume', volume)
            
            print("\n⏳ Converting text to speech...")
            
            self.engine.save_to_file(text, str(filename))
            self.engine.runAndWait()
            
            print(f"✅ Audio saved as: {filename}")
            return filename
            
        except Exception as e:
            print(f"\n❌ Error during conversion: {str(e)}")
            return None
            
    def play_text(self, text, voice_idx, rate, volume):
        try:
            self.engine.setProperty('voice', self.voices[voice_idx].id)
            self.engine.setProperty('rate', rate)
            self.engine.setProperty('volume', volume)
            self.engine.say(text)
            self.engine.runAndWait()
            return True
        except Exception as e:
            print(f"\n❌ Error playing audio: {str(e)}")
            return False
            
    def run(self):
        while True:
            self.display_header()
            
            text, voice_idx, rate, volume = self.get_user_input()
            
            print("\n💾 Would you like to save the audio file?")
            save_choice = input("➜ Enter 'y' for yes, any other key to just play: ")
            
            if save_choice.lower() == 'y':
                filename = self.convert_and_save(text, voice_idx, rate, volume)
                if filename:
                    print("\n▶️ Playing saved audio...")
                    self.play_text(text, voice_idx, rate, volume)
            else:
                print("\n▶️ Playing audio...")
                self.play_text(text, voice_idx, rate, volume)
            
            print("\n🔄 Would you like to convert another text?")
            again = input("➜ Enter 'y' for yes, any other key to exit: ")
            if again.lower() != 'y':
                print("\n👋 Thank you for using Text-to-Speech Converter!")
                break

if __name__ == "__main__":
    converter = RexzeaTTS()
    converter.run()