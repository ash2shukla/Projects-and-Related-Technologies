import skvideo.io
import json
import numpy as np


def read_video():
    videodata = skvideo.io.vread('Sample_Video.mp4')
    print(videodata.shape)
    for frame in videodata:
            print(frame.shape)

    metadata = skvideo.io.ffprobe("Sample_Video.mp4")
    print(metadata.keys())
    print(json.dumps(metadata["video"], indent=4))


def write_video():
    outputdata = np.random.random(size=(5, 480, 680, 3)) * 255
    outputdata = outputdata.astype(np.uint8)

    writer = skvideo.io.FFmpegWriter("noise_video.mp4")
    for i in range(5):
            writer.writeFrame(outputdata[i, :, :, :])
    writer.close()


def main():
    read_video()
    write_video()


if __name__ == "__main__":
    main()