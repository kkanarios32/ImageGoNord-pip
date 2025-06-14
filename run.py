from ImageGoNord import NordPaletteFile, GoNord

# E.g. Replace pixel by pixel
image_dir = "/home/kellen/Pictures/"
image_name = "joyboy.png"
go_nord = GoNord()
image = go_nord.open_image(image_dir + image_name)
save_path = image_dir + "nord-" + image_name

go_nord.enable_avg_algorithm()
# go_nord.enable_gaussian_blur()

go_nord.reset_palette()
go_nord.add_file_to_palette(NordPaletteFile.POLAR_NIGHT)
go_nord.add_file_to_palette(NordPaletteFile.SNOW_STORM)
go_nord.add_file_to_palette(NordPaletteFile.FROST)
go_nord.add_file_to_palette(NordPaletteFile.AURORA)

go_nord.convert_image(image, save_path=save_path)
