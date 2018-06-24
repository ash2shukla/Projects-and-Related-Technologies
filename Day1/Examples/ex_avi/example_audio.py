import wave


def read_audio():
    file_pointer = wave.open('Sample_WAV.wav')
    # Get number of frames from the stream
    print(file_pointer.getnframes())
    # Get number of channels from the stream
    print(file_pointer.getnchannels())
    # Read n frames
    print(file_pointer.readframes(10))
    # Rewing file_pointer to start of stream
    print(file_pointer.rewind())
    print(file_pointer.readframes(10))


def write_audio():
    # The audio written will not play as it has not been modelled properly
    file_pointer = wave.open('New_WAV.wav', 'wb')
    file_pointer.setnchannels(1)
    file_pointer.setsampwidth(2)
    file_pointer.setframerate(44100)
    file_pointer.writeframes(b'123123123131231231231312312312312313')
    file_pointer.close()


if __name__ == "__main__":
    read_audio()
    write_audio()