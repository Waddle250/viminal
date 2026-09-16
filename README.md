# Viminal
A video player for your terminal so you can watch Bad Apple or smth

## What is Viminal?
It's a program made in Python that can play videos and audio in terminals. It's pretty useful if you want to watch a video but don't have the app to and need something smaller.

In a TTY, you are limited to 16-bit color, and rounding will be used to designate a color. If you are in a terminal window, if your terminal app supports full color, that will be used instead for a better experience.

>[!IMPORTANT]
>Do note that because this is rendering text and assigning it a color at a very high rate, it WILL begin to lag at high resolutions. The sweet spot for weak GPUs is around 340-720p, and for high end CPUs I reccommend using at the maximum 2K. By going any higher than your CPU can handle, you put this at a risk of crashing and your fans going supersonic speeds.