import speech_recognition as sr
import os
from datetime import datetime
import json
import logging

class RexzeaSpeechToText:
    def __init__(self):
        self.setup_directories() 
        self.setup_logging()
        self.recognizer = sr.Recognizer()
        self.load_config()
        
        self.recognizer.energy_threshold = 3000
        self.recognizer.dynamic_energy_threshold = True   
        self.recognizer.pause_threshold = 1.2
        
    def setup_directories(self): 
        base_dir = os.path.dirname(os.path.abspath(__file__))
        directories = [
            os.path.join(base_dir, 'save'),
            os.path.join(base_dir, 'save/audio'),
            os.path.join(base_dir, 'save/text')
        ]
        for directory in directories:
            os.makedirs(directory, exist_ok=True)

    def setup_logging(self):
        log_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'save',
            'speech_to_text.log'
        )
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def load_config(self):
        config_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'save',
            'config.json'
        )
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                'language': 'id-ID',
                'save_audio': True,
                'auto_punctuation': True
            }
            with open(config_path, 'w') as f:
                json.dump(self.config, f, indent=4)
    
    def record_and_convert(self):
        try:
            with sr.Microphone() as source:
                print("\nAdjusting environmental noise... Please wait...")
                self.recognizer.adjust_for_ambient_noise(source, duration=2)
                
                print("\nStarting talking... (Press Ctrl+C to stop)")
                print("Tips for best results:")
                print("- Speak clearly and not too fast")
                print("- Keep a distance of about 15-20 cm from the microphone.")
                print("- Avoid background noise")
                
                audio = self.recognizer.listen(
                    source,
                    timeout=None,
                    phrase_time_limit=None
                )
                
                print("\nConvert audio to text...")
                try:
                    text = self.recognizer.recognize_google(
                        audio, 
                        language=self.config.get('language', 'id-ID')
                    )
                except sr.UnknownValueError:
                    # fallback to Sphinx
                    try:
                        text = self.recognizer.recognize_sphinx(audio)
                    except:
                        text = "Unable to recognize speech"
                
                return self.enhance_text(text), audio
                
        except Exception as e:
            logging.error(f"Error in record_and_convert: {e}")
            return f"Error in recording: {str(e)}", None

    def enhance_text(self, text):
        if not text or text.isspace():
            return "No text detected"

        text = text.capitalize()
        if not text.endswith(('.', '!', '?')):
            text += '.'
        
        return text

    def save_to_file(self, text, audio=None):
        # save metadata
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            audio_path = None
            if audio and self.config.get('save_audio', True):
                audio_path = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    'save',
                    'audio',
                    f'recording_{timestamp}.wav'
                )
                with open(audio_path, "wb") as f:
                    f.write(audio.get_wav_data())
            
            text_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                'save',
                'text',
                f'output_{timestamp}.txt'
            )
            
            metadata = {
                'timestamp': timestamp,
                'language': self.config.get('language', 'id-ID'),
                'audio_file': audio_path,
                'word_count': len(text.split()),
                'character_count': len(text)
            }
            
            with open(text_path, "w", encoding="utf-8") as f:
                f.write("=== Metadata ===\n")
                f.write(json.dumps(metadata, indent=4))
                f.write("\n\n=== Hasil Konversi ===\n")
                f.write(text)
                
            return text_path
            
        except Exception as e:
            logging.error(f"Error in save_to_file: {e}")
            return None

def main():
    try:
        stt = RexzeaSpeechToText()
        
        while True:
            print("\n" + "="*50)
            print("Rexzea Speech-to-Text Converter")
            print("="*50)
            
            text, audio = stt.record_and_convert()
            
            print("\nConversion results:")
            print("-"*50)
            print(text)
            print("-"*50)
            
            # save result
            if text and "Error" not in text:
                output_path = stt.save_to_file(text, audio)
                if output_path:
                    print(f"\nThe results have been saved to: {output_path}")
                
                # data statistik
                print("\nStatistik:")
                print(f"- Word Count: {len(text.split())}")
                print(f"- Number of characters: {len(text)}")
            
            lanjut = input("\nWant to record again? (y/n): ").lower()
            if lanjut != 'y':
                break
                
    except KeyboardInterrupt:
        print("\nProgram stopped.")
    except Exception as e:
        print(f"\nThere is an error: {e}")
        logging.error(f"Error in main: {e}")

if __name__ == "__main__":
    main()
