from PIL import Image, ImageDraw

face = Image.open("400.png") 
frame = Image.open("frame.png")
# gray with alpha
frame_gray = frame.copy().convert("LA")
w, h = frame_gray.size
px = list(frame_gray.crop([0,0,w,1]).getdata())
# get values for first line of pixels
px = [px[i*w:(i+1)*w] for i in [0]][0]
# discard transparent ones
px = filter(lambda x: x[1]>0, px)
nontransparent_width = len(list(px))
border_width = w - nontransparent_width

w400, h400 = face.size # probable 400x400
# calculate new size for frame
k = h/w # frame ratio
w_new = w400 + border_width
h_new = int(w_new*k)
frame = frame.resize((w_new, h_new), Image.NEAREST) # no blur resize

pos_x = int(border_width/2)

# start stacking images
canvas = Image.new("RGBA", frame.size)
canvas.paste(face, (pos_x, pos_x)) # need to calculate pos_y??
canvas.paste(frame, frame.convert("RGBA"))
img_draw = ImageDraw.Draw(canvas)
img_draw.text((20, h), 'Hello World', fill='green')
canvas.show()
canvas.save("test.png")
