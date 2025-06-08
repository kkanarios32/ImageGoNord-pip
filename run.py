from ImageGoNord import GoNord

# E.g. Replace pixel by pixel
image_dir = "/home/kellen/Pictures/"
image_name = "obito.jpg"
go_nord = GoNord()
image = go_nord.open_image(image_dir + image_name)
save_path = image_dir + "nord-" + image_name
go_nord.convert_image(image, save_path=save_path)
