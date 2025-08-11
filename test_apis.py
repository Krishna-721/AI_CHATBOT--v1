# test_apis.py - Test script for AI API functionality
import os
import sys


def test_environment():
    """Test if environment variables are set correctly"""
    print("=== Testing Environment Variables ===")

    openai_keys = os.getenv("OPENAI_API_KEY", "")
    gemini_key = os.getenv("GEMINI_KEY", "")

    if openai_keys:
        keys_list = [key.strip() for key in openai_keys.split(",") if key.strip()]
        print(f"✓ OpenAI keys found: {len(keys_list)} key(s)")
        for i, key in enumerate(keys_list):
            print(f"  Key {i + 1}: {key[:10]}...{key[-4:]}")
    else:
        print("✗ No OpenAI API keys found")

    if gemini_key:
        print(f"✓ Gemini key found: {gemini_key[:10]}...{gemini_key[-4:]}")
    else:
        print("✗ No Gemini API key found")

    print()


def test_imports():
    """Test if all required packages are installed"""
    print("=== Testing Package Imports ===")

    try:
        import openai
        print("✓ OpenAI package imported successfully")
    except ImportError as e:
        print(f"✗ OpenAI import failed: {e}")
        return False

    try:
        import google.generativeai as genai
        print("✓ Google Generative AI package imported successfully")
    except ImportError as e:
        print(f"✗ Google Generative AI import failed: {e}")
        return False

    try:
        import speech_recognition as sr
        print("✓ Speech Recognition package imported successfully")
    except ImportError as e:
        print(f"✗ Speech Recognition import failed: {e}")
        return False

    try:
        import pyttsx3
        print("✓ pyttsx3 package imported successfully")
    except ImportError as e:
        print(f"✗ pyttsx3 import failed: {e}")
        return False

    print()
    return True


def test_ai_handler():
    """Test the ai_handler module"""
    print("=== Testing AI Handler Module ===")

    try:
        from ai_handler import get_openai_response, get_gemini_response, get_ai_response
        print("✓ AI handler functions imported successfully")
    except ImportError as e:
        print(f"✗ AI handler import failed: {e}")
        print("Make sure ai_handler.py is in the same directory")
        return False

    print()
    return True


def test_openai_api():
    """Test OpenAI API connectivity"""
    print("=== Testing OpenAI API ===")

    try:
        from ai_handler import get_openai_response

        test_prompt = "Say 'Hello from OpenAI' in exactly those words."
        print(f"Sending test prompt: '{test_prompt}'")

        response = get_openai_response(test_prompt)
        print(f"✓ OpenAI Response: {response}")
        return True

    except Exception as e:
        print(f"✗ OpenAI API failed: {e}")
        return False


def test_gemini_api():
    """Test Gemini API connectivity"""
    print("=== Testing Gemini API ===")

    try:
        from ai_handler import get_gemini_response

        test_prompt = "Say 'Hello from Gemini' in exactly those words."
        print(f"Sending test prompt: '{test_prompt}'")

        response = get_gemini_response(test_prompt)
        print(f"✓ Gemini Response: {response}")
        return True

    except Exception as e:
        print(f"✗ Gemini API failed: {e}")
        return False


def test_fallback_logic():
    """Test the fallback logic"""
    print("=== Testing Fallback Logic ===")

    try:
        from ai_handler import get_ai_response

        test_prompt = "What is 2+2?"
        print(f"Testing fallback with prompt: '{test_prompt}'")

        response = get_ai_response(test_prompt)
        print(f"✓ Fallback Response: {response}")

        if "unavailable" in response.lower():
            print("⚠ Warning: All AI services appear to be unavailable")
            return False
        else:
            print("✓ At least one AI service is working")
            return True

    except Exception as e:
        print(f"✗ Fallback logic failed: {e}")
        return False


def test_audio_devices():
    """Test audio devices for speech recognition and TTS"""
    print("=== Testing Audio Devices ===")

    # Test microphone
    try:
        import speech_recognition as sr
        r = sr.Recognizer()

        print("Available microphones:")
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print(f"  {index}: {name}")

        # Test default microphone
        with sr.Microphone() as source:
            print("✓ Default microphone accessible")

    except Exception as e:
        print(f"✗ Microphone test failed: {e}")

    # Test TTS
    try:
        import pyttsx3
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        if voices:
            print(f"✓ TTS engine initialized with {len(voices)} voice(s)")
            for i, voice in enumerate(voices[:3]):  # Show first 3 voices
                print(f"  Voice {i}: {voice.name}")
        else:
            print("⚠ TTS engine initialized but no voices found")

        engine.stop()

    except Exception as e:
        print(f"✗ TTS test failed: {e}")

    print()


def main():
    """Run all tests"""
    print("AI Chatbot - System Test")
    print("=" * 50)
    print()

    # Run all tests
    test_environment()

    if not test_imports():
        print("❌ Package import tests failed. Please install missing packages:")
        print("   pip install -r requirements.txt")
        return

    if not test_ai_handler():
        print("❌ AI handler module test failed. Check your ai_handler.py file.")
        return

    test_audio_devices()

    # Test APIs
    openai_works = test_openai_api()
    print()

    gemini_works = test_gemini_api()
    print()

    if openai_works or gemini_works:
        test_fallback_logic()
        print()
        print("✅ System is ready! You can run main.py")
    else:
        print("❌ No AI APIs are working. Please check your API keys.")
        print("   Set environment variables:")
        print("   OPENAI_API_KEY=your-key-here")
        print("   GEMINI_KEY=your-key-here")


if __name__ == "__main__":
    main()