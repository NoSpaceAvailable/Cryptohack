from PIL import Image

lemur = Image.open("lemur.png")
flag = Image.open("flag_lemur.png")

lemur_rgb = lemur.convert("RGB")
flag_rgb = flag.convert("RGB")

res = Image.frombytes("RGB", lemur.size, bytes(a ^ b for a, b in zip(lemur_rgb.tobytes(), flag_rgb.tobytes())))
res.show("The flag is:")