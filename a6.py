
N = int(input())

hours = N // 3600
minutes = (N % 3600) // 60
seconds = N % 60

print(f"{hours}:{minutes:02d}:{seconds:02d}")